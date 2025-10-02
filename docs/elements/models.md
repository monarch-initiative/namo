

# Slot: models 



URI: [namo:models](https://w3id.org/monarch-initiative/namo/models)
Alias: models

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NAMModel](NAMModel.md) | A New Approach Methodology (NAM) model, which is a type of model system that ... |  no  |
| [QSARModel](QSARModel.md) | Quantitative Structure-Activity Relationship models that predict  chemical/bi... |  no  |
| [InSilicoModel](InSilicoModel.md) | Computational models that simulate biological processes without physical biol... |  no  |
| [CellLineModel](CellLineModel.md) | A model system based on immortalized cell lines that can be maintained in cul... |  no  |
| [CellularSystem](CellularSystem.md) | Cell-based model systems that use living cells to model biological processes |  no  |
| [TissueOnChip](TissueOnChip.md) | Tissue-level microphysiological systems that model specific tissue functions ... |  no  |
| [MetabolicModel](MetabolicModel.md) | A model that simulates the metabolic processes of an organism or system |  no  |
| [TwoDCellCulture](TwoDCellCulture.md) | Conventional monolayer cell cultures grown on flat surfaces |  no  |
| [OrganOnChip](OrganOnChip.md) | A model system that simulates the physiological functions of an organ using a... |  no  |
| [MicrophysiologicalSystem](MicrophysiologicalSystem.md) | Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials, and... |  no  |
| [DigitalTwin](DigitalTwin.md) | Computational replicas of biological systems for real-time prediction and per... |  no  |
| [MLModel](MLModel.md) | Machine Learning and AI-based models for prediction, mechanism inference, and... |  no  |
| [CoCulture](CoCulture.md) | Co-culture systems combining multiple cell types to mimic  microenvironments ... |  no  |
| [ThreeDCellCulture](ThreeDCellCulture.md) | Three-dimensional cell culture systems including spheroids and organoids |  no  |
| [ModelSystem](ModelSystem.md) |  |  no  |
| [Organoid](Organoid.md) | A 3D cell culture system that self-organizes to recapitulate key structural a... |  no  |
| [AnimalModel](AnimalModel.md) |  |  no  |
| [PBPKModel](PBPKModel.md) | Physiologically Based Pharmacokinetic models that simulate drug  absorption, ... |  no  |






## Properties

* Range: [ModelsRelationship](ModelsRelationship.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:models |
| native | namo:models |




## LinkML Source

<details>
```yaml
name: models
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: models
owner: ModelSystem
domain_of:
- ModelSystem
range: ModelsRelationship
multivalued: true

```
</details>