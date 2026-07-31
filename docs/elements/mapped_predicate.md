---
search:
  boost: 5.0
---

# Slot: mapped_predicate 


_The predicate that is being replaced by the fully qualified representation of predicate + subject and object qualifiers.  Only to be used in test data and mapping data to help with the transition to the fully qualified predicate model. Not to be used in knowledge graphs._



<div data-search-exclude markdown="1">



URI: [namo:mapped_predicate](https://w3id.org/monarch-initiative/namo/mapped_predicate)
Alias: mapped_predicate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PredicateMapping](PredicateMapping.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:mapped_predicate |
| native | namo:mapped_predicate |




## LinkML Source

<details>
```yaml
name: mapped predicate
description: The predicate that is being replaced by the fully qualified representation
  of predicate + subject and object qualifiers.  Only to be used in test data and
  mapping data to help with the transition to the fully qualified predicate model.
  Not to be used in knowledge graphs.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: mapped_predicate
domain_of:
- predicate mapping
range: string

```
</details></div>