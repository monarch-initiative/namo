---
search:
  boost: 5.0
---

# Slot: predicate_mappings 


_A collection of relationships that are not used in biolink, but have biolink patterns that can be used to replace them.  This is a temporary slot to help with the transition to the fully qualified predicate model in Biolink3._



<div data-search-exclude markdown="1">



URI: [namo:predicate_mappings](https://w3id.org/monarch-initiative/namo/predicate_mappings)
Alias: predicate_mappings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MappingCollection](MappingCollection.md) | An abstract container class that holds a set of predicate mappings |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PredicateMapping](PredicateMapping.md) |
| Domain Of | [MappingCollection](MappingCollection.md) |

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
| self | namo:predicate_mappings |
| native | namo:predicate_mappings |




## LinkML Source

<details>
```yaml
name: predicate mappings
description: A collection of relationships that are not used in biolink, but have
  biolink patterns that can be used to replace them.  This is a temporary slot to
  help with the transition to the fully qualified predicate model in Biolink3.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: predicate_mappings
domain_of:
- mapping collection
range: predicate mapping
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>