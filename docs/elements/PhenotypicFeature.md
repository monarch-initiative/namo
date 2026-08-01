---
search:
  boost: 10.0
---

# Class: PhenotypicFeature 


_A combination of entity and quality that makes up a phenotyping statement._



<div data-search-exclude markdown="1">



URI: [biolink:PhenotypicFeature](https://w3id.org/biolink/PhenotypicFeature)





```mermaid
 classDiagram
    class PhenotypicFeature
    click PhenotypicFeature href "../PhenotypicFeature/"
      BiolinkEntity <|-- PhenotypicFeature
        click BiolinkEntity href "../BiolinkEntity/"
      
      PhenotypicFeature : description
        
      PhenotypicFeature : id
        
      PhenotypicFeature : name
        
      
```





## Inheritance
* [BiolinkEntity](BiolinkEntity.md)
    * **PhenotypicFeature**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [biolink:PhenotypicFeature](https://w3id.org/biolink/PhenotypicFeature) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [BiolinkEntity](BiolinkEntity.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [BiolinkEntity](BiolinkEntity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [BiolinkEntity](BiolinkEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PhenotypeOverlap](PhenotypeOverlap.md) | [shared_phenotypes](shared_phenotypes.md) | range | [PhenotypicFeature](PhenotypicFeature.md) |
| [PhenotypeOverlap](PhenotypeOverlap.md) | [model_specific_phenotypes](model_specific_phenotypes.md) | range | [PhenotypicFeature](PhenotypicFeature.md) |
| [PhenotypeOverlap](PhenotypeOverlap.md) | [biological_specific_phenotypes](biological_specific_phenotypes.md) | range | [PhenotypicFeature](PhenotypicFeature.md) |












## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HP

* MP

* UPHENO







### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biolink:PhenotypicFeature |
| native | namo:PhenotypicFeature |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhenotypicFeature
id_prefixes:
- HP
- MP
- UPHENO
description: A combination of entity and quality that makes up a phenotyping statement.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: BiolinkEntity
class_uri: biolink:PhenotypicFeature

```
</details>

### Induced

<details>
```yaml
name: PhenotypicFeature
id_prefixes:
- HP
- MP
- UPHENO
description: A combination of entity and quality that makes up a phenotyping statement.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: BiolinkEntity
attributes:
  id:
    name: id
    description: A unique identifier for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    owner: PhenotypicFeature
    domain_of:
    - NamedThing
    - Reference
    - BiolinkEntity
    range: uriorcurie
    required: true
  name:
    name: name
    description: A human-readable name for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:name
    owner: PhenotypicFeature
    domain_of:
    - NamedThing
    - BiolinkEntity
    range: string
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:description
    owner: PhenotypicFeature
    domain_of:
    - NamedThing
    - BiolinkEntity
    range: string
class_uri: biolink:PhenotypicFeature

```
</details></div>