---
search:
  boost: 5.0
---

# Slot: issue 


_issue of a newspaper, a scientific journal or magazine for reference purpose_



<div data-search-exclude markdown="1">



URI: [namo:issue](https://w3id.org/monarch-initiative/namo/issue)

## Inheritance

* [node_property](node_property.md)
    * **issue**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
| [Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone section o... |  no  |
| [JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published in an... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Publication](Publication.md) |
| Domain Of | [Serial](Serial.md), [Article](Article.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:issue |
| native | namo:issue |
| exact | WIKIDATA_PROPERTY:P433 |




## LinkML Source

<details>
```yaml
name: issue
description: issue of a newspaper, a scientific journal or magazine for reference
  purpose
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- WIKIDATA_PROPERTY:P433
rank: 1000
is_a: node property
domain: publication
domain_of:
- serial
- article
range: string

```
</details></div>