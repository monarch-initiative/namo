---
search:
  boost: 5.0
---

# Slot: process_qualifier 


_Restricts the biological process within which the core concept (or qualified core concept) participates._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:process_qualifier](https://w3id.org/monarch-initiative/namo/process_qualifier)
Alias: process_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **process_qualifier**
            * [subject_activity_qualifier](subject_activity_qualifier.md)
            * [subject_process_qualifier](subject_process_qualifier.md)
            * [object_activity_qualifier](object_activity_qualifier.md)
            * [object_process_qualifier](object_process_qualifier.md)








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
| GO:0009101 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:process_qualifier |
| native | namo:process_qualifier |




## LinkML Source

<details>
```yaml
name: process qualifier
description: Restricts the biological process within which the core concept (or qualified
  core concept) participates.
examples:
- value: GO:0009101
  description: glycoprotein biosynthetic process
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: process_qualifier
range: string

```
</details></div>