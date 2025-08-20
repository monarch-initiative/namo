

# Class: MLModel 


_Machine Learning and AI-based models for prediction, mechanism inference, and hypothesis generation._





URI: [namo:MLModel](https://w3id.org/monarch-initiative/namo/MLModel)





```mermaid
 classDiagram
    class MLModel
    click MLModel href "../MLModel/"
      InSilicoModel <|-- MLModel
        click InSilicoModel href "../InSilicoModel/"
      
      MLModel : biological_organization_level
        
          
    
        
        
        MLModel --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      MLModel : complexity_level
        
          
    
        
        
        MLModel --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      MLModel : computational_method
        
      MLModel : cross_validation
        
          
    
        
        
        MLModel --> "0..1" CrossValidation : cross_validation
        click CrossValidation href "../CrossValidation/"
    

        
      MLModel : description
        
      MLModel : feature_types
        
          
    
        
        
        MLModel --> "*" FeatureTypeEnum : feature_types
        click FeatureTypeEnum href "../FeatureTypeEnum/"
    

        
      MLModel : id
        
      MLModel : ml_algorithm
        
          
    
        
        
        MLModel --> "0..1" MLAlgorithmEnum : ml_algorithm
        click MLAlgorithmEnum href "../MLAlgorithmEnum/"
    

        
      MLModel : model_interpretability
        
          
    
        
        
        MLModel --> "0..1" InterpretabilityLevelEnum : model_interpretability
        click InterpretabilityLevelEnum href "../InterpretabilityLevelEnum/"
    

        
      MLModel : models
        
          
    
        
        
        MLModel --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      MLModel : name
        
      MLModel : prediction_scope
        
      MLModel : references
        
          
    
        
        
        MLModel --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      MLModel : software_platform
        
      MLModel : spatial_context
        
      MLModel : training_data_size
        
      MLModel : type
        
      MLModel : validation_datasets
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * [NAMModel](NAMModel.md)
            * [InSilicoModel](InSilicoModel.md)
                * **MLModel**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ml_algorithm](ml_algorithm.md) | 0..1 <br/> [MLAlgorithmEnum](MLAlgorithmEnum.md) | Type of machine learning algorithm used | direct |
| [feature_types](feature_types.md) | * <br/> [FeatureTypeEnum](FeatureTypeEnum.md) | Types of features used (molecular, phenotypic, imaging, etc | direct |
| [training_data_size](training_data_size.md) | 0..1 <br/> [Integer](Integer.md) | Size of training dataset | direct |
| [model_interpretability](model_interpretability.md) | 0..1 <br/> [InterpretabilityLevelEnum](InterpretabilityLevelEnum.md) | Level of model interpretability (black box, interpretable, explainable) | direct |
| [cross_validation](cross_validation.md) | 0..1 <br/> [CrossValidation](CrossValidation.md) | Cross-validation strategy and results | direct |
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
| self | namo:MLModel |
| native | namo:MLModel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MLModel
description: Machine Learning and AI-based models for prediction, mechanism inference,
  and hypothesis generation.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: InSilicoModel
attributes:
  ml_algorithm:
    name: ml_algorithm
    description: Type of machine learning algorithm used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - MLModel
    range: MLAlgorithmEnum
  feature_types:
    name: feature_types
    description: Types of features used (molecular, phenotypic, imaging, etc.)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - MLModel
    range: FeatureTypeEnum
    multivalued: true
  training_data_size:
    name: training_data_size
    description: Size of training dataset
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - MLModel
    range: integer
  model_interpretability:
    name: model_interpretability
    description: Level of model interpretability (black box, interpretable, explainable)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - MLModel
    range: InterpretabilityLevelEnum
  cross_validation:
    name: cross_validation
    description: Cross-validation strategy and results
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - MLModel
    range: CrossValidation
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: MLModel
description: Machine Learning and AI-based models for prediction, mechanism inference,
  and hypothesis generation.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: InSilicoModel
attributes:
  ml_algorithm:
    name: ml_algorithm
    description: Type of machine learning algorithm used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: ml_algorithm
    owner: MLModel
    domain_of:
    - MLModel
    range: MLAlgorithmEnum
  feature_types:
    name: feature_types
    description: Types of features used (molecular, phenotypic, imaging, etc.)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: feature_types
    owner: MLModel
    domain_of:
    - MLModel
    range: FeatureTypeEnum
    multivalued: true
  training_data_size:
    name: training_data_size
    description: Size of training dataset
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: training_data_size
    owner: MLModel
    domain_of:
    - MLModel
    range: integer
  model_interpretability:
    name: model_interpretability
    description: Level of model interpretability (black box, interpretable, explainable)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: model_interpretability
    owner: MLModel
    domain_of:
    - MLModel
    range: InterpretabilityLevelEnum
  cross_validation:
    name: cross_validation
    description: Cross-validation strategy and results
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: cross_validation
    owner: MLModel
    domain_of:
    - MLModel
    range: CrossValidation
    inlined: true
  computational_method:
    name: computational_method
    description: Primary computational method or algorithm used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: computational_method
    owner: MLModel
    domain_of:
    - InSilicoModel
    range: string
  software_platform:
    name: software_platform
    description: Software platform or programming language used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: software_platform
    owner: MLModel
    domain_of:
    - InSilicoModel
    range: string
  validation_datasets:
    name: validation_datasets
    description: Datasets used for model training and validation
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: validation_datasets
    owner: MLModel
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
    owner: MLModel
    domain_of:
    - InSilicoModel
    range: string
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: MLModel
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: MLModel
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
    owner: MLModel
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: MLModel
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
    owner: MLModel
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
    owner: MLModel
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
    owner: MLModel
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
    owner: MLModel
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: MLModel
    domain_of:
    - NamedThing
    range: string

```
</details>