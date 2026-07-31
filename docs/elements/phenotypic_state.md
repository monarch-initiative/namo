---
search:
  boost: 5.0
---

# Slot: phenotypic_state 


_in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX._



<div data-search-exclude markdown="1">



URI: [namo:phenotypic_state](https://w3id.org/monarch-initiative/namo/phenotypic_state)
Alias: phenotypic_state


## Inheritance

* [association_slot](association_slot.md)
    * **phenotypic_state**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phen... |  no  |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |
| Domain | [Association](Association.md) |
| Domain Of | [GeneExpressionMixin](GeneExpressionMixin.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:phenotypic_state |
| native | namo:phenotypic_state |




## LinkML Source

<details>
```yaml
name: phenotypic state
description: in experiments (e.g. gene expression) assaying diseased or unhealthy
  tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues,
  use XXX.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: phenotypic_state
domain_of:
- gene expression mixin
range: disease or phenotypic feature

```
</details></div>