# Enum: InterpretabilityLevelEnum 



URI: [namo:InterpretabilityLevelEnum](https://w3id.org/monarch-initiative/namo/InterpretabilityLevelEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| BLACK_BOX | None | No interpretability - predictions only |
| INTERPRETABLE | None | Some level of feature importance available |
| EXPLAINABLE | None | Full mechanistic interpretation possible |
| CAUSAL | None | Causal relationships can be inferred |




## Slots

| Name | Description |
| ---  | --- |
| [model_interpretability](model_interpretability.md) | Level of model interpretability (black box, interpretable, explainable) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: InterpretabilityLevelEnum
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  BLACK_BOX:
    text: BLACK_BOX
    description: No interpretability - predictions only
  INTERPRETABLE:
    text: INTERPRETABLE
    description: Some level of feature importance available
  EXPLAINABLE:
    text: EXPLAINABLE
    description: Full mechanistic interpretation possible
  CAUSAL:
    text: CAUSAL
    description: Causal relationships can be inferred

```
</details>