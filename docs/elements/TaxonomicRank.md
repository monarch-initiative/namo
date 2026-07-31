---
search:
  boost: 10.0
---

# Class: TaxonomicRank 


_A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)_



<div data-search-exclude markdown="1">



URI: [namo:TaxonomicRank](https://w3id.org/monarch-initiative/namo/TaxonomicRank)





```mermaid
 classDiagram
    class TaxonomicRank
    click TaxonomicRank href "../TaxonomicRank/"
      OntologyClass <|-- TaxonomicRank
        click OntologyClass href "../OntologyClass/"
      
      TaxonomicRank : id
        
      TaxonomicRank : subsets
        
      
```





## Inheritance
* [OntologyClass](OntologyClass.md)
    * **TaxonomicRank**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity | [OntologyClass](OntologyClass.md) |
| [subsets](subsets.md) | * <br/> [String](String.md) | The set of ontology subsets a term belongs to (e | [OntologyClass](OntologyClass.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OrganismTaxon](OrganismTaxon.md) | [has_taxonomic_rank](has_taxonomic_rank.md) | range | [TaxonomicRank](TaxonomicRank.md) |












## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* TAXRANK







### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:TaxonomicRank |
| native | namo:TaxonomicRank |
| undefined | WIKIDATA:Q427626 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: taxonomic rank
id_prefixes:
- TAXRANK
description: 'A descriptor for the rank within a taxonomic classification. Example
  instance: TAXRANK:0000017 (kingdom)'
from_schema: https://w3id.org/monarch-initiative/namo
mappings:
- WIKIDATA:Q427626
is_a: ontology class

```
</details>

### Induced

<details>
```yaml
name: taxonomic rank
id_prefixes:
- TAXRANK
description: 'A descriptor for the rank within a taxonomic classification. Example
  instance: TAXRANK:0000017 (kingdom)'
from_schema: https://w3id.org/monarch-initiative/namo
mappings:
- WIKIDATA:Q427626
is_a: ontology class
attributes:
  id:
    name: id
    description: A unique identifier for an entity. Must be either a CURIE shorthand
      for a URI or a complete URI
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - AGRKB:primaryId
    - gff3:ID
    - gpi:DB_Object_ID
    rank: 1000
    domain: entity
    identifier: true
    owner: taxonomic rank
    domain_of:
    - Reference
    - ontology class
    - entity
    range: string
    required: true
  subsets:
    name: subsets
    description: The set of ontology subsets a term belongs to (e.g. GO slim subsets,
      MONDO rare disease subset). Carries the values of `oboInOwl:inSubset` annotations
      from source ontologies through to downstream knowledge graphs.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - oboInOwl:inSubset
    rank: 1000
    is_a: node property
    domain: named thing
    owner: taxonomic rank
    domain_of:
    - ontology class
    range: string
    multivalued: true

```
</details></div>