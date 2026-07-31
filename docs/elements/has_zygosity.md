---
search:
  boost: 5.0
---

# Slot: has_zygosity 


_The zygosity characterising a genotype or nucleic acid entity at a particular locus._



<div data-search-exclude markdown="1">



URI: [namo:has_zygosity](https://w3id.org/monarch-initiative/namo/has_zygosity)
Alias: has_zygosity


## Inheritance

* [node_property](node_property.md)
    * **has_zygosity**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Genotype](Genotype.md) | An information content entity that describes a genome by specifying the total... |  no  |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | Association between a Case and a Genetic Variant |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Zygosity](Zygosity.md) |
| Domain | [NucleicAcidEntity](NucleicAcidEntity.md) |
| Domain Of | [Genotype](Genotype.md), [CaseToVariantAssociation](CaseToVariantAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_zygosity |
| native | namo:has_zygosity |




## LinkML Source

<details>
```yaml
name: has zygosity
description: The zygosity characterising a genotype or nucleic acid entity at a particular
  locus.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: nucleic acid entity
alias: has_zygosity
domain_of:
- genotype
- case to variant association
range: zygosity

```
</details></div>