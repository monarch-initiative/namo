---
search:
  boost: 10.0
---

# Class: GrossAnatomicalStructure 


_An anatomical structure that has more than one cell as a part._



<div data-search-exclude markdown="1">



URI: [biolink:GrossAnatomicalStructure](https://w3id.org/biolink/GrossAnatomicalStructure)





```mermaid
 classDiagram
    class GrossAnatomicalStructure
    click GrossAnatomicalStructure href "../GrossAnatomicalStructure/"
      BiolinkEntity <|-- GrossAnatomicalStructure
        click BiolinkEntity href "../BiolinkEntity/"
      
      GrossAnatomicalStructure : description
        
      GrossAnatomicalStructure : id
        
      GrossAnatomicalStructure : name
        
      
```





## Inheritance
* [BiolinkEntity](BiolinkEntity.md)
    * **GrossAnatomicalStructure**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [biolink:GrossAnatomicalStructure](https://w3id.org/biolink/GrossAnatomicalStructure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [BiolinkEntity](BiolinkEntity.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [BiolinkEntity](BiolinkEntity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [BiolinkEntity](BiolinkEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Organoid](Organoid.md) | [organ_modeled](organ_modeled.md) | range | [GrossAnatomicalStructure](GrossAnatomicalStructure.md) |
| [OrganOnChip](OrganOnChip.md) | [organ_modeled](organ_modeled.md) | range | [GrossAnatomicalStructure](GrossAnatomicalStructure.md) |
| [TissueOnChip](TissueOnChip.md) | [anatomical_structure_modeled](anatomical_structure_modeled.md) | range | [GrossAnatomicalStructure](GrossAnatomicalStructure.md) |












## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* UBERON

* NCIT

* MESH







### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biolink:GrossAnatomicalStructure |
| native | namo:GrossAnatomicalStructure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GrossAnatomicalStructure
id_prefixes:
- UBERON
- NCIT
- MESH
description: An anatomical structure that has more than one cell as a part.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: BiolinkEntity
class_uri: biolink:GrossAnatomicalStructure

```
</details>

### Induced

<details>
```yaml
name: GrossAnatomicalStructure
id_prefixes:
- UBERON
- NCIT
- MESH
description: An anatomical structure that has more than one cell as a part.
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
    owner: GrossAnatomicalStructure
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
    owner: GrossAnatomicalStructure
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
    owner: GrossAnatomicalStructure
    domain_of:
    - NamedThing
    - BiolinkEntity
    range: string
class_uri: biolink:GrossAnatomicalStructure

```
</details></div>