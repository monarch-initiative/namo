

# Class: CellLineModel 


_A model system based on immortalized cell lines that can be maintained in culture indefinitely. Examples: HepG2, A549, Caco-2, etc._





URI: [namo:CellLineModel](https://w3id.org/monarch-initiative/namo/CellLineModel)





```mermaid
 classDiagram
    class CellLineModel
    click CellLineModel href "../CellLineModel/"
      TwoDCellCulture <|-- CellLineModel
        click TwoDCellCulture href "../TwoDCellCulture/"
      
      CellLineModel : authentication_method
        
      CellLineModel : biological_organization_level
        
          
    
        
        
        CellLineModel --> "0..1" BiologicalOrganizationLevelEnum : biological_organization_level
        click BiologicalOrganizationLevelEnum href "../BiologicalOrganizationLevelEnum/"
    

        
      CellLineModel : cell_source
        
      CellLineModel : cell_types
        
          
    
        
        
        CellLineModel --> "*" Term : cell_types
        click Term href "../Term/"
    

        
      CellLineModel : complexity_level
        
          
    
        
        
        CellLineModel --> "0..1" ComplexityLevelEnum : complexity_level
        click ComplexityLevelEnum href "../ComplexityLevelEnum/"
    

        
      CellLineModel : confluence_level
        
      CellLineModel : culture_conditions
        
      CellLineModel : description
        
      CellLineModel : id
        
      CellLineModel : models
        
          
    
        
        
        CellLineModel --> "*" ModelsRelationship : models
        click ModelsRelationship href "../ModelsRelationship/"
    

        
      CellLineModel : name
        
      CellLineModel : passage_protocol
        
      CellLineModel : passage_range
        
      CellLineModel : references
        
          
    
        
        
        CellLineModel --> "*" Reference : references
        click Reference href "../Reference/"
    

        
      CellLineModel : spatial_context
        
      CellLineModel : substrate_type
        
      CellLineModel : type
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ModelSystem](ModelSystem.md)
        * [NAMModel](NAMModel.md)
            * [CellularSystem](CellularSystem.md)
                * [TwoDCellCulture](TwoDCellCulture.md)
                    * **CellLineModel**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [passage_range](passage_range.md) | 0..1 <br/> [String](String.md) | Recommended passage number range for experimental use | direct |
| [authentication_method](authentication_method.md) | 0..1 <br/> [String](String.md) | Method used for cell line authentication (e | direct |
| [substrate_type](substrate_type.md) | 0..1 <br/> [String](String.md) | Type of culture substrate (e | [TwoDCellCulture](TwoDCellCulture.md) |
| [confluence_level](confluence_level.md) | 0..1 <br/> [Float](Float.md) | Typical confluence level maintained (0 | [TwoDCellCulture](TwoDCellCulture.md) |
| [passage_protocol](passage_protocol.md) | 0..1 <br/> [String](String.md) | Standard passaging protocol and frequency | [TwoDCellCulture](TwoDCellCulture.md) |
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
| self | namo:CellLineModel |
| native | namo:CellLineModel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellLineModel
description: 'A model system based on immortalized cell lines that can be maintained
  in culture indefinitely. Examples: HepG2, A549, Caco-2, etc.'
from_schema: https://w3id.org/monarch-initiative/namo
is_a: TwoDCellCulture
attributes:
  passage_range:
    name: passage_range
    description: Recommended passage number range for experimental use
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CellLineModel
  authentication_method:
    name: authentication_method
    description: Method used for cell line authentication (e.g., STR profiling, mycoplasma
      testing)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CellLineModel

```
</details>

### Induced

<details>
```yaml
name: CellLineModel
description: 'A model system based on immortalized cell lines that can be maintained
  in culture indefinitely. Examples: HepG2, A549, Caco-2, etc.'
from_schema: https://w3id.org/monarch-initiative/namo
is_a: TwoDCellCulture
attributes:
  passage_range:
    name: passage_range
    description: Recommended passage number range for experimental use
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: passage_range
    owner: CellLineModel
    domain_of:
    - CellLineModel
    range: string
  authentication_method:
    name: authentication_method
    description: Method used for cell line authentication (e.g., STR profiling, mycoplasma
      testing)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: authentication_method
    owner: CellLineModel
    domain_of:
    - CellLineModel
    range: string
  substrate_type:
    name: substrate_type
    description: Type of culture substrate (e.g., plastic, glass, coated surfaces)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: substrate_type
    owner: CellLineModel
    domain_of:
    - TwoDCellCulture
    range: string
  confluence_level:
    name: confluence_level
    description: Typical confluence level maintained (0.0-1.0)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: confluence_level
    owner: CellLineModel
    domain_of:
    - TwoDCellCulture
    range: float
  passage_protocol:
    name: passage_protocol
    description: Standard passaging protocol and frequency
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: passage_protocol
    owner: CellLineModel
    domain_of:
    - TwoDCellCulture
    range: string
  cell_types:
    name: cell_types
    description: Cell types present in the cellular system
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: cell_types
    owner: CellLineModel
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
    owner: CellLineModel
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
    owner: CellLineModel
    domain_of:
    - CellularSystem
    range: string
  biological_organization_level:
    name: biological_organization_level
    description: The level of biological organization represented by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: biological_organization_level
    owner: CellLineModel
    domain_of:
    - NAMModel
    range: BiologicalOrganizationLevelEnum
  spatial_context:
    name: spatial_context
    description: Description of spatial organization and context captured by the model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: spatial_context
    owner: CellLineModel
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
    owner: CellLineModel
    domain_of:
    - NAMModel
    range: ComplexityLevelEnum
  references:
    name: references
    description: Literature references that describe, validate, or support this model
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: references
    owner: CellLineModel
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
    owner: CellLineModel
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
    owner: CellLineModel
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
    owner: CellLineModel
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
    owner: CellLineModel
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: CellLineModel
    domain_of:
    - NamedThing
    range: string

```
</details>