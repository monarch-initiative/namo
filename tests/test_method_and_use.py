"""A model system record of one study's use points to a real method record and study.

`description_scope`, `method` and `studies` on ModelSystem (issue #52) say
whether a record describes a method in general or one study's use of it. A
LinkML rule can't enforce how they fit together (linkml-validate ignores rules
on ModelSystem's subclasses), so these tests check it across the examples:

- a METHOD record names no method and no studies;
- each `method` is the id of a model system record whose scope is METHOD;
- each id in `studies` is the id of a Study record.

The ids are looked up across all of tests/data/valid/, so a use and its method
can be in different files.
"""

from functools import cache
from pathlib import Path

import pytest
import yaml
from linkml_runtime import SchemaView

REPO = Path(__file__).parent.parent
SCHEMA = REPO / "src" / "namo" / "schema" / "namo.yaml"
DATA_DIR_VALID = REPO / "tests" / "data" / "valid"


@cache
def model_system_types() -> frozenset:
    view = SchemaView(str(SCHEMA))
    return frozenset(view.class_descendants("ModelSystem"))


@cache
def records() -> tuple[dict, dict]:
    """Every model system and study in the examples, by id."""
    models, studies = {}, {}

    def walk(node, key=None):
        if isinstance(node, dict):
            if node.get("type") in model_system_types() and "id" in node:
                models[node["id"]] = node
            elif key == "studies" and "id" in node:
                studies[node["id"]] = node
            for k, v in node.items():
                walk(v, k)
        elif isinstance(node, list):
            for item in node:
                walk(item, key)

    for path in sorted(DATA_DIR_VALID.glob("*.yaml")):
        data = yaml.safe_load(path.read_text())
        if path.stem.startswith("Study-") and isinstance(data, dict):
            studies[data["id"]] = data
        walk(data)
    return models, studies


def models_with(slot: str):
    models, _ = records()
    return [pytest.param(m, id=m["id"]) for m in models.values() if m.get(slot)]


def method_records():
    models, _ = records()
    return [
        pytest.param(m, id=m["id"])
        for m in models.values()
        if m.get("description_scope") == "METHOD"
    ]


@pytest.mark.parametrize("model", method_records())
def test_method_record_names_no_method_or_studies(model):
    """A record of a method in general isn't itself a use of one."""
    assert not model.get("method"), "a METHOD record should not name a method"
    assert not model.get("studies"), "a METHOD record should not name studies"


@pytest.mark.parametrize("model", models_with("method"))
def test_method_is_a_method_record(model):
    """`method` names a model system record that describes a method."""
    models, _ = records()
    target = models.get(model["method"])
    assert target is not None, f"no model system record has the id {model['method']}"
    assert target.get("description_scope") == "METHOD", (
        f"{model['method']} is not a METHOD record"
    )


@pytest.mark.parametrize("model", models_with("studies"))
def test_studies_are_study_records(model):
    """Each id in `studies` names a Study record."""
    _, studies = records()
    missing = [s for s in model["studies"] if s not in studies]
    assert not missing, f"no Study record has the id(s) {missing}"
