---
search:
  boost: 5.0
---

# Slot: quantifier_qualifier 


_A measurable quantity for the object of the association_



<div data-search-exclude markdown="1">



URI: [namo:quantifier_qualifier](https://w3id.org/monarch-initiative/namo/quantifier_qualifier)
Alias: quantifier_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * **quantifier_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phen... |  yes  |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and a gene expression site, possibly qualified ... |  yes  |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OntologyClass](OntologyClass.md) |
| Domain | [Association](Association.md) |
| Domain Of | [GeneExpressionMixin](GeneExpressionMixin.md), [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:quantifier_qualifier |
| native | namo:quantifier_qualifier |
| narrow | LOINC:analyzes, LOINC:measured_by, LOINC:property_of, SEMMEDDB:MEASURES, UMLS:measures |




## LinkML Source

<details>
```yaml
name: quantifier qualifier
description: A measurable quantity for the object of the association
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- LOINC:analyzes
- LOINC:measured_by
- LOINC:property_of
- SEMMEDDB:MEASURES
- UMLS:measures
rank: 1000
is_a: association slot
domain: association
alias: quantifier_qualifier
domain_of:
- gene expression mixin
- gene to expression site association
range: ontology class

```
</details></div>