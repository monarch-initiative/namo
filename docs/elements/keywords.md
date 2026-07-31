---
search:
  boost: 5.0
---

# Slot: keywords 


_keywords tagging a publication_



<div data-search-exclude markdown="1">



URI: [namo:keywords](https://w3id.org/monarch-initiative/namo/keywords)

## Inheritance

* [node_property](node_property.md)
    * **keywords**






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
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:keywords |
| native | namo:keywords |




## LinkML Source

<details>
```yaml
name: keywords
description: keywords tagging a publication
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: publication
domain_of:
- publication
range: string
multivalued: true

```
</details></div>