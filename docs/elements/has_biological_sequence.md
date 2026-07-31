---
search:
  boost: 5.0
---

# Slot: has_biological_sequence 


_connects a genomic feature to its sequence_



<div data-search-exclude markdown="1">



URI: [namo:has_biological_sequence](https://w3id.org/monarch-initiative/namo/has_biological_sequence)
Alias: has_biological_sequence


## Inheritance

* [node_property](node_property.md)
    * **has_biological_sequence**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomicEntity](GenomicEntity.md) | A generically dependent continuant that carries biological sequence that is p... |  no  |
| [EpigenomicEntity](EpigenomicEntity.md) | A mixin for entities that represent epigenomic modifications or features asso... |  no  |
| [NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |  no  |
| [RegulatoryRegion](RegulatoryRegion.md) | A region (or regions) of the genome that contains known or putative regulator... |  no  |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | A region (or regions) of a chromatinized genome that has been measured to be ... |  no  |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | A region (or regions) of the genome that contains a region of DNA known or pr... |  no  |
| [Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |  no  |
| [NucleosomeModification](NucleosomeModification.md) | A chemical modification of a histone protein within a nucleosome octomer or a... |  no  |
| [Genome](Genome.md) | A genome is the sum of genetic material within a cell or virion |  no  |
| [CodingSequence](CodingSequence.md) | A contiguous sequence which begins with, and includes, a start codon and ends... |  no  |
| [Genotype](Genotype.md) | An information content entity that describes a genome by specifying the total... |  no  |
| [Haplotype](Haplotype.md) | A set of zero or more Alleles on a single instance of a Sequence[VMC] |  no  |
| [SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibi... |  yes  |
| [Snv](Snv.md) | SNVs are single nucleotide positions in genomic DNA at which different sequen... |  no  |
| [ReagentTargetedGene](ReagentTargetedGene.md) | A gene altered in its expression level in the context of some experiment as a... |  no  |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic backg... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalSequence](BiologicalSequence.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [GenomicEntity](GenomicEntity.md), [EpigenomicEntity](EpigenomicEntity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_biological_sequence |
| native | namo:has_biological_sequence |




## LinkML Source

<details>
```yaml
name: has biological sequence
description: connects a genomic feature to its sequence
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: named thing
alias: has_biological_sequence
domain_of:
- genomic entity
- epigenomic entity
range: biological sequence

```
</details></div>