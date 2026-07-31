---
search:
  boost: 5.0
---

# Slot: association_slot 


_any slot that relates an association to another entity_



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:association_slot](https://w3id.org/monarch-initiative/namo/association_slot)
Alias: association_slot


## Inheritance

* **association_slot**
    * [stoichiometry](stoichiometry.md)
    * [reaction_direction](reaction_direction.md)
    * [reaction_balanced](reaction_balanced.md)
    * [reaction_side](reaction_side.md)
    * [semmed_agreement_count](semmed_agreement_count.md)
    * [support_graphs](support_graphs.md)
    * [has_affinity](has_affinity.md)
    * [FDA_adverse_event_level](FDA_adverse_event_level.md)
    * [qualifiers](qualifiers.md)
    * [clinical_modifier_qualifier](clinical_modifier_qualifier.md)
    * [sequence_variant_qualifier](sequence_variant_qualifier.md)
    * [quantifier_qualifier](quantifier_qualifier.md)
    * [catalyst_qualifier](catalyst_qualifier.md)
    * [qualifier](qualifier.md)
    * [original_subject](original_subject.md)
    * [original_object](original_object.md)
    * [original_predicate](original_predicate.md)
    * [subject_feature_name](subject_feature_name.md)
    * [object_feature_name](object_feature_name.md)
    * [subject_closure](subject_closure.md)
    * [object_closure](object_closure.md)
    * [subject_category](subject_category.md)
    * [object_category](object_category.md)
    * [subject_category_closure](subject_category_closure.md)
    * [object_category_closure](object_category_closure.md)
    * [subject_label_closure](subject_label_closure.md)
    * [object_label_closure](object_label_closure.md)
    * [subject_namespace](subject_namespace.md)
    * [object_namespace](object_namespace.md)
    * [subject](subject.md)
    * [object](object.md)
    * [predicate](predicate.md)
    * [logical_interpretation](logical_interpretation.md)
    * [negated](negated.md)
    * [has_confidence_level](has_confidence_level.md)
    * [has_confidence_score](has_confidence_score.md)
    * [has_evidence_of_type](has_evidence_of_type.md)
    * [has_evidence](has_evidence.md)
    * [has_study_results](has_study_results.md)
    * [log_odds_ratio](log_odds_ratio.md)
    * [log_odds_ratio_95_ci](log_odds_ratio_95_ci.md)
    * [mechanism_of_action](mechanism_of_action.md)
    * [knowledge_source](knowledge_source.md)
    * [supporting_data_source](supporting_data_source.md)
    * [supporting_data_set](supporting_data_set.md)
    * [chi_squared_statistic](chi_squared_statistic.md)
    * [chi_squared_dof](chi_squared_dof.md)
    * [chi_squared_p](chi_squared_p.md)
    * [fisher_exact_odds_ratio](fisher_exact_odds_ratio.md)
    * [fisher_exact_p](fisher_exact_p.md)
    * [z_score](z_score.md)
    * [p_value](p_value.md)
    * [evidence_count](evidence_count.md)
    * [dataset_count](dataset_count.md)
    * [concept_count_subject](concept_count_subject.md)
    * [concept_count_object](concept_count_object.md)
    * [concept_pair_count](concept_pair_count.md)
    * [expected_count](expected_count.md)
    * [relative_frequency_subject](relative_frequency_subject.md)
    * [relative_frequency_object](relative_frequency_object.md)
    * [relative_frequency_subject_confidence_interval](relative_frequency_subject_confidence_interval.md)
    * [relative_frequency_object_confidence_interval](relative_frequency_object_confidence_interval.md)
    * [supporting_text](supporting_text.md)
    * [supporting_documents](supporting_documents.md)
    * [subject_location_in_text](subject_location_in_text.md)
    * [object_location_in_text](object_location_in_text.md)
    * [extraction_confidence_score](extraction_confidence_score.md)
    * [supporting_document_type](supporting_document_type.md)
    * [supporting_document_year](supporting_document_year.md)
    * [supporting_text_section_type](supporting_text_section_type.md)
    * [ln_ratio](ln_ratio.md)
    * [ln_ratio_confidence_interval](ln_ratio_confidence_interval.md)
    * [interacting_molecules_category](interacting_molecules_category.md)
    * [expression_site](expression_site.md)
    * [phenotypic_state](phenotypic_state.md)
    * [allelic_requirement](allelic_requirement.md)
    * [publications](publications.md)
    * [sources](sources.md)
    * [associated_environmental_context](associated_environmental_context.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
    * [clinical_approval_status](clinical_approval_status.md)
    * [max_research_phase](max_research_phase.md)
    * [has_supporting_studies](has_supporting_studies.md)
    * [supporting_study_metadata](supporting_study_metadata.md)
    * [knowledge_level](knowledge_level.md)
    * [agent_type](agent_type.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* edge property
* statement property
* node qualifier
* edge qualifier
* statement qualifier




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:association_slot |
| native | namo:association_slot |




## LinkML Source

<details>
```yaml
name: association slot
description: any slot that relates an association to another entity
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- edge property
- statement property
- node qualifier
- edge qualifier
- statement qualifier
rank: 1000
abstract: true
domain: association
alias: association_slot
range: string

```
</details></div>