---
search:
  boost: 10.0
---

# Class: EnvironmentalExposure 


_A discrete event type where an organism is exposed to an environmental condition._



<div data-search-exclude markdown="1">



URI: [biolink:EnvironmentalExposure](https://w3id.org/biolink/EnvironmentalExposure)





```mermaid
 classDiagram
    class EnvironmentalExposure
    click EnvironmentalExposure href "../EnvironmentalExposure/"
      BiolinkEntity <|-- EnvironmentalExposure
        click BiolinkEntity href "../BiolinkEntity/"
      
      EnvironmentalExposure : description
        
      EnvironmentalExposure : id
        
      EnvironmentalExposure : name
        
      
```





## Inheritance
* [BiolinkEntity](BiolinkEntity.md)
    * **EnvironmentalExposure**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [biolink:EnvironmentalExposure](https://w3id.org/biolink/EnvironmentalExposure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [BiolinkEntity](BiolinkEntity.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [BiolinkEntity](BiolinkEntity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [BiolinkEntity](BiolinkEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnimalModel](AnimalModel.md) | [environment](environment.md) | range | [EnvironmentalExposure](EnvironmentalExposure.md) |












## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* ECTO

* ENVO







### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biolink:EnvironmentalExposure |
| native | namo:EnvironmentalExposure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnvironmentalExposure
id_prefixes:
- ECTO
- ENVO
description: A discrete event type where an organism is exposed to an environmental
  condition.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: BiolinkEntity
class_uri: biolink:EnvironmentalExposure

```
</details>

### Induced

<details>
```yaml
name: EnvironmentalExposure
id_prefixes:
- ECTO
- ENVO
description: A discrete event type where an organism is exposed to an environmental
  condition.
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
    owner: EnvironmentalExposure
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
    owner: EnvironmentalExposure
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
    owner: EnvironmentalExposure
    domain_of:
    - NamedThing
    - BiolinkEntity
    range: string
class_uri: biolink:EnvironmentalExposure

```
</details></div>