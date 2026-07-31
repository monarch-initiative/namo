---
search:
  boost: 5.0
---

# Slot: has_plasma_membrane_part 


_Holds between a cell c and a protein complex or protein p if and only if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane has p as part._



<div data-search-exclude markdown="1">



URI: [namo:has_plasma_membrane_part](https://w3id.org/monarch-initiative/namo/has_plasma_membrane_part)
Alias: has_plasma_membrane_part


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_plasma_membrane_part**








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
| self | namo:has_plasma_membrane_part |
| native | namo:has_plasma_membrane_part |
| exact | RO:0002104 |




## LinkML Source

<details>
```yaml
name: has plasma membrane part
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between a cell c and a protein complex or protein p if and only
  if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane
  has p as part.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002104
rank: 1000
is_a: has part
domain: named thing
inherited: true
alias: has_plasma_membrane_part
range: named thing
multivalued: true

```
</details></div>