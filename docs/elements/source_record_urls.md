---
search:
  boost: 5.0
---

# Slot: source_record_urls 


_A URL linking to a specific web page or document provided by the source, that contains a record of the knowledge expressed in the Edge. If the knowledge is contained in more than one web page on an Information Resource's site, urls MAY be provided for each._



<div data-search-exclude markdown="1">



URI: [namo:source_record_urls](https://w3id.org/monarch-initiative/namo/source_record_urls)
Alias: source_record_urls


## Inheritance

* [node_property](node_property.md)
    * **source_record_urls**






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
| self | namo:source_record_urls |
| native | namo:source_record_urls |




## LinkML Source

<details>
```yaml
name: source record urls
description: A URL linking to a specific web page or document provided by the source,
  that contains a record of the knowledge expressed in the Edge. If the knowledge
  is contained in more than one web page on an Information Resource's site, urls MAY
  be provided for each.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: retrieval source
alias: source_record_urls
domain_of:
- retrieval source
range: uriorcurie
multivalued: true

```
</details></div>