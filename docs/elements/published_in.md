---
search:
  boost: 5.0
---

# Slot: published_in 


_CURIE identifier of a broader publication context within which the publication may be placed._



<div data-search-exclude markdown="1">



URI: [namo:published_in](https://w3id.org/monarch-initiative/namo/published_in)
Alias: published_in


## Inheritance

* [node_property](node_property.md)
    * **published_in**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BookChapter](BookChapter.md) | A section of a book that forms a discrete unit of a larger published work and... |  yes  |
| [Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone section o... |  yes  |
| [JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published in an... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain | [Publication](Publication.md) |
| Domain Of | [BookChapter](BookChapter.md), [Article](Article.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:published_in |
| native | namo:published_in |
| exact | WIKIDATA_PROPERTY:P1433 |




## LinkML Source

<details>
```yaml
name: published in
description: CURIE identifier of a broader publication context within which the publication
  may be placed.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- WIKIDATA_PROPERTY:P1433
rank: 1000
is_a: node property
values_from:
- NLMID
- issn
- isbn
domain: publication
alias: published_in
domain_of:
- book chapter
- article
range: uriorcurie

```
</details></div>