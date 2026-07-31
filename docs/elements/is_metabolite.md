---
search:
  boost: 5.0
---

# Slot: is_metabolite 


_indicates whether a molecular entity is a metabolite_



<div data-search-exclude markdown="1">



URI: [namo:is_metabolite](https://w3id.org/monarch-initiative/namo/is_metabolite)
Alias: is_metabolite


## Inheritance

* [node_property](node_property.md)
    * **is_metabolite**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently ... |  no  |
| [SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability i... |  no  |
| [NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain | [MolecularEntity](MolecularEntity.md) |
| Domain Of | [MolecularEntity](MolecularEntity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_metabolite |
| native | namo:is_metabolite |
| exact | CHEBI:25212 |




## LinkML Source

<details>
```yaml
name: is metabolite
description: indicates whether a molecular entity is a metabolite
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- CHEBI:25212
rank: 1000
is_a: node property
domain: molecular entity
alias: is_metabolite
domain_of:
- molecular entity
range: boolean

```
</details></div>