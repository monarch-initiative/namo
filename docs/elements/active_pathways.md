---
search:
  boost: 5.0
---

# Slot: active_pathways 


_List of biological pathways that are active in both systems._



<div data-search-exclude markdown="1">



URI: [namo:active_pathways](https://w3id.org/monarch-initiative/namo/active_pathways)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PathwayConcordance](PathwayConcordance.md) | Assessment of biological pathway conservation and activity between model and ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PathwayActivityResult](PathwayActivityResult.md) |
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
| self | namo:active_pathways |
| native | namo:active_pathways |




## LinkML Source

<details>
```yaml
name: active_pathways
description: List of biological pathways that are active in both systems.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: PathwayConcordance
domain_of:
- PathwayConcordance
range: PathwayActivityResult
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>