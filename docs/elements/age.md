

# Slot: age 


_The age of the animal used in the model system._





URI: [namo:age](https://w3id.org/monarch-initiative/namo/age)
Alias: age

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
| self | namo:age |
| native | namo:age |




## LinkML Source

<details>
```yaml
name: age
description: The age of the animal used in the model system.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: age
owner: AnimalModel
domain_of:
- AnimalModel
range: Term
bindings:
- range: OrganismAgeEnum
  obligation_level: REQUIRED
  binds_value_of: id

```
</details>