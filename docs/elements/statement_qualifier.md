---
search:
  boost: 5.0
---

# Slot: statement_qualifier 


_A property that qualifies the entirety of the statement made in an association.  It applies to both a fully qualified subject and a fully qualified object as well as the predicate and qualified predicate in an association._



<div data-search-exclude markdown="1">



URI: [namo:statement_qualifier](https://w3id.org/monarch-initiative/namo/statement_qualifier)
Alias: statement_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **statement_qualifier**
            * [causal_mechanism_qualifier](causal_mechanism_qualifier.md)
            * [anatomical_context_qualifier](anatomical_context_qualifier.md)
            * [species_context_qualifier](species_context_qualifier.md)
            * [stage_qualifier](stage_qualifier.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | namo:statement_qualifier |
| native | namo:statement_qualifier |




## LinkML Source

<details>
```yaml
name: statement qualifier
description: A property that qualifies the entirety of the statement made in an association.  It
  applies to both a fully qualified subject and a fully qualified object as well as
  the predicate and qualified predicate in an association.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
domain: association
alias: statement_qualifier
range: string

```
</details></div>