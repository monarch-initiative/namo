---
search:
  boost: 10.0
---

# Class: CellRatio 


_Ratio specification for different cell types in co-culture systems._



<div data-search-exclude markdown="1">



URI: [namo:CellRatio](https://w3id.org/monarch-initiative/namo/CellRatio)





```mermaid
 classDiagram
    class CellRatio
    click CellRatio href "../CellRatio/"
      CellRatio : cell_type
        
          
    
        
        
        CellRatio --> "0..1" Cell : cell_type
        click Cell href "../Cell/"
    

        
      CellRatio : ratio
        
      CellRatio : ratio_type
        
          
    
        
        
        CellRatio --> "0..1" RatioTypeEnum : ratio_type
        click RatioTypeEnum href "../RatioTypeEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cell_type](cell_type.md) | 0..1 <br/> [Cell](Cell.md) | The cell type for which the ratio is specified | direct |
| [ratio](ratio.md) | 0..1 <br/> [Float](Float.md) | Proportion or ratio of this cell type (0 | direct |
| [ratio_type](ratio_type.md) | 0..1 <br/> [RatioTypeEnum](RatioTypeEnum.md) | Type of ratio specification (percentage, absolute, fold) | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CoCulture](CoCulture.md) | [cell_ratios](cell_ratios.md) | range | [CellRatio](CellRatio.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:CellRatio |
| native | namo:CellRatio |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellRatio
description: Ratio specification for different cell types in co-culture systems.
from_schema: https://w3id.org/monarch-initiative/namo
attributes:
  cell_type:
    name: cell_type
    description: The cell type for which the ratio is specified
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CellRatio
    - CellTypeProportion
    range: Cell
    bindings:
    - range: CellTypeEnum
      obligation_level: REQUIRED
      binds_value_of: id
    inlined: true
  ratio:
    name: ratio
    description: Proportion or ratio of this cell type (0.0-1.0 or absolute numbers)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CellRatio
    range: float
  ratio_type:
    name: ratio_type
    description: Type of ratio specification (percentage, absolute, fold)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - CellRatio
    range: RatioTypeEnum

```
</details>

### Induced

<details>
```yaml
name: CellRatio
description: Ratio specification for different cell types in co-culture systems.
from_schema: https://w3id.org/monarch-initiative/namo
attributes:
  cell_type:
    name: cell_type
    description: The cell type for which the ratio is specified
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    owner: CellRatio
    domain_of:
    - CellRatio
    - CellTypeProportion
    range: Cell
    bindings:
    - range: CellTypeEnum
      obligation_level: REQUIRED
      binds_value_of: id
    inlined: true
  ratio:
    name: ratio
    description: Proportion or ratio of this cell type (0.0-1.0 or absolute numbers)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    owner: CellRatio
    domain_of:
    - CellRatio
    range: float
  ratio_type:
    name: ratio_type
    description: Type of ratio specification (percentage, absolute, fold)
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    owner: CellRatio
    domain_of:
    - CellRatio
    range: RatioTypeEnum

```
</details></div>