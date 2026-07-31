---
search:
  boost: 2.0
---


# Enum: ResponseTargetEnum 




_The target of a treatment or intervention_



<div data-search-exclude markdown="1">

URI: [namo:ResponseTargetEnum](https://w3id.org/monarch-initiative/namo/ResponseTargetEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| cohort | None | A group of individuals that are the target of a treatment or intervention |
| cell line | None | A cell line that is the target of a treatment or intervention |
| individual | None | An individual that is the target of a treatment or intervention |
| sample | None | A biological materialsample that is the target of a treatment or intervention |




## Slots

| Name | Description |
| ---  | --- |
| [response_target_context_qualifier](response_target_context_qualifier.md) | a biological response target (a patient, a cohort, a model system, a cell lin... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: ResponseTargetEnum
description: The target of a treatment or intervention
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  cohort:
    text: cohort
    description: A group of individuals that are the target of a treatment or intervention
  cell line:
    text: cell line
    description: A cell line that is the target of a treatment or intervention
  individual:
    text: individual
    description: An individual that is the target of a treatment or intervention
  sample:
    text: sample
    description: A biological materialsample that is the target of a treatment or
      intervention

```
</details>

</div>