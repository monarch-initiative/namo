---
search:
  boost: 5.0
---

# Slot: context_qualifier 


_Restricts the setting/context/location where the core concept (or qualified core concept) resides or occurs._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:context_qualifier](https://w3id.org/monarch-initiative/namo/context_qualifier)
Alias: context_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **context_qualifier**
            * [response_context_qualifier](response_context_qualifier.md)
            * [response_target_context_qualifier](response_target_context_qualifier.md)
            * [subject_context_qualifier](subject_context_qualifier.md)
            * [object_context_qualifier](object_context_qualifier.md)
            * [disease_context_qualifier](disease_context_qualifier.md)








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
| OHMI:0000020 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:context_qualifier |
| native | namo:context_qualifier |




## LinkML Source

<details>
```yaml
name: context qualifier
description: Restricts the setting/context/location where the core concept (or qualified
  core concept) resides or occurs.
examples:
- value: OHMI:0000020
  description: gut microbiome
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: context_qualifier
range: string

```
</details></div>