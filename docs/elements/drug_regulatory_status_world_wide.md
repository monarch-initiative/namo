---
search:
  boost: 5.0
---

# Slot: drug_regulatory_status_world_wide 


_An agglomeration of drug regulatory status worldwide. Not specific to FDA._



<div data-search-exclude markdown="1">



URI: [namo:drug_regulatory_status_world_wide](https://w3id.org/monarch-initiative/namo/drug_regulatory_status_world_wide)
Alias: drug_regulatory_status_world_wide

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular ent... |  no  |
| [MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular e... |  no  |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more mol... |  no  |
| [ProcessedMaterial](ProcessedMaterial.md) | A chemical entity (often a mixture) processed for consumption for nutritional... |  no  |
| [Drug](Drug.md) | A substance intended for use in the diagnosis, cure, mitigation, treatment, o... |  no  |
| [Food](Food.md) | A substance of plant, animal, or artificial origin consumed by a living organ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ApprovalStatusEnum](ApprovalStatusEnum.md) |
| Domain Of | [ChemicalMixture](ChemicalMixture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* max phase




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:drug_regulatory_status_world_wide |
| native | namo:drug_regulatory_status_world_wide |
| exact | NCIT:C172573 |
| narrow | NCIT:R172, NCIT:regimen_has_accepted_use_for_disease, REPODB:clinically_tested_approved_unknown_phase, REPODB:clinically_tested_suspended_phase_0, REPODB:clinically_tested_suspended_phase_1, REPODB:clinically_tested_suspended_phase_1_or_phase_2, REPODB:clinically_tested_suspended_phase_2, REPODB:clinically_tested_suspended_phase_2_or_phase_3, REPODB:clinically_tested_suspended_phase_3, REPODB:clinically_tested_terminated_phase_0, REPODB:clinically_tested_terminated_phase_1, REPODB:clinically_tested_terminated_phase_1_or_phase_2, REPODB:clinically_tested_terminated_phase_2, REPODB:clinically_tested_terminated_phase_2_or_phase_3, REPODB:clinically_tested_terminated_phase_3, REPODB:clinically_tested_withdrawn_phase_0, REPODB:clinically_tested_withdrawn_phase_1, REPODB:clinically_tested_withdrawn_phase_1_or_phase_2, REPODB:clinically_tested_withdrawn_phase_2, REPODB:clinically_tested_withdrawn_phase_2_or_phase_3, REPODB:clinically_tested_withdrawn_phase_3 |




## LinkML Source

<details>
```yaml
name: drug regulatory status world wide
description: An agglomeration of drug regulatory status worldwide. Not specific to
  FDA.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- max phase
exact_mappings:
- NCIT:C172573
narrow_mappings:
- NCIT:R172
- NCIT:regimen_has_accepted_use_for_disease
- REPODB:clinically_tested_approved_unknown_phase
- REPODB:clinically_tested_suspended_phase_0
- REPODB:clinically_tested_suspended_phase_1
- REPODB:clinically_tested_suspended_phase_1_or_phase_2
- REPODB:clinically_tested_suspended_phase_2
- REPODB:clinically_tested_suspended_phase_2_or_phase_3
- REPODB:clinically_tested_suspended_phase_3
- REPODB:clinically_tested_terminated_phase_0
- REPODB:clinically_tested_terminated_phase_1
- REPODB:clinically_tested_terminated_phase_1_or_phase_2
- REPODB:clinically_tested_terminated_phase_2
- REPODB:clinically_tested_terminated_phase_2_or_phase_3
- REPODB:clinically_tested_terminated_phase_3
- REPODB:clinically_tested_withdrawn_phase_0
- REPODB:clinically_tested_withdrawn_phase_1
- REPODB:clinically_tested_withdrawn_phase_1_or_phase_2
- REPODB:clinically_tested_withdrawn_phase_2
- REPODB:clinically_tested_withdrawn_phase_2_or_phase_3
- REPODB:clinically_tested_withdrawn_phase_3
rank: 1000
alias: drug_regulatory_status_world_wide
domain_of:
- chemical mixture
range: ApprovalStatusEnum

```
</details></div>