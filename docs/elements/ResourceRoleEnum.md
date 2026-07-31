---
search:
  boost: 2.0
---


# Enum: ResourceRoleEnum 




_The role played by the information reource in serving as a source for an edge in a TRAPI message. Note that a given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting data' sources.  This enumeration is found in Biolink Model, but is repeated here for convenience._



<div data-search-exclude markdown="1">

URI: [namo:ResourceRoleEnum](https://w3id.org/monarch-initiative/namo/ResourceRoleEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| primary_knowledge_source | None |  |
| aggregator_knowledge_source | None |  |
| supporting_data_source | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [resource_role](resource_role.md) | The role played by the InformationResource in serving as a source for an Edge |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: ResourceRoleEnum
description: The role played by the information reource in serving as a source for
  an edge in a TRAPI message. Note that a given Edge should have one and only one
  'primary' source, and may have any number of 'aggregator' or 'supporting data' sources.  This
  enumeration is found in Biolink Model, but is repeated here for convenience.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  primary_knowledge_source:
    text: primary_knowledge_source
  aggregator_knowledge_source:
    text: aggregator_knowledge_source
  supporting_data_source:
    text: supporting_data_source

```
</details>

</div>