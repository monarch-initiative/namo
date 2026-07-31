---
search:
  boost: 5.0
---

# Slot: author 


_an instance of one (co-)creator primarily responsible for a written work_



<div data-search-exclude markdown="1">



URI: [namo:author](https://w3id.org/monarch-initiative/namo/author)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contributor](contributor.md)
            * **author**








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
| self | namo:author |
| native | namo:author |
| exact | dct:creator, WIKIDATA_PROPERTY:P50 |




## LinkML Source

<details>
```yaml
name: author
description: an instance of one (co-)creator primarily responsible for a written work
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- dct:creator
- WIKIDATA_PROPERTY:P50
rank: 1000
is_a: contributor
domain: agent
inherited: true
range: publication
multivalued: true

```
</details></div>