---
search:
  boost: 5.0
---

# Slot: strand 


_The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand)._



<div data-search-exclude markdown="1">



URI: [namo:strand](https://w3id.org/monarch-initiative/namo/strand)

## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **strand**






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
| self | namo:strand |
| native | namo:strand |
| exact | gff3:strand |




## LinkML Source

<details>
```yaml
name: strand
description: The strand on which a feature is located. Has a value of '+' (sense strand
  or forward strand) or '-' (anti-sense strand or reverse strand).
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- gff3:strand
rank: 1000
is_a: sequence localization attribute
domain: genomic sequence localization
domain_of:
- genomic sequence localization
range: StrandEnum

```
</details></div>