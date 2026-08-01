---
search:
  boost: 10.0
---

# Class: BiolinkEntity 


_Abstract parent for NAMO classes that stand in for a class in the Biolink Model._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [namo:BiolinkEntity](https://w3id.org/monarch-initiative/namo/BiolinkEntity)





```mermaid
 classDiagram
    class BiolinkEntity
    click BiolinkEntity href "../BiolinkEntity/"
      BiolinkEntity <|-- OrganismTaxon
        click OrganismTaxon href "../OrganismTaxon/"
      BiolinkEntity <|-- Cell
        click Cell href "../Cell/"
      BiolinkEntity <|-- GrossAnatomicalStructure
        click GrossAnatomicalStructure href "../GrossAnatomicalStructure/"
      BiolinkEntity <|-- PhenotypicFeature
        click PhenotypicFeature href "../PhenotypicFeature/"
      BiolinkEntity <|-- LifeStage
        click LifeStage href "../LifeStage/"
      BiolinkEntity <|-- EnvironmentalExposure
        click EnvironmentalExposure href "../EnvironmentalExposure/"
      
      BiolinkEntity : description
        
      BiolinkEntity : id
        
      BiolinkEntity : name
        
      
```





## Inheritance
* **BiolinkEntity**
    * [OrganismTaxon](OrganismTaxon.md)
    * [Cell](Cell.md)
    * [GrossAnatomicalStructure](GrossAnatomicalStructure.md)
    * [PhenotypicFeature](PhenotypicFeature.md)
    * [LifeStage](LifeStage.md)
    * [EnvironmentalExposure](EnvironmentalExposure.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | direct |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:BiolinkEntity |
| native | namo:BiolinkEntity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiolinkEntity
description: Abstract parent for NAMO classes that stand in for a class in the Biolink
  Model.
from_schema: https://w3id.org/monarch-initiative/namo
abstract: true
slots:
- id
- name
- description

```
</details>

### Induced

<details>
```yaml
name: BiolinkEntity
description: Abstract parent for NAMO classes that stand in for a class in the Biolink
  Model.
from_schema: https://w3id.org/monarch-initiative/namo
abstract: true
attributes:
  id:
    name: id
    description: A unique identifier for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    owner: BiolinkEntity
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
    owner: BiolinkEntity
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
    owner: BiolinkEntity
    domain_of:
    - NamedThing
    - BiolinkEntity
    range: string

```
</details></div>