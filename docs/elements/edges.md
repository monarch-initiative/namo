---
search:
  boost: 5.0
---

# Slot: edges 


_A list of associations between two entities._



<div data-search-exclude markdown="1">



URI: [namo:edges](https://w3id.org/monarch-initiative/namo/edges)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KnowledgeGraph](KnowledgeGraph.md) | A container representing a knowledge graph serialized in KGX (Knowledge Graph... |  no  |
| [KnowledgeGraph](KnowledgeGraph.md) | A knowledge graph is a structured representation of knowledge in the form of ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Association](Association.md) |
| Domain Of | [KnowledgeGraph](KnowledgeGraph.md), [KnowledgeGraph](KnowledgeGraph.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:edges |
| native | namo:edges |




## LinkML Source

<details>
```yaml
name: edges
description: A list of associations between two entities.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
domain_of:
- KnowledgeGraph
- knowledge graph
range: association
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>