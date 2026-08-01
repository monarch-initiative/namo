# NAMO → Biolink Alignment Plan

**Phase 1 of the broader Biolink alignment effort: replace the generic `Term` class with NAMO-local classes that carry a Biolink `class_uri`.** (The numbered Stages 1–7 below are the steps *within* this phase.)

- Tracking issue: [#19 — All instances of "Term" should be removed from schema.yaml and replaced with the appropriate Biolink class](https://github.com/monarch-initiative/namo/issues/19)
- Biolink Model version targeted: **4.4.3** (local reading copy at `../biolink-model.yaml`)
- Companion document: [`ontology_mapping_plan.md`](ontology_mapping_plan.md) (enum → ontology strategy)
- Status: **approved, ready to execute.** Every claim below was probed against the project toolchain before being written down. No schema changes have been made yet.

---

## Approach

For each Biolink class NAMO needs, NAMO defines **one local class whose `class_uri` is the Biolink CURIE**. The Biolink model is *not* imported.

```yaml
  Cell:
    is_a: BiolinkEntity
    class_uri: biolink:Cell
    description: >-
      The basic structural and functional unit of all organisms.
    id_prefixes:
      - CL
      - UBERON
      - NCIT
      - MESH
```

The generic `Term` class is deleted and its 17 slot ranges are repointed at these classes.

An earlier draft of this plan took the opposite route — `imports: https://w3id.org/biolink/biolink-model` with Biolink's own class names as ranges. That is now rejected. It works, but it costs a mandatory migration of all 27 example files (Biolink's `named thing` requires `category`), five silent class-name collisions (`NamedThing`, `Study`, `Dataset`, `Gene`, `Pathway` — `gen-python` exits 0 and Biolink's definitions quietly win), a 19,151-line / 645-class generated model, and a published JSON Schema that cannot validate anything (`gen-json-schema` emits `{"type": "array", "enum": [...]}` for `category`). Those costs bought inherited Biolink structure that NAMO does not use.

### What "linking out" actually means under this approach

`class_uri` is not cosmetic. It propagates into every generated artifact that has somewhere to put a URI — verified on a scratch build of the full schema:

| Artifact | How the Biolink class appears | Verified output |
|---|---|---|
| Python dataclass | class URI | `m.Cell.class_class_uri == 'https://w3id.org/biolink/Cell'`, `class_class_curie == 'biolink:Cell'` |
| **RDF instance data** | `rdf:type` on the instance | `NCBITaxon:10090 a biolink:OrganismTaxon ; schema:name "Mus musculus"` |
| SHACL | node constraint | `sh:class biolink:OrganismTaxon`, `sh:class biolink:LifeStage`, `sh:class biolink:EnvironmentalExposure` |
| JSON-LD context | term definition | `"Cell": { "@id": "biolink:Cell" }` |
| OWL | mapping axiom | `namo:Cell skos:exactMatch biolink:Cell` (default), or `owl:equivalentClass` with `--assert-equivalent-classes` — see 6b |
| JSON Schema | plain object, no defect | `linkml-validate` returns "No issues found" |

The RDF row is the important one: instance data genuinely types ontology terms as Biolink classes.

### What this approach does not give you

Stated plainly so nobody is surprised later:

1. **No inherited Biolink structure.** `namo:Cell` is not a subclass of `biolink:AnatomicalEntity` anywhere in NAMO's output, and it inherits none of Biolink's slots (`category`, `provided_by`, `xref`, …). The tie to Biolink is an equivalence assertion, not a hierarchy.
2. **NAMO asserts the equivalence itself.** Nothing checks NAMO's `Cell` against Biolink's `cell`. If Biolink 5 renames or re-scopes a class, NAMO will keep asserting the old URI. Mitigation: the pinned version is recorded at the top of this document and in a comment on `BiolinkEntity`; re-check the mapping table on every Biolink upgrade.
3. **`id_prefixes` are advisory.** They are copied from Biolink for documentation and downstream tooling, but neither `gen-python` nor `linkml-validate` enforces them. Real value-space enforcement comes from the `bindings` blocks in Stage 4.
4. **OWL consumers get `skos:exactMatch`, not identity** (unless 6b is adopted). NAMO's OWL declares `namo:Cell` and matches it to `biolink:Cell`; it does not mint `biolink:Cell` itself. That is deliberate — see 6b for why the alternative is worse.

These are accepted. The import approach avoided (1) and (2) but paid the costs listed above.

---

## Verified findings

Everything here was run against this branch's toolchain (LinkML from `uv.lock`, Python 3.13) on a scratch copy of `namo.yaml` carrying the full set of changes in Stages 1–3.

| Check | Result |
|---|---|
| `gen-project -I python` with the local classes | **Exit 0.** No collisions to resolve — nothing is imported, so nothing can collide |
| Generated model size | **3,578 → 3,803 lines** (+225). Compare **19,151 lines / 645 classes** under the import approach |
| Do the class URIs resolve to Biolink? | **Yes.** `Cell`, `GrossAnatomicalStructure`, `OrganismTaxon`, `PhenotypicFeature`, `LifeStage`, `EnvironmentalExposure`, `QuantityValue` all report `class_class_uri = https://w3id.org/biolink/<Name>` |
| Is the `biolink` prefix as currently declared correct? | **Yes — leave it alone.** `namo.yaml:152` maps `biolink: https://w3id.org/biolink/`, and that is the namespace to use. See 1a for why the `/vocab/` form in Biolink's own YAML is not the right target |
| RDF dump before Stage 1 prefixes | **Fails.** `ValueError: Unknown CURIE prefix: CL` — NAMO's prefix map has `UBERON` but not `CL`, `NCBITaxon`, `HP`, `MP`, `HsapDv`, `MmusDv`, `ECTO`, `ENVO`, `UO`, `BFO` |
| RDF dump after Stage 1 prefixes | **Correct.** `NCBITaxon:10090 a biolink:OrganismTaxon`, `MmusDv:0000110 a biolink:LifeStage`, `[ a biolink:QuantityValue ; biolink:has_numeric_value 8e+00 ; biolink:has_unit UO:0000034 ]` |
| Mapped classes under `is_a: NamedThing` | **Breaks RDF typing.** NAMO's inherited `type: designates_type: true` sets `type_added` in `rdflib_dumper`, which then *skips* the `rdf:type` triple. Output degrades to `CL:0002632 namo:type "Cell"` with no Biolink type at all. This is why `BiolinkEntity` is a separate root — see 2a |
| All 27 files in `tests/data/valid/` load unchanged | **Yes**, before the 3b rename. No `category`, no `namo_type`, no data migration |
| Same 27 files after the 3b rename | **3 failures**, all `TissueOnChip-example-00{1,2,3}.yaml`: `unexpected keyword argument 'tissue_modeled'`. That is the entire data migration |
| `linkml-validate` (JSON Schema path) | **"No issues found."** The array/enum `category` defect that broke this under the import approach does not exist here |
| `linkml-run-examples` (the `_test-examples` recipe) | **Exit 0** over `tests/data/valid` |
| `gen-project` with `config.yaml` (the `_test-schema` recipe) | **Exit 0.** All generators emit: excel, graphql, jsonld, jsonschema, owl, prefixmap, protobuf, shacl, shex, sqlschema |
| `gen-pydantic` | **Exit 0.** `class BiolinkEntity(ConfiguredBaseModel)`, `class Cell(BiolinkEntity)`, … |
| `linkml-lint` | **201 → 204 problems.** All 201 pre-existing (`standard_naming`, `canonical_prefixes`, `recommended`). The 3 new ones are cosmetic: a `canonical_prefixes` complaint about the `UMLS` namespace and two missing descriptions on `QuantityValue` attributes. Both fixable in-stage |
| `oaklib` installed? | **Yes** — 0.6.23, `[dependency-groups] dev`, resolved in `uv.lock`. Used for the closure checks in 4a / 4b against Ubergraph |
| `species` / `strain` / `age` / `environment` inlining | **Latent bug, pre-existing.** These four slots have no `inlined: true`, so a full term object raises `... is not a valid URI or CURIE`. Invisible today only because no `AnimalModel` example file exists. Fixed in 3d |

---

## Stage 1 — Prefix hygiene (blocking; do first)

Nothing downstream is correct until the prefix map is. One real edit in the `prefixes:` block around line 150 — plus one deliberate non-edit that has already burned one draft of this plan.

### 1a. Leave the `biolink` prefix as it is

```yaml
  biolink: https://w3id.org/biolink/     # correct as declared — do not change
```

**Do not "fix" this to `https://w3id.org/biolink/vocab/`.** Biolink's own YAML still declares the `/vocab/` form (line 27 of `biolink-model.yaml`, and `id: https://w3id.org/biolink/vocab/`), which makes it a tempting target, but it is the wrong namespace to mint URIs into. `https://w3id.org/biolink/vocab/Cell` redirects to `biolink.github.io/biolink-model/docs/Cell`, which **404s**; `https://w3id.org/biolink/Cell` redirects to `biolink.github.io/biolink-model/Cell/`, which **resolves 200**. NAMO's declaration already points at the namespace that dereferences, so `class_uri: biolink:Cell` expands correctly with no edit.

This note exists because the `/vocab/` string is all over Biolink's source and an earlier draft of this plan changed the prefix to match it. Anyone re-deriving the prefix from `biolink-model.yaml` will reach the wrong answer.

### 1b. Declare the missing ontology prefixes

The schema already uses `CL:`, `NCBITaxon:`, `HP:`, `BFO:` in enum `source_nodes` and in example data, but declares none of them. `gen-project` only warns (`Unrecognized prefix: CL`); the RDF dumper hard-fails.

```yaml
  CL: http://purl.obolibrary.org/obo/CL_
  NCBITaxon: http://purl.obolibrary.org/obo/NCBITaxon_
  HP: http://purl.obolibrary.org/obo/HP_
  MP: http://purl.obolibrary.org/obo/MP_
  UPHENO: http://purl.obolibrary.org/obo/UPHENO_
  HsapDv: http://purl.obolibrary.org/obo/HsapDv_
  MmusDv: http://purl.obolibrary.org/obo/MmusDv_
  ECTO: http://purl.obolibrary.org/obo/ECTO_
  ENVO: http://purl.obolibrary.org/obo/ENVO_
  BFO: http://purl.obolibrary.org/obo/BFO_
  UO: http://purl.obolibrary.org/obo/UO_
```

`UMLS` is also referenced by Biolink's `id_prefixes`. Either omit it from NAMO's copies of `id_prefixes` or declare it as `http://identifiers.org/umls/` — that is the namespace `linkml-lint` treats as canonical, and any other value adds a `canonical_prefixes` warning.

Also note the example files use undeclared local prefixes (`organonchip:`, `microfluidic:`, `gene:`, `assay:`, …). They do not block `just test`, but they do block `rdflib_dumper` on real instance data. Out of scope for this phase; worth its own issue.

---

## Stage 2 — Add the Biolink-mapped classes

### 2a. `BiolinkEntity` — the shared base, deliberately *not* under `NamedThing`

```yaml
  BiolinkEntity:
    abstract: true
    description: >-
      Abstract parent for NAMO classes that stand in for a class in the Biolink
      Model. Each subclass carries the Biolink class URI as its `class_uri`, so
      instances are typed with the Biolink class in RDF, SHACL and JSON-LD
      output. Mappings target Biolink Model 4.4.3.
    slots:
      - id
      - name
      - description
```

**Why not `is_a: NamedThing`.** NAMO's `NamedThing` carries `type: designates_type: true`. `linkml_runtime`'s `rdflib_dumper.inject_triples` only emits `rdf:type` when no type-designator slot was written (`rdflib_dumper.py:156-159`); a populated designator sets `type_added = True` and the `rdf:type` triple is skipped. Under `is_a: NamedThing` the RDF for a cell term degrades to:

```turtle
CL:0002632 schema:name "epithelial cell of lower respiratory tract" ;
    namo:type "Cell" .          # no biolink:Cell anywhere
```

With `BiolinkEntity` as its own root, the same instance dumps as:

```turtle
CL:0002632 a biolink:Cell ;
    schema:name "epithelial cell of lower respiratory tract" .
```

Both variants generate cleanly and load all 27 example files; only the second actually links out. NAMO's `NamedThing` and its `type` designator are untouched — they still drive polymorphic loading of `ModelSystem` subclasses, which is what they are for.

### 2b. The mapped classes

Seven classes, each `is_a: BiolinkEntity` unless noted. Descriptions and `id_prefixes` are taken from Biolink 4.4.3; NAMO trims Biolink's prefix lists to the ontologies NAMO actually curates against.

| NAMO class | `class_uri` | Biolink 4.4.3 source | Consuming slots | `id_prefixes` |
|---|---|---|---|---|
| `OrganismTaxon` | `biolink:OrganismTaxon` | `organism taxon` (line 7311) | `species`, `strain`, `species_modeled` | NCBITaxon, MESH |
| `Cell` | `biolink:Cell` | `cell` (line 9338) | `cell_types` ×2, `cell_type` ×2, `represented_cell_types`, `missing_cell_types` | CL, UBERON, NCIT, MESH |
| `GrossAnatomicalStructure` | `biolink:GrossAnatomicalStructure` | `gross anatomical structure` (line 9380) | `organ_modeled` ×2, `anatomical_structure_modeled` | UBERON, NCIT, MESH |
| `PhenotypicFeature` | `biolink:PhenotypicFeature` | `phenotypic feature` (line 9188) | `shared_phenotypes`, `model_specific_phenotypes`, `biological_specific_phenotypes` | HP, MP, UPHENO |
| `LifeStage` | `biolink:LifeStage` | `life stage` (line 9055) | `life_stage` (new, 3a) | HsapDv, MmusDv, UBERON |
| `EnvironmentalExposure` | `biolink:EnvironmentalExposure` | `environmental exposure` (line 10388) | `environment` | ECTO, ENVO |
| `QuantityValue` | `biolink:QuantityValue` | `quantity value` (line 7108) | `age_value` (new, 3a) | — (not an identified entity) |

`QuantityValue` is the one exception to `is_a: BiolinkEntity`. Biolink's `quantity value` is `is_a: annotation`, not a `named thing` — it has no `id`, so it is inlined by value:

```yaml
  QuantityValue:
    class_uri: biolink:QuantityValue
    description: >-
      A value of an attribute that is quantitative and measurable, expressed as
      a combination of a unit and a numeric value.
    attributes:
      has_numeric_value:
        slot_uri: biolink:has_numeric_value
        range: double
        description: >-
          The numeric portion of the quantity.
      has_unit:
        slot_uri: biolink:has_unit
        range: uriorcurie
        description: >-
          The unit of measurement, as a UO CURIE.
```

The `slot_uri` entries matter — without them the predicates would be `namo:has_numeric_value`. Verified output:

```turtle
animal:1 namo:age_value [ a biolink:QuantityValue ;
            biolink:has_numeric_value 8e+00 ;
            biolink:has_unit UO:0000034 ] .
```

Give both attributes a `description` or `linkml-lint` adds two `recommended` warnings.

---

## Stage 3 — Repoint the 17 `Term` ranges

`inlined` / `inlined_as_list` / `multivalued` / `required` flags stay as they are, except where 3d adds a missing one. Two slots change beyond their range: `age` is split (3a) and `tissue_modeled` is renamed (3b).

| Line | Owner | Attribute | `range: Term` → | Rationale |
|---|---|---|---|---|
| 247 | `AnimalModel` | `species` | `OrganismTaxon` | `values_from: NCBITaxon`; matches existing `SpeciesEnum` |
| 256 | `AnimalModel` | `strain` | `OrganismTaxon` | Biolink has **no** Strain class; `organism taxon` docs: "Can also be used to represent strains or subspecies". Binding dropped per D5 — see 4f |
| 264 | `AnimalModel` | `age` | **removed** — split into `life_stage` + `age_value` | Per D2; see 3a |
| 272 | `AnimalModel` | `environment` | `EnvironmentalExposure` | Per D3 |
| 322 | `CellularSystem` | `cell_types` | `Cell` | See deviation note in 3c |
| 406 | `Organoid` | `organ_modeled` | `GrossAnatomicalStructure` | Per Issue 19; Biolink aliases it 'tissue', 'organ' |
| 482 | `OrganOnChip` | `organ_modeled` | `GrossAnatomicalStructure` | Per Issue 19 |
| 491 | `OrganOnChip` | `cell_types` | `Cell` | Same concept as line 322 |
| 515 | `TissueOnChip` | `tissue_modeled` → **renamed** `anatomical_structure_modeled` | `GrossAnatomicalStructure` | Per Issue 19; rename per 3b |
| 588 | `PBPKModel` | `species_modeled` | `OrganismTaxon` | Per Issue 19 |
| 669 | `CellRatio` | `cell_type` | `Cell` | Not in Issue 19 |
| 1055 | `PhenotypeOverlap` | `shared_phenotypes` | `PhenotypicFeature` | Per Issue 19 |
| 1061 | `PhenotypeOverlap` | `model_specific_phenotypes` | `PhenotypicFeature` | Per Issue 19 |
| 1067 | `PhenotypeOverlap` | `biological_specific_phenotypes` | `PhenotypicFeature` | Per Issue 19 |
| 1086 | `CellTypeCoverage` | `represented_cell_types` | `Cell` | Not in Issue 19 |
| 1092 | `CellTypeCoverage` | `missing_cell_types` | `Cell` | Not in Issue 19 |
| 1270 | `CellTypeProportion` | `cell_type` | `Cell` | Not in Issue 19 |

Then **delete the `Term` class** (lines 1380–1385) — last in the stage, so `just lint` and `gen-python` catch any missed reference.

### 3a. Split `AnimalModel.age` (per D2)

`age` conflated developmental stage with chronological age. Replace the single slot with two:

```yaml
      life_stage:
        range: LifeStage
        inlined: true
        description: >-
          The developmental or life-cycle stage of the animal used in the model system.
        bindings:
          - binds_value_of: id
            range: LifeStageEnum
            obligation_level: REQUIRED
      age_value:
        range: QuantityValue
        inlined: true
        description: >-
          Chronological age of the animal at the time of study, as a numeric value
          with a unit.
```

In instance data:

```yaml
life_stage:
  id: "MmusDv:0000110"
  name: "mature stage"       # Ubergraph's label for this term
age_value:
  has_numeric_value: 8.0
  has_unit: "UO:0000034"      # week
```

Note there is no `category` line — that requirement was an artifact of the import approach. No current example file populates `age`, so this split costs no data migration.

### 3b. Rename `TissueOnChip.tissue_modeled` → `anatomical_structure_modeled`

The old name asserted "tissue" while the data holds an organ (`skin of body`), a barrier (`blood-brain barrier`), and a tract (`digestive tract`) — see the closure results in 4b. The new name matches both the data and the Biolink class it now ranges over:

```yaml
      anatomical_structure_modeled:
        range: GrossAnatomicalStructure
        inlined: true
        description: >-
          The anatomical structure being modeled — a tissue, organ, or other
          multicellular structure.
        bindings:
          - binds_value_of: id
            range: AnatomicalStructureEnum
            obligation_level: REQUIRED
```

The Biolink mapping *is* the range: `GrossAnatomicalStructure` carries `class_uri: biolink:GrossAnatomicalStructure`. No separate `exact_mappings` entry is needed on the slot.

**Migration cost of the rename** — 3 hand-maintained files plus 1 hand-written doc; everything else regenerates:

| Path | Kind |
|---|---|
| `tests/data/valid/TissueOnChip-example-001.yaml` | hand-edit (1 occurrence) |
| `tests/data/valid/TissueOnChip-example-002.yaml` | hand-edit (1 occurrence) |
| `tests/data/valid/TissueOnChip-example-003.yaml` | hand-edit (1 occurrence) |
| `docs/how-to/curate.md` | hand-edit — the `TissueOnChip` row of the model-class table, line 88, lists `tissue_modeled` as a required field |
| `docs/elements/*`, `docs/schema/namo.yaml`, `examples/output/*`, `project/*`, `src/namo/datamodel/*` | **generated** — `just gen-project` / `gen-doc` / `_ensure_examples_output` rewrite these; do not hand-edit |

Note `docs/elements/tissue_modeled.md` and `docs/elements/Term.md` are generated pages that will disappear on the next `just gen-doc`; if `docs/` is version-controlled, expect deletions in the diff. New pages appear for `BiolinkEntity`, `Cell`, `GrossAnatomicalStructure`, `OrganismTaxon`, `PhenotypicFeature`, `LifeStage`, `EnvironmentalExposure`, and `QuantityValue`.

### 3c. Deviation from Issue 19 on `cell_types`

The issue asks for `cell_types` → `biolink:anatomical_entity`. Biolink's own `anatomical entity` description says the opposite:

> This is a grouping class with three concrete subclasses that should be preferred when applicable: `biolink:Cell` for whole cells, `biolink:CellularComponent` for subcellular and intracellular structures, and `biolink:GrossAnatomcialStructure` for multicellular parts.

`CellTypeEnum` is already rooted at `CL:0000000`, so **`Cell` is correct and more specific.** Worth a note on the issue before closing it.

### 3d. Add the missing `inlined: true` flags

`species` (247), `strain` (256), and `environment` (272) have no inlining flag, so LinkML treats them as references and rejects a full term object:

```
ValueError: OrganismTaxon({'id': 'NCBITaxon:10090', ...}) is not a valid URI or CURIE
```

This is a pre-existing bug — the same failure occurs today with `range: Term`. It is invisible only because no `AnimalModel` example file exists. Add `inlined: true` to all three while repointing them; the other Term-ranged slots already carry `inlined` or `inlined_as_list`.

---

## Stage 4 — Enum and binding alignment

**Nothing in `just test` currently enforces these enums.** `_test-python` uses `yaml_loader` + dataclasses and `_test-examples` uses `linkml-run-examples`; neither expands a `reachable_from` enum nor checks a `bindings` block. NAMO's enum constraints are therefore declared but **unenforced at test time**, and will stay that way until a validation step is wired into the suite. So the tightening in 4a carries no immediate CI risk — and equally, 4a–4f should not be considered done until that step exists. Adding it is tracked in 6c.

### 4a. Narrow `OrganEnum` to `UBERON:0000062` (organ) — per D4

Currently `reachable_from: UBERON:0001062`, the anatomy root, which includes cells and subcellular parts:

```yaml
  OrganEnum:
    reachable_from:
      source_nodes:
        - UBERON:0000062      # organ
      is_direct: false
      relationship_types:
        - rdfs:subClassOf
        - BFO:0000050         # part_of
```

**Closure check: verified safe.** Computed with oaklib against Ubergraph — `descendants(UBERON:0000062, predicates=[IS_A, PART_OF])` yields 19,578 terms. **All 11 distinct `organ_modeled` values in `tests/data/valid/` fall inside it:**

| Value | Label | File |
|---|---|---|
| `UBERON:0000160` | intestine | `Organoid-example-takahashi-2023.yaml` |
| `UBERON:0000948` | heart | `Organoid-example-005.yaml` |
| `UBERON:0000955` | brain | `Organoid-example-001.yaml`, `Organoid-example-006.yaml` |
| `UBERON:0001005` | respiratory airway | `OrganOnChip-example-001.yaml` |
| `UBERON:0002048` | lung | `OrganOnChip-example-zhu-2024.yaml` |
| `UBERON:0002107` | liver | `Organoid-example-002.yaml` |
| `UBERON:0002108` | small intestine | `Organoid-example-003.yaml` |
| `UBERON:0002113` | kidney | `Organoid-example-004.yaml` |
| `UBERON:0002186` | bronchiole | `OrganOnChip-example-003.yaml` (via `part_of` lung) |
| `UBERON:0002299` | alveolus of lung | `OrganOnChip-example-002.yaml` (via `part_of` lung) |

**D4 requires no data recuration.** Note in particular that `UBERON:0001005` ("respiratory airway") *passes* — an earlier draft flagged it as at-risk on the assumption it was a conduit outside the organ closure. It is reachable, so `OrganOnChip-example-001.yaml` is fine as written. Including `BFO:0000050` (`part_of`) in `relationship_types` is what carries `bronchiole` and `alveolus of lung`; dropping it would break both.

### 4b. Add `AnatomicalStructureEnum`, bind `anatomical_structure_modeled`

The slot (renamed in 3b) is currently unbound. The obvious root for the old `tissue_modeled` name was `UBERON:0000479` (tissue), but the closure check says that fails on real data. `descendants(UBERON:0000479, [IS_A, PART_OF])` = 6,435 terms, and of the three distinct values only one is inside it:

| Value | Label | File | `UBERON:0000479` (tissue) | `UBERON:0000062` (organ) | `UBERON:0010000` |
|---|---|---|---|---|---|
| `UBERON:0000120` | blood-brain barrier | `TissueOnChip-example-001.yaml` | **PASS** | FAIL | PASS |
| `UBERON:0002097` | skin of body | `TissueOnChip-example-003.yaml` | FAIL | PASS | PASS |
| `UBERON:0001555` | digestive tract | `TissueOnChip-example-002.yaml` | FAIL | FAIL | PASS |

No organ-or-tissue combination covers all three: `digestive tract` is outside both. Only `UBERON:0010000` (multicellular anatomical structure) covers the set — which is also exactly what Biolink's `gross anatomical structure` gives as its `exact_mappings`, so it is the right root and it lines up with the slot's new name:

```yaml
  AnatomicalStructureEnum:
    reachable_from:
      source_nodes:
        - UBERON:0010000      # multicellular anatomical structure
      is_direct: false
      relationship_types:
        - rdfs:subClassOf
        - BFO:0000050         # part_of
```

Recuration is no longer the alternative it was under the old name: `anatomical_structure_modeled` is *supposed* to admit organs, tissues, and tracts alike, so all three existing values are correct as curated. `TissueEnum` is not created.

**`organ_modeled` stays separate** (per D7). It keeps its own name, its own `OrganEnum`, and the stricter `UBERON:0000062` root from 4a, even though it shares the `GrossAnatomicalStructure` range with `anatomical_structure_modeled`. Two enums therefore coexist by design: `OrganEnum` (organ closure, for `Organoid` and `OrganOnChip`) and `AnatomicalStructureEnum` (multicellular-structure closure, for `TissueOnChip`). The stricter organ constraint is a feature of this split, not an inconsistency to reconcile.

### 4c. Add `LifeStageEnum`, drop the dangling `OrganismAgeEnum`

`AnimalModel.age` bound `OrganismAgeEnum`, which **is never defined anywhere in the schema** — only an empty `AgeEnum` exists. With `age` now split (3a), the binding moves to the new `life_stage` slot. Delete the unused `AgeEnum` and the dangling `OrganismAgeEnum` reference.

**A single `UBERON:0000105` root does not work** — an earlier draft of this section proposed one, and the closure check refutes it. The species-specific developmental ontologies are not asserted as subclasses of UBERON's life-cycle-stage term: in Ubergraph, `ancestors(MmusDv:0000110, [IS_A])` is `{MmusDv:0000000, BFO:0000003, BFO:0000001}` — no UBERON at all. `descendants(UBERON:0000105, [IS_A, PART_OF])` returns 55 terms and contains neither `MmusDv:0000110` nor any `HsapDv` term. A UBERON-only root would therefore reject exactly the CURIEs Biolink's `life stage` advertises in its `id_prefixes` (HsapDv, MmusDv, ZFS, FBdv, WBls, UBERON) — including the worked example in 3a. Compose instead, as 4d does for phenotypes:

```yaml
  LifeStageEnum:
    include:
      - reachable_from:
          source_nodes: [UBERON:0000105]     # life cycle stage, 55 terms
          is_direct: false
          relationship_types: [rdfs:subClassOf]
      - reachable_from:
          source_nodes: [HsapDv:0000000]     # human life cycle stage, 239 terms
          is_direct: false
          relationship_types: [rdfs:subClassOf]
      - reachable_from:
          source_nodes: [MmusDv:0000000]     # mouse life cycle stage, 134 terms
          is_direct: false
          relationship_types: [rdfs:subClassOf]
```

Add ZFS / FBdv / WBls roots the same way if NAMO ever curates those organisms.

`age_value` takes no binding — it is a `QuantityValue`, not an ontology term.

### 4d. Add `PhenotypeEnum`, bind the three `PhenotypeOverlap` slots

Biolink `phenotypic feature` spans HP/MP/UPHENO, so compose:

```yaml
  PhenotypeEnum:
    include:
      - reachable_from:
          source_nodes: [HP:0000118]     # phenotypic abnormality
          is_direct: false
          relationship_types: [rdfs:subClassOf]
      - reachable_from:
          source_nodes: [MP:0000001]     # mammalian phenotype
          is_direct: false
          relationship_types: [rdfs:subClassOf]
```

This makes `PhenotypeOverlap.phenotype_ontology` (free text documenting "HPO, MP") redundant — flag for deprecation.

### 4e. Bind the four unbound cell-type slots

`CellRatio.cell_type`, `CellTypeCoverage.represented_cell_types`, `CellTypeCoverage.missing_cell_types`, and `CellTypeProportion.cell_type` → existing `CellTypeEnum`.

### 4f. Delete `StrainEnum`; leave `strain` unconstrained — per D5

`AnimalModel.strain` becomes `range: OrganismTaxon` with **no `bindings` block**. The empty `StrainEnum` is deleted rather than populated. Strain identity is carried by whatever CURIE the curator supplies — NCBITaxon strain-rank nodes, RS, JAX. This was the right call regardless of preference: LinkML dynamic enums cannot filter by taxonomic rank, so an `NCBITaxon:1`-rooted `StrainEnum` would have been indistinguishable from `SpeciesEnum` and enforced nothing useful.

---

## Stage 5 — Migrate example and test data

**Three files and one doc page.** That is the whole migration, and all of it comes from the 3b rename — not from the Biolink alignment itself.

1. **Rename `tissue_modeled:` → `anatomical_structure_modeled:`** in `TissueOnChip-example-001.yaml`, `-002.yaml`, and `-003.yaml`.
2. **Update `docs/how-to/curate.md`**, the `TissueOnChip` row at line 88.
3. **Nothing else.** No `category` field, no `type:` → `namo_type:` rename, no anatomy recuration. Verified: all 27 files in `tests/data/valid/` load against the regenerated dataclasses with no edits other than item 1, and the closure checks in 4a/4b confirm every existing anatomy value stays inside its new enum.

`examples/output/` regenerates via `_ensure_examples_output`; `tests/data/invalid/` is currently empty. Three hand-edits do not need a migration script.

For comparison, the rejected import approach required editing all 27 files to add `category` to every ontology reference *and* every NAMO entity, plus a global `type:` → `namo_type:` rename.

---

## Stage 6 — Validation, generator config, and impact

### 6a. `just test` passes unchanged

`_test-schema` (`gen-project` with `config.yaml`) exits 0; `_test-python` loads all 27 examples through the generated dataclasses; `_test-examples` (`linkml-run-examples`) exits 0. `linkml-validate` against the JSON Schema also reports "No issues found" — worth adding to the suite now that it works, since it did not under the import approach.

### 6b. Decide the OWL mapping predicate

`gen-owl` uses NAMO's native class URIs for subjects and expresses `class_uri` as a mapping:

```turtle
namo:Cell a owl:Class ;
    rdfs:label "Cell" ;
    rdfs:subClassOf namo:BiolinkEntity ;
    skos:exactMatch biolink:Cell .
```

Two options, both verified:

- **`--assert-equivalent-classes`** upgrades that line to `owl:equivalentClass biolink:Cell`. **Recommended** — it is the assertion this whole design is making, and it is what an OWL reasoner needs to actually merge the classes. Set it in `config.yaml` under `generator_args.owl` as `assert_equivalent_classes: true`.
- **`--no-use-native-uris`** makes `biolink:Cell` itself the subject. **Not recommended**: NAMO would then publish `biolink:Cell rdfs:subClassOf namo:BiolinkEntity` with NAMO's own label and definition, i.e. NAMO redefining Biolink's classes in Biolink's namespace. That is precisely the overreach this approach is meant to avoid.

While editing `config.yaml`, note `gen-owl` now emits a deprecation warning recommending an explicit `consolidate_cardinality_axioms` setting ([linkml#3191](https://github.com/linkml/linkml/issues/3191)); set it either way to silence it.

### 6c. Wire enum validation into the test suite

`oaklib` 0.6.23 is a dev dependency, so closure checks are runnable ad hoc (4a, 4b) — but no `just test` step expands dynamic enums or enforces `bindings`, so Stage 4's constraints remain unenforced in CI. Add a step that validates the `reachable_from` enums and `bindings` against the example data; otherwise these enums are documentation rather than validation. Minor: `oaklib` is the only unpinned entry in the `dev` group; pin it for reproducibility like its neighbours.

### 6d. Impact on generated artifacts

Modest. The Python model grows 3,578 → 3,803 lines (+6%), against 19,151 under the import approach. `docs/elements/` gains 8 pages and loses 2 (`Term.md`, `tissue_modeled.md`); no docs filtering is needed. Generation time is unchanged.

### 6e. Run order

`just lint` → `just gen-project` → `just test`, then confirm the link-out landed:

```bash
grep "biolink:Cell" project/owl/namo.owl.ttl          # skos:exactMatch / owl:equivalentClass
grep "biolink:Cell" project/shacl/namo.shacl.ttl      # sh:class
grep -A1 '"Cell"' project/jsonld/namo.context.jsonld  # "@id": "biolink:Cell"
```

**Stage order:** 1 → 2 → 3 → 4 → 5. Stage 1 is blocking — the RDF dumper hard-fails on the undeclared ontology prefixes, and the `biolink` prefix must be left at `https://w3id.org/biolink/` (1a). Stage 3's `Term` deletion goes last within its stage. Stage 5 must land in the same commit as 3b or the suite goes red on three files.

---

## Stage 7 — Deferred: `Gene`, `Pathway`, `Study`, `Dataset`

Under the import approach these four were **blocking**: they collide with Biolink class names and generation silently emits Biolink's definitions instead of NAMO's. With no import there is no collision, so none of this blocks Issue 19. It is listed here because the modeling problems are real and worth their own issue.

| NAMO class | Line | Assessment |
|---|---|---|
| `Gene` | 1168 | Conflates the entity with differential-expression results (`fold_change`, `p_value`, `adjusted_p_value`). **Cannot** carry `class_uri: biolink:Gene` as written — that would assert a p-value is a property of a gene. Fix first by splitting: a `Gene` mapped to `biolink:Gene` for identity, plus a NAMO result class holding `gene: {range: Gene}` and the statistics |
| `Pathway` | 1196 | Same shape (`activity_score`, `enrichment_score` on the entity). Same split, then `class_uri: biolink:Pathway` |
| `Study` | 201 | Adds four attributes (`context_of_use`, `biological_context`, `perturbations`, `endpoints`) to what is recognisably Biolink's `study`. `class_uri: biolink:Study` is defensible — the pattern tolerates extra slots — but check the added slots do not contradict `study`'s `is_a: activity` semantics before asserting equivalence |
| `Dataset` | 180 | Same reasoning against Biolink's `dataset` (`is_a: information content entity`), holding `model_systems` / `studies` |

`NamedThing` stays as it is (`class_uri: schema:Thing`). Mapping it to `biolink:NamedThing` would assert that every NAMO entity carries Biolink's required `category`, which is false.

---

## Resolved decisions

D1 has been re-decided under the local-class approach; D2–D7 are unchanged in substance, with implementation details updated. D8 is new.

**D1 — Does NAMO's `NamedThing` become Biolink's `named thing`? → No; superseded.**
Under the import approach this was a "yes" and it drove the `category`-everywhere migration. With no import, NAMO's `NamedThing` is untouched and the Biolink-mapped classes hang off a separate abstract root, `BiolinkEntity` (2a). This is not merely a simplification: putting them under `NamedThing` would inherit the `type` designator and suppress the `rdf:type biolink:X` triple, defeating the alignment. Consequence: no `category` in any example file, and no `type` → `namo_type` rename.

**D2 — What does `AnimalModel.age` mean? → Split into `life_stage` + `age_value`.**
Implemented in 3a; binding follows in 4c. No data migration cost — no example file currently populates `age`.

**D3 — `AnimalModel.environment` → `EnvironmentalExposure`** (`class_uri: biolink:EnvironmentalExposure`), ECTO/ENVO CURIEs. No `category` needed in instance data.

**D4 — `OrganEnum` root → `UBERON:0000062` (organ).**
The stricter option, and the closure check in 4a confirms it is **safe**: all 11 distinct `organ_modeled` values validate, so no recuration is needed. The knock-on effect landed on the tissue slot instead — see 4b, where `UBERON:0000479` (tissue) fails 2 of 3 values. That, plus the fact that the values are organs and tracts rather than tissues, is what prompted the 3b rename to `anatomical_structure_modeled` with an `UBERON:0010000` root.

**D5 — Constrain `strain`? → No constraint beyond the class.**
`range: OrganismTaxon`, no `bindings`; empty `StrainEnum` deleted. Implemented in 4f.

**D6 — `TissueOnChip.tissue_modeled` → `anatomical_structure_modeled`, ranged over `GrossAnatomicalStructure`.**
Implemented in 3b, with its enum in 4b (`AnatomicalStructureEnum`, root `UBERON:0010000`) and its data migration in Stage 5.

**D7 — Fold `organ_modeled` into `anatomical_structure_modeled` as well? → No.**
`organ_modeled` keeps its own name and its own `OrganEnum` at the stricter `UBERON:0000062` root. `Organoid` and `OrganOnChip` continue to declare organs specifically; only `TissueOnChip` gets the broader slot. Two anatomy enums coexist by design — see the note at the end of 4b.

**D8 — OWL mapping predicate → `owl:equivalentClass`.**
Set `assert_equivalent_classes: true` in `config.yaml`; keep native URIs. Rationale in 6b.

---

## Cost summary

| | Local classes with `class_uri` (this plan) | Import `biolink-model` (rejected) |
|---|---|---|
| Example-file migration | 3 files, from a rename unrelated to Biolink | all 27 files: `category` on every term *and* every entity, plus `type` → `namo_type` |
| Class-name collisions to resolve | none | 5, failing silently (`NamedThing`, `Study`, `Dataset`, `Gene`, `Pathway`) |
| Generated Python model | 3,803 lines | 19,151 lines / 645 classes |
| Published JSON Schema | validates | non-validating for every `named thing` descendant |
| `just test` | passes | passes (only because it bypasses JSON Schema) |
| Blocking prerequisites | prefix map (Stage 1) | prefix map, collisions, type designator |
| Biolink structure inherited | none — equivalence assertion only | full hierarchy and slots |
| Biolink URIs in Python / RDF / SHACL / JSON-LD | yes | yes |

The one column the import approach wins is inherited structure, and NAMO does not consume it. Everything else favours local classes.

The residual risk is drift: NAMO asserts these equivalences unilaterally against Biolink 4.4.3 and nothing re-checks them. The mapping table in 2b is the artifact to review on every Biolink upgrade.
