# Enum: CrossValidationMethodEnum 



URI: [namo:CrossValidationMethodEnum](https://w3id.org/monarch-initiative/namo/CrossValidationMethodEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| K_FOLD | OBI:0200032 | K-fold cross-validation |
| STRATIFIED_K_FOLD | None | Stratified k-fold cross-validation |
| LEAVE_ONE_OUT | OBI:0200033 | Leave-one-out cross-validation |
| TIME_SERIES_SPLIT | None | Time series cross-validation |
| MONTE_CARLO | None | Monte Carlo cross-validation |




## Slots

| Name | Description |
| ---  | --- |
| [cv_method](cv_method.md) | Type of cross-validation used |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: CrossValidationMethodEnum
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  K_FOLD:
    text: K_FOLD
    description: K-fold cross-validation
    meaning: OBI:0200032
  STRATIFIED_K_FOLD:
    text: STRATIFIED_K_FOLD
    description: Stratified k-fold cross-validation
  LEAVE_ONE_OUT:
    text: LEAVE_ONE_OUT
    description: Leave-one-out cross-validation
    meaning: OBI:0200033
  TIME_SERIES_SPLIT:
    text: TIME_SERIES_SPLIT
    description: Time series cross-validation
  MONTE_CARLO:
    text: MONTE_CARLO
    description: Monte Carlo cross-validation

```
</details>