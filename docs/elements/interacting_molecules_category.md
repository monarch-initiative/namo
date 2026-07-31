---
search:
  boost: 5.0
---

# Slot: interacting_molecules_category 

<div data-search-exclude markdown="1">



URI: [namo:interacting_molecules_category](https://w3id.org/monarch-initiative/namo/interacting_molecules_category)
Alias: interacting_molecules_category


## Inheritance

* [association_slot](association_slot.md)
    * **interacting_molecules_category**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OntologyClass](OntologyClass.md) |
| Domain | [Association](Association.md) |
| Domain Of | [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| MI:1048 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:interacting_molecules_category |
| native | namo:interacting_molecules_category |
| exact | MI:1046 |




## LinkML Source

<details>
```yaml
name: interacting molecules category
examples:
- value: MI:1048
  description: smallmolecule-protein
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- MI:1046
rank: 1000
is_a: association slot
values_from:
- MI
domain: association
alias: interacting_molecules_category
domain_of:
- pairwise molecular interaction
range: ontology class

```
</details></div>