

# Slot: sensor_integration 


_Sensors integrated for real-time monitoring_





URI: [namo:sensor_integration](https://w3id.org/monarch-initiative/namo/sensor_integration)
Alias: sensor_integration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TissueOnChip](TissueOnChip.md) | Tissue-level microphysiological systems that model specific tissue functions ... |  no  |
| [OrganOnChip](OrganOnChip.md) | A model system that simulates the physiological functions of an organ using a... |  no  |
| [MicrophysiologicalSystem](MicrophysiologicalSystem.md) | Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials,  an... |  no  |






## Properties

* Range: [IntegratedSensorEnum](IntegratedSensorEnum.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:sensor_integration |
| native | namo:sensor_integration |




## LinkML Source

<details>
```yaml
name: sensor_integration
description: Sensors integrated for real-time monitoring
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: sensor_integration
owner: MicrophysiologicalSystem
domain_of:
- MicrophysiologicalSystem
range: IntegratedSensorEnum
multivalued: true

```
</details>