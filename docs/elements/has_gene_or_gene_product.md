---
search:
  boost: 5.0
---

# Slot: has_gene_or_gene_product 


_connects an entity with one or more gene or gene products_



<div data-search-exclude markdown="1">



URI: [namo:has_gene_or_gene_product](https://w3id.org/monarch-initiative/namo/has_gene_or_gene_product)
Alias: has_gene_or_gene_product


## Inheritance

* [node_property](node_property.md)
    * **has_gene_or_gene_product**
        * [has_gene](has_gene.md)






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneGroupingMixin](GeneGroupingMixin.md) | any grouping of multiple genes or gene products |  no  |
| [ProteinDomain](ProteinDomain.md) | A conserved part of protein sequence and (tertiary) structure that can evolve... |  no  |
| [ProteinFamily](ProteinFamily.md) | A set of proteins coding for diverse functions which, by virtue of their high... |  no  |
| [GeneFamily](GeneFamily.md) | any grouping of multiple genes or gene products related by common descent |  no  |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic backg... |  no  |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | drug to gene interaction exposure is a drug exposure is where the interaction... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gene](Gene.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [GeneGroupingMixin](GeneGroupingMixin.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_gene_or_gene_product |
| native | namo:has_gene_or_gene_product |




## LinkML Source

<details>
```yaml
name: has gene or gene product
description: connects an entity with one or more gene or gene products
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: named thing
alias: has_gene_or_gene_product
domain_of:
- gene grouping mixin
range: gene
multivalued: true

```
</details></div>