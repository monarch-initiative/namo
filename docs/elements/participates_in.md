---
search:
  boost: 5.0
---

# Slot: participates_in 


_holds between a continuant and a process, where the continuant is somehow involved in the process_



<div data-search-exclude markdown="1">



URI: [namo:participates_in](https://w3id.org/monarch-initiative/namo/participates_in)
Alias: participates_in


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **participates_in**
            * [is_input_of](is_input_of.md)
            * [is_output_of](is_output_of.md)
            * [catalyzes](catalyzes.md)
            * [is_substrate_of](is_substrate_of.md)
            * [actively_involved_in](actively_involved_in.md)
            * [enables](enables.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) |
| Domain | [Occurrent](Occurrent.md) |

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
| Inverse | [has_participant](has_participant.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:participates_in |
| native | namo:participates_in |
| exact | RO:0000056, BFO:0000056 |
| narrow | DRUGBANK:pathway, HMDB:in_pathway, LOINC:is_given_pharmaceutical_substance_for, NCIT:R130, NCIT:R37, NCIT:R131, NCIT:R51, NCIT:R53, OBI:0000295, RO:0002216, RO:0002505, SNOMED:has_direct_device |




## LinkML Source

<details>
```yaml
name: participates in
description: holds between a continuant and a process, where the continuant is somehow
  involved in the process
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0000056
- BFO:0000056
narrow_mappings:
- DRUGBANK:pathway
- HMDB:in_pathway
- LOINC:is_given_pharmaceutical_substance_for
- NCIT:R130
- NCIT:R37
- NCIT:R131
- NCIT:R51
- NCIT:R53
- OBI:0000295
- RO:0002216
- RO:0002505
- SNOMED:has_direct_device
rank: 1000
is_a: related to at instance level
domain: occurrent
inherited: true
alias: participates_in
inverse: has participant
range: biological process or activity
multivalued: true

```
</details></div>