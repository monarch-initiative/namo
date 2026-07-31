---
search:
  boost: 2.0
---


# Enum: StrandEnum 




_strand_



<div data-search-exclude markdown="1">

URI: [namo:StrandEnum](https://w3id.org/monarch-initiative/namo/StrandEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| + | None | Positive |
| - | None | Negative |
| . | None | Unstranded |
| ? | None | Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [genome_build](genome_build.md) | The version of the genome on which a feature is located |
| [strand](strand.md) | The strand on which a feature is located |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: StrandEnum
description: strand
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  +:
    text: +
    description: Positive
  '-':
    text: '-'
    description: Negative
  .:
    text: .
    description: Unstranded
  '?':
    text: '?'
    description: Unknown

```
</details>

</div>