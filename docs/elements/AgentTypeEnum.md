---
search:
  boost: 2.0
---


# Enum: AgentTypeEnum 




_An enumeration of agent types responsible for generating a statement of knowledge, as defined by the Translator Knowledge Level / Agent Type (KL/AT) standard. Values distinguish human (manual) agents from automated agents (including data analysis pipelines, computational models, text-mining agents, image-processing agents) and mixed cases such as manual validation of automated output._



<div data-search-exclude markdown="1">

URI: [namo:AgentTypeEnum](https://w3id.org/monarch-initiative/namo/AgentTypeEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| manual_agent | None | A human agent who is responsible for generating a statement of knowledge ||
| automated_agent | None | An automated agent, typically a software program or tool, that is responsible... ||
| data_analysis_pipeline | None | An automated agent that executes an analysis workflow over data and reports t... | Is-A: NONE<br>|
| computational_model | None | An automated agent that generates knowledge statements (typically predictions... | Is-A: NONE<br>|
| text_mining_agent | None | An automated agent that uses Natural Language Processing to recognize concept... | Is-A: NONE<br>|
| image_processing_agent | None | An automated agent that processes images to generate textual statements of kn... | Is-A: NONE<br>|
| manual_validation_of_automated_agent | None | A human agent reviews and validates/approves the veracity of knowledge that i... ||
| not_provided | None | The agent type is not provided, typically because it cannot be determined fro... ||




## Slots

| Name | Description |
| ---  | --- |
| [agent_type](agent_type.md) | Describes the high-level category of agent who originally generated a stateme... |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: AgentTypeEnum
description: An enumeration of agent types responsible for generating a statement
  of knowledge, as defined by the Translator Knowledge Level / Agent Type (KL/AT)
  standard. Values distinguish human (manual) agents from automated agents (including
  data analysis pipelines, computational models, text-mining agents, image-processing
  agents) and mixed cases such as manual validation of automated output.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  manual_agent:
    text: manual_agent
    description: A human agent who is responsible for generating a statement of knowledge.
      The human may utilize computationally generated information as evidence for
      the resulting knowledge, but the human is the one who ultimately interprets/reasons
      with this evidence to produce a statement of knowledge.
  automated_agent:
    text: automated_agent
    description: An automated agent, typically a software program or tool, that is
      responsible for generating a statement of knowledge. Human contribution to the
      knowledge creation process ends with the definition and coding of algorithms
      or analysis pipelines that get executed by the automated agent.
  data_analysis_pipeline:
    text: data_analysis_pipeline
    description: An automated agent that executes an analysis workflow over data and
      reports the direct results of the analysis. These typically report statistical
      associations/correlations between variables in the input dataset, and do not
      interpret/infer broader conclusions from associations the analysis reveals in
      the data.
    is_a: automated_agent
    notes:
    - If an analysis pipeline includes any rules for generating broader conclusions
      based on the dataset-specific statistical correlations it calculates (e.g. create
      a 'treats' edge when the analysis reveals a drug-disease correlation in the
      data with statistical scores that meet a certain threshold) - we would consider
      this agent to be a Computational Model rather than just a Data Analysis Pipeline.
  computational_model:
    text: computational_model
    description: An automated agent that generates knowledge statements (typically
      predictions) based on rules/logic explicitly encoded in an algorithm (e.g. heuristic
      models, supervised classifiers), or learned from patterns observed in data (e.g.
      ML models, unsupervised classifiers).
    is_a: automated_agent
    notes:
    - The bar is quite low relatively for what is considered to be a ‘computational
      model’ by our definition. Even agents/tools that apply simple rules or logic
      to the output of an ingest or analysis pipeline to allow for a stronger or more
      general conclusion to be stated can qualify an agent as a model. For example,
      an ingest pipeline that applies rules to its ingest of clinical trials data
      to create a 'treats' prediction edge when the source reports a drug to be in
      phase 2 or 3 trials represents a computational model because it is automatically
      drawing a stronger conclusion than the source reports, based on logic encoded
      in the ingest pipeline. Similarly, a data analysis pipeline that is extended
      with rules to automatically generate broader conclusions based on dataset-specific
      statistical correlations (e.g. create a 'treats' edge when the analysis reveals
      a drug-disease correlation in the data with statistical scores that meet a certain
      threshold), would also qualify as a computational model by our definition.
  text_mining_agent:
    text: text_mining_agent
    description: An automated agent that uses Natural Language Processing to recognize
      concepts and/or relationships in text, and report them using formally encoded
      semantics (e.g. as an edge in a knowledge graph).
    is_a: automated_agent
    notes:
    - The original statement in the source text is typically made by a human / manual
      agent, but if a specific encoding of this knowledge is produced by a text-mining
      tool, it has an agent_type of 'text_mining_agent'. Examples of text mining agents
      include SemmedDB, and the Translator Text-Mining Knowledge Provider. Note that
      text-mining tools are prone to erroneous interpretation of concepts and relationships,
      and can fail to provide important details about the context in which the original
      knowledge was reported - so users should always consult the source text for
      a text-mined statement to assess its veracity and relevance.
  image_processing_agent:
    text: image_processing_agent
    description: An automated agent that processes images to generate textual statements
      of knowledge derived from the image and/or expressed in text the image depicts
      (e.g. via OCR).
    is_a: automated_agent
  manual_validation_of_automated_agent:
    text: manual_validation_of_automated_agent
    description: A human agent reviews and validates/approves the veracity of knowledge
      that is initially generated by an automated agent.
    notes:
    - This term applies when a human was only involved in evaluating the veracity
      of a knowledge statement that was generated by an automated agent. It is important
      to indicate when such manual review has occurred, because it can give a user
      more confidence in an automated statement.
  not_provided:
    text: not_provided
    description: The agent type is not provided, typically because it cannot be determined
      from available information if the agent that generated the knowledge is manual
      or automated.

```
</details>

</div>