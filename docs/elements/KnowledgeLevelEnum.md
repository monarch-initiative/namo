---
search:
  boost: 2.0
---


# Enum: KnowledgeLevelEnum 




_An enumeration characterizing the type of knowledge expressed in a statement and the kind of evidence and reasoning that supports it, as defined by the Translator Knowledge Level / Agent Type (KL/AT) standard. Values include knowledge assertion, logical entailment, prediction, statistical association, text co-occurrence, direct observation, and not-provided._



<div data-search-exclude markdown="1">

URI: [namo:KnowledgeLevelEnum](https://w3id.org/monarch-initiative/namo/KnowledgeLevelEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| knowledge_assertion | None | A statement of purported fact that is put forth by an agent as true, based on... |
| logical_entailment | None | A statement reporting a conclusion that follows logically from premises repre... |
| prediction | None | A statement of a possible fact based on probabilistic forms of reasoning over... |
| statistical_association | None | A statement that reports concepts representing variables in a dataset to be s... |
| text_co_occurrence | None | A statement reporting that mentions of two concepts in some corpus of text (e |
| observation | None | A statement reporting (and possibly quantifying) a phenomenon that was observ... |
| not_provided | None | The knowledge level is not provided, typically because it cannot be determine... |




## Slots

| Name | Description |
| ---  | --- |
| [knowledge_level](knowledge_level.md) | Describes the level of knowledge expressed in a statement, based on the reaso... |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: KnowledgeLevelEnum
description: An enumeration characterizing the type of knowledge expressed in a statement
  and the kind of evidence and reasoning that supports it, as defined by the Translator
  Knowledge Level / Agent Type (KL/AT) standard. Values include knowledge assertion,
  logical entailment, prediction, statistical association, text co-occurrence, direct
  observation, and not-provided.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  knowledge_assertion:
    text: knowledge_assertion
    description: A statement of purported fact that is put forth by an agent as true,
      based on assessment of direct evidence. Assertions are likely but not definitively
      true.
    notes:
    - Knowledge Assertions are supported by direct evidence deemed sufficient by some
      agent to support a confidence assertion of truth. Our certainty in this truth
      is not absolute, but is typically higher than for Predictions.
    aliases:
    - assertion
  logical_entailment:
    text: logical_entailment
    description: A statement reporting a conclusion that follows logically from premises
      representing established facts or knowledge assertions (e.g. fingernail part
      of finger, finger part of hand --> fingernail part of hand).
    notes:
    - These statements report entailed conclusions derived through dedictive inference.
      They are not directly asserted by a source, but logically follow from statement(s)
      a source does make - and are necessarily true if their supporting premises are
      true. In practice, these will primarily be entailments based on logic encoded
      in ontologies. Examples include propagation of annotated knowledge to hierarchically-related
      concepts, across paths through a graph constructed from transitive relationships,
      or sets of relationships that support property chain inference.
    aliases:
    - deductive_inference
  prediction:
    text: prediction
    description: A statement of a possible fact based on probabilistic forms of reasoning
      over more indirect forms of evidence, that lead to more speculative conclusions.
    notes:
    - Predictions typically result from non-deductive forms of reasoning - e.g. inductive
      and deductive inference, or statistical inference where conclusions are drawn
      about a broader/global population based on data from a representative cohort.
      For example, a prediction that a drug may treat a particular disease based on
      its chemical similarity to known drugs that treat the disease, and the fact
      that it can inhibit proteins in a pathway that is associated with the disease
      As Predictions are based on weaker forms of inference and evidence, they are
      typically considered lower confidence statements as compared to Knowledge Assertions
      and Logical Entailments.
    aliases:
    - hypothesis
  statistical_association:
    text: statistical_association
    description: A statement that reports concepts representing variables in a dataset
      to be statistically associated with each other in a particular cohort (e.g.
      'Metformin Treatment (variable 1) is correlated with Diabetes Diagnosis (variable
      2) in EHR dataset X').
    notes:
    - Such statements report the direct results of some statistical analysis. Their
      scope is limited tp the cohort/dataset interrogated in the analysis, and they
      do not make broader claims or draw more meaningful conclusions about the domain
      of discourse. Note however that such Statistical Associations can be used as
      evidence to support a more pointed/precise Prediction or Assertion of knowledge.
      For example, e.g. a Statistical Association between 'Metformin Prescription'
      and 'Diabetes Diagnosis' in EHR records could support a Prediction that 'Metformin
      treats Diabetes', or 'Metformin causes Diabetes'. This 'treats' edge may have
      a knowledge_level of 'Prediction', but the provider could use the 'evidence_type'
      edge property to indicate that this prediction is based on a 'Statistical Association'.
      Because Statistical Associations directly report analysis-specific results,
      we can consider them to be inherently true statements, whose broader utility
      is dependent on subsequent generalization of the reported result to a broader
      population, and/or interpretation of the result as support for a more meaningful
      statements about the domain of discourse.
  text_co_occurrence:
    text: text_co_occurrence
    description: A statement reporting that mentions of two concepts in some corpus
      of text (e.g. the biomedical literature) occur together at a statistically significant
      frequency - suggesting that a real-world biological or clinical relationship
      may exist between the concepts.
    notes:
    - Such statements often utilize NLP/text-mining to identify concept mentions in
      text, but the reported statement is generated by a data analysis pipeline that
      performs calculations on mention counts and determines the strength of their
      correlation.
  observation:
    text: observation
    description: A statement reporting (and possibly quantifying) a phenomenon that
      was observed to occur - absent any analysis or interpretation that generates
      a statistical association or supports a broader conclusion or inference.
    notes:
    - An observation that "56362 people self-reported taking melatonin to treat migraines"
      is agnostic to whether melatonin is an effective or approved treatment - it
      only claims that it was taken for this purpose. Such observations, however,
      may be used as the basis for predicting that a drug may be efficacious against
      a disease.
  not_provided:
    text: not_provided
    description: The knowledge level is not provided, typically because it cannot
      be determined from available. information.
    notes:
    - This term is most often applied for text-mined edges, as NLP tools are typically
      not able to detect a specific knowledge level for the concept relationships
      they extract (e.g. whether the author was predicting or asserting a relationship,
      or merely observed it to occur).

```
</details>

</div>