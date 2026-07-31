---
search:
  boost: 5.0
---

# Slot: summary 


_executive  summary of a publication_



<div data-search-exclude markdown="1">



URI: [namo:summary](https://w3id.org/monarch-initiative/namo/summary)

## Inheritance

* [node_property](node_property.md)
    * **summary**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Publication](Publication.md) | Any ‘published’ piece of information |  no  |
| [Book](Book.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
| [BookChapter](BookChapter.md) | A section of a book that forms a discrete unit of a larger published work and... |  no  |
| [Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
| [Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone section o... |  no  |
| [JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published in an... |  no  |
| [Patent](Patent.md) | a legal document granted by a patent issuing authority which confers upon the... |  no  |
| [WebPage](WebPage.md) | a document that is published according to World Wide Web standards, which may... |  no  |
| [PreprintPublication](PreprintPublication.md) | a document reresenting an early version of an author's original scholarly wor... |  no  |
| [DrugLabel](DrugLabel.md) | a document accompanying a drug or its container that provides written, printe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Publication](Publication.md) |
| Domain Of | [Publication](Publication.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* abstract




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:summary |
| native | namo:summary |
| exact | dct:abstract, WIKIDATA:Q333291 |




## LinkML Source

<details>
```yaml
name: summary
description: executive  summary of a publication
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- abstract
exact_mappings:
- dct:abstract
- WIKIDATA:Q333291
rank: 1000
is_a: node property
domain: publication
domain_of:
- publication
range: string

```
</details></div>