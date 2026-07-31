---
search:
  boost: 5.0
---

# Slot: enrichment_statistics 


_Statistical measures of pathway enrichment._



<div data-search-exclude markdown="1">



URI: [namo:enrichment_statistics](https://w3id.org/monarch-initiative/namo/enrichment_statistics)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PathwayConcordance](PathwayConcordance.md) | Assessment of biological pathway conservation and activity between model and ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EnrichmentStatistics](EnrichmentStatistics.md) |
| Domain Of | [PathwayConcordance](PathwayConcordance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PathwayConcordance](PathwayConcordance.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:enrichment_statistics |
| native | namo:enrichment_statistics |




## LinkML Source

<details>
```yaml
name: enrichment_statistics
description: Statistical measures of pathway enrichment.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: PathwayConcordance
domain_of:
- PathwayConcordance
range: EnrichmentStatistics
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>