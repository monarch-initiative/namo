---
search:
  boost: 10.0
---

# Class: EpigenomicEntity 


_A mixin for entities that represent epigenomic modifications or features associated with heritable changes in gene expression that do not involve changes to the DNA sequence itself._



<div data-search-exclude markdown="1">



URI: [namo:EpigenomicEntity](https://w3id.org/monarch-initiative/namo/EpigenomicEntity)





```mermaid
 classDiagram
    class EpigenomicEntity
    click EpigenomicEntity href "../EpigenomicEntity/"
      EpigenomicEntity <|-- NucleosomeModification
        click NucleosomeModification href "../NucleosomeModification/"
      
      EpigenomicEntity : has_biological_sequence
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_biological_sequence](has_biological_sequence.md) | 0..1 <br/> [BiologicalSequence](BiologicalSequence.md) | connects a genomic feature to its sequence | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [NucleosomeModification](NucleosomeModification.md) | A chemical modification of a histone protein within a nucleosome octomer or a... |










## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:EpigenomicEntity |
| native | namo:EpigenomicEntity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: epigenomic entity
description: A mixin for entities that represent epigenomic modifications or features
  associated with heritable changes in gene expression that do not involve changes
  to the DNA sequence itself.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
slots:
- has biological sequence

```
</details>

### Induced

<details>
```yaml
name: epigenomic entity
description: A mixin for entities that represent epigenomic modifications or features
  associated with heritable changes in gene expression that do not involve changes
  to the DNA sequence itself.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
attributes:
  has biological sequence:
    name: has biological sequence
    description: connects a genomic feature to its sequence
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    alias: has_biological_sequence
    owner: epigenomic entity
    domain_of:
    - genomic entity
    - epigenomic entity
    range: biological sequence

```
</details></div>