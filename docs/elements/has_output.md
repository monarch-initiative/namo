---
search:
  boost: 5.0
---

# Slot: has_output 


_holds between a process and a continuant, where the continuant is an output of the process_



<div data-search-exclude markdown="1">



URI: [namo:has_output](https://w3id.org/monarch-initiative/namo/has_output)
Alias: has_output


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_participant](has_participant.md)
            * **has_output**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | Either an individual molecular activity, or a collection of causally connecte... |  no  |
| [MolecularActivity](MolecularActivity.md) | An execution of a molecular function carried out by a gene product or macromo... |  yes  |
| [BiologicalProcess](BiologicalProcess.md) | One or more causally connected executions of molecular functions |  no  |
| [Pathway](Pathway.md) | A hierarchical ordering of connected molecular reactions (steps) that represe... |  no  |
| [PhysiologicalProcess](PhysiologicalProcess.md) | A biological or chemical function within a living organism |  no  |
| [Behavior](Behavior.md) | The internally coordinated responses (actions or inactions) of organisms (ind... |  no  |
| [PathologicalProcess](PathologicalProcess.md) | A biologic function or a process having an abnormal or deleterious effect at ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) |
| Domain Of | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| opposite_of | has input |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_output |
| native | namo:has_output |
| exact | RO:0002234 |
| narrow | NCIT:R31, OBI:0000299, PathWhiz:has_right_element, RO:0002296, RO:0002297, RO:0002298, RO:0002299, RO:0002588, RO:0004008 |




## LinkML Source

<details>
```yaml
name: has output
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: has input
description: holds between a process and a continuant, where the continuant is an
  output of the process
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002234
narrow_mappings:
- NCIT:R31
- OBI:0000299
- PathWhiz:has_right_element
- RO:0002296
- RO:0002297
- RO:0002298
- RO:0002299
- RO:0002588
- RO:0004008
rank: 1000
is_a: has participant
domain: biological process or activity
inherited: true
alias: has_output
domain_of:
- biological process or activity
range: named thing
multivalued: true

```
</details></div>