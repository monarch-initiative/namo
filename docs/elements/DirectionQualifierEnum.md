---
search:
  boost: 2.0
---


# Enum: DirectionQualifierEnum 




_An enumeration of values that qualify a change or effect by its direction, i.e., whether the referenced quantity or activity is increased (including up-regulated) or decreased (including down-regulated)._



<div data-search-exclude markdown="1">

URI: [namo:DirectionQualifierEnum](https://w3id.org/monarch-initiative/namo/DirectionQualifierEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| increased | None |  ||
| upregulated | None |  | Is-A: NONE<br>|
| decreased | None |  ||
| downregulated | None |  | Is-A: NONE<br>|




## Slots

| Name | Description |
| ---  | --- |
| [subject_direction_qualifier](subject_direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [object_direction_qualifier](object_direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [object_direction_qualifier](object_direction_qualifier.md) |  |
| [object_direction_qualifier](object_direction_qualifier.md) |  |
| [subject_direction_qualifier](subject_direction_qualifier.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: DirectionQualifierEnum
description: An enumeration of values that qualify a change or effect by its direction,
  i.e., whether the referenced quantity or activity is increased (including up-regulated)
  or decreased (including down-regulated).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  increased:
    text: increased
  upregulated:
    text: upregulated
    is_a: increased
    exact_mappings:
    - RO:0002213
    close_mappings:
    - RO:0002336
    narrow_mappings:
    - RO:0004032
    - RO:0004034
    - RO:0002629
  decreased:
    text: decreased
  downregulated:
    text: downregulated
    is_a: decreased
    exact_mappings:
    - RO:0004035
    - RO:0002212
    close_mappings:
    - RO:0002335
    broad_mappings:
    - RO:0004033

```
</details>

</div>