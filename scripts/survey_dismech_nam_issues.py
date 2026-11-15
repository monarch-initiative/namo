"""List the DisMech issues that may bear on how DisMech models NAMs.

Used to compare DisMech's model schema (ExperimentalModel, AnimalModel,
ComputationalModel, ModelMechanismLink) with NAMO's before DisMech's models move
to nams-registry. It casts a wide net; reading the titles and sorting them into
themes is left to a person.

Three passes, merged and de-duplicated by issue number:

1. A full-text search of open and closed issues for each term in SEARCH_TERMS.
2. Every issue carrying the `models` label.
3. Every issue carrying the `schema` label whose title matches SCHEMA_TITLE_RE.

Prints one tab-separated line per issue, sorted by number:

    <number> <state> <labels> <found by> <title>

<found by> lists the passes that returned the issue, so a reader can see why a
title is there. Needs the GitHub CLI (`gh`), logged in.

Usage: python scripts/survey_dismech_nam_issues.py [--repo OWNER/NAME] > out.tsv
"""

import argparse
import json
import re
import subprocess
import sys

SEARCH_TERMS = [
    "ExperimentalModel",
    "experimental model",
    "NAMO",
    "namo_type",
    "model system",
    "NAM",
    "in vitro",
    "organoid",
    "iPSC",
    "cell line",
    "in chemico",
    "model_type",
    "modeled_mechanisms",
    "animal model",
    "OECD",
    "test guideline",
    "assay",
]

SCHEMA_TITLE_RE = re.compile(
    r"model|NAM|assay|cell|organoid|ipsc|vitro|vivo|chemico|oecd|guideline|namo"
    r"|species|organism|in silico|test method|AOP|key event|toxic|chemical|exposure",
    re.IGNORECASE,
)

LIMIT = 500


def gh_issues(repo: str, *args: str) -> list[dict]:
    """Run `gh issue list` on REPO with ARGS and return the parsed issues."""
    cmd = [
        "gh", "issue", "list", "--repo", repo, "--state", "all",
        "--limit", str(LIMIT), "--json", "number,title,state,labels", *args,
    ]  # fmt: skip
    out = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout
    issues = json.loads(out)
    if len(issues) == LIMIT:
        print(f"warning: {' '.join(args)} hit the {LIMIT}-issue limit", file=sys.stderr)
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", default="monarch-initiative/dismech")
    repo = parser.parse_args().repo

    found: dict[int, dict] = {}

    def add(issues: list[dict], how: str) -> None:
        for issue in issues:
            entry = found.setdefault(issue["number"], {**issue, "found_by": []})
            if how not in entry["found_by"]:
                entry["found_by"].append(how)

    for term in SEARCH_TERMS:
        add(gh_issues(repo, "--search", f"{term} in:title,body"), f"search:{term}")
    add(gh_issues(repo, "--label", "models"), "label:models")
    schema = gh_issues(repo, "--label", "schema")
    add([i for i in schema if SCHEMA_TITLE_RE.search(i["title"])], "label:schema")

    for number in sorted(found):
        issue = found[number]
        labels = ",".join(label["name"] for label in issue["labels"])
        found_by = ";".join(issue["found_by"])
        print(f"{number}\t{issue['state']}\t{labels}\t{found_by}\t{issue['title']}")


if __name__ == "__main__":
    main()
