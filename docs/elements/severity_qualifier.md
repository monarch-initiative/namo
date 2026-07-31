---
search:
  boost: 0.5
---

# Slot: severity_qualifier  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 


_a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_



<div data-search-exclude markdown="1">



URI: [namo:severity_qualifier](https://w3id.org/monarch-initiative/namo/severity_qualifier)
Alias: severity_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **severity_qualifier**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SeverityValue](SeverityValue.md) |
| Domain | [Association](Association.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:severity_qualifier |
| native | namo:severity_qualifier |




## LinkML Source

<details>
```yaml
name: severity qualifier
description: a qualifier used in a phenotypic association to state how severe the
  phenotype is in the subject
deprecated: 'true'
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
domain: association
alias: severity_qualifier
range: severity value

```
</details></div>