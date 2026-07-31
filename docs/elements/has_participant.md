---
search:
  boost: 5.0
---

# Slot: has_participant 


_holds between a process and a continuant, where the continuant is somehow involved in the process_



<div data-search-exclude markdown="1">



URI: [namo:has_participant](https://w3id.org/monarch-initiative/namo/has_participant)
Alias: has_participant


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_participant**
            * [has_input](has_input.md)
            * [has_output](has_output.md)
            * [has_catalyst](has_catalyst.md)
            * [has_substrate](has_substrate.md)
            * [actively_involves](actively_involves.md)
            * [enabled_by](enabled_by.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Occurrent](Occurrent.md) |
| Domain | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) |

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




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_participant |
| native | namo:has_participant |
| exact | RO:0000057, RO:has_participant |
| narrow | BFO:0000167, LOINC:has_subject, NCIT:process_involves_gene, NBO-PROPERTY:has_participant, PathWhiz:has_bound, PathWhiz:has_compound, PathWhiz:has_element_collection, PathWhiz:has_enzyme, OBI:0000293, PathWhiz:has_nucleic_acid, PathWhiz:has_protein, PathWhiz:has_reaction, RO:0002565, RO:0004007, RO:0004020, RO:0004021, SNOMED:has_indirect_device, SNOMED:has_procedure_device, SNOMED:has_recipient_category |
| close | WIKIDATA_PROPERTY:P2283 |




## LinkML Source

<details>
```yaml
name: has participant
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a process and a continuant, where the continuant is somehow
  involved in the process
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0000057
- RO:has_participant
close_mappings:
- WIKIDATA_PROPERTY:P2283
narrow_mappings:
- BFO:0000167
- LOINC:has_subject
- NCIT:process_involves_gene
- NBO-PROPERTY:has_participant
- PathWhiz:has_bound
- PathWhiz:has_compound
- PathWhiz:has_element_collection
- PathWhiz:has_enzyme
- OBI:0000293
- PathWhiz:has_nucleic_acid
- PathWhiz:has_protein
- PathWhiz:has_reaction
- RO:0002565
- RO:0004007
- RO:0004020
- RO:0004021
- SNOMED:has_indirect_device
- SNOMED:has_procedure_device
- SNOMED:has_recipient_category
rank: 1000
is_a: related to at instance level
domain: biological process or activity
inherited: true
alias: has_participant
range: occurrent
multivalued: true

```
</details></div>