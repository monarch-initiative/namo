# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the NAMO (New Approach Methodology Ontology and Schema) project - a LinkML-based schema for modeling new approach methodologies in biomedical research. The project generates multiple representations (Python, Java, OWL, JSON Schema, etc.) from a single LinkML YAML schema definition.

## Essential Commands

### Build and Generate
```bash
# Generate all project artifacts (Python models, docs, etc.)
just gen-project

# Generate documentation only
just gen-doc

# Build complete site (project + docs)
just site

# Clean all generated files
just clean
```

### Testing and Validation
```bash
# Run all tests (schema, Python, examples)
just test

# Run linting on the schema
just lint

# Test schema generation only
just _test-schema

# Run Python unit tests
uv run python -m pytest

# Test with specific file
uv run python -m pytest tests/test_data.py
```

### Development Workflow
```bash
# Install dependencies
just install

# Update LinkML to latest version
just _update-linkml

# Serve documentation locally for preview
just testdoc
# or directly:
uv run mkdocs serve
```

### Deployment
```bash
# Deploy documentation to GitHub Pages
just deploy
```

## Architecture

### Schema-First Development
The source of truth is the LinkML schema at `src/namo/schema/namo.yaml`. All other representations are generated from this schema:

- **Python datamodels**: Generated into `src/namo/datamodel/` (both standard and Pydantic versions)
- **Project artifacts**: Generated into `project/` directory (Java, OWL, JSON Schema, GraphQL, etc.)
- **Documentation**: Generated into `docs/elements/` from the schema

### Key Components

1. **LinkML Schema** (`src/namo/schema/namo.yaml`): Defines the ontology structure with classes like:
   - `Dataset`: Top-level container for model systems and studies
   - `ModelSystem`: Abstract base for different model types (AnimalModel, CellLineModel, Organoid, etc.)
   - `Study`: Research investigation with context, perturbations, endpoints
   - `NamedThing`: Base class for identifiable entities

2. **Build System**: Uses `just` command runner with recipes defined in `justfile`. Configuration is stored in `config.public.mk` for environment variables.

3. **Testing Strategy**:
   - Schema validation tests ensure the LinkML schema is valid
   - Python datamodel tests validate that example data loads correctly
   - Example data in `tests/data/valid/` and `tests/data/invalid/` directories

4. **Documentation**: MkDocs-based site with auto-generated schema documentation. Deployed to GitHub Pages.

## Important Configuration

- **Schema name**: `namo` (defined in `config.public.mk`)
- **Python package**: `namo` with datamodels in `namo.datamodel`
- **Dependencies**: Managed by `uv` (see `pyproject.toml` and `uv.lock`)
- **Python version**: Requires Python >=3.9,<4.0

## Development Notes

- Always edit the source schema at `src/namo/schema/namo.yaml` - never edit generated files
- The `project/` directory contains generated artifacts that are git-ignored by default
- Use `just` commands rather than running generators directly for consistency
- The project uses `uv` for dependency management - always use `uv run` for Python commands

## Schema Design Patterns

### Working with Ontology Terms
- The `Term` class is used for ontology references throughout the schema
- For single-valued Term attributes, use `inlined: true` to allow full Term objects in YAML
- For multi-valued Term attributes, use `inlined_as_list: true` (not just `inlined: true`)
- Example data should include both `id` (ontology CURIE) and `name` (human-readable label) for clarity

### Attribute Organization
- **Intrinsic properties** belong directly on model classes (e.g., cell_types, organ_modeled on OrganOnChip)
- **Relationship properties** go in the `models` attribute via `ModelsRelationship` (e.g., disease being modeled, phenotypes recapitulated)
- This separation keeps the schema clean and allows rich annotation of model-disease relationships

### Adding New Model Types
When extending NAMModel subclasses:
1. Focus on properties intrinsic to the model system itself
2. Use appropriate ontology references (UBERON for anatomy, CL for cell types, etc.)
3. Include both technical specifications and biological components
4. Test with example YAML files that include full Term objects with id and name

### Testing Considerations
- Run `just test` after schema changes to validate:
  - Schema generation works
  - Python datamodels are created correctly  
  - Example YAML files validate against the schema
- Example files in `tests/data/valid/` serve as both tests and documentation
- Include comments in YAML examples to explain ontology term meanings