---
search:
  boost: 5.0
---

# Slot: translation_of 


_inverse of translates to_



<div data-search-exclude markdown="1">



URI: [namo:translation_of](https://w3id.org/monarch-initiative/namo/translation_of)
Alias: translation_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **translation_of**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Transcript](Transcript.md) |
| Domain | [Protein](Protein.md) |

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
| Inverse | [translates_to](translates_to.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:translation_of |
| native | namo:translation_of |
| close | RO:0002512, SIO:010083 |




## LinkML Source

<details>
```yaml
name: translation of
description: inverse of translates to
from_schema: https://w3id.org/monarch-initiative/namo
close_mappings:
- RO:0002512
- SIO:010083
rank: 1000
is_a: related to at instance level
domain: protein
inherited: true
alias: translation_of
inverse: translates to
range: transcript
multivalued: true

```
</details></div>