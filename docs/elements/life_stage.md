---
search:
  boost: 5.0
---

# Slot: life_stage 


_The developmental or life-cycle stage of the animal used in the model system._



<div data-search-exclude markdown="1">



URI: [namo:life_stage](https://w3id.org/monarch-initiative/namo/life_stage)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnimalModel](AnimalModel.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LifeStage](LifeStage.md) |
| Domain Of | [AnimalModel](AnimalModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnimalModel](AnimalModel.md) |


<details>
<summary>Advanced Properties</summary>
**Term Bindings:**
- EnumBinding({
  'range': 'LifeStageEnum',
  'obligation_level': ObligationLevelEnum(text='REQUIRED', description='The metadata element is required to be present in the model'),
  'binds_value_of': 'id'
})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:life_stage |
| native | namo:life_stage |




## LinkML Source

<details>
```yaml
name: life_stage
description: The developmental or life-cycle stage of the animal used in the model
  system.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: AnimalModel
domain_of:
- AnimalModel
range: LifeStage
bindings:
- range: LifeStageEnum
  obligation_level: REQUIRED
  binds_value_of: id
inlined: true

```
</details></div>