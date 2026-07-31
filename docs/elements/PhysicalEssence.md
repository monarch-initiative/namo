---
search:
  boost: 10.0
---

# Class: PhysicalEssence 


_Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge._



<div data-search-exclude markdown="1">



URI: [namo:PhysicalEssence](https://w3id.org/monarch-initiative/namo/PhysicalEssence)





```mermaid
 classDiagram
    class PhysicalEssence
    click PhysicalEssence href "../PhysicalEssence/"
      PhysicalEssenceOrOccurrent <|-- PhysicalEssence
        click PhysicalEssenceOrOccurrent href "../PhysicalEssenceOrOccurrent/"
      

      PhysicalEssence <|-- PhysicalEntity
        click PhysicalEntity href "../PhysicalEntity/"
      PhysicalEssence <|-- ChemicalEntity
        click ChemicalEntity href "../ChemicalEntity/"
      PhysicalEssence <|-- NucleicAcidEntity
        click NucleicAcidEntity href "../NucleicAcidEntity/"
      PhysicalEssence <|-- RegulatoryRegion
        click RegulatoryRegion href "../RegulatoryRegion/"
      PhysicalEssence <|-- AccessibleDnaRegion
        click AccessibleDnaRegion href "../AccessibleDnaRegion/"
      PhysicalEssence <|-- TranscriptionFactorBindingSite
        click TranscriptionFactorBindingSite href "../TranscriptionFactorBindingSite/"
      PhysicalEssence <|-- AnatomicalEntity
        click AnatomicalEntity href "../AnatomicalEntity/"
      PhysicalEssence <|-- Gene
        click Gene href "../Gene/"
      PhysicalEssence <|-- Genome
        click Genome href "../Genome/"
      PhysicalEssence <|-- Genotype
        click Genotype href "../Genotype/"
      PhysicalEssence <|-- Haplotype
        click Haplotype href "../Haplotype/"
      PhysicalEssence <|-- SequenceVariant
        click SequenceVariant href "../SequenceVariant/"
      PhysicalEssence <|-- ReagentTargetedGene
        click ReagentTargetedGene href "../ReagentTargetedGene/"
      PhysicalEssence <|-- GenomicBackgroundExposure
        click GenomicBackgroundExposure href "../GenomicBackgroundExposure/"
      

      
```





## Inheritance
* [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md)
    * **PhysicalEssence**


## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [PhysicalEntity](PhysicalEntity.md) | An entity that has material reality (a |
| [ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemi... |
| [NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |
| [RegulatoryRegion](RegulatoryRegion.md) | A region (or regions) of the genome that contains known or putative regulator... |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | A region (or regions) of a chromatinized genome that has been measured to be ... |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | A region (or regions) of the genome that contains a region of DNA known or pr... |
| [AnatomicalEntity](AnatomicalEntity.md) | A part of a cellular organism at or above the granularity of a protein comple... |
| [Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |
| [Genome](Genome.md) | A genome is the sum of genetic material within a cell or virion |
| [Genotype](Genotype.md) | An information content entity that describes a genome by specifying the total... |
| [Haplotype](Haplotype.md) | A set of zero or more Alleles on a single instance of a Sequence[VMC] |
| [SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibi... |
| [ReagentTargetedGene](ReagentTargetedGene.md) | A gene altered in its expression level in the context of some experiment as a... |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic backg... |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:PhysicalEssence |
| native | namo:PhysicalEssence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: physical essence
description: Semantic mixin concept.  Pertains to entities that have physical properties
  such as mass, volume, or charge.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: physical essence or occurrent
mixin: true

```
</details>

### Induced

<details>
```yaml
name: physical essence
description: Semantic mixin concept.  Pertains to entities that have physical properties
  such as mass, volume, or charge.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: physical essence or occurrent
mixin: true

```
</details></div>