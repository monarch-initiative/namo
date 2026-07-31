---
search:
  boost: 5.0
---

# Slot: direction_qualifier 


_Composes with the core concept (+ aspect if provided) to describe a change in its direction or degree._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:direction_qualifier](https://w3id.org/monarch-initiative/namo/direction_qualifier)
Alias: direction_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **direction_qualifier**
            * [subject_direction_qualifier](subject_direction_qualifier.md)
            * [object_direction_qualifier](object_direction_qualifier.md)








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




## Notes

* the qualifier ‘increased’ combines with a core concept of ‘Gene X’ and an aspect of ‘expression’ to express the composed concept ‘increased expression of Gene X’ the qualifier ‘decreased’ combines with a core concept of ‘Protein X’ and an aspect of ‘abundance’ to express the composed concept ‘decreased abundance of Protein X’



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:direction_qualifier |
| native | namo:direction_qualifier |




## LinkML Source

<details>
```yaml
name: direction qualifier
description: Composes with the core concept (+ aspect if provided) to describe a change
  in its direction or degree.
notes:
- the qualifier ‘increased’ combines with a core concept of ‘Gene X’ and an aspect
  of ‘expression’ to express the composed concept ‘increased expression of Gene X’
  the qualifier ‘decreased’ combines with a core concept of ‘Protein X’ and an aspect
  of ‘abundance’ to express the composed concept ‘decreased abundance of Protein X’
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: direction_qualifier
range: string

```
</details></div>