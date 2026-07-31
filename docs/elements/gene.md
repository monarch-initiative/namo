---
search:
  boost: 5.0
---

# Slot: gene 


_The gene this measurement is about. Identifier prefixes follow Biolink's `gene` (HGNC, NCBIGene, ENSEMBL, ...), which replaces the former gene_symbol / ensembl_id / entrez_id attributes._



<div data-search-exclude markdown="1">



URI: [namo:gene](https://w3id.org/monarch-initiative/namo/gene)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneExpressionResult](GeneExpressionResult.md) | A differential-expression measurement for a single gene in a model system |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gene](Gene.md) |
| Domain Of | [GeneExpressionResult](GeneExpressionResult.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeneExpressionResult](GeneExpressionResult.md) |




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneExpressionResult](GeneExpressionResult.md) | [Gene](Gene.md) | range | [Gene](Gene.md) |
| [ProteinDomain](ProteinDomain.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [ProteinFamily](ProteinFamily.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [GeneGroupingMixin](GeneGroupingMixin.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [GeneFamily](GeneFamily.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [SequenceVariant](SequenceVariant.md) | [has_gene](has_gene.md) | range | [Gene](Gene.md) |
| [Snv](Snv.md) | [has_gene](has_gene.md) | range | [Gene](Gene.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object](object.md) | range | [Gene](Gene.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject](subject.md) | range | [Gene](Gene.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object](object.md) | range | [Gene](Gene.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object](object.md) | range | [Gene](Gene.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject](subject.md) | range | [Gene](Gene.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object](object.md) | range | [Gene](Gene.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject](subject.md) | range | [Gene](Gene.md) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:Gene |
| native | namo:Gene |
| exact | SO:0000704, SIO:010035, WIKIDATA:Q7187, dcid:Gene |
| narrow | bioschemas:gene |
| broad | NCIT:C45822 |




## LinkML Source

<details>
```yaml
name: gene
description: The gene this measurement is about. Identifier prefixes follow Biolink's
  `gene` (HGNC, NCBIGene, ENSEMBL, ...), which replaces the former gene_symbol / ensembl_id
  / entrez_id attributes.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: GeneExpressionResult
domain_of:
- GeneExpressionResult
range: gene
inlined: true

```
</details></div>