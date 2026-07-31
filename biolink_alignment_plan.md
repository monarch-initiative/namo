# NAMO → Biolink Alignment Plan

**Phase 1 of the broader Biolink alignment effort: replace the generic `Term` class by linking out to Biolink classes.** (The numbered Stages 1–6 below are the steps *within* this phase.)

- Tracking issue: [#19 — All instances of "Term" should be removed from schema.yaml and replaced with the appropriate Biolink class](https://github.com/monarch-initiative/namo/issues/19)
- Biolink Model version targeted: **4.4.3**
- Companion document: [`ontology_mapping_plan.md`](ontology_mapping_plan.md) (enum → ontology strategy)
- Status: **Stages 1–4 applied; Stage 5 is the remaining work.** All seven design decisions (D1–D7) are resolved and folded into the stages below. The schema generates cleanly and every enum reference resolves. The test suite is red — 27/27 — entirely on instance data that Stage 5 migrates; see Stage 3's closing note for the breakdown.

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
| Bare URL import under `SchemaView` | **Fails.** `ValueError: Unknown CURIE prefix: https` — import strings are CURIE-expanded, so only `prefix:name` works. `gen-python` (SchemaLoader) accepts URLs; most other generators do not. Drove the 1b revision |
| Nested relative import (`biolink-model` → `attributes`) | **Resolves against the root schema's directory**, not the importing file's. Any non-co-located biolink-model looks for `attributes.yaml` beside `namo.yaml` and fails. Forced vendoring — see 1b |
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
| `is_a: <biolink class>` to resolve a same-name collision | **Does not work, and is worse than shadowing.** A NAMO class named `Dataset` deriving from Biolink's `dataset` fails with `ValueError: Cyclic wrapper inheritance at DatasetId`. The collision is on the *name*, independent of parentage — so renaming is forced. Corrected step 2c |
| Two type designators on one class (`namo_type` + inherited `category`) | **Generates, but both stay live and must agree per instance.** `namo_type: OrganOnChip` + `category: ...ModelSystem` dispatched on `namo_type`, then failed the `category` check. Resolved by deleting `type` outright — see 2b |
| `gen-project` from the repo root | **Fails.** Resolves Biolink's nested `attributes` import against the *invocation cwd* (`<repo>/attributes.yaml`), unlike `gen-python` (schema dir) and `SchemaView` (root-schema dir). Three different behaviours in one toolchain. Fix verified: run from the schema directory — see 1e |

---

## Stage 1 — Wire up the import ✅ DONE

Applied and verified. `SchemaView` loads `namo.yaml` with an import closure of `['linkml:types', 'attributes', 'biolink-model', 'namo']` and 383 visible classes; all seven Biolink classes needed as Stage 3 ranges resolve. `gen-python` now fails **only** with the expected Stage 2a collision — `ValueError: Conflicting URIs (https://w3id.org/biolink/vocab/, https://w3id.org/monarch-initiative/namo) for item: id` — which is the documented intermediate state until Stage 2 lands. 1b was revised during execution; see below.

### 1a. Fix the `biolink` prefix

`src/namo/schema/namo.yaml` line 152 declares:

```yaml
  biolink: https://w3id.org/biolink/
```

Biolink's own declaration is `https://w3id.org/biolink/vocab/`. Left as-is, every emitted Biolink URI is wrong.

### 1b. Add the import — vendored, pinned to v4.4.3

**Revised during execution.** This step originally specified a pinned remote URL. That does not work: two LinkML import-resolution behaviours, both verified, rule it out.

1. **`SchemaView` cannot resolve bare URL imports.** It runs every import string through CURIE expansion, so `https://…` fails with `ValueError: Unknown CURIE prefix: https`. Only `prefix:name` form is accepted. (`gen-python` uses the older `SchemaLoader` and *does* accept URLs — which is why the first probe looked fine. Most of the toolchain, including `gen-doc`, `gen-pydantic` and `gen-json-schema`, is SchemaView-based.)
2. **Nested relative imports resolve against the root schema's directory, not the importing file's.** `biolink-model.yaml` declares `imports: [linkml:types, attributes]`. However biolink-model is reached, LinkML then looks for `attributes.yaml` next to `namo.yaml` and fails. Introducing a `biolink_source:` prefix fixes (1) but not (2).

So both files are vendored into `src/namo/schema/`, beside `namo.yaml`:

```yaml
imports:
  - linkml:types
  - biolink-model          # no .yaml - LinkML appends it
```

| Vendored file | Size | Source |
|---|---|---|
| `src/namo/schema/biolink-model.yaml` | 518 KB | `raw.githubusercontent.com/biolink/biolink-model/v4.4.3/biolink-model.yaml` |
| `src/namo/schema/attributes.yaml` | 15 KB | `raw.githubusercontent.com/biolink/biolink-model/v4.4.3/attributes.yaml` |

Both are byte-identical to upstream v4.4.3 and must stay that way — the repo hygiene changes in 1d exist to guarantee it. They must also stay in this directory; moving them to a subdirectory reintroduces problem (2).

Upside beyond making it work: the pin is now structural rather than a URL that could be edited or rot, and `just test` no longer needs network access.

> **MAINTENANCE — bumping the Biolink version.** Re-download *both* files at the same tag, confirm `version:` in `biolink-model.yaml` matches, and re-run the 4a/4b closure checks (UBERON roots may shift between releases). Update the version references in this document, in the `imports:` comment in `namo.yaml`, and in the two `pyproject.toml` exclude comments.

### 1c. Add `default_curi_maps`

NAMO already uses `NCBITaxon:1`, `CL:0000000`, `BFO:0000050`, and `rdfs:subClassOf` in its `enums` block with none of those prefixes declared. Biolink resolves these via curi maps; NAMO needs the same:

```yaml
default_curi_maps:
  - obo_context
  - idot_context
  - monarch_context
  - semweb_context
```

Verified after the change: `NCBITaxon`, `CL`, `BFO`, `rdfs`, `HP`, `MP`, `UBERON`, `UO`, `HsapDv`, `MmusDv`, `ECTO` and `ENVO` all resolve through `SchemaView.namespaces()`.

### 1d. Repo hygiene forced by vendoring

Dropping two upstream files into a directory the tooling treats as "ours" has four consequences. All four are addressed; none is optional.

| Change | Why |
|---|---|
| `justfile`: `lint` now targets `{{source_schema_path}}`, not `{{source_schema_dir}}` | `linkml-lint` on a directory recursively lints *every* YAML in it, so it would have linted the vendored Biolink schema as two additional schemas |
| `.pre-commit-config.yaml`: top-level `exclude` for both vendored files | `trailing-whitespace` and `end-of-file-fixer` would **rewrite** them, destroying byte-fidelity with upstream; `yamllint` reports 1,538 problems in them; `codespell`/`typos` flag upstream prose |
| `pyproject.toml`: both files added to `[tool.codespell] skip` and `[tool.typos.files] extend-exclude` | Same reason, for direct (non-pre-commit) invocations |
| `pyproject.toml`: `nam`/`nams`/`giv` added to codespell `ignore-words-list`; `NAM`/`NAMs`/`GIV` to `[tool.typos.default.extend-words]` | **Pre-existing latent bug, not caused by vendoring.** Both spell-checkers treat "NAM" as a misspelling of "NAME" and "GIV" as one of "GIVE", and `typos` auto-fixes in place. Running the hooks over `namo.yaml` rewrote the `NAMModel` class to `NAMEModel` (plus its `is_a:` references and the `NAMModel.md` doc link) and the `GIVReST` prefix — an official standard, doi:10.14573/altex.2501011 — to `GIVEReST` in both the prefix declaration and `NAMModel.exact_mappings`. Both caught and reverted; the allowlist prevents recurrence, and also protects the five `docs/` files that reference GIVReST |

Known remaining noise, neither a regression nor in scope for Stage 1:

- **`just lint` still exits 1** — but it did before Stage 1 too. All findings are warnings, zero errors (201 → 1,024). The increase is because `linkml-lint` walks the import closure and reports on Biolink's own elements (`association` ×119, `gene` ×59, …) even when pointed at a single file. There is no flag to exclude imported elements; `--ignore-warnings` or `--max-warnings` would be a lint-policy decision to take separately.
- **`yamllint` on `namo.yaml` still exits 1** — also pre-existing, and now *better*: 29 errors → 2 (the project's own whitespace hooks cleaned up the rest). The remaining two are indentation findings in untouched content.

### 1e. `gen-project` must run from the schema directory — ✅ DONE

Applied. `just _test-schema` and `just gen-python` both exit 0.

`gen-project` resolves Biolink's nested `attributes` import against the **invocation cwd**, so from the repo root it looks for `<repo>/attributes.yaml` and dies with `FileNotFoundError`. This is a third resolution behaviour, distinct from `gen-python` (schema dir) and `SchemaView` (root-schema dir), and there is no `--importmap` option on `gen-project` to override it.

Verified fix — run the generator from the schema directory, with the output path made absolute:

```
cd src/namo/schema && uv run gen-project -d /abs/path/to/project namo.yaml   # exit 0, all artifacts produced
```

In `justfile` terms that means, for each affected recipe:

```make
gen-project:
  cd {{source_schema_dir}} && uv run gen-project {{config_yaml}} \
    -d {{justfile_directory()}}/{{dest}} {{schema_name}}.yaml
```

**Audit result — `gen-project` is the only affected generator.** Every generator the justfile invokes was run against the real schema from the repo root:

| Generator | From repo root | Action |
|---|---|---|
| `gen-project` | **rc=1**, `FileNotFoundError: <repo>/attributes.yaml` | **`cd` applied** (3 sites) |
| `gen-doc` | rc=0 | left alone |
| `gen-pydantic` | rc=0 | left alone |
| `gen-owl` | rc=0 | left alone |
| `gen-typescript` | rc=0 | left alone |
| `gen-java` | rc=0 | left alone |
| `linkml-lint` | rc=1 — pre-existing warnings only, not an import failure | left alone |
| `gen-yaml` | rc=1 — **separate regression**, see 1g | left alone |

The three `gen-project` sites now `cd` into the schema directory: the `gen-python`, `gen-project` and `_test-schema` recipes. Each is a single `cd … && …` line, which is self-contained because `just` runs every recipe line in its own shell.

Two knock-on changes this forced:

1. **Output paths made absolute** via `justfile_directory()`, since they were repo-root-relative.
2. **A new `config_yaml_abs` variable.** `{{config_yaml}}` expands to `--config-file config.yaml`, a repo-root-relative path that fails the moment the cwd changes (`Error: Invalid value for '--config-file': 'config.yaml': No such file or directory`). The absolute variant is used only in the `cd`-ing recipes; the original is untouched for everything else.

Non-fatal noise during a successful run, all from Biolink's own definitions: `ERROR:linkml.generators.sqltablegen:Unknown range base: None for broad_synonym = label type` (and the other synonym slots), plus an openpyxl sheet-name-length warning.

### 1f. `attributes.yaml` must be committed — ✅ DONE

Commit `fd4b00a` ("Stage 1 changes done") committed `biolink-model.yaml` but **not** `src/namo/schema/attributes.yaml`, and the working-tree copy was removed. Since `biolink-model.yaml` imports it, the schema became unloadable for anyone at that commit — `FileNotFoundError: .../src/namo/schema/attributes.yaml`.

Restored from the pinned v4.4.3 tag, `git add`-ed, and now present in `HEAD`. `biolink-model.yaml` was re-verified byte-identical to upstream at the same time. The file is easy to miss precisely because its name gives no hint that it belongs to Biolink — the `imports:` comment in `namo.yaml` names both files for this reason, and the `pyproject.toml` / pre-commit excludes list both explicitly.

### 1g. `gen-yaml` is broken by the Biolink import — ✅ DONE (switched to `gen-linkml`)

Found during the 1e audit; **not** a cwd problem.

```
yaml.representer.RepresenterError: ('cannot represent an object',
  JsonObj(canonical_predicate=Annotation({'tag': 'canonical_predicate', 'value': True}),
          opposite_of=Annotation({'tag': 'opposite_of', 'value': 'has output'})))
```

`gen-yaml` cannot serialise the `annotations:` that Biolink puts on its slots. Confirmed a genuine regression: the same command on the pre-Biolink schema (`10de27f`) exits 0.

This breaks the `_gen-yaml` recipe, which produces `docs/schema/namo.yaml` — and since `gen-doc: _gen-yaml`, it breaks **`just gen-doc`, `just site` and `just deploy`**. Note `gen-doc` *itself* is fine (rc=0); only its dependency fails.

**Fix applied:** `_gen-yaml` now calls `gen-linkml` instead, which handles annotations:

```make
uv run gen-linkml -f yaml --no-mergeimports {{source_schema_path}} > {{merged_schema_path}}
```

`-f yaml` is required (`gen-linkml` defaults to JSON). `--no-mergeimports` keeps Biolink referenced rather than inlined — merging it produces a ~270,000-line file.

Verified: `just _gen-yaml` and `just gen-doc` both exit 0. The output parses as YAML and is correctly scoped — **47 classes, 33 enums, zero Biolink classes inlined**, Biolink ranges preserved as references, `Term` absent, all four renamed classes present.

Rejected alternatives, for the record: `gen-yaml --no-mergeimports` (not an option; silently ignored, still fails), `gen-yaml --no-metadata` (still fails), `gen-yaml --raw` (exits 0 but emits an *unresolved* 2,241-line schema, not a substitute for the resolved one).

**Still worth reporting upstream.** `gen-yaml` fails on any annotation-bearing schema, and Biolink is the most widely-imported LinkML schema there is. A fix would allow reverting to the simpler command.

**Cost: the merged schema grew 5,238 → 17,905 lines.** Most of that is not `gen-linkml` verbosity — it is the Biolink alignment itself. Every NAMO class now inherits Biolink's slot set (`id`, `iri`, `category`, `type`, `name`, `description`, `has_attribute`, `deprecated`, `provided_by`, `xref`, `synonym`, …), and a resolved schema materialises all of them per class. Any working merged schema would now be roughly this size. Review that diff once properly rather than skimming it.

### 1h. Documentation output — ⚠️ NEEDS A DECISION

Two consequences of the import surfaced once `gen-doc` could run again.

**`docs/elements/` went from 289 to 1,216 pages.** Biolink's classes and slots each get their own page. `--no-render-imports` does **not** help — it yields 1,216 vs 1,226, so the pages are produced regardless of that flag. There is no generator option that scopes the docs to NAMO-defined elements; doing so would need a custom template directory or a post-generation filter. Left as-is for now: the published site is currently ~80% Biolink reference material.

**Stale pages are not cleaned automatically.** `gen-doc` writes but never deletes, so pages for removed elements persist. After Stages 2–3, `Term.md`, `tissue_modeled.md`, `age.md`, `gene_symbol.md`, `ensembl_id.md`, `entrez_id.md` and `pathway_database.md` were all orphaned. Cleared by `rm -f docs/elements/*.md` before regenerating — worth folding into the recipe, since `just clean` already does this but `just gen-doc` alone does not.

**A subtler hazard — `Study.md` and `Dataset.md` still exist, but now describe Biolink's classes**, not NAMO's; NAMO's live at `NAMStudy.md` and `NAMDataset.md`. Same for `Gene.md` / `Pathway.md`. This upgrades a Stage 5 item from "update the links" to something sharper: the `[Dataset](Dataset.md)` and `[Studies](Study.md)` links in `namo.yaml`'s own `description:` block still **resolve**, they just now point at the wrong class. A silently-wrong link is worse than a broken one, so this should be fixed with the rest of Stage 5's prose propagation.

---

## Stage 2 — Clear the collisions ✅ DONE

Applied and verified. `gen-python` exits 0 — the `Conflicting URIs … for item: id` blocker from Stage 1 is cleared — and the generated model has no duplicate NAMO/Biolink classes. Hierarchy comes out as intended:

```
NAMDataset  -> Dataset(InformationContentEntity) -> NamedThing   # biolink
NAMStudy    -> Study(Activity)                   -> NamedThing   # biolink
GeneExpressionResult, PathwayActivityResult      -> NamedThing   # biolink
```

Biolink's own `NamedThing`, `Dataset`, `Study`, `Gene` and `Pathway` remain present and distinct. The single duplicate class in the output, `KnowledgeGraph`, is **pre-existing in a pure-Biolink generation** (it appears twice there too) and is not caused by NAMO.

Step 2c below was materially wrong as planned and has been corrected in place; 2b took its fallback branch.

The underlying rule: importing Biolink means NAMO may not define any slot or class name Biolink already defines. There were nine — four slots (2a, 2b) and five classes (2c).

### 2a. Delete NAMO's local `id`, `name`, `description` slot definitions

Biolink's `id` is already `identifier: true, required: true` — functionally identical to NAMO's. Keeping NAMO's kills `gen-python` outright with `Conflicting URIs … for item: id`. All three are now inherited from Biolink's `named thing`.

### 2b. Delete NAMO's type designator; `category` becomes the sole one

**The two-designator check ran first, as planned, and came back against `namo_type`.** The fallback branch was taken: `type` is deleted outright rather than renamed.

What the check showed. Declaring `namo_type: {designates_type: true}` on a class that also inherits Biolink's `category` **does generate** (exit 0) — but both designators stay live and must agree on every instance. An instance carrying `namo_type: "OrganOnChip"` together with `category: "…:ModelSystem"` first dispatched on `namo_type` to `OrganOnChip`, then failed the inherited `category` check:

```
ValueError: Wrong type designator value: class OrganOnChip has no subclass with
  ['class_class_curie', 'class_class_uri', 'class_model_uri']='desig:ModelSystem'
```

Two designators means every instance must carry two consistent fields forever. `category` is required by Biolink's `named thing` and cannot be dropped, so `namo_type` is the one that goes.

**Consequence for Stage 5:** migration items 2 and 3 collapse into one. `type: "OrganOnChip"` becomes `category: "namo:OrganOnChip"` — verified, `OrganOnChip.class_class_curie == "namo:OrganOnChip"`.

The `slots:` block is now empty and has been replaced by a comment recording why NAMO defines no slots of its own.

### 2c. Resolve five class-name collisions

This is the dangerous one — generation succeeds and the wrong classes silently win, which would make `tests/test_data.py`'s `getattr(namo.datamodel.namo, target_class_name)` return Biolink's class instead of NAMO's.

**Correction to this step as originally planned.** It said to resolve four of the five collisions with `is_a` while keeping the NAMO names. That does not work. The collision is on the *name*: once Biolink is imported, `dataset`/`study`/`gene`/`pathway` exist in the namespace no matter what NAMO's classes derive from, and both camel-case to the same Python identifier. For `Dataset` it is worse than shadowing — a NAMO class named `Dataset` deriving from Biolink's `dataset` fails generation outright:

```
ValueError: Cyclic wrapper inheritance at DatasetId
```

**Renaming is therefore forced**, and it is a public API change. Names below were chosen by the maintainer: the `NAM` prefix matches the existing `NAMModel` class, keeping the codebase internally consistent.

| Was | Now | Resolution |
|---|---|---|
| `NamedThing` | *(deleted)* | Adopt Biolink's `named thing` (per D1). All 15 remaining `is_a: NamedThing` became `is_a: named thing`. NAMO's version (`class_uri: schema:Thing`, slots id/name/description/type) was itself a re-creation of Biolink's — exactly what this plan sets out to stop. No rename needed: deleting it removes the collision |
| `Dataset` | `NAMDataset` | `is_a: dataset` (Biolink's, `is_a: information content entity`), keeping `model_systems` / `studies`. Its `studies` range updated to `NAMStudy` |
| `Study` | `NAMStudy` | `is_a: study` (Biolink's, `is_a: activity`), keeping NAMO's four attributes (`context_of_use`, `biological_context`, `perturbations`, `endpoints`) |
| `Gene` | `GeneExpressionResult` | Split per D-choice: identity comes from Biolink `gene` via a `gene: {range: gene}` attribute; `fold_change` / `p_value` / `adjusted_p_value` stay here. The old `gene_symbol` / `ensembl_id` / `entrez_id` attributes are dropped — Biolink's `gene` id_prefixes (HGNC, NCBIGene, ENSEMBL, …) replace them |
| `Pathway` | `PathwayActivityResult` | Same split: `pathway: {range: pathway}` for identity, `activity_score` / `enrichment_score` here. Old `pathway_database` / `pathway_id` dropped in favour of Biolink `pathway` id_prefixes (REACT, KEGG, GO, …) |

Four range references were updated alongside: `MolecularSimilarity.differentially_expressed_genes` and `.conserved_genes` → `GeneExpressionResult`; `PathwayConcordance.active_pathways` and `.divergent_pathways` → `PathwayActivityResult`.

Stage 2c is wider than Issue 19, but it is not optional — it is the price of the import, and skipping it produces a schema that generates cleanly and is quietly wrong.

**Not yet propagated (Stage 5 work):** the renames are schema-only so far. `docs/how-to/curate.md`, the `Dataset`/`Study` references in `namo.yaml`'s own `description:` prose and its `NAMModel.md`-style doc links, and any example data still use the old names.

---

## Stage 3 — Repoint the 17 `Term` ranges at Biolink classes ✅ DONE

Applied and verified. All 17 `range: Term` sites are gone, the `Term` class is deleted, and `gen-python` exits 0. Every one of the 18 resulting slots resolves to a real Biolink class — confirmed via `SchemaView.induced_slot`, and confirmed in the generated Python as genuine Biolink URIs:

```
Cell                     https://w3id.org/biolink/vocab/Cell
GrossAnatomicalStructure https://w3id.org/biolink/vocab/GrossAnatomicalStructure
OrganismTaxon            https://w3id.org/biolink/vocab/OrganismTaxon
LifeStage                https://w3id.org/biolink/vocab/LifeStage
PhenotypicFeature        https://w3id.org/biolink/vocab/PhenotypicFeature
EnvironmentalExposure    https://w3id.org/biolink/vocab/EnvironmentalExposure
QuantityValue            https://w3id.org/biolink/vocab/QuantityValue
```

Biolink class names are lowercase-with-spaces in LinkML source. `inlined` / `inlined_as_list` / `multivalued` / `required` flags all stayed as they were. Two slots changed beyond their range: `age` was split (3a) and `tissue_modeled` renamed (3b).

**Two forward references are live but unresolved until Stage 4.** `life_stage` binds `LifeStageEnum` (4c) and `anatomical_structure_modeled` binds `AnatomicalStructureEnum` (4b); neither enum exists yet. This does not break generation — the schema already shipped a dangling binding to the never-defined `OrganismAgeEnum`, which is the same tolerated condition — but it is a real loose end that 4b/4c close.

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

### Stage 3 exit state — 27/27 tests failing, all Stage 5 data work

Regenerating the datamodel and running `pytest` gives a clean, fully-categorised failure set. Every failure is instance data, none is a schema defect:

| Count | Error | Fixed by |
|---|---|---|
| 19 | `ValueError: category must be supplied` | Stage 5 items 1–2 |
| 5 | `TypeError: GeneExpressionResult.__init__() got an unexpected keyword argument 'gene_symbol'` | Stage 5 item 4 |
| 3 | `TypeError: TissueOnChip.__init__() got an unexpected keyword argument 'tissue_modeled'` | Stage 5 item 3 |

> **Careful with a bare `pytest` here.** Run on its own it reported **27 passed**, because it imports the committed `src/namo/datamodel/namo.py`, which was still the pre-Stage-1 model. The green was an artifact of a stale datamodel. Regenerate first (`just gen-python`, or the 1e-corrected invocation) before trusting any result — `just test` does this via `_test-python`, a plain `pytest` does not.

---

## Stage 4 — Enum and binding alignment ✅ DONE

Applied and verified. `gen-python` exits 0, **63 enums defined, zero dangling enum references** — which closes the two forward references Stage 3 left open (`LifeStageEnum`, `AnatomicalStructureEnum`) *and* the pre-existing dangling `OrganismAgeEnum`, a bug that predated this work. `StrainEnum` and `AgeEnum` are deleted. The test failure profile is byte-for-byte unchanged from Stage 3 (19 / 5 / 3), so nothing here regressed anything.

Closure checks re-run against Ubergraph with the enums as actually written:

| Enum | Root | Closure | Curated values | Failures |
|---|---|---|---|---|
| `OrganEnum` | `UBERON:0000062` + `part_of` | 19,578 | 10 `organ_modeled` | none |
| `AnatomicalStructureEnum` | `UBERON:0010000` + `part_of` | 56,644 | 3 `anatomical_structure_modeled` | none |
| `CellTypeEnum` | `CL:0000000` | 31,921 | **53** distinct CL CURIEs | none |
| `LifeStageEnum` | `UBERON:0000105` | 54 | none yet | n/a |
| `PhenotypeEnum` | `HP:0000118` + `MP:0000001` | — | none yet | n/a |

The `CellTypeEnum` row is the one that carried real risk: 4e binds four slots that were **never constrained before**, so those values had never been checked against CL. All 53 validate.

Two enums have no data to validate against — `LifeStageEnum` (nothing populates `life_stage`) and `PhenotypeEnum` (no example file populates the three `PhenotypeOverlap` phenotype slots). Their roots are sound but unexercised; the first curated value through either path is where they actually get tested.

**`oaklib` (0.6.23) is now a dev dependency**, so closure checks can be computed — the table at the top of this stage reports real results against Ubergraph rather than expectations.

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

This makes `PhenotypeOverlap.phenotype_ontology` (free text documenting "HPO, MP") redundant: the source ontology is now carried by each term's own CURIE prefix. It has been given a `deprecated:` annotation rather than deleted, so existing data keeps loading; remove it in a later cleanup.

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

2. **`type:` → `category:`** on every top-level object, with the value becoming a CURIE. The 2b check resolved this: `namo_type` was dropped, so the former items 2 and 3 are now a single edit rather than two.

   ```yaml
   # before
   type: "OrganOnChip"
   # after
   category: "namo:OrganOnChip"      # == OrganOnChip.class_class_curie
   ```

   This simultaneously satisfies D1's requirement that every NAMO entity carry a `category` (inherited from Biolink `named thing`, where it is required) and supplies the sole type designator.

3. **Rename `tissue_modeled:` → `anatomical_structure_modeled:`** in the three `TissueOnChip-example-*.yaml` files, and update the `TissueOnChip` row of `docs/how-to/curate.md` (line 88). Full inventory in 3b.

4. **Propagate the Stage 2c class renames — larger than first estimated.** An earlier draft of this plan said the renames had "no instance-data footprint" because no `Dataset-*`/`Study-*`/`Gene-*`/`Pathway-*` example *files* exist. That was wrong: `Gene` and `Pathway` objects appear **nested** inside `MolecularSimilarity` and `PathwayConcordance` blocks, and **26 of the 27 files** in `tests/data/valid/` use the removed attributes. This is the single largest item in Stage 5.

   Each nested gene object must fold its identity fields into a Biolink `gene`:

   ```yaml
   # before
   - id: "gene:075"
     name: "CYP3A4"
     gene_symbol: "CYP3A4"
     ensembl_id: "ENSG00000160868"
     fold_change: 1.8
     p_value: 0.001
   # after
   - id: "gene:075"
     category: "namo:GeneExpressionResult"
     gene:
       id: "ENSEMBL:ENSG00000160868"     # was ensembl_id
       name: "CYP3A4"                    # was gene_symbol
       category: "biolink:Gene"
     fold_change: 1.8
     p_value: 0.001
   ```

   Note the identifier change: `id: "gene:075"` was a local surrogate key. The real gene identity now lives on the nested object as a resolvable CURIE, which is the point of the split — but it means the migration is a genuine recuration, not a mechanical rename. `pathway_database` + `pathway_id` collapse the same way into a nested `pathway:` CURIE.

   Prose and docs also reference the renamed classes:
   - `namo.yaml`'s own `description:` block — `[Dataset](Dataset.md)` and `[Studies](Study.md)` links, and the surrounding text.
   - `docs/how-to/curate.md` — model-class table.

5. **No anatomy recuration needed.** The closure checks confirm all 11 `organ_modeled` values pass `UBERON:0000062` and all 3 `anatomical_structure_modeled` values pass `UBERON:0010000`.

`name:` is preserved throughout, so the CLAUDE.md convention of including both `id` and `name` for clarity survives. Items 1–3 are mechanical and should be a one-off migration script rather than 27 hand edits; `examples/output/` is regenerated by `_ensure_examples_output` anyway. **Item 4 is not mechanical** — mapping `gene_symbol`/`ensembl_id` onto a single resolvable CURIE is a curation judgement per gene, and should be reviewed rather than scripted blindly.

Note that `tests/test_data.py` derives the target class from the filename (`Path(filepath).stem.split("-")[0]`), so any future example file must be named after a class that still exists — `NAMStudy-example-001.yaml`, not `Study-example-001.yaml`.

---

## Stage 6 — Validation and impact

- **`just test` still works.** `_test-python` loads via `yaml_loader` + generated dataclasses, and `_test-examples` uses `linkml-run-examples` — neither goes through JSON Schema, so the `category` array/enum defect does not break the suite. The dataclass path was confirmed to load cleanly with scalar `category`.
- **But `project/namo.schema.json` becomes non-validating** for any class descending from Biolink `named thing`, because `gen-json-schema` emits `{"type": "array", "enum": [...]}` for `category`. That is an upstream LinkML defect, not something NAMO can override (the `category` override fails `gen-python`). Anyone consuming the published JSON Schema will hit it — this deserves an upstream issue against `linkml`, plus a note in the NAMO docs.
- **Wire enum validation into the test suite.** `oaklib` 0.6.23 is now a dev dependency, so closure checks are runnable ad hoc (4a, 4b) — but no `just test` step expands dynamic enums or enforces `bindings`, so Stage 4's constraints remain unenforced in CI. Add a step that validates the `reachable_from` enums and `bindings` against the example data, otherwise these enums are documentation rather than validation. Minor: `oaklib` is the only unpinned entry in the `dev` group; pin it for reproducibility like its neighbours.
- **Generated artifacts balloon:** 49 → 645 Python classes, ~19k lines. Expect `just gen-project` and `just gen-doc` to slow substantially, and `docs/elements/` to gain hundreds of pages unless `gen-doc` is constrained. Worth deciding whether the docs build should be filtered to NAMO-defined classes only.
- **Run order:** `just lint` → `just gen-project` → `just test`, then grep the OWL output for `https://w3id.org/biolink/vocab/Cell` to confirm Stage 1a landed.
- **Stage order:** 1 → 2 (designator check first) → 3 (Term deletion last) → 4 → 5. Stage 2 before 3 is mandatory. **Stages 1–2 are now applied, and the suite is red until Stage 5 lands** — every example file still carries `type:` instead of `category:` and lacks `category` on its ontology references. That was always going to be true between 2b/2c and 5; it just means the branch is not in a committable-green state until Stage 5 completes.
- **Stage 1 leftovers:** `1e` (gen-project cwd), `1f` (`attributes.yaml`) and `1g` (`gen-yaml` → `gen-linkml`) are all closed — the whole `just` pipeline runs again. `1h` (docs output: 1,216 pages, stale-page cleanup, and `Study.md`/`Dataset.md` now describing Biolink's classes) is open and needs a decision.

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
