---
search:
  boost: 5.0
---

# Slot: cell_types 

<div data-search-exclude markdown="1">



URI: [namo:cell_types](https://w3id.org/monarch-initiative/namo/cell_types)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CellularSystem](CellularSystem.md) | Cell-based model systems that use living cells to model biological processes |  no  |
| [TwoDCellCulture](TwoDCellCulture.md) | Conventional monolayer cell cultures grown on flat surfaces |  no  |
| [ThreeDCellCulture](ThreeDCellCulture.md) | Three-dimensional cell culture systems including spheroids and organoids |  no  |
| [CoCulture](CoCulture.md) | Co-culture systems combining multiple cell types to mimic  microenvironments ... |  no  |
| [Organoid](Organoid.md) | A 3D cell culture system that self-organizes to recapitulate key structural a... |  no  |
| [CellLineModel](CellLineModel.md) | A model system based on immortalized cell lines that can be maintained in cul... |  no  |
| [OrganOnChip](OrganOnChip.md) | A model system that simulates the physiological functions of an organ using a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CellularSystem](CellularSystem.md), [OrganOnChip](OrganOnChip.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:cell_types |
| native | namo:cell_types |




## LinkML Source

<details>
```yaml
name: cell_types
domain_of:
- CellularSystem
- OrganOnChip
range: string

```
</details></div>