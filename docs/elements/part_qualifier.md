---
search:
  boost: 5.0
---

# Slot: part_qualifier 


_defines a specific part/component of the core concept (used in cases there this specific part has no IRI we can use to directly represent it)._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:part_qualifier](https://w3id.org/monarch-initiative/namo/part_qualifier)
Alias: part_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **part_qualifier**
            * [subject_part_qualifier](subject_part_qualifier.md)
            * [object_part_qualifier](object_part_qualifier.md)








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
| polyA tail |
| upstream control region |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:part_qualifier |
| native | namo:part_qualifier |




## LinkML Source

<details>
```yaml
name: part qualifier
description: defines a specific part/component of the core concept (used in cases
  there this specific part has no IRI we can use to directly represent it).
examples:
- value: polyA tail
- value: upstream control region
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: part_qualifier
range: string

```
</details></div>