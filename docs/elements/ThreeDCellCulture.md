

# Class: ThreeDCellCulture 


_Three-dimensional cell culture systems including spheroids and organoids. More physiologically relevant with 3D architecture._





URI: [namo:ThreeDCellCulture](https://w3id.org/monarch-initiative/namo/ThreeDCellCulture)





```mermaid
 classDiagram
    class ThreeDCellCulture
    click ThreeDCellCulture href "../ThreeDCellCulture/"
      CellularSystem <|-- ThreeDCellCulture
        click CellularSystem href "../CellularSystem/"
      

      ThreeDCellCulture <|-- Organoid
        click Organoid href "../Organoid/"
      

      ThreeDCellCulture : biological_organization_level
        
          
    
        
        
        ThreeDCellCulture --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      ThreeDCellCulture : cell_source
        
      ThreeDCellCulture : cell_types
        
          
    
        
        
        ThreeDCellCulture --> "*" Term : cell_types
        click Term href "../Term/"
    

        
      ThreeDCellCulture : complexity_level
        
          
    
        
        
        ThreeDCellCulture --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      ThreeDCellCulture : culture_conditions
        
      ThreeDCellCulture : description
        
      ThreeDCellCulture : id
        
      ThreeDCellCulture : matrix_composition
        
      ThreeDCellCulture : models
        
          
    
        
        
        ThreeDCellCulture --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      ThreeDCellCulture : name
        
      ThreeDCellCulture : references
        
          
    
        
        
        ThreeDCellCulture --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      ThreeDCellCulture : size_range
        
      ThreeDCellCulture : spatial_context
        
      ThreeDCellCulture : three_d_architecture
        
          
    
        
        
        ThreeDCellCulture --> "0..1" ThreeDArchitectureEnum : three_d_architecture
        click ThreeDArchitectureEnum href "../ThreeDArchitectureEnum/"
    

        
      ThreeDCellCulture : type
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * [NAMModel](NAMModel.md)
            * [CellularSystem](CellularSystem.md)
                * **ThreeDCellCulture**
                    * [Organoid](Organoid.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [three_d_architecture](three_d_architecture.md) | 0..1 <br/> [ThreeDArchitectureEnum](ThreeDArchitectureEnum.md) | Type of 3D architecture (spheroid, organoid, scaffold-based, etc | direct |
| [matrix_composition](matrix_composition.md) | 0..1 <br/> [String](String.md) | Composition of extracellular matrix or scaffold material | direct |
| [size_range](size_range.md) | 0..1 <br/> [String](String.md) | Typical size range of 3D structures | direct |
| [cell_types](cell_types.md) | * <br/> [Term](Term.md) | Cell types present in the cellular system | [CellularSystem](CellularSystem.md) |
| [cell_source](cell_source.md) | 0..1 <br/> [String](String.md) | Source of cells (e | [CellularSystem](CellularSystem.md) |
| [culture_conditions](culture_conditions.md) | 0..1 <br/> [String](String.md) | Standard culture conditions and media used | [CellularSystem](CellularSystem.md) |
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
| self | namo:ThreeDCellCulture |
| native | namo:ThreeDCellCulture |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ThreeDCellCulture
description: Three-dimensional cell culture systems including spheroids and organoids.
  More physiologically relevant with 3D architecture.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: CellularSystem
attributes:
  three_d_architecture:
    name: three_d_architecture
    description: Type of 3D architecture (spheroid, organoid, scaffold-based, etc.)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - ThreeDCellCulture
    range: ThreeDArchitectureEnum
  matrix_composition:
    name: matrix_composition
    description: Composition of extracellular matrix or scaffold material
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - ThreeDCellCulture
  size_range:
    name: size_range
    description: Typical size range of 3D structures
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - ThreeDCellCulture

```
</details>

### Induced

<details>
```yaml
name: ThreeDCellCulture
description: Three-dimensional cell culture systems including spheroids and organoids.
  More physiologically relevant with 3D architecture.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: CellularSystem
attributes:
  three_d_architecture:
    name: three_d_architecture
    description: Type of 3D architecture (spheroid, organoid, scaffold-based, etc.)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: three_d_architecture
    owner: ThreeDCellCulture
    domain_of:
    - ThreeDCellCulture
    range: ThreeDArchitectureEnum
  matrix_composition:
    name: matrix_composition
    description: Composition of extracellular matrix or scaffold material
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: matrix_composition
    owner: ThreeDCellCulture
    domain_of:
    - ThreeDCellCulture
    range: string
  size_range:
    name: size_range
    description: Typical size range of 3D structures
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: size_range
    owner: ThreeDCellCulture
    domain_of:
    - ThreeDCellCulture
    range: string
  cell_types:
    name: cell_types
    description: Cell types present in the cellular system
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: cell_types
    owner: ThreeDCellCulture
    domain_of:
    - CellularSystem
    - OrganOnChip
    range: Term
    bindings:
    - range: CellTypeEnum
      obligation_level: REQUIRED
      binds_value_of: id
    multivalued: true
    inlined: true
    inlined_as_list: true
  cell_source:
    name: cell_source
    description: Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: cell_source
    owner: ThreeDCellCulture
    domain_of:
    - CellularSystem
    - OrganOnChip
    range: string
  culture_conditions:
    name: culture_conditions
    description: Standard culture conditions and media used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: culture_conditions
    owner: ThreeDCellCulture
    domain_of:
    - CellularSystem
    range: string
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: ThreeDCellCulture
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: ThreeDCellCulture
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
    owner: ThreeDCellCulture
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: ThreeDCellCulture
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
    owner: ThreeDCellCulture
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
    owner: ThreeDCellCulture
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
    owner: ThreeDCellCulture
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
    owner: ThreeDCellCulture
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: ThreeDCellCulture
    domain_of:
    - NamedThing
    range: string

```
</details>