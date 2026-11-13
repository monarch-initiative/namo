"""Plan the runs of linkml-reference-validator for `just test` (_test-references).

Prints one line per class, tab-separated:

    <class> <titled references in its files> <file> [<file> ...]

Each example file is validated as the class named before the first "-" in its
file name. The count is the number of references with a title written in those
files, so the recipe can fail when the validator checks fewer titles than that.

linkml-reference-validator follows each slot's declared range and does not read
the `type` designator. A Dataset's `model_systems` have the range ModelSystem,
which is abstract and has no `references`, so the validator never reaches the
references inside them. Each model system is therefore written to its own file
in OUT_DIR and validated as the class its `type` names.

Usage: python scripts/reference_check_plan.py EXAMPLES_DIR OUT_DIR
"""

import shutil
import sys
from collections import defaultdict
from pathlib import Path

import yaml


def count_titled_references(obj) -> int:
    """Count the references with a title anywhere under obj."""
    if isinstance(obj, dict):
        n = 0
        for key, value in obj.items():
            if key == "references" and isinstance(value, list):
                n += sum(
                    1 for ref in value if isinstance(ref, dict) and ref.get("title")
                )
            else:
                n += count_titled_references(value)
        return n
    if isinstance(obj, list):
        return sum(count_titled_references(item) for item in obj)
    return 0


def main(examples_dir: Path, out_dir: Path) -> None:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    files: dict[str, list[Path]] = defaultdict(list)
    expected: dict[str, int] = defaultdict(int)

    for path in sorted(examples_dir.glob("*.yaml")):
        cls = path.name.split("-")[0]
        data = yaml.safe_load(path.read_text())
        if cls == "Dataset":
            model_systems = data.pop("model_systems", None) or []
            for i, system in enumerate(model_systems, start=1):
                system_cls = system.get("type")
                if not system_cls:
                    sys.exit(
                        f"error: model_systems[{i}] in {path} has no type, so its references cannot be checked"
                    )
                out = out_dir / f"{system_cls}-from-{path.stem}-{i}.yaml"
                out.write_text(
                    yaml.safe_dump(system, sort_keys=False, allow_unicode=True)
                )
                files[system_cls].append(out)
                expected[system_cls] += count_titled_references(system)
        files[cls].append(path)
        expected[cls] += count_titled_references(data)

    for cls in sorted(files):
        print("\t".join([cls, str(expected[cls]), *map(str, files[cls])]))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(Path(sys.argv[1]), Path(sys.argv[2]))
