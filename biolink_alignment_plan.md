# NAMO → Biolink Alignment Plan

**Phase 1 of the broader Biolink alignment effort: replace the generic `Term` class by linking out to Biolink classes.** (The numbered Stages 1–6 below are the steps *within* this phase.)

- Tracking issue: [#19 — All instances of "Term" should be removed from schema.yaml and replaced with the appropriate Biolink class](https://github.com/monarch-initiative/namo/issues/19)
- Biolink Model version targeted: **4.4.3**
- Companion document: [`ontology_mapping_plan.md`](ontology_mapping_plan.md) (enum → ontology strategy)
- Status: **approved, ready to execute.** All seven design decisions (D1–D7) are resolved and folded into the stages below. No schema changes have been made yet.

---

## Approach

NAMO imports the published Biolink schema and uses Biolink's own classes as slot ranges. No local copies of Biolink classes, no mirrored hierarchy inside NAMO. The generic `Term` class is deleted outright.

An earlier draft proposed defining NAMO-local classes carrying `class_uri: biolink:X`. That was rejected: it recreates Biolink's classes and hierarchy inside NAMO rather than referencing them. The approach below genuinely links out — verified below.

The import drags in prerequisites that are **not optional** — a wrong prefix, missing curi maps, and nine name collisions with Biolink. Those are Stages 1–2, and they must land before any `Term` range is touched.

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
| `oaklib` installed? | **Yes** — 0.6.23, declared in `[dependency-groups] dev`, resolved in `uv.lock`. Used to compute the closure checks in 4a / 4b against Ubergraph |

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

**Interaction with D1 — verify early.** Because NAMO classes now inherit from Biolink `named thing` (2c), they inherit Biolink's `category`, which is *also* `designates_type: true`. That leaves two type designators on the same class: inherited `category` and declared `namo_type`. Confirm LinkML tolerates this as the first action in Stage 2. If it does not, drop `namo_type` entirely and use `category: "namo:OrganOnChip"` as the sole designator — which is arguably the better end state anyway, and removes migration item 2 from Stage 5.

### 2c. Resolve five class-name collisions

This is the dangerous one — generation succeeds and the wrong classes silently win, which would make `tests/test_data.py`'s `getattr(namo.datamodel.namo, target_class_name)` return Biolink's class instead of NAMO's.

| NAMO class | Line | Resolution |
|---|---|---|
| `NamedThing` | 191 | **Delete it; adopt Biolink's `named thing`** (per D1). Every NAMO class currently declaring `is_a: NamedThing` becomes `is_a: named thing`. NAMO's version (`class_uri: schema:Thing`, slots id/name/description/type) was itself a re-creation of Biolink's — exactly what this plan sets out to stop |
| `Study` | 201 | `is_a: study` (Biolink's, `is_a: activity`), keeping NAMO's four attributes (`context_of_use`, `biological_context`, `perturbations`, `endpoints`) as additions. Extending ≠ recreating |
| `Dataset` | 180 | `is_a: dataset` (Biolink's, `is_a: information content entity`), keeping `model_systems` / `studies` |
| `Gene` | 1168 | NAMO's `Gene` conflates the entity with differential-expression results (`fold_change`, `p_value`, `adjusted_p_value`). Split: use Biolink `gene` for identity, move the statistics to a NAMO-specific result class holding `gene: {range: gene}` |
| `Pathway` | 1196 | Same shape (`activity_score`, `enrichment_score` on the entity). Use Biolink `pathway`; move statistics to a NAMO result class |

Stage 2c is wider than Issue 19, but it is not optional — it is the price of the import, and skipping it produces a schema that generates cleanly and is quietly wrong.

---

## Stage 3 — Repoint the 17 `Term` ranges at Biolink classes

Biolink class names are lowercase-with-spaces in LinkML source. `inlined` / `inlined_as_list` / `multivalued` / `required` flags all stay as they are. Two slots change beyond their range: `age` is split (3a) and `tissue_modeled` is renamed (3b).

| Line | Owner | Attribute | `range: Term` → | Rationale |
|---|---|---|---|---|
| 247 | `AnimalModel` | `species` | `organism taxon` | `values_from: NCBITaxon`; matches existing `SpeciesEnum` |
| 256 | `AnimalModel` | `strain` | `organism taxon` | Biolink has **no** Strain class; `organism taxon` docs: "Can also be used to represent strains or subspecies". Binding dropped per D5 — see 4f |
| 264 | `AnimalModel` | `age` | **removed** — split into `life_stage` + `age_value` | Per D2; see 3a |
| 272 | `AnimalModel` | `environment` | `environmental exposure` | Per D3. `is_a: exposure event`; ECTO/ENVO CURIEs |
| 322 | `CellularSystem` | `cell_types` | `cell` | See deviation note below |
| 406 | `Organoid` | `organ_modeled` | `gross anatomical structure` | Per Issue 19; Biolink aliases it 'tissue', 'organ' |
| 482 | `OrganOnChip` | `organ_modeled` | `gross anatomical structure` | Per Issue 19 |
| 491 | `OrganOnChip` | `cell_types` | `cell` | Same concept as line 322 |
| 515 | `TissueOnChip` | `tissue_modeled` → **renamed** `anatomical_structure_modeled` | `gross anatomical structure` | Per Issue 19; rename per 3b |
| 588 | `PBPKModel` | `species_modeled` | `organism taxon` | Per Issue 19 |
| 669 | `CellRatio` | `cell_type` | `cell` | Not in Issue 19 |
| 1055 | `PhenotypeOverlap` | `shared_phenotypes` | `phenotypic feature` | Per Issue 19 |
| 1061 | `PhenotypeOverlap` | `model_specific_phenotypes` | `phenotypic feature` | Per Issue 19 |
| 1067 | `PhenotypeOverlap` | `biological_specific_phenotypes` | `phenotypic feature` | Per Issue 19 |
| 1086 | `CellTypeCoverage` | `represented_cell_types` | `cell` | Not in Issue 19 |
| 1092 | `CellTypeCoverage` | `missing_cell_types` | `cell` | Not in Issue 19 |
| 1270 | `CellTypeProportion` | `cell_type` | `cell` | Not in Issue 19 |

Then **delete the `Term` class** (lines 1380–1385) — last in the stage, so `just lint` catches any missed reference.

### 3a. Split `AnimalModel.age` (per D2)

`age` conflated developmental stage with chronological age. Replace the single slot with two:

```yaml
      life_stage:
        range: life stage
        inlined: true
        description: >-
          The developmental or life-cycle stage of the animal used in the model system.
        bindings:
          - binds_value_of: id
            range: LifeStageEnum
            obligation_level: REQUIRED
      age_value:
        range: quantity value
        inlined: true
        description: >-
          Chronological age of the animal at the time of study, as a numeric value
          with a unit.
```

Useful property of `quantity value`: it is `is_a: annotation`, **not** a descendant of `named thing`. It has no `id` and no `category`, so it is inlined by value and needs no `category` in instance data. Its slots are `has numeric value` (range `double`) and `has unit` (range `unit`, a string type with `id_prefixes: [UO]`):

```yaml
life_stage:
  id: "MmusDv:0000110"
  name: "adult stage"
  category: "biolink:LifeStage"
age_value:
  has_numeric_value: 8.0
  has_unit: "UO:0000034"      # week
```

No current example file populates `age`, so this split costs no data migration.

### 3b. Rename `TissueOnChip.tissue_modeled` → `anatomical_structure_modeled`

The old name asserted "tissue" while the data holds an organ (`skin of body`), a barrier (`blood-brain barrier`), and a tract (`digestive tract`) — see the closure results in 4b. The new name matches both the data and the Biolink class it now ranges over:

```yaml
      anatomical_structure_modeled:
        range: gross anatomical structure
        inlined: true
        description: >-
          The anatomical structure being modeled — a tissue, organ, or other
          multicellular structure.
        bindings:
          - binds_value_of: id
            range: AnatomicalStructureEnum
            obligation_level: REQUIRED
```

The Biolink mapping *is* the range: `gross anatomical structure` resolves to `class_class_uri = https://w3id.org/biolink/vocab/GrossAnatomicalStructure` (verified). No separate `exact_mappings` entry is needed on the slot.

**Migration cost of the rename** — 3 hand-maintained files plus 1 hand-written doc; everything else regenerates:

| Path | Kind |
|---|---|
| `tests/data/valid/TissueOnChip-example-001.yaml` | hand-edit (1 occurrence) |
| `tests/data/valid/TissueOnChip-example-002.yaml` | hand-edit (1 occurrence) |
| `tests/data/valid/TissueOnChip-example-003.yaml` | hand-edit (1 occurrence) |
| `docs/how-to/curate.md` | hand-edit — the `TissueOnChip` row of the model-class table, line 88, lists `tissue_modeled` as a required field |
| `docs/elements/*`, `docs/schema/namo.yaml`, `examples/output/*`, `project/*`, `src/namo/datamodel/*` | **generated** — `just gen-project` / `gen-doc` / `_ensure_examples_output` rewrite these; do not hand-edit |

Note `docs/elements/tissue_modeled.md` and `docs/elements/Term.md` are generated pages that will disappear on the next `just gen-doc`; if `docs/` is version-controlled, expect deletions in the diff.

### 3c. Deviation from Issue 19 on `cell_types`

The issue asks for `cell_types` → `biolink:anatomical_entity`. Biolink's own `anatomical entity` description says the opposite:

> This is a grouping class with three concrete subclasses that should be preferred when applicable: `biolink:Cell` for whole cells, `biolink:CellularComponent` for subcellular and intracellular structures, and `biolink:GrossAnatomcialStructure` for multicellular parts.

`CellTypeEnum` is already rooted at `CL:0000000`, so **`cell` is correct and more specific.** Worth a note on the issue before closing it.

---

## Stage 4 — Enum and binding alignment

**`oaklib` (0.6.23) is now a dev dependency**, so closure checks can be computed — 4a and 4b below report real results against Ubergraph rather than expectations.

**But nothing in `just test` yet enforces these enums.** `_test-python` uses `yaml_loader` + dataclasses and `_test-examples` uses `linkml-run-examples`; neither expands a `reachable_from` enum or checks a `bindings` block. NAMO's enum constraints are therefore declared but **unenforced at test time**, and will stay that way until a validation step is wired into the suite. So the tightening in 4a carries no immediate CI risk — and equally, 4a–4f should not be considered done until that step exists. Adding it is tracked in Stage 6.

### 4a. Narrow `OrganEnum` to `UBERON:0000062` (organ) — per D4

Currently `reachable_from: UBERON:0001062`, the anatomy root, which includes cells and subcellular parts. Biolink's `gross anatomical structure` maps to `UBERON:0010000`; D4 chose the stricter `UBERON:0000062`:

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

**D4 requires no data recuration.** Note in particular that `UBERON:0001005` ("respiratory airway") *passes* — an earlier draft of this plan flagged it as at-risk on the assumption it was a conduit outside the organ closure. It is reachable, so `OrganOnChip-example-001.yaml` is fine as written. Including `BFO:0000050` (`part_of`) in `relationship_types` is what carries `bronchiole` and `alveolus of lung`; dropping it would break both.

### 4b. Add `AnatomicalStructureEnum`, bind `anatomical_structure_modeled`

The slot (renamed in 3b) is currently unbound. The obvious root for the old `tissue_modeled` name was `UBERON:0000479` (tissue), but the closure check says that fails on real data. `descendants(UBERON:0000479, [IS_A, PART_OF])` = 6,435 terms, and of the three distinct values only one is inside it:

| Value | Label | File | `UBERON:0000479` (tissue) | `UBERON:0000062` (organ) | `UBERON:0010000` |
|---|---|---|---|---|---|
| `UBERON:0000120` | blood-brain barrier | `TissueOnChip-example-001.yaml` | **PASS** | FAIL | PASS |
| `UBERON:0002097` | skin of body | `TissueOnChip-example-003.yaml` | FAIL | PASS | PASS |
| `UBERON:0001555` | digestive tract | `TissueOnChip-example-002.yaml` | FAIL | FAIL | PASS |

No organ-or-tissue combination covers all three: `digestive tract` is outside both. Only `UBERON:0010000` (multicellular anatomical structure) covers the set — which is also exactly what Biolink's `gross anatomical structure` maps to, so it is the right root and it lines up with the slot's new name:

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

**`organ_modeled` stays separate** (per D7). It keeps its own name, its own `OrganEnum`, and the stricter `UBERON:0000062` root from 4a, even though it shares the `gross anatomical structure` range with `anatomical_structure_modeled`. Two enums therefore coexist by design: `OrganEnum` (organ closure, for `Organoid` and `OrganOnChip`) and `AnatomicalStructureEnum` (multicellular-structure closure, for `TissueOnChip`). The stricter organ constraint is a feature of this split, not an inconsistency to reconcile.

### 4c. Add `LifeStageEnum`, drop the dangling `OrganismAgeEnum`

`AnimalModel.age` bound `OrganismAgeEnum`, which **is never defined anywhere in the schema** — only an empty `AgeEnum` exists. With `age` now split (3a), the binding moves to the new `life_stage` slot. Delete the unused `AgeEnum` and the dangling `OrganismAgeEnum` reference:

```yaml
  LifeStageEnum:
    reachable_from:
      source_nodes:
        - UBERON:0000105      # life cycle stage
      is_direct: false
      relationship_types:
        - rdfs:subClassOf
```

`age_value` takes no binding — it is a `quantity value`, not an ontology term.

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

`AnimalModel.strain` becomes `range: organism taxon` with **no `bindings` block**. The empty `StrainEnum` is deleted rather than populated. Strain identity is carried by whatever CURIE the curator supplies — NCBITaxon strain-rank nodes, RS, JAX — constrained only by `organism taxon`'s own `id_prefixes` (`NCBITaxon`, `MESH`, `UMLS`). This was the right call regardless of preference: LinkML dynamic enums cannot filter by taxonomic rank, so an `NCBITaxon:1`-rooted `StrainEnum` would have been indistinguishable from `SpeciesEnum` and enforced nothing useful.

---

## Stage 5 — Migrate example and test data

Unlike the rejected local-class approach, importing Biolink **does** require touching instance data. Scope: the **27 files in `tests/data/valid/`** (`tests/data/invalid/` is currently empty, and `examples/output/` regenerates):

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

2. **`type:` → `namo_type:`** on every top-level object (from 2b) — *unless* the 2b designator check sends us to `category` instead, in which case this becomes `type: "OrganOnChip"` → `category: "namo:OrganOnChip"` and item 3 is subsumed.

3. **Add `category` to every NAMO entity too.** Unconditional, per D1: NAMO classes now descend from Biolink `named thing`, which requires `category`. E.g. a top-level `OrganOnChip` gains `category: "namo:OrganOnChip"`.

4. **Rename `tissue_modeled:` → `anatomical_structure_modeled:`** in the three `TissueOnChip-example-*.yaml` files, and update the `TissueOnChip` row of `docs/how-to/curate.md` (line 88). Full inventory in 3b.

5. **No anatomy recuration needed.** The closure checks confirm all 11 `organ_modeled` values pass `UBERON:0000062` and all 3 `anatomical_structure_modeled` values pass `UBERON:0010000`.

`name:` is preserved throughout, so the CLAUDE.md convention of including both `id` and `name` for clarity survives. Items 1–4 are mechanical and should be a one-off migration script rather than 27 hand edits; `examples/output/` is regenerated by `_ensure_examples_output` anyway.

---

## Stage 6 — Validation and impact

- **`just test` still works.** `_test-python` loads via `yaml_loader` + generated dataclasses, and `_test-examples` uses `linkml-run-examples` — neither goes through JSON Schema, so the `category` array/enum defect does not break the suite. The dataclass path was confirmed to load cleanly with scalar `category`.
- **But `project/namo.schema.json` becomes non-validating** for any class descending from Biolink `named thing`, because `gen-json-schema` emits `{"type": "array", "enum": [...]}` for `category`. That is an upstream LinkML defect, not something NAMO can override (the `category` override fails `gen-python`). Anyone consuming the published JSON Schema will hit it — this deserves an upstream issue against `linkml`, plus a note in the NAMO docs.
- **Wire enum validation into the test suite.** `oaklib` 0.6.23 is now a dev dependency, so closure checks are runnable ad hoc (4a, 4b) — but no `just test` step expands dynamic enums or enforces `bindings`, so Stage 4's constraints remain unenforced in CI. Add a step that validates the `reachable_from` enums and `bindings` against the example data, otherwise these enums are documentation rather than validation. Minor: `oaklib` is the only unpinned entry in the `dev` group; pin it for reproducibility like its neighbours.
- **Generated artifacts balloon:** 49 → 645 Python classes, ~19k lines. Expect `just gen-project` and `just gen-doc` to slow substantially, and `docs/elements/` to gain hundreds of pages unless `gen-doc` is constrained. Worth deciding whether the docs build should be filtered to NAMO-defined classes only.
- **Run order:** `just lint` → `just gen-project` → `just test`, then grep the OWL output for `https://w3id.org/biolink/vocab/Cell` to confirm Stage 1a landed.
- **Stage order:** 1 → 2 (designator check first) → 3 (Term deletion last) → 4 → 5. Stage 2 before 3 is mandatory; Stage 5 must land in the same commit as 2b/2c/3 or the suite goes red.

---

## Resolved decisions

All seven are settled; their consequences are folded into Stages 2–5 above. Recorded here for provenance — nothing in this plan is left to decide at execution time.

**D1 — Does NAMO's `NamedThing` become Biolink's `named thing`? → Yes.**
NAMO's own `NamedThing` is deleted and every `is_a: NamedThing` becomes `is_a: named thing` (2c). Commits us to `category` on *every* NAMO entity in every example file (Stage 5 item 3, now unconditional) and raises the two-designator question handled in 2b.

**D2 — What does `AnimalModel.age` mean? → Split into `life_stage` + `age_value`.**
Implemented in 3a; binding follows in 4c. No data migration cost — no example file currently populates `age`.

**D3 — `AnimalModel.environment` → `environmental exposure`.**
Biolink `environmental exposure`, `is_a: exposure event`, ECTO/ENVO CURIEs. It descends from `named thing`, so instances need `category: "biolink:EnvironmentalExposure"`.

**D4 — `OrganEnum` root → `UBERON:0000062` (organ).**
The stricter option, and the closure check in 4a confirms it is **safe**: all 11 distinct `organ_modeled` values validate, so no recuration is needed. The knock-on effect landed on the tissue slot instead — see 4b, where `UBERON:0000479` (tissue) fails 2 of 3 values. That, plus the fact that the values are organs and tracts rather than tissues, is what prompted the 3b rename to `anatomical_structure_modeled` with an `UBERON:0010000` root.

**D5 — Constrain `strain`? → No constraint beyond the class.**
`range: organism taxon`, no `bindings`; empty `StrainEnum` deleted. Implemented in 4f.

**D6 — `TissueOnChip.tissue_modeled` → `anatomical_structure_modeled`, ranged over `gross anatomical structure`.**
Implemented in 3b, with its enum in 4b (`AnatomicalStructureEnum`, root `UBERON:0010000`) and its data migration in Stage 5 item 4.

**D7 — Fold `organ_modeled` into `anatomical_structure_modeled` as well? → No.**
`organ_modeled` keeps its own name and its own `OrganEnum` at the stricter `UBERON:0000062` root. `Organoid` and `OrganOnChip` continue to declare organs specifically; only `TissueOnChip` gets the broader slot. Two anatomy enums coexist by design — see the note at the end of 4b.

---

## Cost summary

This approach costs materially more than defining local Biolink-shaped classes: a required data migration, five class collisions to resolve, a 13× larger generated model, and a broken published JSON Schema. It is, however, the only way to genuinely reference Biolink rather than copy it.

Note also that Stage 2 grows the blast radius beyond `Term`: `Gene`, `Pathway`, `Study`, `Dataset`, and `NamedThing` all have to be settled before the `Term` work can land safely.
