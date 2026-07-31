---
search:
  boost: 5.0
---

# Slot: phase 


_The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2._



<div data-search-exclude markdown="1">



URI: [namo:phase](https://w3id.org/monarch-initiative/namo/phase)

## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **phase**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhaseEnum](PhaseEnum.md) |
| Domain | [CodingSequence](CodingSequence.md) |
| Domain Of | [GenomicSequenceLocalization](GenomicSequenceLocalization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:phase |
| native | namo:phase |
| exact | gff3:phase |




## LinkML Source

<details>
```yaml
name: phase
description: The phase for a coding sequence entity. For example, phase of a CDS as
  represented in a GFF3 with a value of 0, 1 or 2.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- gff3:phase
rank: 1000
is_a: sequence localization attribute
domain: coding sequence
domain_of:
- genomic sequence localization
range: PhaseEnum

```
</details></div>