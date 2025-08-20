# Enum: CocultureConfigurationEnum 



URI: [namo:CocultureConfigurationEnum](https://w3id.org/monarch-initiative/namo/CocultureConfigurationEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| DIRECT_CONTACT | None | Cells in direct physical contact |
| TRANSWELL | None | Cells separated by permeable membrane |
| CONDITIONED_MEDIA | None | Cells exposed to media conditioned by other cells |
| MICROPATTERN | None | Cells patterned in defined spatial arrangements |
| GRADIENT | None | Cells exposed to chemical or physical gradients |




## Slots

| Name | Description |
| ---  | --- |
| [coculture_configuration](coculture_configuration.md) | Configuration of co-culture (direct contact, transwell, conditioned media) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: CocultureConfigurationEnum
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  DIRECT_CONTACT:
    text: DIRECT_CONTACT
    description: Cells in direct physical contact
  TRANSWELL:
    text: TRANSWELL
    description: Cells separated by permeable membrane
  CONDITIONED_MEDIA:
    text: CONDITIONED_MEDIA
    description: Cells exposed to media conditioned by other cells
  MICROPATTERN:
    text: MICROPATTERN
    description: Cells patterned in defined spatial arrangements
  GRADIENT:
    text: GRADIENT
    description: Cells exposed to chemical or physical gradients

```
</details>