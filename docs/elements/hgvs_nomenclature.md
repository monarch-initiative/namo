---
search:
  boost: 5.0
---

# Slot: hgvs_nomenclature 


_HGVS syntax refers to the specific rules and conventions used by the Human Variant Nomenclature Committee to describe the location and change in DNA, RNA, and protein sequence variants.  This slot is used to capture all the different forms of HGVS nomenclature that may be used to describe a sequence variant, including genomic, transcript, and protein HGVS expressions/nomenclatures and is thus multivalued._



<div data-search-exclude markdown="1">



URI: [namo:hgvs_nomenclature](https://w3id.org/monarch-initiative/namo/hgvs_nomenclature)
Alias: hgvs_nomenclature


## Inheritance

* [node_property](node_property.md)
    * **hgvs_nomenclature**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibi... |  no  |
| [Snv](Snv.md) | SNVs are single nucleotide positions in genomic DNA at which different sequen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [SequenceVariant](SequenceVariant.md) |
| Domain Of | [SequenceVariant](SequenceVariant.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## Comments

* For more information, please see: https://hgvs-nomenclature.org/stable/background/simple/ and examples: https://hgvs-nomenclature.org/stable/recommendations/summary/.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:hgvs_nomenclature |
| native | namo:hgvs_nomenclature |




## LinkML Source

<details>
```yaml
name: hgvs nomenclature
description: HGVS syntax refers to the specific rules and conventions used by the
  Human Variant Nomenclature Committee to describe the location and change in DNA,
  RNA, and protein sequence variants.  This slot is used to capture all the different
  forms of HGVS nomenclature that may be used to describe a sequence variant, including
  genomic, transcript, and protein HGVS expressions/nomenclatures and is thus multivalued.
comments:
- 'For more information, please see: https://hgvs-nomenclature.org/stable/background/simple/
  and examples: https://hgvs-nomenclature.org/stable/recommendations/summary/.'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: sequence variant
alias: hgvs_nomenclature
domain_of:
- sequence variant
range: string
multivalued: true

```
</details></div>