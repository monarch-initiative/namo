

# Slot: id 


_A unique identifier for a thing_





URI: [schema:identifier](http://schema.org/identifier)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetabolicModel](MetabolicModel.md) | A model that simulates the metabolic processes of an organism or system |  no  |
| [ThreeDCellCulture](ThreeDCellCulture.md) | Three-dimensional cell culture systems including spheroids and organoids |  no  |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |
| [ModelSystem](ModelSystem.md) |  |  no  |
| [FunctionalParity](FunctionalParity.md) | Evaluation of functional capabilities and physiological responses between sys... |  no  |
| [PhenotypeOverlap](PhenotypeOverlap.md) | Comparison of phenotypic manifestations between model and biological systems |  no  |
| [FunctionalAssay](FunctionalAssay.md) | A functional assay used to assess biological capabilities |  no  |
| [BiologicalSystem](BiologicalSystem.md) |  |  no  |
| [Term](Term.md) | A term is a concept or entity that can be defined and used in a specific cont... |  no  |
| [Gene](Gene.md) | A gene entity with identifiers and expression information |  no  |
| [Reproducibility](Reproducibility.md) | Assessment of experimental reproducibility and consistency of the model syste... |  no  |
| [OrganOnChip](OrganOnChip.md) | A model system that simulates the physiological functions of an organ using a... |  no  |
| [PBPKModel](PBPKModel.md) | Physiologically Based Pharmacokinetic models that simulate drug  absorption, ... |  no  |
| [TissueOnChip](TissueOnChip.md) | Tissue-level microphysiological systems that model specific tissue functions ... |  no  |
| [Study](Study.md) | A study is a structured investigation or analysis, often involving the collec... |  no  |
| [CellTypeCoverage](CellTypeCoverage.md) | Assessment of cell type representation and cellular diversity between systems |  no  |
| [CoCulture](CoCulture.md) | Co-culture systems combining multiple cell types to mimic  microenvironments ... |  no  |
| [MLModel](MLModel.md) | Machine Learning and AI-based models for prediction, mechanism inference, and... |  no  |
| [Organoid](Organoid.md) | A 3D cell culture system that self-organizes to recapitulate key structural a... |  no  |
| [InSilicoModel](InSilicoModel.md) | Computational models that simulate biological processes without physical biol... |  no  |
| [DigitalTwin](DigitalTwin.md) | Computational replicas of biological systems for real-time prediction and per... |  no  |
| [NAMModel](NAMModel.md) | A New Approach Methodology (NAM) model, which is a type of model system that ... |  no  |
| [PathwayConcordance](PathwayConcordance.md) | Assessment of biological pathway conservation and activity between model and ... |  no  |
| [MicrophysiologicalSystem](MicrophysiologicalSystem.md) | Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials,  an... |  no  |
| [PBPKCompartment](PBPKCompartment.md) | A physiological compartment in a PBPK model |  no  |
| [TwoDCellCulture](TwoDCellCulture.md) | Conventional monolayer cell cultures grown on flat surfaces |  no  |
| [MechanicalStimulation](MechanicalStimulation.md) | Specification of mechanical forces applied to the model system |  no  |
| [CellularSystem](CellularSystem.md) | Cell-based model systems that use living cells to model biological processes |  no  |
| [MicrofluidicDesign](MicrofluidicDesign.md) | Detailed specification of a microfluidic device design including its architec... |  no  |
| [Pathway](Pathway.md) | A biological pathway with activity and enrichment information |  no  |
| [QSARModel](QSARModel.md) | Quantitative Structure-Activity Relationship models that predict  chemical/bi... |  no  |
| [AnimalModel](AnimalModel.md) |  |  no  |
| [Reference](Reference.md) | A literature reference with identifier and title for citing published work |  no  |
| [MolecularSimilarity](MolecularSimilarity.md) | Detailed assessment of molecular-level concordance between model and biologic... |  no  |
| [CellLineModel](CellLineModel.md) | A model system based on immortalized cell lines that can be maintained in cul... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:identifier |
| native | namo:id |




## LinkML Source

<details>
```yaml
name: id
description: A unique identifier for a thing
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
slot_uri: schema:identifier
identifier: true
alias: id
domain_of:
- NamedThing
- Reference
range: uriorcurie
required: true

```
</details>