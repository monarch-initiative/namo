---
search:
  boost: 5.0
---

# Slot: affects_likelihood_of 


_Holds between two entities where the presence or application of one alters the chance that the other will come to be._



<div data-search-exclude markdown="1">



URI: [namo:affects_likelihood_of](https://w3id.org/monarch-initiative/namo/affects_likelihood_of)
Alias: affects_likelihood_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **affects_likelihood_of**
            * [preventative_for_condition](preventative_for_condition.md) [ [treats](treats.md)]
            * [promotes_condition](promotes_condition.md)
            * [predisposes_to_condition](predisposes_to_condition.md) [ [promotes_condition](promotes_condition.md)]








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








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)




## Notes

* - This predicate implies causation, where the 'affected' entity is something that does not yet exist, and the actions/execution of effector impact the likelihood that this entity may come to be. It is NOT to be used for a statistical associations that describe correlations between two feature variables (use predicates in the 'associated with likelihood of' hierarchy here.)



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
| self | namo:affects_likelihood_of |
| native | namo:affects_likelihood_of |




## LinkML Source

<details>
```yaml
name: affects likelihood of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between two entities where the presence or application of one alters
  the chance that the other will come to be.
notes:
- '- This predicate implies causation, where the ''affected'' entity is something
  that does not yet exist, and the actions/execution of effector impact the likelihood
  that this entity may come to be. It is NOT to be used for a statistical associations
  that describe correlations between two feature variables (use predicates in the
  ''associated with likelihood of'' hierarchy here.)'
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: affects_likelihood_of
range: named thing
multivalued: true

```
</details></div>