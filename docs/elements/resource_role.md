---
search:
  boost: 5.0
---

# Slot: resource_role 


_The role played by the InformationResource in serving as a source for an Edge. Note that a given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting data' sources._



<div data-search-exclude markdown="1">



URI: [namo:resource_role](https://w3id.org/monarch-initiative/namo/resource_role)
Alias: resource_role


## Inheritance

* [node_property](node_property.md)
    * **resource_role**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RetrievalSource](RetrievalSource.md) | Provides information about how a particular InformationResource served as a s... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ResourceRoleEnum](ResourceRoleEnum.md) |
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
| self | namo:resource_role |
| native | namo:resource_role |




## LinkML Source

<details>
```yaml
name: resource role
description: The role played by the InformationResource in serving as a source for
  an Edge. Note that a given Edge should have one and only one 'primary' source, and
  may have any number of 'aggregator' or 'supporting data' sources.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: retrieval source
alias: resource_role
domain_of:
- retrieval source
range: ResourceRoleEnum

```
</details></div>