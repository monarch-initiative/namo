<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# namo

New Approach Methodology Ontology and Schema

## Documentation Website

[https://monarch-initiative.github.io/namo](https://monarch-initiative.github.io/namo)

## Ontology

NAMO is a semantic data model with ontology-like elements. We export it as an ontology to facilitate browsing and ontology API calls:

- [https://bioportal.bioontology.org/ontologies/NAMO](https://bioportal.bioontology.org/ontologies/NAMO)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation (do not edit)
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [namo](src/namo)
    * [schema/](src/namo/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/namo/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
