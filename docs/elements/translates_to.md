---
search:
  boost: 5.0
---

# Slot: translates_to 


_x (amino acid chain/polypeptide) is the ribosomal translation of y (transcript) if and only if a ribosome reads y (transcript) through a series of triplet codon-amino acid adaptor activities (GO:0030533) and produces x (amino acid chain/polypeptide)_



<div data-search-exclude markdown="1">



URI: [namo:translates_to](https://w3id.org/monarch-initiative/namo/translates_to)
Alias: translates_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **translates_to**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Protein](Protein.md) |
| Domain | [Transcript](Transcript.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:translates_to |
| native | namo:translates_to |
| close | RO:0002513, SIO:010082 |




## LinkML Source

<details>
```yaml
name: translates to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: x (amino acid chain/polypeptide) is the ribosomal translation of y (transcript)
  if and only if a ribosome reads y (transcript) through a series of triplet codon-amino
  acid adaptor activities (GO:0030533) and produces x (amino acid chain/polypeptide)
from_schema: https://w3id.org/monarch-initiative/namo
close_mappings:
- RO:0002513
- SIO:010082
rank: 1000
is_a: related to at instance level
domain: transcript
inherited: true
alias: translates_to
range: protein
multivalued: true

```
</details></div>