---
search:
  boost: 5.0
---

# Slot: derivative_qualifier 


_A qualifier that composes with a core subject/object  concept to describe something that is derived from the core concept.  For example, the qualifier ‘metabolite’ combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite of Chemical X’._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:derivative_qualifier](https://w3id.org/monarch-initiative/namo/derivative_qualifier)
Alias: derivative_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **derivative_qualifier**
            * [subject_derivative_qualifier](subject_derivative_qualifier.md)
            * [object_derivative_qualifier](object_derivative_qualifier.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)





## Examples

| Value |
| --- |
| metabolite |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:derivative_qualifier |
| native | namo:derivative_qualifier |




## LinkML Source

<details>
```yaml
name: derivative qualifier
description: A qualifier that composes with a core subject/object  concept to describe
  something that is derived from the core concept.  For example, the qualifier ‘metabolite’
  combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite
  of Chemical X’.
examples:
- value: metabolite
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: derivative_qualifier
range: string

```
</details></div>