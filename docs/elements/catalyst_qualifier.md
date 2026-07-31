---
search:
  boost: 5.0
---

# Slot: catalyst_qualifier 


_a qualifier that connects an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change._



<div data-search-exclude markdown="1">



URI: [namo:catalyst_qualifier](https://w3id.org/monarch-initiative/namo/catalyst_qualifier)
Alias: catalyst_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * **catalyst_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | A causal relationship between two chemical entities, where the subject repres... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| Domain | [Association](Association.md) |
| Domain Of | [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:catalyst_qualifier |
| native | namo:catalyst_qualifier |




## LinkML Source

<details>
```yaml
name: catalyst qualifier
description: a qualifier that connects an association between two causally connected
  entities (for example, two chemical entities, or a chemical entity in that changes
  location) and the gene product, gene, or complex that enables or catalyzes the change.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: catalyst_qualifier
domain_of:
- chemical entity to chemical derivation association
range: macromolecular machine mixin
multivalued: true

```
</details></div>