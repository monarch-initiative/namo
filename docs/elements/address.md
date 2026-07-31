---
search:
  boost: 5.0
---

# Slot: address 


_the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?)._



<div data-search-exclude markdown="1">



URI: [namo:address](https://w3id.org/monarch-initiative/namo/address)

## Inheritance

* [node_property](node_property.md)
    * **address**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Agent](Agent.md) | person, group, organization or project that provides a piece of information (... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [Agent](Agent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:address |
| native | namo:address |




## LinkML Source

<details>
```yaml
name: address
description: the particulars of the place where someone or an organization is situated.  For
  now, this slot is a simple text "blob" containing all relevant details of the given
  location for fitness of purpose. For the moment, this "address" can include other
  contact details such as email and phone number(?).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: named thing
domain_of:
- agent
range: string

```
</details></div>