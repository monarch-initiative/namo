---
search:
  boost: 5.0
---

# Slot: associated_with_likelihood_of 


_A a relationship that holds between two concepts represented by variables for which a statistical dependence is demonstrated, wherein the state or value of one variable predicts the future state or value of the other.  E.g. the statement “An Atrial Fibrillation (Afib) diagnosis is associated with likelihood of a Myocardial Infraction (MI) diagnosis” asserts that the state of having Afib is associated with an increased or decreased likelihood that a patient will later exhibit MI._



<div data-search-exclude markdown="1">



URI: [namo:associated_with_likelihood_of](https://w3id.org/monarch-initiative/namo/associated_with_likelihood_of)
Alias: associated_with_likelihood_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * **associated_with_likelihood_of**
                * [associated_with_increased_likelihood_of](associated_with_increased_likelihood_of.md)
                * [associated_with_decreased_likelihood_of](associated_with_decreased_likelihood_of.md)








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
| self | namo:associated_with_likelihood_of |
| native | namo:associated_with_likelihood_of |




## LinkML Source

<details>
```yaml
name: associated with likelihood of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A a relationship that holds between two concepts represented by variables
  for which a statistical dependence is demonstrated, wherein the state or value of
  one variable predicts the future state or value of the other.  E.g. the statement
  “An Atrial Fibrillation (Afib) diagnosis is associated with likelihood of a Myocardial
  Infraction (MI) diagnosis” asserts that the state of having Afib is associated with
  an increased or decreased likelihood that a patient will later exhibit MI.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: associated with
domain: named thing
inherited: true
alias: associated_with_likelihood_of
range: named thing
multivalued: true

```
</details></div>