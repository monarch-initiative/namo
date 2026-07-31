---
search:
  boost: 5.0
---

# Slot: associated_with_response_to 


_A statistical association used to indicate that the object of a statement using this predicate induces a response of some kind in the subject entity.  Intentionally broad in definition, this predicate should be used with qualifiers to narrow the type of response (E.g. whether the response is therapeutic, phenotypic, detrimental, resistant, etc. is captured in context, direction, and aspect qualifiers)._



<div data-search-exclude markdown="1">



URI: [namo:associated_with_response_to](https://w3id.org/monarch-initiative/namo/associated_with_response_to)
Alias: associated_with_response_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * **associated_with_response_to**
                * [associated_with_sensitivity_to](associated_with_sensitivity_to.md)
                * [associated_with_resistance_to](associated_with_resistance_to.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
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
| self | namo:associated_with_response_to |
| native | namo:associated_with_response_to |




## LinkML Source

<details>
```yaml
name: associated with response to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A statistical association used to indicate that the object of a statement
  using this predicate induces a response of some kind in the subject entity.  Intentionally
  broad in definition, this predicate should be used with qualifiers to narrow the
  type of response (E.g. whether the response is therapeutic, phenotypic, detrimental,
  resistant, etc. is captured in context, direction, and aspect qualifiers).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: associated with
domain: named thing
inherited: true
alias: associated_with_response_to
range: named thing
multivalued: true

```
</details></div>