---
search:
  boost: 5.0
---

# Slot: iso_abbreviation 


_Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself._



<div data-search-exclude markdown="1">



URI: [namo:iso_abbreviation](https://w3id.org/monarch-initiative/namo/iso_abbreviation)
Alias: iso_abbreviation


## Inheritance

* [node_property](node_property.md)
    * **iso_abbreviation**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
| [Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone section o... |  yes  |
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
| self | namo:iso_abbreviation |
| native | namo:iso_abbreviation |
| exact | WIKIDATA_PROPERTY:P1160 |




## LinkML Source

<details>
```yaml
name: iso abbreviation
description: Standard abbreviation for periodicals in the International Organization
  for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/.
  If the 'published in' property is set, then the iso abbreviation pertains to the
  broader publication context (the journal) within which the given publication node
  is embedded, not the publication itself.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- WIKIDATA_PROPERTY:P1160
rank: 1000
is_a: node property
domain: publication
alias: iso_abbreviation
domain_of:
- serial
- article
range: string

```
</details></div>