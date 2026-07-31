---
search:
  boost: 5.0
---

# Slot: genome_build 


_The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens._



<div data-search-exclude markdown="1">



URI: [namo:genome_build](https://w3id.org/monarch-initiative/namo/genome_build)
Alias: genome_build


## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **genome_build**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StrandEnum](StrandEnum.md) |
| Domain | [GenomicSequenceLocalization](GenomicSequenceLocalization.md) |
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
| self | namo:genome_build |
| native | namo:genome_build |
| exact | gff3:strand |




## LinkML Source

<details>
```yaml
name: genome build
description: The version of the genome on which a feature is located. For example,
  GRCh38 for Homo sapiens.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- gff3:strand
rank: 1000
is_a: sequence localization attribute
domain: genomic sequence localization
alias: genome_build
domain_of:
- genomic sequence localization
range: StrandEnum

```
</details></div>