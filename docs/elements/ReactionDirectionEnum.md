---
search:
  boost: 2.0
---


# Enum: ReactionDirectionEnum 




_An enumeration of possible directions for a biochemical reaction, indicating whether it proceeds left-to-right, right-to-left, is bidirectional (reversible), or has no net direction._



<div data-search-exclude markdown="1">

URI: [namo:ReactionDirectionEnum](https://w3id.org/monarch-initiative/namo/ReactionDirectionEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| left_to_right | None |  |
| right_to_left | None |  |
| bidirectional | None |  |
| neutral | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [reaction_direction](reaction_direction.md) | the direction of a reaction as constrained by the direction enum (ie: left_to... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: ReactionDirectionEnum
description: An enumeration of possible directions for a biochemical reaction, indicating
  whether it proceeds left-to-right, right-to-left, is bidirectional (reversible),
  or has no net direction.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  left_to_right:
    text: left_to_right
  right_to_left:
    text: right_to_left
  bidirectional:
    text: bidirectional
  neutral:
    text: neutral

```
</details>

</div>