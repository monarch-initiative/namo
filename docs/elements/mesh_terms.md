---
search:
  boost: 5.0
---

# Slot: mesh_terms 


_mesh terms tagging a publication_



<div data-search-exclude markdown="1">



URI: [namo:mesh_terms](https://w3id.org/monarch-initiative/namo/mesh_terms)
Alias: mesh_terms


## Inheritance

* [node_property](node_property.md)
    * **mesh_terms**






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
| Range | [Uriorcurie](Uriorcurie.md) |
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
| self | namo:mesh_terms |
| native | namo:mesh_terms |
| exact | dcid:MeSHTerm |




## LinkML Source

<details>
```yaml
name: mesh terms
description: mesh terms tagging a publication
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- dcid:MeSHTerm
rank: 1000
is_a: node property
values_from:
- MESH
domain: publication
alias: mesh_terms
domain_of:
- publication
range: uriorcurie
multivalued: true

```
</details></div>