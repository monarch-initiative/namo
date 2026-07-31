---
search:
  boost: 5.0
---

# Slot: associated_with_resistance_to 


_A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of resistance to treatment by the chemical._



<div data-search-exclude markdown="1">



URI: [namo:associated_with_resistance_to](https://w3id.org/monarch-initiative/namo/associated_with_resistance_to)
Alias: associated_with_resistance_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [associated_with_response_to](associated_with_response_to.md)
                * **associated_with_resistance_to**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalEntity](ChemicalEntity.md) |
| Domain | [NamedThing](NamedThing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:associated_with_resistance_to |
| native | namo:associated_with_resistance_to |




## LinkML Source

<details>
```yaml
name: associated with resistance to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A relation that holds between a named thing and a chemical that specifies
  that the change in the named thing is found to be associated with the degree of
  resistance to treatment by the chemical.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: associated with response to
domain: named thing
inherited: true
alias: associated_with_resistance_to
range: chemical entity
multivalued: true

```
</details></div>