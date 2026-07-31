---
search:
  boost: 5.0
---

# Slot: subclass_of 


_holds between two classes where the domain class is a specialization of the range class_



<div data-search-exclude markdown="1">



URI: [namo:subclass_of](https://w3id.org/monarch-initiative/namo/subclass_of)
Alias: subclass_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **subclass_of**








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








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






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
| self | namo:subclass_of |
| native | namo:subclass_of |
| exact | rdfs:subClassOf, SEMMEDDB:ISA, WIKIDATA_PROPERTY:P279, CHEMBL.MECHANISM:subset_of, GO:isa, MESH:isa, RXNORM:isa, VANDF:isa |
| narrow | CHEBI:has_parent_hydride, LOINC:has_archetype, LOINC:has_parent_group, LOINC:is_presence_guidance_for, NCIT:gene_product_has_chemical_classification, NCIT:R36, NCIT:R42, NCIT:A16, NCIT:A11, NCIT:A14, NCIT:A3, NDDF:has_dose_form, RXNORM:has_dose_form, RXNORM:has_doseformgroup, SNOMED:entire_anatomy_structure_of, SNOMED:has_dose_form, rdfs:subPropertyOf |
| close | LOINC:class_of, LOINC:has_class |




## LinkML Source

<details>
```yaml
name: subclass of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two classes where the domain class is a specialization
  of the range class
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- rdfs:subClassOf
- SEMMEDDB:ISA
- WIKIDATA_PROPERTY:P279
- CHEMBL.MECHANISM:subset_of
- GO:isa
- MESH:isa
- RXNORM:isa
- VANDF:isa
close_mappings:
- LOINC:class_of
- LOINC:has_class
narrow_mappings:
- CHEBI:has_parent_hydride
- LOINC:has_archetype
- LOINC:has_parent_group
- LOINC:is_presence_guidance_for
- NCIT:gene_product_has_chemical_classification
- NCIT:R36
- NCIT:R42
- NCIT:A16
- NCIT:A11
- NCIT:A14
- NCIT:A3
- NDDF:has_dose_form
- RXNORM:has_dose_form
- RXNORM:has_doseformgroup
- SNOMED:entire_anatomy_structure_of
- SNOMED:has_dose_form
- rdfs:subPropertyOf
rank: 1000
is_a: related to at concept level
domain: ontology class
inherited: true
alias: subclass_of
range: ontology class
multivalued: true

```
</details></div>