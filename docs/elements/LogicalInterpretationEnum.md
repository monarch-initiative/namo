---
search:
  boost: 2.0
---


# Enum: LogicalInterpretationEnum 




_An enumeration of logical interpretations that can be applied to a triple to indicate whether the relation should be read as existential on both sides (some-some), universal-existential (all-some), or its inverse (inverse all-some)._



<div data-search-exclude markdown="1">

URI: [namo:LogicalInterpretationEnum](https://w3id.org/monarch-initiative/namo/LogicalInterpretationEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| some_some | os:SomeSomeInterpretation | A modifier on a triple that causes the triple to be interpreted as a some-som... |
| all_some | os:AllSomeInterpretation | A modifier on a triple that causes the triple to be interpreted as an all-som... |
| inverse_all_some | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [logical_interpretation](logical_interpretation.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: LogicalInterpretationEnum
description: An enumeration of logical interpretations that can be applied to a triple
  to indicate whether the relation should be read as existential on both sides (some-some),
  universal-existential (all-some), or its inverse (inverse all-some).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  some_some:
    text: some_some
    description: A modifier on a triple that causes the triple to be interpreted as
      a some-some statement
    meaning: os:SomeSomeInterpretation
  all_some:
    text: all_some
    description: A modifier on a triple that causes the triple to be interpreted as
      an all-some statement.
    meaning: os:AllSomeInterpretation
  inverse_all_some:
    text: inverse_all_some

```
</details>

</div>