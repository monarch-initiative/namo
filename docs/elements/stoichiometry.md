---
search:
  boost: 5.0
---

# Slot: stoichiometry 


_the relationship between the relative quantities of substances taking part in a reaction or forming a compound, typically a ratio of whole integers._



<div data-search-exclude markdown="1">



URI: [namo:stoichiometry](https://w3id.org/monarch-initiative/namo/stoichiometry)

## Inheritance

* [association_slot](association_slot.md)
    * **stoichiometry**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | An association between a biochemical reaction and a participating molecular e... |  no  |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | A specialization of reaction-to-participant association in which the particip... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain | [Association](Association.md) |
| Domain Of | [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:stoichiometry |
| native | namo:stoichiometry |




## LinkML Source

<details>
```yaml
name: stoichiometry
description: the relationship between the relative quantities of substances taking
  part in a reaction or forming a compound, typically a ratio of whole integers.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
domain_of:
- reaction to participant association
range: integer

```
</details></div>