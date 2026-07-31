---
search:
  boost: 5.0
---

# Slot: volume 


_volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication_



<div data-search-exclude markdown="1">



URI: [namo:volume](https://w3id.org/monarch-initiative/namo/volume)

## Inheritance

* [node_property](node_property.md)
    * **volume**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BookChapter](BookChapter.md) | A section of a book that forms a discrete unit of a larger published work and... |  no  |
| [Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
| [Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone section o... |  no  |
| [PBPKCompartment](PBPKCompartment.md) | A physiological compartment in a PBPK model |  no  |
| [JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published in an... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Publication](Publication.md) |
| Domain Of | [PBPKCompartment](PBPKCompartment.md), [BookChapter](BookChapter.md), [Serial](Serial.md), [Article](Article.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:volume |
| native | namo:volume |
| exact | WIKIDATA_PROPERTY:P478 |




## LinkML Source

<details>
```yaml
name: volume
description: volume of a book or music release in a collection/series or a published
  collection of journal issues in a serial publication
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- WIKIDATA_PROPERTY:P478
rank: 1000
is_a: node property
domain: publication
domain_of:
- PBPKCompartment
- book chapter
- serial
- article
range: string

```
</details></div>