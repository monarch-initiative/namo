

# Class: CoCulture 


_Co-culture systems combining multiple cell types to mimic  microenvironments and cell-cell interactions._





URI: [namo:CoCulture](https://w3id.org/monarch-initiative/namo/CoCulture)





```mermaid
 classDiagram
    class CoCulture
    click CoCulture href "../CoCulture/"
      CellularSystem <|-- CoCulture
        click CellularSystem href "../CellularSystem/"
      
      CoCulture : biological_organization_level
        
          
    
        
        
        CoCulture --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      CoCulture : cell_ratios
        
          
    
        
        
        CoCulture --> "*" CellRatio : cell_ratios
        click CellRatio href "../CellRatio/"
    

        
      CoCulture : cell_source
        
      CoCulture : cell_types
        
          
    
        
        
        CoCulture --> "*" Term : cell_types
        click Term href "../Term/"
    

        
      CoCulture : coculture_configuration
        
          
    
        
        
        CoCulture --> "0..1" CocultureConfigurationEnum : coculture_configuration
        click CocultureConfigurationEnum href "../CocultureConfigurationEnum/"
    

        
      CoCulture : complexity_level
        
          
    
        
        
        CoCulture --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      CoCulture : culture_conditions
        
      CoCulture : description
        
      CoCulture : id
        
      CoCulture : interaction_mechanisms
        
      CoCulture : models
        
          
    
        
        
        CoCulture --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      CoCulture : name
        
      CoCulture : references
        
          
    
        
        
        CoCulture --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      CoCulture : spatial_context
        
      CoCulture : type
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * [NAMModel](NAMModel.md)
            * [CellularSystem](CellularSystem.md)
                * **CoCulture**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [coculture_configuration](coculture_configuration.md) | 0..1 <br/> [CocultureConfigurationEnum](CocultureConfigurationEnum.md) | Configuration of co-culture (direct contact, transwell, conditioned media) | direct |
| [cell_ratios](cell_ratios.md) | * <br/> [CellRatio](CellRatio.md) | Ratios of different cell types in the co-culture | direct |
| [interaction_mechanisms](interaction_mechanisms.md) | * <br/> [String](String.md) | Mechanisms of cell-cell interaction (paracrine, direct contact, mechanical) | direct |
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
| self | namo:CoCulture |
| native | namo:CoCulture |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CoCulture
description: Co-culture systems combining multiple cell types to mimic  microenvironments
  and cell-cell interactions.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: CellularSystem
attributes:
  coculture_configuration:
    name: coculture_configuration
    description: Configuration of co-culture (direct contact, transwell, conditioned
      media)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CoCulture
    range: CocultureConfigurationEnum
  cell_ratios:
    name: cell_ratios
    description: Ratios of different cell types in the co-culture
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CoCulture
    range: CellRatio
    multivalued: true
    inlined: true
    inlined_as_list: true
  interaction_mechanisms:
    name: interaction_mechanisms
    description: Mechanisms of cell-cell interaction (paracrine, direct contact, mechanical)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CoCulture
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: CoCulture
description: Co-culture systems combining multiple cell types to mimic  microenvironments
  and cell-cell interactions.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: CellularSystem
attributes:
  coculture_configuration:
    name: coculture_configuration
    description: Configuration of co-culture (direct contact, transwell, conditioned
      media)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: coculture_configuration
    owner: CoCulture
    domain_of:
    - CoCulture
    range: CocultureConfigurationEnum
  cell_ratios:
    name: cell_ratios
    description: Ratios of different cell types in the co-culture
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: cell_ratios
    owner: CoCulture
    domain_of:
    - CoCulture
    range: CellRatio
    multivalued: true
    inlined: true
    inlined_as_list: true
  interaction_mechanisms:
    name: interaction_mechanisms
    description: Mechanisms of cell-cell interaction (paracrine, direct contact, mechanical)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: interaction_mechanisms
    owner: CoCulture
    domain_of:
    - CoCulture
    range: string
    multivalued: true
  cell_types:
    name: cell_types
    description: Cell types present in the cellular system
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: cell_types
    owner: CoCulture
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
    owner: CoCulture
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
    owner: CoCulture
    domain_of:
    - CellularSystem
    range: string
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: CoCulture
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: CoCulture
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
    owner: CoCulture
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: CoCulture
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
    owner: CoCulture
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
    owner: CoCulture
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
    owner: CoCulture
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
    owner: CoCulture
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: CoCulture
    domain_of:
    - NamedThing
    range: string

```
</details>