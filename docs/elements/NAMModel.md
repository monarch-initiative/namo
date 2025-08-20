

# Class: NAMModel 


_A New Approach Methodology (NAM) model, which is a type of model system that does not involve the use of animals._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [namo:NAMModel](https://w3id.org/monarch-initiative/namo/NAMModel)





```mermaid
 classDiagram
    class NAMModel
    click NAMModel href "../NAMModel/"
      ModelSystem <|-- NAMModel
        click ModelSystem href "../ModelSystem/"
      

      NAMModel <|-- CellularSystem
        click CellularSystem href "../CellularSystem/"
      NAMModel <|-- MicrophysiologicalSystem
        click MicrophysiologicalSystem href "../MicrophysiologicalSystem/"
      NAMModel <|-- InSilicoModel
        click InSilicoModel href "../InSilicoModel/"
      

      NAMModel : biological_organization_level
        
          
    
        
        
        NAMModel --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      NAMModel : complexity_level
        
          
    
        
        
        NAMModel --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      NAMModel : description
        
      NAMModel : id
        
      NAMModel : models
        
          
    
        
        
        NAMModel --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      NAMModel : name
        
      NAMModel : references
        
          
    
        
        
        NAMModel --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      NAMModel : spatial_context
        
      NAMModel : type
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * **NAMModel**
            * [CellularSystem](CellularSystem.md)
            * [MicrophysiologicalSystem](MicrophysiologicalSystem.md)
            * [InSilicoModel](InSilicoModel.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [biological_organization_level](biological_organization_level.md) | 0..1 <br/> [BiologicalOrganizationLevelEnum](BiologicalOrganizationLevelEnum.md) | The level of biological organization represented by the model | direct |
| [spatial_context](spatial_context.md) | 0..1 <br/> [String](String.md) | Description of spatial organization and context captured by the model | direct |
| [complexity_level](complexity_level.md) | 0..1 <br/> [ComplexityLevelEnum](ComplexityLevelEnum.md) | Level of biological complexity represented (subcellular, cellular, tissue, or... | direct |
| [references](references.md) | * <br/> [Reference](Reference.md) | Literature references that describe, validate, or support this model | direct |
| [models](models.md) | * <br/> [ModelsRelationship](ModelsRelationship.md) |  | [ModelSystem](ModelSystem.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [NamedThing](NamedThing.md) |
| [type](type.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:NAMModel |
| native | namo:NAMModel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NAMModel
description: A New Approach Methodology (NAM) model, which is a type of model system
  that does not involve the use of animals.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: ModelSystem
abstract: true
attributes:
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - NAMModel
  complexity_level:
    name: complexity_level
    description: Level of biological complexity represented (subcellular, cellular,
      tissue, organ, system)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - NAMModel
    range: Reference
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: NAMModel
description: A New Approach Methodology (NAM) model, which is a type of model system
  that does not involve the use of animals.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: ModelSystem
abstract: true
attributes:
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: NAMModel
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: NAMModel
    domain_of:
    - NAMModel
    range: string
  complexity_level:
    name: complexity_level
    description: Level of biological complexity represented (subcellular, cellular,
      tissue, organ, system)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: complexity_level
    owner: NAMModel
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: NAMModel
    domain_of:
    - NAMModel
    range: Reference
    multivalued: true
    inlined: true
    inlined_as_list: true
  models:
    name: models
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: models
    owner: NAMModel
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
    owner: NAMModel
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
    owner: NAMModel
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
    owner: NAMModel
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: NAMModel
    domain_of:
    - NamedThing
    range: string

```
</details>