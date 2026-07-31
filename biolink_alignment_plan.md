# NAMO → Biolink Alignment Plan

**Stage 1 of the broader Biolink alignment effort: replace the generic `Term` class by linking out to Biolink classes.**

- Tracking issue: [#19 — All instances of "Term" should be removed from schema.yaml and replaced with the appropriate Biolink class](https://github.com/monarch-initiative/namo/issues/19)
- Biolink Model version targeted: **4.4.3**
- Companion document: [`ontology_mapping_plan.md`](ontology_mapping_plan.md) (enum → ontology strategy)
- Status: **proposed** — no schema changes applied

---

## Approach

NAMO imports the published Biolink schema and uses Biolink's own classes as slot ranges. No local copies of Biolink classes, no mirrored hierarchy inside NAMO. The generic `Term` class is deleted outright.

An earlier draft of this plan proposed defining NAMO-local classes carrying `class_uri: biolink:X`. That was rejected: it recreates Biolink's classes and hierarchy inside NAMO rather than referencing them. The approach below genuinely links out — verified below.

The import drags in four prerequisites that are **not optional**. Those are Stages 1–2.

---

## Verified findings

Everything in this plan was probed end-to-end against the project toolchain before being written down.

| Check | Result |
|---|---|
| `imports: - https://w3id.org/biolink/biolink-model` | **Works.** `gen-python` exit 0 |
| Local `../biolink-model.yaml` as the import target | **Fails.** It declares `imports: [linkml:types, attributes]` and `attributes.yaml` is not present next to it (`FileNotFoundError: .../attributes.yaml`). The local copy is unusable as an import; it is fine as a reading reference |
| Do ranges actually resolve to Biolink? | **Yes.** `range: cell` → `class_class_uri = https://w3id.org/biolink/vocab/Cell`; `range: gross anatomical structure` → `.../GrossAnatomicalStructure`. Genuine link-out |
| Generation weight | Python model goes to **645 classes / 19,151 lines** (from 49 NAMO classes) |
| NAMO redefining `id` while importing biolink | **Hard failure:** `ValueError: Conflicting URIs (https://w3id.org/biolink/vocab/, …) for item: id` |
| NAMO overriding `category` locally (even with explicit `slot_uri`) | **Hard failure**, same `Conflicting URIs` error |
| Class-name collisions | **Silent corruption.** `gen-python` exits 0 but emits *two* `class NamedThing`, `class Study`, `class Dataset`, `class Gene`, `class Pathway`. Biolink's definition is emitted second and wins — confirmed `m.NamedThing.class_class_uri == https://w3id.org/biolink/vocab/NamedThing` |
| `category` on instance data | **Required** (Biolink's `named thing` sets `slot_usage: category: required: true`) |
| `category` written as a list | **Fails** the dataclass loader: `Wrong type designator value … ='['biolink:GrossAnatomicalStructure']'` |
| `category` written as a scalar | **Passes.** `yaml_loader.load(...)` returns a real `GrossAnatomicalStructure` |
| `linkml-validate` / JSON Schema path | **Broken for these classes** — `gen-json-schema` emits `{"type": "array", "enum": ["biolink:Cell"]}`, which no value can satisfy. Survivable because `just test` does not use it (see Stage 6) |

---

## Stage 1 — Wire up the import

### 1a. Fix the `biolink` prefix

`src/namo/schema/namo.yaml` line 152 declares:

```yaml
  biolink: https://w3id.org/biolink/
```

Biolink's own declaration is `https://w3id.org/biolink/vocab/`. Left as-is, every emitted Biolink URI is wrong.

### 1b. Add the import, pinned

Tracking `main` would let an upstream Biolink release break NAMO silently. Pin to the version this plan targets:

```yaml
imports:
  - linkml:types
  - https://raw.githubusercontent.com/biolink/biolink-model/v4.4.3/biolink-model.yaml
```

`https://w3id.org/biolink/biolink-model` also resolves and is what was tested; it is unpinned. Use it only to float with upstream.

### 1c. Add `default_curi_maps`

NAMO already uses `NCBITaxon:1`, `CL:0000000`, `BFO:0000050`, and `rdfs:subClassOf` in its `enums` block with none of those prefixes declared. Biolink resolves these via curi maps; NAMO needs the same:

```yaml
default_curi_maps:
  - obo_context
  - idot_context
  - monarch_context
  - semweb_context
```

---

## Stage 2 — Clear the collisions (blocking; do before Stage 3)

Importing Biolink means NAMO may not define any slot or class name Biolink already defines. There are nine.

### 2a. Delete NAMO's local `id`, `name`, `description` slot definitions

Lines 1388–1398. Biolink's `id` is already `identifier: true, required: true` — functionally identical to NAMO's. Keeping NAMO's kills `gen-python` outright.

### 2b. Rename NAMO's type designator

NAMO's `type: designates_type: true` collides with Biolink's `type` (which is `slot_uri: rdf:type`, multivalued, *not* a designator). Rename to `namo_type` — verified working.

**This is a data migration:** every example file's `type: "OrganOnChip"` becomes `namo_type: "OrganOnChip"`.

### 2c. Resolve five class-name collisions

This is the dangerous one — generation succeeds and the wrong classes silently win, which would make `tests/test_data.py`'s `getattr(namo.datamodel.namo, target_class_name)` return Biolink's class instead of NAMO's.

| NAMO class | Line | Resolution |
|---|---|---|
| `NamedThing` | 191 | **Adopt Biolink's `named thing`.** NAMO's version (`class_uri: schema:Thing`, slots id/name/description/type) is itself a re-creation of Biolink's — exactly what this plan sets out to stop. See **D1**: this forces `category` onto every NAMO entity |
| `Study` | 201 | `is_a: study` (Biolink's, `is_a: activity`), keeping NAMO's four attributes (`context_of_use`, `biological_context`, `perturbations`, `endpoints`) as additions. Extending ≠ recreating |
| `Dataset` | 180 | `is_a: dataset` (Biolink's, `is_a: information content entity`), keeping `model_systems` / `studies` |
| `Gene` | 1168 | NAMO's `Gene` conflates the entity with differential-expression results (`fold_change`, `p_value`, `adjusted_p_value`). Split: use Biolink `gene` for identity, move the statistics to a NAMO-specific result class holding `gene: {range: gene}` |
| `Pathway` | 1196 | Same shape (`activity_score`, `enrichment_score` on the entity). Use Biolink `pathway`; move statistics to a NAMO result class |

Stage 2c is wider than Issue 19, but it is not optional — it is the price of the import, and skipping it produces a schema that generates cleanly and is quietly wrong.

---

## Stage 3 — Repoint the 17 `Term` ranges at Biolink classes

Biolink class names are lowercase-with-spaces in LinkML source. `inlined` / `inlined_as_list` / `multivalued` / `required` flags all stay as they are.

| Line | Owner | Attribute | `range: Term` → | Rationale |
|---|---|---|---|---|
| 247 | `AnimalModel` | `species` | `organism taxon` | `values_from: NCBITaxon`; matches existing `SpeciesEnum` |
| 256 | `AnimalModel` | `strain` | `organism taxon` | Biolink has **no** Strain class; `organism taxon` docs: "Can also be used to represent strains or subspecies" |
| 264 | `AnimalModel` | `age` | `life stage` | See **D2** |
| 272 | `AnimalModel` | `environment` | `environmental exposure` | `is_a: exposure event`; ECTO/ENVO CURIEs. See **D3** |
| 322 | `CellularSystem` | `cell_types` | `cell` | See deviation note below |
| 406 | `Organoid` | `organ_modeled` | `gross anatomical structure` | Per Issue 19; Biolink aliases it 'tissue', 'organ' |
| 482 | `OrganOnChip` | `organ_modeled` | `gross anatomical structure` | Per Issue 19 |
| 491 | `OrganOnChip` | `cell_types` | `cell` | Same concept as line 322 |
| 515 | `TissueOnChip` | `tissue_modeled` | `gross anatomical structure` | Per Issue 19 |
| 588 | `PBPKModel` | `species_modeled` | `organism taxon` | Per Issue 19 |
| 669 | `CellRatio` | `cell_type` | `cell` | Not in Issue 19 |
| 1055 | `PhenotypeOverlap` | `shared_phenotypes` | `phenotypic feature` | Per Issue 19 |
| 1061 | `PhenotypeOverlap` | `model_specific_phenotypes` | `phenotypic feature` | Per Issue 19 |
| 1067 | `PhenotypeOverlap` | `biological_specific_phenotypes` | `phenotypic feature` | Per Issue 19 |
| 1086 | `CellTypeCoverage` | `represented_cell_types` | `cell` | Not in Issue 19 |
| 1092 | `CellTypeCoverage` | `missing_cell_types` | `cell` | Not in Issue 19 |
| 1270 | `CellTypeProportion` | `cell_type` | `cell` | Not in Issue 19 |

Then **delete the `Term` class** (lines 1380–1385) — last in the stage, so `just lint` catches any missed reference.

### Deviation from Issue 19

The issue asks for `cell_types` → `biolink:anatomical_entity`. Biolink's own `anatomical entity` description says the opposite:

> This is a grouping class with three concrete subclasses that should be preferred when applicable: `biolink:Cell` for whole cells, `biolink:CellularComponent` for subcellular and intracellular structures, and `biolink:GrossAnatomcialStructure` for multicellular parts.

`CellTypeEnum` is already rooted at `CL:0000000`, so **`cell` is correct and more specific.** Worth a note on the issue before closing it.

---

## Stage 4 — Enum and binding alignment

### 4a. `OrganEnum` is too broad

It is currently `reachable_from: UBERON:0001062` — the anatomy root, which includes cells and subcellular parts. Biolink's `gross anatomical structure` maps to `UBERON:0010000`:

```yaml
  OrganEnum:
    reachable_from:
      source_nodes:
        - UBERON:0010000      # multicellular anatomical structure
      is_direct: false
      relationship_types:
        - rdfs:subClassOf
        - BFO:0000050         # part_of
```

The only *tightening* change in the plan — see **D4**.

### 4b. Add `TissueEnum`, bind `TissueOnChip.tissue_modeled`

Currently unbound:

```yaml
  TissueEnum:
    reachable_from:
      source_nodes:
        - UBERON:0000479      # tissue
      is_direct: false
      relationship_types:
        - rdfs:subClassOf
```

### 4c. Fix the dangling `OrganismAgeEnum`

`AnimalModel.age` binds `OrganismAgeEnum`, which **is never defined anywhere in the schema** — only an empty `AgeEnum` exists. Replace with an enum matching the `life stage` range, and delete the unused `AgeEnum`:

```yaml
  LifeStageEnum:
    reachable_from:
      source_nodes:
        - UBERON:0000105      # life cycle stage
      is_direct: false
      relationship_types:
        - rdfs:subClassOf
```

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

### 4f. `StrainEnum` is empty

With `strain` ranging over `organism taxon`, the coherent option is `reachable_from: NCBITaxon:1`; LinkML dynamic enums cannot filter by taxonomic rank, so this will not actually restrict to strain-rank nodes. See **D5**.

---

## Stage 5 — Migrate example and test data

Unlike the rejected local-class approach, importing Biolink **does** require touching instance data. Three mechanical edits across `tests/data/valid/`, `tests/data/invalid/`, and `examples/output/`:

1. **Add `category` to every ontology reference**, scalar form (verified — the list form fails the type-designator check):

   ```yaml
   organ_modeled:
     id: "UBERON:0001005"
     name: "respiratory airway"
     category: "biolink:GrossAnatomicalStructure"   # <- new, scalar not list
   cell_types:
     - id: "CL:0002632"
       name: "epithelial cell of lower respiratory tract"
       category: "biolink:Cell"
   ```

2. **`type:` → `namo_type:`** on every top-level object (from 2b).

3. **If D1 lands as recommended** (NAMO `NamedThing` adopts Biolink's), every NAMO entity also needs its own `category`, e.g. `category: "namo:OrganOnChip"`.

`name:` is preserved throughout, so the CLAUDE.md convention of including both `id` and `name` for clarity survives. This is scriptable — worth a one-off migration script rather than 40 hand edits, and `examples/output/` is regenerated by `_ensure_examples_output` anyway.

---

## Stage 6 — Validation and impact

- **`just test` still works.** `_test-python` loads via `yaml_loader` + generated dataclasses, and `_test-examples` uses `linkml-run-examples` — neither goes through JSON Schema, so the `category` array/enum defect does not break the suite. The dataclass path was confirmed to load cleanly with scalar `category`.
- **But `project/namo.schema.json` becomes non-validating** for any class descending from Biolink `named thing`, because `gen-json-schema` emits `{"type": "array", "enum": [...]}` for `category`. That is an upstream LinkML defect, not something NAMO can override (the `category` override fails `gen-python`). Anyone consuming the published JSON Schema will hit it — this deserves an upstream issue against `linkml`, plus a note in the NAMO docs.
- **Generated artifacts balloon:** 49 → 645 Python classes, ~19k lines. Expect `just gen-project` and `just gen-doc` to slow substantially, and `docs/elements/` to gain hundreds of pages unless `gen-doc` is constrained. Worth deciding whether the docs build should be filtered to NAMO-defined classes only.
- **Run order:** `just lint` → `just gen-project` → `just test`, then grep the OWL output for `https://w3id.org/biolink/vocab/Cell` to confirm Stage 1a landed.
- **Stage order:** 1 → 2 → 3 (Term deletion last) → 4 → 5. Stage 2 before 3 is mandatory; Stage 5 must land in the same commit as 2b/3 or the suite goes red.

---

## Open decisions

**D1 — Does NAMO's `NamedThing` become Biolink's `named thing`?**
The directive to stop recreating Biolink classes points at NAMO's `NamedThing` directly. But adopting Biolink's forces `category` onto *every* NAMO entity in every example file (Stage 5, item 3). Lower-churn fallback: rename NAMO's to something non-colliding and keep it independent — resolves the crash but leaves the duplication in place. Recommendation: adopt Biolink's; it is the only version consistent with the directive.

**D2 — What does `AnimalModel.age` mean?**
If *developmental stage* ("adult", "P21"), `life stage` is right. If *chronological age* ("8 weeks"), no ontology-term class fits — that wants `biolink:QuantityValue`. Cleanest: split into `life_stage` + `age_value`. Default if unspecified: `life stage`.

**D3 — `AnimalModel.environment`**
`environmental exposure` (an exposure *event*, ECTO-flavoured — recommended) vs. `environmental feature` (a planetary entity, `ENVO:01000254`, i.e. the physical facility).

**D4 — `OrganEnum` root**
`UBERON:0010000` (multicellular anatomical structure — safe, still correct; recommended) vs. `UBERON:0000062` (organ — stricter, but rejects `UBERON:0001005`, which `OrganOnChip-example-001.yaml` currently uses).

**D5 — Constrain `strain`?**
`NCBITaxon:1`-rooted binding (cannot restrict to strain rank) vs. no binding vs. adding `RS` / JAX identifiers as an extra source.

---

## Cost summary

This approach costs materially more than defining local Biolink-shaped classes: a required data migration, five class collisions to resolve, a 13× larger generated model, and a broken published JSON Schema. It is, however, the only way to genuinely reference Biolink rather than copy it.

Note also that Stage 2 grows the blast radius beyond `Term`: `Gene`, `Pathway`, `Study`, `Dataset`, and `NamedThing` all have to be settled before the `Term` work can land safely.
