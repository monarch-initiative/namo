

# Class: DigitalTwin 


_Computational replicas of biological systems for real-time prediction and personalized modeling._





URI: [namo:DigitalTwin](https://w3id.org/monarch-initiative/namo/DigitalTwin)





```mermaid
 classDiagram
    class DigitalTwin
    click DigitalTwin href "../DigitalTwin/"
      InSilicoModel <|-- DigitalTwin
        click InSilicoModel href "../InSilicoModel/"
      
      DigitalTwin : biological_organization_level
        
          
    
        
        
        DigitalTwin --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      DigitalTwin : complexity_level
        
          
    
        
        
        DigitalTwin --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      DigitalTwin : computational_method
        
      DigitalTwin : description
        
      DigitalTwin : id
        
      DigitalTwin : models
        
          
    
        
        
        DigitalTwin --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      DigitalTwin : name
        
      DigitalTwin : personalization_parameters
        
      DigitalTwin : prediction_scope
        
      DigitalTwin : real_time_data_sources
        
      DigitalTwin : references
        
          
    
        
        
        DigitalTwin --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      DigitalTwin : software_platform
        
      DigitalTwin : spatial_context
        
      DigitalTwin : twin_scope
        
          
    
        
        
        DigitalTwin --> "0..1" DigitalTwinScopeEnum : twin_scope
        click DigitalTwinScopeEnum href "../DigitalTwinScopeEnum/"
    

        
      DigitalTwin : type
        
      DigitalTwin : update_frequency
        
      DigitalTwin : validation_datasets
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * [NAMModel](NAMModel.md)
            * [InSilicoModel](InSilicoModel.md)
                * **DigitalTwin**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [twin_scope](twin_scope.md) | 0..1 <br/> [DigitalTwinScopeEnum](DigitalTwinScopeEnum.md) | Scope of digital twin (organ, patient, population) | direct |
| [real_time_data_sources](real_time_data_sources.md) | * <br/> [String](String.md) | Sources of real-time data for model updating | direct |
| [personalization_parameters](personalization_parameters.md) | * <br/> [String](String.md) | Parameters used for personalization (genetic, phenotypic, etc | direct |
| [update_frequency](update_frequency.md) | 0..1 <br/> [String](String.md) | Frequency of model updates based on new data | direct |
| [computational_method](computational_method.md) | 0..1 <br/> [String](String.md) | Primary computational method or algorithm used | [InSilicoModel](InSilicoModel.md) |
| [software_platform](software_platform.md) | 0..1 <br/> [String](String.md) | Software platform or programming language used | [InSilicoModel](InSilicoModel.md) |
| [validation_datasets](validation_datasets.md) | * <br/> [String](String.md) | Datasets used for model training and validation | [InSilicoModel](InSilicoModel.md) |
| [prediction_scope](prediction_scope.md) | 0..1 <br/> [String](String.md) | Scope and limitations of model predictions | [InSilicoModel](InSilicoModel.md) |
| [biological_organization_level](biological_organization_level.md) | 0..1 <br/> [BiologicalOrganizationLevelEnum](BiologicalOrganizationLevelEnum.md) | The level of biological organization represented by the model | [NAMModel](NAMModel.md) |
| [spatial_context](spatial_context.md) | 0..1 <br/> [String](String.md) | Description of spatial organization and context captured by the model | [NAMModel](NAMModel.md) |
| [complexity_level](complexity_level.md) | 0..1 <br/> [ComplexityLevelEnum](ComplexityLevelEnum.md) | Level of biological complexity represented (subcellular, cellular, tissue, or... | [NAMModel](NAMModel.md) |
| [references](references.md) | * <br/> [Reference](Reference.md) | Literature references that describe, validate, or support this model | [NAMModel](NAMModel.md) |
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
| self | namo:DigitalTwin |
| native | namo:DigitalTwin |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DigitalTwin
description: Computational replicas of biological systems for real-time prediction
  and personalized modeling.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: InSilicoModel
attributes:
  twin_scope:
    name: twin_scope
    description: Scope of digital twin (organ, patient, population)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - DigitalTwin
    range: DigitalTwinScopeEnum
  real_time_data_sources:
    name: real_time_data_sources
    description: Sources of real-time data for model updating
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - DigitalTwin
    multivalued: true
  personalization_parameters:
    name: personalization_parameters
    description: Parameters used for personalization (genetic, phenotypic, etc.)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - DigitalTwin
    multivalued: true
  update_frequency:
    name: update_frequency
    description: Frequency of model updates based on new data
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - DigitalTwin

```
</details>

### Induced

<details>
```yaml
name: DigitalTwin
description: Computational replicas of biological systems for real-time prediction
  and personalized modeling.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: InSilicoModel
attributes:
  twin_scope:
    name: twin_scope
    description: Scope of digital twin (organ, patient, population)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: twin_scope
    owner: DigitalTwin
    domain_of:
    - DigitalTwin
    range: DigitalTwinScopeEnum
  real_time_data_sources:
    name: real_time_data_sources
    description: Sources of real-time data for model updating
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: real_time_data_sources
    owner: DigitalTwin
    domain_of:
    - DigitalTwin
    range: string
    multivalued: true
  personalization_parameters:
    name: personalization_parameters
    description: Parameters used for personalization (genetic, phenotypic, etc.)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: personalization_parameters
    owner: DigitalTwin
    domain_of:
    - DigitalTwin
    range: string
    multivalued: true
  update_frequency:
    name: update_frequency
    description: Frequency of model updates based on new data
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: update_frequency
    owner: DigitalTwin
    domain_of:
    - DigitalTwin
    range: string
  computational_method:
    name: computational_method
    description: Primary computational method or algorithm used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: computational_method
    owner: DigitalTwin
    domain_of:
    - InSilicoModel
    range: string
  software_platform:
    name: software_platform
    description: Software platform or programming language used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: software_platform
    owner: DigitalTwin
    domain_of:
    - InSilicoModel
    range: string
  validation_datasets:
    name: validation_datasets
    description: Datasets used for model training and validation
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: validation_datasets
    owner: DigitalTwin
    domain_of:
    - InSilicoModel
    range: string
    multivalued: true
  prediction_scope:
    name: prediction_scope
    description: Scope and limitations of model predictions
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: prediction_scope
    owner: DigitalTwin
    domain_of:
    - InSilicoModel
    range: string
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: DigitalTwin
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: DigitalTwin
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
    owner: DigitalTwin
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: DigitalTwin
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
    owner: DigitalTwin
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
    owner: DigitalTwin
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
    owner: DigitalTwin
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
    owner: DigitalTwin
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: DigitalTwin
    domain_of:
    - NamedThing
    range: string

```
</details>