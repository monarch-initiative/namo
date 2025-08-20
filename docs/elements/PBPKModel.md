

# Class: PBPKModel 


_Physiologically Based Pharmacokinetic models that simulate drug  absorption, distribution, metabolism, and excretion._





URI: [namo:PBPKModel](https://w3id.org/monarch-initiative/namo/PBPKModel)





```mermaid
 classDiagram
    class PBPKModel
    click PBPKModel href "../PBPKModel/"
      InSilicoModel <|-- PBPKModel
        click InSilicoModel href "../InSilicoModel/"
      
      PBPKModel : biological_organization_level
        
          
    
        
        
        PBPKModel --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      PBPKModel : compartments
        
          
    
        
        
        PBPKModel --> "*" PBPKCompartment : compartments
        click PBPKCompartment href "../PBPKCompartment/"
    

        
      PBPKModel : complexity_level
        
          
    
        
        
        PBPKModel --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      PBPKModel : computational_method
        
      PBPKModel : description
        
      PBPKModel : drug_properties
        
          
    
        
        
        PBPKModel --> "0..1" DrugProperties : drug_properties
        click DrugProperties href "../DrugProperties/"
    

        
      PBPKModel : elimination_pathways
        
      PBPKModel : id
        
      PBPKModel : models
        
          
    
        
        
        PBPKModel --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      PBPKModel : name
        
      PBPKModel : prediction_scope
        
      PBPKModel : references
        
          
    
        
        
        PBPKModel --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      PBPKModel : software_platform
        
      PBPKModel : spatial_context
        
      PBPKModel : species_modeled
        
          
    
        
        
        PBPKModel --> "0..1" Term : species_modeled
        click Term href "../Term/"
    

        
      PBPKModel : type
        
      PBPKModel : validation_datasets
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * [NAMModel](NAMModel.md)
            * [InSilicoModel](InSilicoModel.md)
                * **PBPKModel**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [compartments](compartments.md) | * <br/> [PBPKCompartment](PBPKCompartment.md) | Physiological compartments included in the model | direct |
| [species_modeled](species_modeled.md) | 0..1 <br/> [Term](Term.md) | Species for which the model is designed | direct |
| [drug_properties](drug_properties.md) | 0..1 <br/> [DrugProperties](DrugProperties.md) | Physicochemical and pharmacological properties modeled | direct |
| [elimination_pathways](elimination_pathways.md) | * <br/> [String](String.md) | Drug elimination and metabolism pathways included | direct |
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
| self | namo:PBPKModel |
| native | namo:PBPKModel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PBPKModel
description: Physiologically Based Pharmacokinetic models that simulate drug  absorption,
  distribution, metabolism, and excretion.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: InSilicoModel
attributes:
  compartments:
    name: compartments
    description: Physiological compartments included in the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - PBPKModel
    range: PBPKCompartment
    multivalued: true
    inlined: true
    inlined_as_list: true
  species_modeled:
    name: species_modeled
    description: Species for which the model is designed
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - PBPKModel
    range: Term
    inlined: true
  drug_properties:
    name: drug_properties
    description: Physicochemical and pharmacological properties modeled
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - PBPKModel
    range: DrugProperties
    inlined: true
  elimination_pathways:
    name: elimination_pathways
    description: Drug elimination and metabolism pathways included
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - PBPKModel
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: PBPKModel
description: Physiologically Based Pharmacokinetic models that simulate drug  absorption,
  distribution, metabolism, and excretion.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: InSilicoModel
attributes:
  compartments:
    name: compartments
    description: Physiological compartments included in the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: compartments
    owner: PBPKModel
    domain_of:
    - PBPKModel
    range: PBPKCompartment
    multivalued: true
    inlined: true
    inlined_as_list: true
  species_modeled:
    name: species_modeled
    description: Species for which the model is designed
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: species_modeled
    owner: PBPKModel
    domain_of:
    - PBPKModel
    range: Term
    inlined: true
  drug_properties:
    name: drug_properties
    description: Physicochemical and pharmacological properties modeled
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: drug_properties
    owner: PBPKModel
    domain_of:
    - PBPKModel
    range: DrugProperties
    inlined: true
  elimination_pathways:
    name: elimination_pathways
    description: Drug elimination and metabolism pathways included
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: elimination_pathways
    owner: PBPKModel
    domain_of:
    - PBPKModel
    range: string
    multivalued: true
  computational_method:
    name: computational_method
    description: Primary computational method or algorithm used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: computational_method
    owner: PBPKModel
    domain_of:
    - InSilicoModel
    range: string
  software_platform:
    name: software_platform
    description: Software platform or programming language used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: software_platform
    owner: PBPKModel
    domain_of:
    - InSilicoModel
    range: string
  validation_datasets:
    name: validation_datasets
    description: Datasets used for model training and validation
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: validation_datasets
    owner: PBPKModel
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
    owner: PBPKModel
    domain_of:
    - InSilicoModel
    range: string
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: PBPKModel
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: PBPKModel
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
    owner: PBPKModel
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: PBPKModel
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
    owner: PBPKModel
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
    owner: PBPKModel
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
    owner: PBPKModel
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
    owner: PBPKModel
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: PBPKModel
    domain_of:
    - NamedThing
    range: string

```
</details>