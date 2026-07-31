---
search:
  boost: 5.0
---

# Slot: affiliation 


_a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations._



<div data-search-exclude markdown="1">



URI: [namo:affiliation](https://w3id.org/monarch-initiative/namo/affiliation)

## Inheritance

* [node_property](node_property.md)
    * **affiliation**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Agent](Agent.md) | person, group, organization or project that provides a piece of information (... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain | [Agent](Agent.md) |
| Domain Of | [Agent](Agent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:affiliation |
| native | namo:affiliation |




## LinkML Source

<details>
```yaml
name: affiliation
description: a professional relationship between one provider (often a person) within
  another provider (often an organization). Target provider identity should be specified
  by a CURIE. Providers may have multiple affiliations.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: agent
domain_of:
- agent
range: uriorcurie
multivalued: true

```
</details></div>