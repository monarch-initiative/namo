---
search:
  boost: 5.0
---

# Slot: symbol 


_Symbol for a particular thing_



<div data-search-exclude markdown="1">



URI: [namo:symbol](https://w3id.org/monarch-initiative/namo/symbol)

## Inheritance

* [node_property](node_property.md)
    * **symbol**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [Gene](Gene.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:symbol |
| native | namo:symbol |
| exact | AGRKB:symbol, gpi:DB_Object_Symbol |




## LinkML Source

<details>
```yaml
name: symbol
description: Symbol for a particular thing
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- AGRKB:symbol
- gpi:DB_Object_Symbol
rank: 1000
is_a: node property
domain: named thing
domain_of:
- gene
range: string

```
</details></div>