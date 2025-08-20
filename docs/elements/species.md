

# Slot: species 


_The species of the animal used in the model system._





URI: [namo:species](https://w3id.org/monarch-initiative/namo/species)
Alias: species

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnimalModel](AnimalModel.md) |  |  no  |






## Properties

* Range: [Term](Term.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:species |
| native | namo:species |




## LinkML Source

<details>
```yaml
name: species
description: The species of the animal used in the model system.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: species
owner: AnimalModel
domain_of:
- AnimalModel
range: Term
bindings:
- range: SpeciesEnum
  obligation_level: REQUIRED
  binds_value_of: id
required: true

```
</details>