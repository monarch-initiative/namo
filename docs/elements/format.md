---
search:
  boost: 5.0
---

# Slot: format 


_The file format, physical medium, or representational form of the information content entity; for digital resources typically a MIME type or format identifier. Corresponds to dct:format._



<div data-search-exclude markdown="1">



URI: [namo:format](https://w3id.org/monarch-initiative/namo/format)

## Inheritance

* [node_property](node_property.md)
    * **format**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InformationContentEntity](InformationContentEntity.md) | a piece of information that typically describes some topic of discourse or is... |  no  |
| [NAMDataset](NAMDataset.md) |  |  no  |
| [StudyVariable](StudyVariable.md) | a variable that is used as a measure in the investigation of a study |  no  |
| [CommonDataElement](CommonDataElement.md) | A Common Data Element (CDE) is a standardized, precisely defined question, pa... |  no  |
| [Dataset](Dataset.md) | an item that refers to a collection of data from a data source |  no  |
| [DatasetDistribution](DatasetDistribution.md) | an item that holds distribution level information about a dataset |  no  |
| [DatasetVersion](DatasetVersion.md) | an item that holds version level information about a dataset |  no  |
| [DatasetSummary](DatasetSummary.md) | an item that holds summary level information about a dataset |  no  |
| [ConfidenceLevel](ConfidenceLevel.md) | Level of confidence in a statement |  no  |
| [Evidence](Evidence.md) | Dereferences detailed evidence that supports an association |  no  |
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
| [RetrievalSource](RetrievalSource.md) | Provides information about how a particular InformationResource served as a s... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [InformationContentEntity](InformationContentEntity.md) |
| Domain Of | [InformationContentEntity](InformationContentEntity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:format |
| native | namo:format |
| exact | dct:format, WIKIDATA_PROPERTY:P2701 |




## LinkML Source

<details>
```yaml
name: format
description: The file format, physical medium, or representational form of the information
  content entity; for digital resources typically a MIME type or format identifier.
  Corresponds to dct:format.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- dct:format
- WIKIDATA_PROPERTY:P2701
rank: 1000
is_a: node property
domain: information content entity
domain_of:
- information content entity
range: string

```
</details></div>