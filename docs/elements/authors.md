---
search:
  boost: 5.0
---

# Slot: authors 


_connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication._



<div data-search-exclude markdown="1">



URI: [namo:authors](https://w3id.org/monarch-initiative/namo/authors)

## Inheritance

* [node_property](node_property.md)
    * **authors**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Publication](Publication.md) | Any ‘published’ piece of information |  no  |
| [Reference](Reference.md) | A literature reference with identifier and title for citing published work |  no  |
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
| Range | [Agent](Agent.md) |
| Domain | [Publication](Publication.md) |
| Domain Of | [Reference](Reference.md), [Publication](Publication.md) |

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
| self | namo:authors |
| native | namo:authors |




## LinkML Source

<details>
```yaml
name: authors
description: connects an publication to the list of authors who contributed to the
  publication. This property should be a comma-delimited list of author names. It
  is recommended that an author's name be formatted as "surname, firstname initial.".   Note
  that this property is a node annotation expressing the citation list of authorship
  which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation
  defined edges which point to full details about an author and possibly, some qualifiers
  which clarify the specific status of a given author in the publication.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: publication
domain_of:
- Reference
- publication
range: agent
multivalued: true

```
</details></div>