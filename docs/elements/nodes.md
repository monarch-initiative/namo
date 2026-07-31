---
search:
  boost: 5.0
---

# Slot: nodes 


_A list of entities that can be a subject or object of an association_



<div data-search-exclude markdown="1">



URI: [namo:nodes](https://w3id.org/monarch-initiative/namo/nodes)
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
| Range | [Entity](Entity.md) |
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
| self | namo:nodes |
| native | namo:nodes |




## LinkML Source

<details>
```yaml
name: nodes
description: A list of entities that can be a subject or object of an association
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
domain_of:
- KnowledgeGraph
- knowledge graph
range: entity
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>