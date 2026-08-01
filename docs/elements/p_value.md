---
search:
  boost: 5.0
---

# Slot: p_value 

<div data-search-exclude markdown="1">



URI: [namo:p_value](https://w3id.org/monarch-initiative/namo/p_value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gene](Gene.md) | A gene entity with identifiers and expression information |  no  |
| [StatisticalSignificance](StatisticalSignificance.md) | Statistical measures of significance for molecular comparisons |  no  |
| [EnrichmentStatistics](EnrichmentStatistics.md) | Statistical measures for pathway enrichment analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Gene](Gene.md), [StatisticalSignificance](StatisticalSignificance.md), [EnrichmentStatistics](EnrichmentStatistics.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:p_value |
| native | namo:p_value |




## LinkML Source

<details>
```yaml
name: p_value
domain_of:
- Gene
- StatisticalSignificance
- EnrichmentStatistics
range: string

```
</details></div>