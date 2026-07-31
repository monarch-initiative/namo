---
search:
  boost: 5.0
---

# Slot: transcribed_to 


_inverse of transcribed from_



<div data-search-exclude markdown="1">



URI: [namo:transcribed_to](https://w3id.org/monarch-initiative/namo/transcribed_to)
Alias: transcribed_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **transcribed_to**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Transcript](Transcript.md) |
| Domain | [Gene](Gene.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [transcribed_from](transcribed_from.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:transcribed_to |
| native | namo:transcribed_to |
| exact | RO:0002511, SIO:010080 |




## LinkML Source

<details>
```yaml
name: transcribed to
description: inverse of transcribed from
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002511
- SIO:010080
rank: 1000
is_a: related to at instance level
domain: gene
inherited: true
alias: transcribed_to
inverse: transcribed from
range: transcript
multivalued: true

```
</details></div>