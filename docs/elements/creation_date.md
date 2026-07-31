---
search:
  boost: 5.0
---

# Slot: creation_date 


_date on which an entity was created. This can be applied to nodes or edges_



<div data-search-exclude markdown="1">



URI: [namo:creation_date](https://w3id.org/monarch-initiative/namo/creation_date)
Alias: creation_date


## Inheritance

* [node_property](node_property.md)
    * **creation_date**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InformationContentEntity](InformationContentEntity.md) | a piece of information that typically describes some topic of discourse or is... |  no  |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial is a research study that prospectively assigns human partici... |  no  |
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
| Range | [Date](Date.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [InformationContentEntity](InformationContentEntity.md), [ClinicalTrial](ClinicalTrial.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* publication date
* date started




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:creation_date |
| native | namo:creation_date |
| exact | dct:createdOn, WIKIDATA_PROPERTY:P577 |




## LinkML Source

<details>
```yaml
name: creation date
description: date on which an entity was created. This can be applied to nodes or
  edges
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- publication date
- date started
exact_mappings:
- dct:createdOn
- WIKIDATA_PROPERTY:P577
rank: 1000
is_a: node property
domain: named thing
alias: creation_date
domain_of:
- information content entity
- clinical trial
range: date

```
</details></div>