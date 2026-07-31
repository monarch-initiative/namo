---
search:
  boost: 2.0
---


# Enum: DrugAvailabilityEnum 




_An enumeration describing how a drug or chemical entity may be obtained, distinguishing products that are available over the counter from those that require a prescription._



<div data-search-exclude markdown="1">

URI: [namo:DrugAvailabilityEnum](https://w3id.org/monarch-initiative/namo/DrugAvailabilityEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| over_the_counter | None | chemical entity is available over the counter without a prescription |
| prescription | None | chemical entity is available by prescription |




## Slots

| Name | Description |
| ---  | --- |
| [available_from](available_from.md) | The regulatory or commercial availability channel through which a drug or che... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: DrugAvailabilityEnum
description: An enumeration describing how a drug or chemical entity may be obtained,
  distinguishing products that are available over the counter from those that require
  a prescription.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  over_the_counter:
    text: over_the_counter
    description: chemical entity is available over the counter without a prescription.
  prescription:
    text: prescription
    description: chemical entity is available by prescription.

```
</details>

</div>