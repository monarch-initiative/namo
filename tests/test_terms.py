"""Ontology terms in the schema and the examples, checked with linkml-term-validator.

The checks run offline, against the lookups committed in cache/. A new term is
not in the cache, so it fails here until `just validate-terms` has looked it up
and the cache is committed. conf/oak_config.yaml says where each ontology is
looked up.
"""

import glob
import os
from functools import cache
from pathlib import Path

import pytest
import yaml
from linkml_runtime import SchemaView

REPO = Path(__file__).parent.parent
SCHEMA = REPO / "src" / "namo" / "schema" / "namo.yaml"
CACHE = REPO / "cache"
OAK_CONFIG = REPO / "conf" / "oak_config.yaml"
DATA_DIR_VALID = REPO / "tests" / "data" / "valid"

ISSUE = "see https://github.com/monarch-initiative/namo/issues/51"

# Known problems, until they are fixed. strict: a test fails once its problem is
# fixed, so the entry is removed here when the fix lands.

# Enum values whose `meaning` is right but whose name, title, description and
# aliases do not match the term's label, so each needs the label as an alias
# (not a title: gen-pydantic names the Python enum member after the title);
# and the EDAM values, whose CURIEs should be written EDAM:topic_NNNN.
SCHEMA_TERM_GAPS = {
    "SurfaceCoatingEnum.POLY_L_LYSINE": "needs alias: poly(L-lysine) macromolecule",
    "SurfaceCoatingEnum.RGD_PEPTIDE": "NCIT:C13288 is RGD Motif; needs an alias or another term",
    "PBPKCompartmentEnum.MUSCLE": "needs alias: skeletal muscle tissue",
    "PBPKCompartmentEnum.FAT": "needs alias: adipose tissue",
    "PBPKCompartmentEnum.SKIN": "needs alias: skin of body",
    "PBPKCompartmentEnum.BONE": "needs alias: bone tissue",
    "PBPKCompartmentEnum.GI_TRACT": "needs alias: alimentary part of gastrointestinal system",
    "PBPKCompartmentEnum.PLASMA": "needs alias: blood plasma",
    "FeatureTypeEnum.TRANSCRIPTOMIC": "EDAM:3308 should be EDAM:topic_3308 (Transcriptomics)",
    "FeatureTypeEnum.PROTEOMIC": "EDAM:0121 should be EDAM:topic_0121 (Proteomics)",
    "FeatureTypeEnum.METABOLOMIC": "EDAM:3172 should be EDAM:topic_3172 (Metabolomics)",
    "FeatureTypeEnum.IMAGING": "EDAM:3382 should be EDAM:topic_3382 (Imaging)",
    "CrossValidationMethodEnum.K_FOLD": "needs alias: K-fold cross validation method",
    "CrossValidationMethodEnum.LEAVE_ONE_OUT": "needs alias: leave one out cross validation method",
}

# Example files with a CL id whose label is not the one given: either the id is
# for another cell type, or the label is an outdated one.
DATA_TERM_GAPS = {
    "CellLineModel-example-001": "CL:0002138 is not hepatic stellate cell",
    "CoCulture-example-001": "CL:0002138 is not hepatic stellate cell",
    "Dataset-GI-toxicity-example": "CL:0000678, CL:0000683, CL:0002250, CL:0009003 are other cell types",
    "OrganOnChip-example-002": "CL:0002062, CL:0002063 labels are outdated",
    "OrganOnChip-example-003": "CL:0002145, CL:0002370 labels are outdated",
    "OrganOnChip-example-zhu-2024": "CL:0002062 label is outdated",
    "Organoid-example-002": "CL:0000183 is not cholangiocyte; CL:0002138 is not hepatic stellate cell",
    "Organoid-example-003": "CL:0009019 is not tuft cell",
    "Organoid-example-004": "the kidney tubule CL ids are for other cell types",
    "Organoid-example-takahashi-2023": "CL:0000036 is not epithelial cell",
    "ThreeDCellCulture-example-002": "CL:0002418 is not epithelial cell of ovary",
    "TissueOnChip-example-002": "CL:0009019 is not tuft cell",
}


def gap(known: dict, key: str) -> list:
    if key in known:
        return [pytest.mark.xfail(reason=f"{known[key]} ({ISSUE})", strict=True)]
    return []


# ----------------------------------------------------------------- schema


@cache
def schema_issues() -> dict:
    """The validator's issues for the schema, by enum value."""
    from linkml_term_validator.models import ValidationConfig
    from linkml_term_validator.validator import EnumValidator

    config = ValidationConfig(cache_dir=CACHE, oak_config_path=OAK_CONFIG, offline=True)
    result = EnumValidator(config).validate_schema(SCHEMA)
    issues = {}
    for issue in result.issues:
        issues.setdefault(f"{issue.enum_name}.{issue.value_name}", []).append(issue)
    return issues


def enum_values_with_meaning():
    view = SchemaView(str(SCHEMA))
    for enum_name, enum_def in view.all_enums().items():
        for value_name, value in (enum_def.permissible_values or {}).items():
            if value.meaning:
                key = f"{enum_name}.{value_name}"
                yield pytest.param(key, id=key, marks=gap(SCHEMA_TERM_GAPS, key))


@pytest.mark.parametrize("key", enum_values_with_meaning())
def test_schema_meaning(key):
    """The value's `meaning` is a term whose label is the value's name or title."""
    problems = schema_issues().get(key, [])
    assert not problems, "\n".join(f"{p.message}: {p.actual_label!r}" for p in problems)


# ------------------------------------------------------------------- data


@cache
def data_validator():
    from linkml.validator import Validator
    from linkml_term_validator.plugins import BindingValidationPlugin, DynamicEnumPlugin

    options = {
        "cache_dir": str(CACHE),
        "oak_config_path": str(OAK_CONFIG),
        "offline": True,
    }
    return Validator(
        schema=str(SCHEMA),
        validation_plugins=[
            DynamicEnumPlugin(**options),
            BindingValidationPlugin(validate_labels=True, **options),
        ],
    )


def example_files():
    for path in sorted(glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))):
        stem = Path(path).stem
        yield pytest.param(path, id=stem, marks=gap(DATA_TERM_GAPS, stem))


@pytest.mark.parametrize("filepath", example_files())
def test_example_terms(filepath):
    """Each term exists, is in the enum it is bound to, and has its ontology label.

    The file is checked as the class named before the first "-" in its name.
    """
    target_class = Path(filepath).stem.split("-")[0]
    instance = yaml.safe_load(Path(filepath).read_text())
    results = data_validator().validate(instance, target_class=target_class).results
    assert not results, "\n".join(r.message for r in results)
