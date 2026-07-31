---
search:
  boost: 2.0
---


# Enum: DruggableGeneCategoryEnum 




_An enumeration of druggability categories for gene targets as defined by the IDG (Illuminating the Druggable Genome) / Pharos target development level classification: Tclin (targets of approved drugs), Tchem (targets with potent bioactives), Tbio (targets with biological knowledge), and Tdark (poorly characterized targets)._



<div data-search-exclude markdown="1">

URI: [namo:DruggableGeneCategoryEnum](https://w3id.org/monarch-initiative/namo/DruggableGeneCategoryEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| tclin | None | These targets have activities in DrugCentral (ie |
| tbio | None | These targets have activities in ChEMBL, Guide to Pharmacology or DrugCentral... |
| tchem | None | These targets do not have known drug or small molecule activities that satisf... |
| tdark | None | These are targets about which virtually nothing is known |




## Slots

| Name | Description |
| ---  | --- |
| [druggable_gene_category](druggable_gene_category.md) | Classification of druggable genes based on knowledge about drug or small mole... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: DruggableGeneCategoryEnum
description: 'An enumeration of druggability categories for gene targets as defined
  by the IDG (Illuminating the Druggable Genome) / Pharos target development level
  classification: Tclin (targets of approved drugs), Tchem (targets with potent bioactives),
  Tbio (targets with biological knowledge), and Tdark (poorly characterized targets).'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  tclin:
    text: tclin
    description: These targets have activities in DrugCentral (ie. approved drugs)
      with known mechanism of action.
  tbio:
    text: tbio
    description: These targets have activities in ChEMBL, Guide to Pharmacology or
      DrugCentral that satisfy the activity thresholds detailed below.
  tchem:
    text: tchem
    description: 'These targets do not have known drug or small molecule activities
      that satisfy the activity thresholds detailed below AND satisfy one or more
      of the following criteria: target is above the cutoff criteria for the target
      is annotated with a Gene Ontology Molecular Function or Biological Process leaf
      term(s) with an Experimental Evidence code'
  tdark:
    text: tdark
    description: 'These are targets about which virtually nothing is known. They do
      not have known drug or small molecule activities that satisfy the activity thresholds
      detailed below AND satisfy two or more of the following criteria: A PubMed text-mining
      score from Jensen Lab less than 5, greater than or equal TO 3 Gene RIFs, or
      less than or equal to 50 Antibodies available according to http://antibodypedia.com.'

```
</details>

</div>