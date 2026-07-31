---
search:
  boost: 5.0
---

# Slot: contraindicated_in 


_Holds between a substance, procedure, or activity and a medical condition or circumstance, where an authority has established that the substance, procedure, or activity should not be applied as an intervention in patients with the condition or circumstance because it can result in detrimental outcomes._



<div data-search-exclude markdown="1">



URI: [namo:contraindicated_in](https://w3id.org/monarch-initiative/namo/contraindicated_in)
Alias: contraindicated_in


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **contraindicated_in**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalEntity](BiologicalEntity.md) |
| Domain | [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |










## Notes

* This predicate relates the intervention with a specific disease, phenotype, or other medical circumstance that puts patients at high risk for detrimental outcomes.  This may be a different condition from the one that the drug would be used to treat (e.g. pseudoephedrine is contraindicated in people with high-blood pressure as a treatment for nasal congestion), a biological state (e.g. isotretinoin is contraindicated in people who are pregnant as a treatment for acne), or being on a different medication (e.g. aspirin is contraindicated in people taking warfarin as a preventative treatment for stroke).



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| opposite_of | treats |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:contraindicated_in |
| native | namo:contraindicated_in |
| exact | NCIT:C37933 |




## LinkML Source

<details>
```yaml
name: contraindicated in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: treats
description: Holds between a substance, procedure, or activity and a medical condition
  or circumstance, where an authority has established that the substance, procedure,
  or activity should not be applied as an intervention in patients with the condition
  or circumstance because it can result in detrimental outcomes.
notes:
- This predicate relates the intervention with a specific disease, phenotype, or other
  medical circumstance that puts patients at high risk for detrimental outcomes.  This
  may be a different condition from the one that the drug would be used to treat (e.g.
  pseudoephedrine is contraindicated in people with high-blood pressure as a treatment
  for nasal congestion), a biological state (e.g. isotretinoin is contraindicated
  in people who are pregnant as a treatment for acne), or being on a different medication
  (e.g. aspirin is contraindicated in people taking warfarin as a preventative treatment
  for stroke).
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- NCIT:C37933
rank: 1000
is_a: related to at instance level
domain: chemical or drug or treatment
inherited: true
alias: contraindicated_in
range: biological entity
multivalued: true

```
</details></div>