---
search:
  boost: 5.0
---

# Slot: name 


_A human-readable name for a thing_



<div data-search-exclude markdown="1">



URI: [schema:name](http://schema.org/name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |
| [BiolinkEntity](BiolinkEntity.md) | Abstract parent for NAMO classes that stand in for a class in the Biolink Mod... |  no  |
| [Study](Study.md) | A study is a structured investigation or analysis, often involving the collec... |  no  |
| [ModelSystem](ModelSystem.md) |  |  no  |
| [AnimalModel](AnimalModel.md) |  |  no  |
| [NAMModel](NAMModel.md) | A New Approach Methodology (NAM) model, which is a type of model system that ... |  no  |
| [CellularSystem](CellularSystem.md) | Cell-based model systems that use living cells to model biological processes |  no  |
| [TwoDCellCulture](TwoDCellCulture.md) | Conventional monolayer cell cultures grown on flat surfaces |  no  |
| [ThreeDCellCulture](ThreeDCellCulture.md) | Three-dimensional cell culture systems including spheroids and organoids |  no  |
| [CoCulture](CoCulture.md) | Co-culture systems combining multiple cell types to mimic  microenvironments ... |  no  |
| [Organoid](Organoid.md) | A 3D cell culture system that self-organizes to recapitulate key structural a... |  no  |
| [CellLineModel](CellLineModel.md) | A model system based on immortalized cell lines that can be maintained in cul... |  no  |
| [MicrophysiologicalSystem](MicrophysiologicalSystem.md) | Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials, and... |  no  |
| [OrganOnChip](OrganOnChip.md) | A model system that simulates the physiological functions of an organ using a... |  no  |
| [TissueOnChip](TissueOnChip.md) | Tissue-level microphysiological systems that model specific tissue functions ... |  no  |
| [InSilicoModel](InSilicoModel.md) | Computational models that simulate biological processes without physical biol... |  no  |
| [QSARModel](QSARModel.md) | Quantitative Structure-Activity Relationship models that predict  chemical/bi... |  no  |
| [PBPKModel](PBPKModel.md) | Physiologically Based Pharmacokinetic models that simulate drug  absorption, ... |  no  |
| [DigitalTwin](DigitalTwin.md) | Computational replicas of biological systems for real-time prediction and per... |  no  |
| [MLModel](MLModel.md) | Machine Learning and AI-based models for prediction, mechanism inference, and... |  no  |
| [MetabolicModel](MetabolicModel.md) | A model that simulates the metabolic processes of an organism or system |  no  |
| [PBPKCompartment](PBPKCompartment.md) | A physiological compartment in a PBPK model |  no  |
| [MicrofluidicDesign](MicrofluidicDesign.md) | Detailed specification of a microfluidic device design including its architec... |  no  |
| [MechanicalStimulation](MechanicalStimulation.md) | Specification of mechanical forces applied to the model system |  no  |
| [BiologicalSystem](BiologicalSystem.md) |  |  no  |
| [MolecularSimilarity](MolecularSimilarity.md) | Detailed assessment of molecular-level concordance between model and biologic... |  no  |
| [PathwayConcordance](PathwayConcordance.md) | Assessment of biological pathway conservation and activity between model and ... |  no  |
| [PhenotypeOverlap](PhenotypeOverlap.md) | Comparison of phenotypic manifestations between model and biological systems |  no  |
| [CellTypeCoverage](CellTypeCoverage.md) | Assessment of cell type representation and cellular diversity between systems |  no  |
| [FunctionalParity](FunctionalParity.md) | Evaluation of functional capabilities and physiological responses between sys... |  no  |
| [Reproducibility](Reproducibility.md) | Assessment of experimental reproducibility and consistency of the model syste... |  no  |
| [Gene](Gene.md) | A gene entity with identifiers and expression information |  no  |
| [Pathway](Pathway.md) | A biological pathway with activity and enrichment information |  no  |
| [FunctionalAssay](FunctionalAssay.md) | A functional assay used to assess biological capabilities |  no  |
| [OrganismTaxon](OrganismTaxon.md) | A classification of a set of organisms |  no  |
| [Cell](Cell.md) | The basic structural and functional unit of all organisms |  no  |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | An anatomical structure that has more than one cell as a part |  no  |
| [PhenotypicFeature](PhenotypicFeature.md) | A combination of entity and quality that makes up a phenotyping statement |  no  |
| [LifeStage](LifeStage.md) | A stage of development or growth of an organism, including post-natal adult s... |  no  |
| [EnvironmentalExposure](EnvironmentalExposure.md) | A discrete event type where an organism is exposed to an environmental condit... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [NamedThing](NamedThing.md), [BiolinkEntity](BiolinkEntity.md) |
| Slot URI | [schema:name](http://schema.org/name) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:name |
| native | namo:name |




## LinkML Source

<details>
```yaml
name: name
description: A human-readable name for a thing
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
slot_uri: schema:name
domain_of:
- NamedThing
- BiolinkEntity
range: string

```
</details></div>