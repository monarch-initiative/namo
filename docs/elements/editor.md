---
search:
  boost: 5.0
---

# Slot: editor 


_editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node)._



<div data-search-exclude markdown="1">



URI: [namo:editor](https://w3id.org/monarch-initiative/namo/editor)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contributor](contributor.md)
            * **editor**








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
| self | namo:editor |
| native | namo:editor |
| exact | WIKIDATA_PROPERTY:P98 |




## LinkML Source

<details>
```yaml
name: editor
description: editor of a compiled work such as a book or a periodical (newspaper or
  an academic journal). Note that in the case of publications which have a containing
  "published in" node property, the editor association may not be attached directly
  to the embedded child publication, but only made in between the parent's publication
  node and the editorial agent of the encompassing publication (e.g. only from the
  Book referenced by the 'published_in' property of a book chapter Publication node).
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- WIKIDATA_PROPERTY:P98
rank: 1000
is_a: contributor
domain: agent
inherited: true
range: publication
multivalued: true

```
</details></div>