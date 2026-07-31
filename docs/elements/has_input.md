---
search:
  boost: 5.0
---

# Slot: has_input 


_holds between a process and a continuant, where the continuant is an input into the process_



<div data-search-exclude markdown="1">



URI: [namo:has_input](https://w3id.org/monarch-initiative/namo/has_input)
Alias: has_input


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_participant](has_participant.md)
            * **has_input**
                * [consumes](consumes.md)






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
| opposite_of | has output |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_input |
| native | namo:has_input |
| exact | RO:0002233, SEMMEDDB:USES |
| narrow | LOINC:has_fragments_for_synonyms, LOINC:has_system, PathWhiz:has_left_element, RO:0002590, RO:0004009, SNOMED:has_finding_method, SNOMED:has_precondition, SNOMED:has_specimen_source_identity, SNOMED:has_specimen_substance, SNOMED:uses_access_device, SNOMED:uses_device, SNOMED:uses_energy, SNOMED:uses_substance |




## LinkML Source

<details>
```yaml
name: has input
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: has output
description: holds between a process and a continuant, where the continuant is an
  input into the process
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002233
- SEMMEDDB:USES
narrow_mappings:
- LOINC:has_fragments_for_synonyms
- LOINC:has_system
- PathWhiz:has_left_element
- RO:0002590
- RO:0004009
- SNOMED:has_finding_method
- SNOMED:has_precondition
- SNOMED:has_specimen_source_identity
- SNOMED:has_specimen_substance
- SNOMED:uses_access_device
- SNOMED:uses_device
- SNOMED:uses_energy
- SNOMED:uses_substance
rank: 1000
is_a: has participant
domain: biological process or activity
inherited: true
alias: has_input
domain_of:
- biological process or activity
range: named thing
multivalued: true

```
</details></div>