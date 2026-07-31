---
search:
  boost: 5.0
---

# Slot: superclass_of 


_holds between two classes where the domain class is a super class of the range class_



<div data-search-exclude markdown="1">



URI: [namo:superclass_of](https://w3id.org/monarch-initiative/namo/superclass_of)
Alias: superclass_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **superclass_of**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OntologyClass](OntologyClass.md) |
| Domain | [OntologyClass](OntologyClass.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [subclass_of](subclass_of.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:superclass_of |
| native | namo:superclass_of |
| exact | WIKIDATA:Q66088480, CHEMBL.MECHANISM:superset_of, GO:inverse_isa, RXNORM:inverse_isa, MESH:inverse_isa, VANDF:inverse_isa |
| narrow | NCIT:cdrh_parent_of, NCIT:ctcae_5_parent_of, NCIT:subset_includes_concept, OMIM:has_manifestation, SNOMED:has_basic_dose_form, UMLS:RB |




## LinkML Source

<details>
```yaml
name: superclass of
description: holds between two classes where the domain class is a super class of
  the range class
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- WIKIDATA:Q66088480
- CHEMBL.MECHANISM:superset_of
- GO:inverse_isa
- RXNORM:inverse_isa
- MESH:inverse_isa
- VANDF:inverse_isa
narrow_mappings:
- NCIT:cdrh_parent_of
- NCIT:ctcae_5_parent_of
- NCIT:subset_includes_concept
- OMIM:has_manifestation
- SNOMED:has_basic_dose_form
- UMLS:RB
rank: 1000
is_a: related to at concept level
domain: ontology class
inherited: true
alias: superclass_of
inverse: subclass of
range: ontology class
multivalued: true

```
</details></div>