---
search:
  boost: 5.0
---

# Slot: enabled_by 


_holds between a process and a physical entity, where the physical entity executes the process_



<div data-search-exclude markdown="1">



URI: [namo:enabled_by](https://w3id.org/monarch-initiative/namo/enabled_by)
Alias: enabled_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_participant](has_participant.md)
            * **enabled_by**






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
| Range | [PhysicalEntity](PhysicalEntity.md) |
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


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [enables](enables.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| opposite_of | prevented by |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:enabled_by |
| native | namo:enabled_by |
| exact | RO:0002333 |




## LinkML Source

<details>
```yaml
name: enabled by
annotations:
  opposite_of:
    tag: opposite_of
    value: prevented by
description: holds between a process and a physical entity, where the physical entity
  executes the process
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002333
rank: 1000
is_a: has participant
domain: biological process or activity
inherited: true
alias: enabled_by
domain_of:
- biological process or activity
inverse: enables
range: physical entity
multivalued: true

```
</details></div>