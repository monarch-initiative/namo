---
search:
  boost: 5.0
---

# Slot: url 


_This slot holds a string representation of a URL for an external resource about the node it is present on. Unlike an 'xref' that is primarily represented by a CURIE, this slot is intended to hold a full URL that can be used to directly access a resource. When linking to an external resource that cannot be represented by a unique CURIE, this slot should be used.  However, when the intent is to link to the default URI expansion of a CURIE related to the node it is present on, the xref slot should be used instead._



<div data-search-exclude markdown="1">



URI: [namo:url](https://w3id.org/monarch-initiative/namo/url)

## Inheritance

* [node_property](node_property.md)
    * **url**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Reference](Reference.md) | A literature reference with identifier and title for citing published work |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Entity](Entity.md) |
| Domain Of | [Reference](Reference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:url |
| native | namo:url |




## LinkML Source

<details>
```yaml
name: url
description: This slot holds a string representation of a URL for an external resource
  about the node it is present on. Unlike an 'xref' that is primarily represented
  by a CURIE, this slot is intended to hold a full URL that can be used to directly
  access a resource. When linking to an external resource that cannot be represented
  by a unique CURIE, this slot should be used.  However, when the intent is to link
  to the default URI expansion of a CURIE related to the node it is present on, the
  xref slot should be used instead.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: entity
domain_of:
- Reference
range: string

```
</details></div>