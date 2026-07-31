---
search:
  boost: 10.0
---

# Class: CellTypeProportion 


_Quantitative comparison of cell type proportions between systems._



<div data-search-exclude markdown="1">



URI: [namo:CellTypeProportion](https://w3id.org/monarch-initiative/namo/CellTypeProportion)





```mermaid
 classDiagram
    class CellTypeProportion
    click CellTypeProportion href "../CellTypeProportion/"
      CellTypeProportion : biological_proportion
        
      CellTypeProportion : cell_type
        
          
    
        
        
        CellTypeProportion --> "0..1" Cell : cell_type
        click Cell href "../Cell/"
    

        
      CellTypeProportion : model_proportion
        
      CellTypeProportion : proportion_ratio
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cell_type](cell_type.md) | 0..1 <br/> [Cell](Cell.md) | The cell type being compared | direct |
| [model_proportion](model_proportion.md) | 0..1 <br/> [Float](Float.md) | Proportion of this cell type in the model system | direct |
| [biological_proportion](biological_proportion.md) | 0..1 <br/> [Float](Float.md) | Proportion of this cell type in the biological system | direct |
| [proportion_ratio](proportion_ratio.md) | 0..1 <br/> [Float](Float.md) | Ratio of model to biological proportions | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CellTypeCoverage](CellTypeCoverage.md) | [cell_type_proportions](cell_type_proportions.md) | range | [CellTypeProportion](CellTypeProportion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:CellTypeProportion |
| native | namo:CellTypeProportion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellTypeProportion
description: Quantitative comparison of cell type proportions between systems.
from_schema: https://w3id.org/monarch-initiative/namo
attributes:
  cell_type:
    name: cell_type
    description: The cell type being compared.
    from_schema: https://w3id.org/monarch-initiative/namo
    domain_of:
    - CellRatio
    - CellTypeProportion
    range: cell
    bindings:
    - range: CellTypeEnum
      obligation_level: REQUIRED
      binds_value_of: id
    inlined: true
  model_proportion:
    name: model_proportion
    description: Proportion of this cell type in the model system.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CellTypeProportion
    range: float
  biological_proportion:
    name: biological_proportion
    description: Proportion of this cell type in the biological system.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CellTypeProportion
    range: float
  proportion_ratio:
    name: proportion_ratio
    description: Ratio of model to biological proportions.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CellTypeProportion
    range: float

```
</details>

### Induced

<details>
```yaml
name: CellTypeProportion
description: Quantitative comparison of cell type proportions between systems.
from_schema: https://w3id.org/monarch-initiative/namo
attributes:
  cell_type:
    name: cell_type
    description: The cell type being compared.
    from_schema: https://w3id.org/monarch-initiative/namo
    owner: CellTypeProportion
    domain_of:
    - CellRatio
    - CellTypeProportion
    range: cell
    bindings:
    - range: CellTypeEnum
      obligation_level: REQUIRED
      binds_value_of: id
    inlined: true
  model_proportion:
    name: model_proportion
    description: Proportion of this cell type in the model system.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    owner: CellTypeProportion
    domain_of:
    - CellTypeProportion
    range: float
  biological_proportion:
    name: biological_proportion
    description: Proportion of this cell type in the biological system.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    owner: CellTypeProportion
    domain_of:
    - CellTypeProportion
    range: float
  proportion_ratio:
    name: proportion_ratio
    description: Ratio of model to biological proportions.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    owner: CellTypeProportion
    domain_of:
    - CellTypeProportion
    range: float

```
</details></div>