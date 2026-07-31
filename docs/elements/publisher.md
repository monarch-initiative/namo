---
search:
  boost: 5.0
---

# Slot: publisher 


_organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node)._



<div data-search-exclude markdown="1">



URI: [namo:publisher](https://w3id.org/monarch-initiative/namo/publisher)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contributor](contributor.md)
            * **publisher**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Publication](Publication.md) |
| Domain | [Agent](Agent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:publisher |
| native | namo:publisher |
| exact | dct:publisher, WIKIDATA_PROPERTY:P123 |




## LinkML Source

<details>
```yaml
name: publisher
description: organization or person responsible for publishing books, periodicals,
  podcasts, games or software. Note that in the case of publications which have a
  containing "published in" node property, the publisher association may not be attached
  directly to the embedded child publication, but only made in between the parent's
  publication node and the publisher agent of the encompassing publication (e.g. only
  from the Journal referenced by the 'published_in' property of an journal article
  Publication node).
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- dct:publisher
- WIKIDATA_PROPERTY:P123
rank: 1000
is_a: contributor
domain: agent
inherited: true
range: publication
multivalued: true

```
</details></div>