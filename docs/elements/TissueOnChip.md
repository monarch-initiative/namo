

# Class: TissueOnChip 


_Tissue-level microphysiological systems that model specific tissue functions and multi-cellular interactions._





URI: [namo:TissueOnChip](https://w3id.org/monarch-initiative/namo/TissueOnChip)





```mermaid
 classDiagram
    class TissueOnChip
    click TissueOnChip href "../TissueOnChip/"
      MicrophysiologicalSystem <|-- TissueOnChip
        click MicrophysiologicalSystem href "../MicrophysiologicalSystem/"
      
      TissueOnChip : barrier_functions
        
      TissueOnChip : biological_organization_level
        
          
    
        
        
        TissueOnChip --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      TissueOnChip : complexity_level
        
          
    
        
        
        TissueOnChip --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      TissueOnChip : description
        
      TissueOnChip : id
        
      TissueOnChip : mechanical_forces
        
          
    
        
        
        TissueOnChip --> "0..1" MechanicalStimulation : mechanical_forces
        click MechanicalStimulation href "../MechanicalStimulation/"
    

        
      TissueOnChip : microfluidic_design
        
          
    
        
        
        TissueOnChip --> "0..1" MicrofluidicDesign : microfluidic_design
        click MicrofluidicDesign href "../MicrofluidicDesign/"
    

        
      TissueOnChip : models
        
          
    
        
        
        TissueOnChip --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      TissueOnChip : name
        
      TissueOnChip : perfusion_system
        
      TissueOnChip : references
        
          
    
        
        
        TissueOnChip --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      TissueOnChip : sensor_integration
        
          
    
        
        
        TissueOnChip --> "*" IntegratedSensorEnum : sensor_integration
        click IntegratedSensorEnum href "../IntegratedSensorEnum/"
    

        
      TissueOnChip : spatial_context
        
      TissueOnChip : tissue_architecture
        
      TissueOnChip : tissue_modeled
        
          
    
        
        
        TissueOnChip --> "0..1" Term : tissue_modeled
        click Term href "../Term/"
    

        
      TissueOnChip : type
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * [NAMModel](NAMModel.md)
            * [MicrophysiologicalSystem](MicrophysiologicalSystem.md)
                * **TissueOnChip**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [tissue_modeled](tissue_modeled.md) | 0..1 <br/> [Term](Term.md) | The specific tissue being modeled | direct |
| [tissue_architecture](tissue_architecture.md) | 0..1 <br/> [String](String.md) | Description of tissue-level architecture and organization | direct |
| [barrier_functions](barrier_functions.md) | * <br/> [String](String.md) | Tissue barrier functions modeled (epithelial, endothelial, etc | direct |
| [microfluidic_design](microfluidic_design.md) | 0..1 <br/> [MicrofluidicDesign](MicrofluidicDesign.md) | Detailed design specifications of the microfluidic device | [MicrophysiologicalSystem](MicrophysiologicalSystem.md) |
| [mechanical_forces](mechanical_forces.md) | 0..1 <br/> [MechanicalStimulation](MechanicalStimulation.md) | Mechanical forces applied to the model system | [MicrophysiologicalSystem](MicrophysiologicalSystem.md) |
| [perfusion_system](perfusion_system.md) | 0..1 <br/> [String](String.md) | Description of perfusion and flow systems | [MicrophysiologicalSystem](MicrophysiologicalSystem.md) |
| [sensor_integration](sensor_integration.md) | * <br/> [IntegratedSensorEnum](IntegratedSensorEnum.md) | Sensors integrated for real-time monitoring | [MicrophysiologicalSystem](MicrophysiologicalSystem.md) |
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
| self | namo:TissueOnChip |
| native | namo:TissueOnChip |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TissueOnChip
description: Tissue-level microphysiological systems that model specific tissue functions
  and multi-cellular interactions.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: MicrophysiologicalSystem
attributes:
  tissue_modeled:
    name: tissue_modeled
    description: The specific tissue being modeled
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - TissueOnChip
    range: Term
    inlined: true
  tissue_architecture:
    name: tissue_architecture
    description: Description of tissue-level architecture and organization
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - TissueOnChip
  barrier_functions:
    name: barrier_functions
    description: Tissue barrier functions modeled (epithelial, endothelial, etc.)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - TissueOnChip
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: TissueOnChip
description: Tissue-level microphysiological systems that model specific tissue functions
  and multi-cellular interactions.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: MicrophysiologicalSystem
attributes:
  tissue_modeled:
    name: tissue_modeled
    description: The specific tissue being modeled
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: tissue_modeled
    owner: TissueOnChip
    domain_of:
    - TissueOnChip
    range: Term
    inlined: true
  tissue_architecture:
    name: tissue_architecture
    description: Description of tissue-level architecture and organization
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: tissue_architecture
    owner: TissueOnChip
    domain_of:
    - TissueOnChip
    range: string
  barrier_functions:
    name: barrier_functions
    description: Tissue barrier functions modeled (epithelial, endothelial, etc.)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: barrier_functions
    owner: TissueOnChip
    domain_of:
    - TissueOnChip
    range: string
    multivalued: true
  microfluidic_design:
    name: microfluidic_design
    description: Detailed design specifications of the microfluidic device
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: microfluidic_design
    owner: TissueOnChip
    domain_of:
    - MicrophysiologicalSystem
    range: MicrofluidicDesign
    inlined: true
  mechanical_forces:
    name: mechanical_forces
    description: Mechanical forces applied to the model system
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: mechanical_forces
    owner: TissueOnChip
    domain_of:
    - MicrophysiologicalSystem
    range: MechanicalStimulation
    inlined: true
  perfusion_system:
    name: perfusion_system
    description: Description of perfusion and flow systems
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: perfusion_system
    owner: TissueOnChip
    domain_of:
    - MicrophysiologicalSystem
    range: string
  sensor_integration:
    name: sensor_integration
    description: Sensors integrated for real-time monitoring
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: sensor_integration
    owner: TissueOnChip
    domain_of:
    - MicrophysiologicalSystem
    range: IntegratedSensorEnum
    multivalued: true
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: TissueOnChip
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: TissueOnChip
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
    owner: TissueOnChip
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: TissueOnChip
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
    owner: TissueOnChip
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
    owner: TissueOnChip
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
    owner: TissueOnChip
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
    owner: TissueOnChip
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: TissueOnChip
    domain_of:
    - NamedThing
    range: string

```
</details>