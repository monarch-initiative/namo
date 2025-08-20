# Enum: RatioTypeEnum 



URI: [namo:RatioTypeEnum](https://w3id.org/monarch-initiative/namo/RatioTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| PERCENTAGE | None | Percentage of total cells |
| ABSOLUTE | None | Absolute cell numbers |
| FOLD | None | Fold ratio relative to reference |




## Slots

| Name | Description |
| ---  | --- |
| [ratio_type](ratio_type.md) | Type of ratio specification (percentage, absolute, fold) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: RatioTypeEnum
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  PERCENTAGE:
    text: PERCENTAGE
    description: Percentage of total cells
  ABSOLUTE:
    text: ABSOLUTE
    description: Absolute cell numbers
  FOLD:
    text: FOLD
    description: Fold ratio relative to reference

```
</details>