"""Plan the runs of linkml-reference-validator for `just test` (_test-references).

Prints one line per class, tab-separated:

    <class> <titled references in its files> <file> [<file> ...]

Each example file is validated as the class named before the first "-" in its
file name. The count is the number of references with a title written in those
files, so the recipe can fail when the validator checks fewer titles than that.

linkml-reference-validator follows each slot's declared range and does not read
the `type` designator. That is enough because `references` is declared on
ModelSystem itself, so the validator reaches the references inside a Dataset's
`model_systems` while treating each one as a ModelSystem. A reference slot
declared only on a subclass would be skipped there, and the count would catch
it.

Usage: python scripts/reference_check_plan.py EXAMPLES_DIR
"""

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


def main(examples_dir: Path) -> None:
    files: dict[str, list[Path]] = defaultdict(list)
    expected: dict[str, int] = defaultdict(int)

    for path in sorted(examples_dir.glob("*.yaml")):
        cls = path.name.split("-")[0]
        files[cls].append(path)
        expected[cls] += count_titled_references(yaml.safe_load(path.read_text()))

    for cls in sorted(files):
        print("\t".join([cls, str(expected[cls]), *map(str, files[cls])]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(Path(sys.argv[1]))
