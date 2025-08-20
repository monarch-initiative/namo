

# Class: TwoDCellCulture 


_Conventional monolayer cell cultures grown on flat surfaces. Simple but limited in physiological relevance._





URI: [namo:TwoDCellCulture](https://w3id.org/monarch-initiative/namo/TwoDCellCulture)





```mermaid
 classDiagram
    class TwoDCellCulture
    click TwoDCellCulture href "../TwoDCellCulture/"
      CellularSystem <|-- TwoDCellCulture
        click CellularSystem href "../CellularSystem/"
      

      TwoDCellCulture <|-- CellLineModel
        click CellLineModel href "../CellLineModel/"
      

      TwoDCellCulture : biological_organization_level
        
          
    
        
        
        TwoDCellCulture --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      TwoDCellCulture : cell_source
        
      TwoDCellCulture : cell_types
        
          
    
        
        
        TwoDCellCulture --> "*" Term : cell_types
        click Term href "../Term/"
    

        
      TwoDCellCulture : complexity_level
        
          
    
        
        
        TwoDCellCulture --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      TwoDCellCulture : confluence_level
        
      TwoDCellCulture : culture_conditions
        
      TwoDCellCulture : description
        
      TwoDCellCulture : id
        
      TwoDCellCulture : models
        
          
    
        
        
        TwoDCellCulture --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      TwoDCellCulture : name
        
      TwoDCellCulture : passage_protocol
        
      TwoDCellCulture : references
        
          
    
        
        
        TwoDCellCulture --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      TwoDCellCulture : spatial_context
        
      TwoDCellCulture : substrate_type
        
      TwoDCellCulture : type
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * [NAMModel](NAMModel.md)
            * [CellularSystem](CellularSystem.md)
                * **TwoDCellCulture**
                    * [CellLineModel](CellLineModel.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [substrate_type](substrate_type.md) | 0..1 <br/> [String](String.md) | Type of culture substrate (e | direct |
| [confluence_level](confluence_level.md) | 0..1 <br/> [Float](Float.md) | Typical confluence level maintained (0 | direct |
| [passage_protocol](passage_protocol.md) | 0..1 <br/> [String](String.md) | Standard passaging protocol and frequency | direct |
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
| self | namo:TwoDCellCulture |
| native | namo:TwoDCellCulture |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TwoDCellCulture
description: Conventional monolayer cell cultures grown on flat surfaces. Simple but
  limited in physiological relevance.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: CellularSystem
attributes:
  substrate_type:
    name: substrate_type
    description: Type of culture substrate (e.g., plastic, glass, coated surfaces)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - TwoDCellCulture
  confluence_level:
    name: confluence_level
    description: Typical confluence level maintained (0.0-1.0)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - TwoDCellCulture
    range: float
  passage_protocol:
    name: passage_protocol
    description: Standard passaging protocol and frequency
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - TwoDCellCulture

```
</details>

### Induced

<details>
```yaml
name: TwoDCellCulture
description: Conventional monolayer cell cultures grown on flat surfaces. Simple but
  limited in physiological relevance.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: CellularSystem
attributes:
  substrate_type:
    name: substrate_type
    description: Type of culture substrate (e.g., plastic, glass, coated surfaces)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: substrate_type
    owner: TwoDCellCulture
    domain_of:
    - TwoDCellCulture
    range: string
  confluence_level:
    name: confluence_level
    description: Typical confluence level maintained (0.0-1.0)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: confluence_level
    owner: TwoDCellCulture
    domain_of:
    - TwoDCellCulture
    range: float
  passage_protocol:
    name: passage_protocol
    description: Standard passaging protocol and frequency
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: passage_protocol
    owner: TwoDCellCulture
    domain_of:
    - TwoDCellCulture
    range: string
  cell_types:
    name: cell_types
    description: Cell types present in the cellular system
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: cell_types
    owner: TwoDCellCulture
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
    owner: TwoDCellCulture
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
    owner: TwoDCellCulture
    domain_of:
    - CellularSystem
    range: string
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: TwoDCellCulture
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: TwoDCellCulture
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
    owner: TwoDCellCulture
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: TwoDCellCulture
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
    owner: TwoDCellCulture
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
    owner: TwoDCellCulture
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
    owner: TwoDCellCulture
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
    owner: TwoDCellCulture
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: TwoDCellCulture
    domain_of:
    - NamedThing
    range: string

```
</details>