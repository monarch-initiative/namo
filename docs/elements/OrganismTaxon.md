---
search:
  boost: 10.0
---

# Class: OrganismTaxon 


_A classification of a set of organisms. Can also be used to represent strains or subspecies._



<div data-search-exclude markdown="1">



URI: [biolink:OrganismTaxon](https://w3id.org/biolink/OrganismTaxon)





```mermaid
 classDiagram
    class OrganismTaxon
    click OrganismTaxon href "../OrganismTaxon/"
      BiolinkEntity <|-- OrganismTaxon
        click BiolinkEntity href "../BiolinkEntity/"
      
      OrganismTaxon : description
        
      OrganismTaxon : id
        
      OrganismTaxon : name
        
      
```





## Inheritance
* [BiolinkEntity](BiolinkEntity.md)
    * **OrganismTaxon**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [biolink:OrganismTaxon](https://w3id.org/biolink/OrganismTaxon) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [BiolinkEntity](BiolinkEntity.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [BiolinkEntity](BiolinkEntity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [BiolinkEntity](BiolinkEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnimalModel](AnimalModel.md) | [species](species.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [AnimalModel](AnimalModel.md) | [strain](strain.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [PBPKModel](PBPKModel.md) | [species_modeled](species_modeled.md) | range | [OrganismTaxon](OrganismTaxon.md) |












## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* NCBITaxon

* MESH







### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biolink:OrganismTaxon |
| native | namo:OrganismTaxon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OrganismTaxon
id_prefixes:
- NCBITaxon
- MESH
description: A classification of a set of organisms. Can also be used to represent
  strains or subspecies.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: BiolinkEntity
class_uri: biolink:OrganismTaxon

```
</details>

### Induced

<details>
```yaml
name: OrganismTaxon
id_prefixes:
- NCBITaxon
- MESH
description: A classification of a set of organisms. Can also be used to represent
  strains or subspecies.
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
    owner: OrganismTaxon
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
    owner: OrganismTaxon
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
    owner: OrganismTaxon
    domain_of:
    - NamedThing
    - BiolinkEntity
    range: string
class_uri: biolink:OrganismTaxon

```
</details></div>