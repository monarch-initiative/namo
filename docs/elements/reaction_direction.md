---
search:
  boost: 5.0
---

# Slot: reaction_direction 


_the direction of a reaction as constrained by the direction enum (ie: left_to_right, neutral, etc.)_



<div data-search-exclude markdown="1">



URI: [namo:reaction_direction](https://w3id.org/monarch-initiative/namo/reaction_direction)
Alias: reaction_direction


## Inheritance

* [association_slot](association_slot.md)
    * **reaction_direction**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | An association between a biochemical reaction and a participating molecular e... |  no  |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | A specialization of reaction-to-participant association in which the particip... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReactionDirectionEnum](ReactionDirectionEnum.md) |
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
| self | namo:reaction_direction |
| native | namo:reaction_direction |
| narrow | NCIT:C42677 |




## LinkML Source

<details>
```yaml
name: reaction direction
description: 'the direction of a reaction as constrained by the direction enum (ie:
  left_to_right, neutral, etc.)'
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- NCIT:C42677
rank: 1000
is_a: association slot
domain: association
alias: reaction_direction
domain_of:
- reaction to participant association
range: ReactionDirectionEnum

```
</details></div>