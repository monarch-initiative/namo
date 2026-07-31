---
search:
  boost: 5.0
---

# Slot: associated_environmental_context 


_An attribute that can be applied to an association where the association holds between two entities located or occurring in a particular environment. For example, two microbial taxa may interact in the context of a human gut; a disease may give rise to a particular phenotype in a particular environmental exposure._

_ # TODO: add examples of values for this property._



<div data-search-exclude markdown="1">



URI: [namo:associated_environmental_context](https://w3id.org/monarch-initiative/namo/associated_environmental_context)
Alias: associated_environmental_context


## Inheritance

* [association_slot](association_slot.md)
    * **associated_environmental_context**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | An interaction relationship between two taxa |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |
| Domain Of | [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:associated_environmental_context |
| native | namo:associated_environmental_context |




## LinkML Source

<details>
```yaml
name: associated environmental context
description: "An attribute that can be applied to an association where the association\
  \ holds between two entities located or occurring in a particular environment. For\
  \ example, two microbial taxa may interact in the context of a human gut; a disease\
  \ may give rise to a particular phenotype in a particular environmental exposure.\n\
  \ # TODO: add examples of values for this property."
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: associated_environmental_context
domain_of:
- organism taxon to organism taxon interaction
range: string

```
</details></div>