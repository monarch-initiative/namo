

# Class: CellularSystem 


_Cell-based model systems that use living cells to model biological processes. Includes 2D cultures, 3D systems, and co-cultures._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [namo:CellularSystem](https://w3id.org/monarch-initiative/namo/CellularSystem)





```mermaid
 classDiagram
    class CellularSystem
    click CellularSystem href "../CellularSystem/"
      NAMModel <|-- CellularSystem
        click NAMModel href "../NAMModel/"
      

      CellularSystem <|-- TwoDCellCulture
        click TwoDCellCulture href "../TwoDCellCulture/"
      CellularSystem <|-- ThreeDCellCulture
        click ThreeDCellCulture href "../ThreeDCellCulture/"
      CellularSystem <|-- CoCulture
        click CoCulture href "../CoCulture/"
      

      CellularSystem : biological_organization_level
        
          
    
        
        
        CellularSystem --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      CellularSystem : cell_source
        
      CellularSystem : cell_types
        
          
    
        
        
        CellularSystem --> "*" Term : cell_types
        click Term href "../Term/"
    

        
      CellularSystem : complexity_level
        
          
    
        
        
        CellularSystem --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      CellularSystem : culture_conditions
        
      CellularSystem : description
        
      CellularSystem : id
        
      CellularSystem : models
        
          
    
        
        
        CellularSystem --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      CellularSystem : name
        
      CellularSystem : references
        
          
    
        
        
        CellularSystem --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      CellularSystem : spatial_context
        
      CellularSystem : type
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * [NAMModel](NAMModel.md)
            * **CellularSystem**
                * [TwoDCellCulture](TwoDCellCulture.md)
                * [ThreeDCellCulture](ThreeDCellCulture.md)
                * [CoCulture](CoCulture.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cell_types](cell_types.md) | * <br/> [Term](Term.md) | Cell types present in the cellular system | direct |
| [cell_source](cell_source.md) | 0..1 <br/> [String](String.md) | Source of cells (e | direct |
| [culture_conditions](culture_conditions.md) | 0..1 <br/> [String](String.md) | Standard culture conditions and media used | direct |
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
| self | namo:CellularSystem |
| native | namo:CellularSystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellularSystem
description: Cell-based model systems that use living cells to model biological processes.
  Includes 2D cultures, 3D systems, and co-cultures.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: NAMModel
abstract: true
attributes:
  cell_types:
    name: cell_types
    description: Cell types present in the cellular system
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
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
    domain_of:
    - CellularSystem
    - OrganOnChip
  culture_conditions:
    name: culture_conditions
    description: Standard culture conditions and media used
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CellularSystem

```
</details>

### Induced

<details>
```yaml
name: CellularSystem
description: Cell-based model systems that use living cells to model biological processes.
  Includes 2D cultures, 3D systems, and co-cultures.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: NAMModel
abstract: true
attributes:
  cell_types:
    name: cell_types
    description: Cell types present in the cellular system
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: cell_types
    owner: CellularSystem
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
    owner: CellularSystem
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
    owner: CellularSystem
    domain_of:
    - CellularSystem
    range: string
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: CellularSystem
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: CellularSystem
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
    owner: CellularSystem
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: CellularSystem
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
    owner: CellularSystem
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
    owner: CellularSystem
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
    owner: CellularSystem
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
    owner: CellularSystem
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: CellularSystem
    domain_of:
    - NamedThing
    range: string

```
</details>