---
search:
  boost: 5.0
---

# Slot: intact_confidence_value 


_A score defined by MI / IntAct that represents the degree of confidence in the existence of a particular interaction by assessing the annotation of that specific interaction in a standards-compliant dataset. The score given to an interaction will increase as the number of experimental evidences supporting that interaction increases. Experimental evidences contribute more highly to the final score than evidences derived by predictive algorithms or literature text-mining methods. Range is 0-1, with higher scores indicated more confidence. See here for details: https://www.ebi.ac.uk/intact/documentation/user-guide#interaction_scoring._



<div data-search-exclude markdown="1">



URI: [namo:intact_confidence_value](https://w3id.org/monarch-initiative/namo/intact_confidence_value)
Alias: intact_confidence_value

<!-- no inheritance hierarchy -->







## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* intact miscore
* intact interaction score




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:intact_confidence_value |
| native | namo:intact_confidence_value |




## LinkML Source

<details>
```yaml
name: intact confidence value
description: 'A score defined by MI / IntAct that represents the degree of confidence
  in the existence of a particular interaction by assessing the annotation of that
  specific interaction in a standards-compliant dataset. The score given to an interaction
  will increase as the number of experimental evidences supporting that interaction
  increases. Experimental evidences contribute more highly to the final score than
  evidences derived by predictive algorithms or literature text-mining methods. Range
  is 0-1, with higher scores indicated more confidence. See here for details: https://www.ebi.ac.uk/intact/documentation/user-guide#interaction_scoring.'
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- intact miscore
- intact interaction score
rank: 1000
alias: intact_confidence_value
range: string

```
</details></div>