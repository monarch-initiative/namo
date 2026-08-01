---
search:
  boost: 2.0
---


# Enum: LifeStageEnum 




_Developmental and life-cycle stages. Composed rather than rooted at UBERON:0000105 alone: the species-specific developmental ontologies are not asserted as subclasses of it (MmusDv:0000110 has MmusDv:0000000 as its only ontology ancestor), so a UBERON-only root would reject the species-specific terms Biolink's `life stage` lists in its id_prefixes._



<div data-search-exclude markdown="1">

URI: [namo:LifeStageEnum](https://w3id.org/monarch-initiative/namo/LifeStageEnum)


_This is a dynamic enum_

## Enumeration Operations
**Includes:**

- **Reachable from**
    - Source nodes: UBERON:0000105
    - Via relationships: rdfs:subClassOf

- **Reachable from**
    - Source nodes: HsapDv:0000000
    - Via relationships: rdfs:subClassOf

- **Reachable from**
    - Source nodes: MmusDv:0000000
    - Via relationships: rdfs:subClassOf














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: LifeStageEnum
description: 'Developmental and life-cycle stages. Composed rather than rooted at
  UBERON:0000105 alone: the species-specific developmental ontologies are not asserted
  as subclasses of it (MmusDv:0000110 has MmusDv:0000000 as its only ontology ancestor),
  so a UBERON-only root would reject the species-specific terms Biolink''s `life stage`
  lists in its id_prefixes.'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
include:
- reachable_from:
    source_nodes:
    - UBERON:0000105
    relationship_types:
    - rdfs:subClassOf
    is_direct: false
- reachable_from:
    source_nodes:
    - HsapDv:0000000
    relationship_types:
    - rdfs:subClassOf
    is_direct: false
- reachable_from:
    source_nodes:
    - MmusDv:0000000
    relationship_types:
    - rdfs:subClassOf
    is_direct: false

```
</details>

</div>