

# Class: ModelSystem 


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [namo:ModelSystem](https://w3id.org/monarch-initiative/namo/ModelSystem)





```mermaid
 classDiagram
    class ModelSystem
    click ModelSystem href "../ModelSystem/"
      NamedThing <|-- ModelSystem
        click NamedThing href "../NamedThing/"
      

      ModelSystem <|-- AnimalModel
        click AnimalModel href "../AnimalModel/"
      ModelSystem <|-- NAMModel
        click NAMModel href "../NAMModel/"
      

      ModelSystem : description
        
      ModelSystem : id
        
      ModelSystem : models
        
          
    
        
        
        ModelSystem --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      ModelSystem : name
        
      ModelSystem : type
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **ModelSystem**
        * [AnimalModel](AnimalModel.md)
        * [NAMModel](NAMModel.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [models](models.md) | * <br/> [ModelsRelationship](ModelsRelationship.md) |  | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [NamedThing](NamedThing.md) |
| [type](type.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [model_systems](model_systems.md) | range | [ModelSystem](ModelSystem.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:ModelSystem |
| native | namo:ModelSystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModelSystem
from_schema: https://w3id.org/monarch-initiative/namo
is_a: NamedThing
abstract: true
attributes:
  models:
    name: models
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - ModelSystem
    range: ModelsRelationship
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: ModelSystem
from_schema: https://w3id.org/monarch-initiative/namo
is_a: NamedThing
abstract: true
attributes:
  models:
    name: models
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: models
    owner: ModelSystem
    domain_of:
    - ModelSystem
    range: ModelsRelationship
    multivalued: true
  id:
    name: id
    description: A unique identifier for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: ModelSystem
    domain_of:
    - NamedThing
    - Reference
    range: uriorcurie
    required: true
  name:
    name: name
    description: A human-readable name for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: ModelSystem
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: ModelSystem
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: ModelSystem
    domain_of:
    - NamedThing
    range: string

```
</details>