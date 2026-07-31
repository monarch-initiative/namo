---
search:
  boost: 5.0
---

# Slot: upstream_resource_ids 


_An upstream InformationResource from which the resource being described directly retrieved a record of the knowledge expressed in the Edge, or data used to generate this knowledge. This is an array because there are cases where a merged Edge holds knowledge that was retrieved from multiple sources._



<div data-search-exclude markdown="1">



URI: [namo:upstream_resource_ids](https://w3id.org/monarch-initiative/namo/upstream_resource_ids)
Alias: upstream_resource_ids


## Inheritance

* [node_property](node_property.md)
    * **upstream_resource_ids**






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
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:upstream_resource_ids |
| native | namo:upstream_resource_ids |




## LinkML Source

<details>
```yaml
name: upstream resource ids
description: An upstream InformationResource from which the resource being described
  directly retrieved a record of the knowledge expressed in the Edge, or data used
  to generate this knowledge. This is an array because there are cases where a merged
  Edge holds knowledge that was retrieved from multiple sources.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: retrieval source
alias: upstream_resource_ids
domain_of:
- retrieval source
range: uriorcurie
multivalued: true

```
</details></div>