---
search:
  boost: 5.0
---

# Slot: treats 


_Holds between an intervention (substance, procedure, or activity) and a medical condition (disease or phenotypic feature), and states that the intervention is, in some population(s), able to ameliorate, stabilize, or cure the condition or delay, prevent, or reduce the risk of it manifesting in the first place. ‘Treats’ edges should be asserted (knowledge_level: assertion) only in cases where there is strong supporting evidence - i.e. in some population(s) the intervention is approved for the condition, passed phase 3 or in phase 4 trials for the condition, or is an otherwise established treatment in the medical community (e.g. a widely-accepted or formally recommended off-label use). In the absence of such evidence, weaker predicates should be used in asserted edges (e.g. ‘in clinical trials for’ or ‘beneficial in models of’). ‘Treats’ edges based on weaker or indirect forms of evidence can however be created as predictions (knowledge_level: prediction) and should point to the more foundational asserted edges that support them._



<div data-search-exclude markdown="1">



URI: [namo:treats](https://w3id.org/monarch-initiative/namo/treats)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)
            * **treats**







## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |
| [ameliorates_condition](ameliorates_condition.md) | Holds between an entity and an existing medical condition (disease or phenoty... | disease or phenotypic feature |  |
| [preventative_for_condition](preventative_for_condition.md) | Holds between a substance, procedure, or activity and a medical condition (di... | disease or phenotypic feature |  |



## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |
| Domain | [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |
| Mixin | Yes |








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)



## Aliases


* is substance that treats
* indicated for
* ameliorates or prevents condition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:treats |
| native | namo:treats |
| exact | DRUGBANK:treats, WIKIDATA_PROPERTY:P2175 |
| narrow | RO:0002606, NCIT:regimen_has_accepted_use_for_disease, REPODB:clinically_tested_approved_unknown_phase, REPODB:clinically_tested_suspended_phase_0, REPODB:clinically_tested_suspended_phase_1, REPODB:clinically_tested_suspended_phase_1_or_phase_2, REPODB:clinically_tested_suspended_phase_2, REPODB:clinically_tested_suspended_phase_2_or_phase_3, REPODB:clinically_tested_suspended_phase_3, REPODB:clinically_tested_terminated_phase_0, REPODB:clinically_tested_terminated_phase_1, REPODB:clinically_tested_terminated_phase_1_or_phase_2, REPODB:clinically_tested_terminated_phase_2, REPODB:clinically_tested_terminated_phase_2_or_phase_3, REPODB:clinically_tested_terminated_phase_3, REPODB:clinically_tested_withdrawn_phase_0, REPODB:clinically_tested_withdrawn_phase_1, REPODB:clinically_tested_withdrawn_phase_1_or_phase_2, REPODB:clinically_tested_withdrawn_phase_2, REPODB:clinically_tested_withdrawn_phase_2_or_phase_3, REPODB:clinically_tested_withdrawn_phase_3, SNOMED:plays_role |
| broad | DRUGBANK:treats, SEMMEDDB:TREATS, WIKIDATA_PROPERTY:P2175, MONDO:disease_responds_to |
| related | MONDO:disease_responds_to |




## LinkML Source

<details>
```yaml
name: treats
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: 'Holds between an intervention (substance, procedure, or activity) and
  a medical condition (disease or phenotypic feature), and states that the intervention
  is, in some population(s), able to ameliorate, stabilize, or cure the condition
  or delay, prevent, or reduce the risk of it manifesting in the first place. ‘Treats’
  edges should be asserted (knowledge_level: assertion) only in cases where there
  is strong supporting evidence - i.e. in some population(s) the intervention is approved
  for the condition, passed phase 3 or in phase 4 trials for the condition, or is
  an otherwise established treatment in the medical community (e.g. a widely-accepted
  or formally recommended off-label use). In the absence of such evidence, weaker
  predicates should be used in asserted edges (e.g. ‘in clinical trials for’ or ‘beneficial
  in models of’). ‘Treats’ edges based on weaker or indirect forms of evidence can
  however be created as predictions (knowledge_level: prediction) and should point
  to the more foundational asserted edges that support them.'
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- is substance that treats
- indicated for
- ameliorates or prevents condition
exact_mappings:
- DRUGBANK:treats
- WIKIDATA_PROPERTY:P2175
related_mappings:
- MONDO:disease_responds_to
narrow_mappings:
- RO:0002606
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
- SNOMED:plays_role
broad_mappings:
- DRUGBANK:treats
- SEMMEDDB:TREATS
- WIKIDATA_PROPERTY:P2175
- MONDO:disease_responds_to
rank: 1000
is_a: treats or applied or studied to treat
mixin: true
domain: chemical or drug or treatment
inherited: true
range: disease or phenotypic feature
multivalued: true

```
</details></div>