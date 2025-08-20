

# Slot: strain 


_The specific strain of the animal used in the model system._





URI: [namo:strain](https://w3id.org/monarch-initiative/namo/strain)
Alias: strain

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnimalModel](AnimalModel.md) |  |  no  |






## Properties

* Range: [Term](Term.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:strain |
| native | namo:strain |




## LinkML Source

<details>
```yaml
name: strain
description: The specific strain of the animal used in the model system.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: strain
owner: AnimalModel
domain_of:
- AnimalModel
range: Term
bindings:
- range: StrainEnum
  obligation_level: REQUIRED
  binds_value_of: id

```
</details>