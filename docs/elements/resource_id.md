---
search:
  boost: 5.0
---

# Slot: resource_id 


_The CURIE for an Information Resource that served as a source of knowledge expressed in an Edge, or a source of data used to generate this knowledge._



<div data-search-exclude markdown="1">



URI: [namo:resource_id](https://w3id.org/monarch-initiative/namo/resource_id)
Alias: resource_id


## Inheritance

* [node_property](node_property.md)
    * **resource_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RetrievalSource](RetrievalSource.md) | Provides information about how a particular InformationResource served as a s... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain | [RetrievalSource](RetrievalSource.md) |
| Domain Of | [RetrievalSource](RetrievalSource.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:resource_id |
| native | namo:resource_id |




## LinkML Source

<details>
```yaml
name: resource id
description: The CURIE for an Information Resource that served as a source of knowledge
  expressed in an Edge, or a source of data used to generate this knowledge.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: retrieval source
alias: resource_id
domain_of:
- retrieval source
range: uriorcurie

```
</details></div>