# Enum: DigitalTwinScopeEnum 



URI: [namo:DigitalTwinScopeEnum](https://w3id.org/monarch-initiative/namo/DigitalTwinScopeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ORGAN | None | Digital twin of a specific organ |
| PATIENT | None | Digital twin of an individual patient |
| POPULATION | MAMO:0000028 | Digital twin representing a population |
| PATHWAY | None | Digital twin of biological pathways |
| DISEASE | None | Digital twin of disease progression |




## Slots

| Name | Description |
| ---  | --- |
| [twin_scope](twin_scope.md) | Scope of digital twin (organ, patient, population) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: DigitalTwinScopeEnum
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  ORGAN:
    text: ORGAN
    description: Digital twin of a specific organ
  PATIENT:
    text: PATIENT
    description: Digital twin of an individual patient
  POPULATION:
    text: POPULATION
    description: Digital twin representing a population
    meaning: MAMO:0000028
  PATHWAY:
    text: PATHWAY
    description: Digital twin of biological pathways
  DISEASE:
    text: DISEASE
    description: Digital twin of disease progression

```
</details>