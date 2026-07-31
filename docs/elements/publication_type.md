---
search:
  boost: 5.0
---

# Slot: publication_type 


_Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass._



<div data-search-exclude markdown="1">



URI: [dct:type](http://purl.org/dc/terms/type)
Alias: publication_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Publication](Publication.md) | Any ‘published’ piece of information |  yes  |
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
| Domain Of | [Publication](Publication.md) |
| Slot URI | [dct:type](http://purl.org/dc/terms/type) |

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
| self | dct:type |
| native | namo:publication_type |




## LinkML Source

<details>
```yaml
name: publication type
description: Ontology term for publication type may be drawn from Dublin Core types
  (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned
  Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html),
  the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation
  of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres
  (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata
  (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication
  type ontology. When a given publication type ontology term is used within a given
  knowledge graph, then the CURIE identified term must be documented in the graph
  as a concept node of biolink:category biolink:OntologyClass.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
values_from:
- dctypes
- fabio
- MESH_PUB
- COAR_RESOURCE
- WIKIDATA
slot_uri: dct:type
alias: publication_type
domain_of:
- publication
range: string
multivalued: true

```
</details></div>