

# Slot: validation_datasets 


_Datasets used for model training and validation_





URI: [namo:validation_datasets](https://w3id.org/monarch-initiative/namo/validation_datasets)
Alias: validation_datasets

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InSilicoModel](InSilicoModel.md) | Computational models that simulate biological processes without physical biol... |  no  |
| [MetabolicModel](MetabolicModel.md) | A model that simulates the metabolic processes of an organism or system |  no  |
| [PBPKModel](PBPKModel.md) | Physiologically Based Pharmacokinetic models that simulate drug  absorption, ... |  no  |
| [DigitalTwin](DigitalTwin.md) | Computational replicas of biological systems for real-time prediction and per... |  no  |
| [QSARModel](QSARModel.md) | Quantitative Structure-Activity Relationship models that predict  chemical/bi... |  no  |
| [MLModel](MLModel.md) | Machine Learning and AI-based models for prediction, mechanism inference, and... |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:validation_datasets |
| native | namo:validation_datasets |




## LinkML Source

<details>
```yaml
name: validation_datasets
description: Datasets used for model training and validation
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: validation_datasets
owner: InSilicoModel
domain_of:
- InSilicoModel
range: string
multivalued: true

```
</details>