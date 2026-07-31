---
search:
  boost: 5.0
---

# Slot: stage_qualifier 


_stage during which gene or protein expression of takes place._



<div data-search-exclude markdown="1">



URI: [namo:stage_qualifier](https://w3id.org/monarch-initiative/namo/stage_qualifier)
Alias: stage_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [statement_qualifier](statement_qualifier.md)
            * **stage_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phen... |  no  |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and a gene expression site, possibly qualified ... |  yes  |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LifeStage](LifeStage.md) |
| Domain | [Association](Association.md) |
| Domain Of | [GeneExpressionMixin](GeneExpressionMixin.md), [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)





## Examples

| Value |
| --- |
| UBERON:0000069 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:stage_qualifier |
| native | namo:stage_qualifier |




## LinkML Source

<details>
```yaml
name: stage qualifier
description: stage during which gene or protein expression of takes place.
examples:
- value: UBERON:0000069
  description: larval stage
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: statement qualifier
domain: association
alias: stage_qualifier
domain_of:
- gene expression mixin
- gene to expression site association
range: life stage

```
</details></div>