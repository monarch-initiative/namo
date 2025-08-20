# Enum: MLAlgorithmEnum 



URI: [namo:MLAlgorithmEnum](https://w3id.org/monarch-initiative/namo/MLAlgorithmEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| RANDOM_FOREST | None | Random Forest algorithm |
| SUPPORT_VECTOR_MACHINE | OBI:0000700 | Support Vector Machine |
| NEURAL_NETWORK | None | Artificial Neural Networks |
| DEEP_LEARNING | None | Deep learning models |
| GRADIENT_BOOSTING | MESH:D000098404 | Gradient boosting methods |
| LINEAR_REGRESSION | OBI:0200103 | Linear regression models |
| LOGISTIC_REGRESSION | OBI:0200002 | Logistic regression models |
| NAIVE_BAYES | None | Naive Bayes classifier |
| K_MEANS | OBI:0200041 | K-means clustering |
| REINFORCEMENT_LEARNING | None | Reinforcement learning approaches |




## Slots

| Name | Description |
| ---  | --- |
| [ml_algorithm](ml_algorithm.md) | Type of machine learning algorithm used |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: MLAlgorithmEnum
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  RANDOM_FOREST:
    text: RANDOM_FOREST
    description: Random Forest algorithm
  SUPPORT_VECTOR_MACHINE:
    text: SUPPORT_VECTOR_MACHINE
    description: Support Vector Machine
    meaning: OBI:0000700
  NEURAL_NETWORK:
    text: NEURAL_NETWORK
    description: Artificial Neural Networks
  DEEP_LEARNING:
    text: DEEP_LEARNING
    description: Deep learning models
  GRADIENT_BOOSTING:
    text: GRADIENT_BOOSTING
    description: Gradient boosting methods
    meaning: MESH:D000098404
  LINEAR_REGRESSION:
    text: LINEAR_REGRESSION
    description: Linear regression models
    meaning: OBI:0200103
  LOGISTIC_REGRESSION:
    text: LOGISTIC_REGRESSION
    description: Logistic regression models
    meaning: OBI:0200002
  NAIVE_BAYES:
    text: NAIVE_BAYES
    description: Naive Bayes classifier
  K_MEANS:
    text: K_MEANS
    description: K-means clustering
    meaning: OBI:0200041
  REINFORCEMENT_LEARNING:
    text: REINFORCEMENT_LEARNING
    description: Reinforcement learning approaches

```
</details>