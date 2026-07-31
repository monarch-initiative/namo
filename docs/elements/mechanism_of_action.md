---
search:
  boost: 5.0
---

# Slot: mechanism_of_action 


_a boolean flag to indicate if the edge is part of a path or subgraph of a knowledge graph that constitutes the mechanism of action for a result._



<div data-search-exclude markdown="1">



URI: [namo:mechanism_of_action](https://w3id.org/monarch-initiative/namo/mechanism_of_action)
Alias: mechanism_of_action


## Inheritance

* [association_slot](association_slot.md)
    * **mechanism_of_action**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain | [Association](Association.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:mechanism_of_action |
| native | namo:mechanism_of_action |
| exact | NCIT:C54680, MI:2044, LOINC:MTHU019741 |




## LinkML Source

<details>
```yaml
name: mechanism of action
description: a boolean flag to indicate if the edge is part of a path or subgraph
  of a knowledge graph that constitutes the mechanism of action for a result.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- NCIT:C54680
- MI:2044
- LOINC:MTHU019741
rank: 1000
is_a: association slot
domain: association
alias: mechanism_of_action
range: boolean

```
</details></div>