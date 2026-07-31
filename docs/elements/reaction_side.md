---
search:
  boost: 5.0
---

# Slot: reaction_side 


_the side of a reaction being modeled (ie: left or right)_



<div data-search-exclude markdown="1">



URI: [namo:reaction_side](https://w3id.org/monarch-initiative/namo/reaction_side)
Alias: reaction_side


## Inheritance

* [association_slot](association_slot.md)
    * **reaction_side**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | An association between a biochemical reaction and a participating molecular e... |  no  |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | A specialization of reaction-to-participant association in which the particip... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReactionSideEnum](ReactionSideEnum.md) |
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
| self | namo:reaction_side |
| native | namo:reaction_side |




## LinkML Source

<details>
```yaml
name: reaction side
description: 'the side of a reaction being modeled (ie: left or right)'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: reaction_side
domain_of:
- reaction to participant association
range: ReactionSideEnum

```
</details></div>