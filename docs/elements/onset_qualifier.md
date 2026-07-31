---
search:
  boost: 5.0
---

# Slot: onset_qualifier 


_a qualifier used in a phenotypic association to state when the phenotype appears is in the subject._



<div data-search-exclude markdown="1">



URI: [namo:onset_qualifier](https://w3id.org/monarch-initiative/namo/onset_qualifier)
Alias: onset_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **onset_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenot... |  no  |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e |  no  |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | An association between a Case (patient) and a Disease |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Onset](Onset.md) |
| Domain | [Association](Association.md) |
| Domain Of | [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md), [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md), [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)




## Notes

* This  is in Biolink to support HP ontology annotations which use "onset" (with terms from HP) as an annotation on a disease to phenotypic feature association.  Please only use it for this purpose.  If the intent is to describe the onset of a disease in the context of a treatment, use object_aspect_qualifier and object_direction_qualifier to capture "delayed onset" or "exacerbated onset" slot.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:onset_qualifier |
| native | namo:onset_qualifier |




## LinkML Source

<details>
```yaml
name: onset qualifier
description: a qualifier used in a phenotypic association to state when the phenotype
  appears is in the subject.
notes:
- This  is in Biolink to support HP ontology annotations which use "onset" (with terms
  from HP) as an annotation on a disease to phenotypic feature association.  Please
  only use it for this purpose.  If the intent is to describe the onset of a disease
  in the context of a treatment, use object_aspect_qualifier and object_direction_qualifier
  to capture "delayed onset" or "exacerbated onset" slot.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: qualifier
domain: association
alias: onset_qualifier
domain_of:
- disease to phenotypic feature association
- case to phenotypic feature association
- case to disease association
range: onset

```
</details></div>