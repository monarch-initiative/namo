---
search:
  boost: 10.0
---

# Class: IceesStudyResult 


_A study result that represents a result, from a supporting Study, which is specifically associated with an Integrated Clinical and Environmental Exposures Service (ICEES) knowledge assertion._



<div data-search-exclude markdown="1">



URI: [namo:IceesStudyResult](https://w3id.org/monarch-initiative/namo/IceesStudyResult)





```mermaid
 classDiagram
    class IceesStudyResult
    click IceesStudyResult href "../IceesStudyResult/"
      StudyResult <|-- IceesStudyResult
        click StudyResult href "../StudyResult/"
      
      IceesStudyResult : broad_synonym
        
      IceesStudyResult : category
        
      IceesStudyResult : chi_squared_dof
        
      IceesStudyResult : chi_squared_p
        
      IceesStudyResult : chi_squared_statistic
        
      IceesStudyResult : deprecated
        
      IceesStudyResult : description
        
      IceesStudyResult : equivalent_identifiers
        
      IceesStudyResult : exact_synonym
        
      IceesStudyResult : fisher_exact_odds_ratio
        
      IceesStudyResult : fisher_exact_p
        
      IceesStudyResult : full_name
        
      IceesStudyResult : has_attribute
        
          
    
        
        
        IceesStudyResult --> "*" Attribute : has_attribute
        click Attribute href "../Attribute/"
    

        
      IceesStudyResult : id
        
      IceesStudyResult : information_content
        
      IceesStudyResult : iri
        
      IceesStudyResult : log_odds_ratio
        
      IceesStudyResult : log_odds_ratio_95_ci
        
      IceesStudyResult : name
        
      IceesStudyResult : narrow_synonym
        
      IceesStudyResult : provided_by
        
      IceesStudyResult : related_synonym
        
      IceesStudyResult : synonym
        
      IceesStudyResult : taxon
        
      IceesStudyResult : total_sample_size
        
      IceesStudyResult : type
        
      IceesStudyResult : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [StudyResult](StudyResult.md)
            * **IceesStudyResult**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [chi_squared_statistic](chi_squared_statistic.md) | 0..1 <br/> [Float](Float.md) | The chi-squared statistic measures how much observed data deviate from expect... | direct |
| [chi_squared_dof](chi_squared_dof.md) | 0..1 <br/> [Integer](Integer.md) | Degrees of freedom (dof) in a chi-squared test referring to the number of val... | direct |
| [chi_squared_p](chi_squared_p.md) | 0..1 <br/> [Float](Float.md) | The chi-square p-value tells you the probability that the observed difference... | direct |
| [total_sample_size](total_sample_size.md) | 0..1 <br/> [Integer](Integer.md) | The total number of patients or participants within a sample population | direct |
| [fisher_exact_odds_ratio](fisher_exact_odds_ratio.md) | 0..1 <br/> [Float](Float.md) | The Fisher Exact Test is used to determine whether there is a non-random asso... | direct |
| [fisher_exact_p](fisher_exact_p.md) | 0..1 <br/> [Float](Float.md) | The Fisher exact p-value tells you the probability of observing a table as ex... | direct |
| [log_odds_ratio](log_odds_ratio.md) | 0..1 <br/> [Float](Float.md) | The natural logarithm of the odds ratio (OR), or the ratio of the odds of an ... | direct |
| [log_odds_ratio_95_ci](log_odds_ratio_95_ci.md) | * <br/> [Float](Float.md) | The ninety-five percent confidence range in which the true log odds ratio for... | direct |
| [provided_by](provided_by.md) | * <br/> [String](String.md) | The value in this node property represents the knowledge provider that create... | [NamedThing](NamedThing.md) |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge... | [NamedThing](NamedThing.md) |
| [full_name](full_name.md) | 0..1 <br/> [LabelType](LabelType.md) | a long-form human readable name for a thing | [NamedThing](NamedThing.md) |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing | [NamedThing](NamedThing.md) |
| [exact_synonym](exact_synonym.md) | * <br/> [LabelType](LabelType.md) | An alternate label for an entity that denotes exactly the same meaning as the... | [NamedThing](NamedThing.md) |
| [broad_synonym](broad_synonym.md) | * <br/> [LabelType](LabelType.md) | An alternate label for an entity whose meaning is broader (more general) than... | [NamedThing](NamedThing.md) |
| [narrow_synonym](narrow_synonym.md) | * <br/> [LabelType](LabelType.md) | An alternate label for an entity whose meaning is narrower (more specific) th... | [NamedThing](NamedThing.md) |
| [related_synonym](related_synonym.md) | * <br/> [LabelType](LabelType.md) | An alternate label that is related to the primary label but is neither exactl... | [NamedThing](NamedThing.md) |
| [equivalent_identifiers](equivalent_identifiers.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A set of identifiers that are considered equivalent to the primary identifier... | [NamedThing](NamedThing.md) |
| [information_content](information_content.md) | 0..1 <br/> [Float](Float.md) | Information content (IC) value for a term, primarily from Automats | [NamedThing](NamedThing.md) |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity | [NamedThing](NamedThing.md) |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md) |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md) |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | * <br/> [String](String.md) | An rdf:type property asserting that an entity is an instance of a particular ... | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | * <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |
| [deprecated](deprecated.md) | 0..1 <br/> [Boolean](Boolean.md) | A boolean flag indicating that an entity is no longer considered current or v... | [Entity](Entity.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:IceesStudyResult |
| native | namo:IceesStudyResult |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: icees study result
description: A study result that represents a result, from a supporting Study, which
  is specifically associated with an Integrated Clinical and Environmental Exposures
  Service (ICEES) knowledge assertion.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: study result
slots:
- chi squared statistic
- chi squared dof
- chi squared p
- total sample size
- fisher exact odds ratio
- fisher exact p
- log odds ratio
- log odds ratio 95 ci

```
</details>

### Induced

<details>
```yaml
name: icees study result
description: A study result that represents a result, from a supporting Study, which
  is specifically associated with an Integrated Clinical and Environmental Exposures
  Service (ICEES) knowledge assertion.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: study result
attributes:
  chi squared statistic:
    name: chi squared statistic
    description: The chi-squared statistic measures how much observed data deviate
      from expected values under the null hypothesis.
    examples:
    - value: '26.38523077566414'
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - STATO:0000030
    rank: 1000
    is_a: association slot
    domain: association
    alias: chi_squared_statistic
    owner: icees study result
    domain_of:
    - icees study result
    range: float
  chi squared dof:
    name: chi squared dof
    description: Degrees of freedom (dof) in a chi-squared test referring to the number
      of values in the final calculation of a statistic that are free to vary
    examples:
    - value: '1'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: chi_squared_dof
    owner: icees study result
    domain_of:
    - icees study result
    range: integer
  chi squared p:
    name: chi squared p
    description: The chi-square p-value tells you the probability that the observed
      differences (or associations) in your data occurred by random chance, assuming
      the null hypothesis is true.
    examples:
    - value: '2.7967079822744063e-07'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: chi_squared_p
    owner: icees study result
    domain_of:
    - icees study result
    range: float
  total sample size:
    name: total sample size
    description: The total number of patients or participants within a sample population.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: dataset count
    domain: association
    alias: total_sample_size
    owner: icees study result
    domain_of:
    - icees study result
    range: integer
  fisher exact odds ratio:
    name: fisher exact odds ratio
    description: "The Fisher Exact Test is used to determine whether there is a non-random\
      \ association between two categorical variables in a 2×2 contingency table,\
      \ especially when sample sizes are small. The odds ratio (OR) quantifies the\
      \ strength of that association.\n   OR = 1 implies No association\n   OR > 1\
      \ implies Positive association (Group A more likely to have Outcome 1)\n   OR\
      \ < 1 implies Negative association (Group A less likely to have Outcome 1)"
    examples:
    - value: '3.226188583240579'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: fisher_exact_odds_ratio
    owner: icees study result
    domain_of:
    - icees study result
    range: float
  fisher exact p:
    name: fisher exact p
    description: The Fisher exact p-value tells you the probability of observing a
      table as extreme as (or more extreme than) your actual data, assuming that the
      null hypothesis of independence is true. It's most commonly used for 2×2 contingency
      tables, especially when sample sizes are small or expected counts are low.
    examples:
    - value: '2.8581244515361156e-06'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: fisher_exact_p
    owner: icees study result
    domain_of:
    - icees study result
    range: float
  log odds ratio:
    name: log odds ratio
    description: The natural logarithm of the odds ratio (OR), or the ratio of the
      odds of an event Y occurring in an exposed group versus the odds of an event
      Y occurring in a non-exposed group.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: log_odds_ratio
    owner: icees study result
    domain_of:
    - icees study result
    range: float
  log odds ratio 95 ci:
    name: log odds ratio 95 ci
    description: The ninety-five percent confidence range in which the true log odds
      ratio for the sample population falls. To calculate the 95% confidence interval
      (CI) for a log odds ratio (a pair of numbers), you need the standard error (SE)
      of the log odds ratio.  This interval helps you understand the precision of
      your estimate and whether the association is statistically significant.
    examples:
    - value: '[0.6996904681742875, 1.6429124024089072]'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: log_odds_ratio_95_ci
    owner: icees study result
    domain_of:
    - icees study result
    range: float
    multivalued: true
  provided by:
    name: provided by
    description: The value in this node property represents the knowledge provider
      that created or assembled the node and all of its attributes.  Used internally
      to represent how a particular node made its way into a knowledge provider or
      graph.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    alias: provided_by
    owner: icees study result
    domain_of:
    - named thing
    range: string
    multivalued: true
  xref:
    name: xref
    description: A database cross reference or alternative identifier for a NamedThing
      or edge between two NamedThings.  This property should point to a database record
      or webpage that supports the existence of the edge, or gives more detail about
      the edge. This property can be used on a node or edge to provide multiple URIs
      or CURIE cross references.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - dbxref
    - Dbxref
    - DbXref
    - record_url
    - source_record_urls
    narrow_mappings:
    - gff3:Dbxref
    - gpi:DB_Xrefs
    rank: 1000
    domain: named thing
    owner: icees study result
    domain_of:
    - named thing
    - publication
    - retrieval source
    - gene
    - gene product mixin
    range: uriorcurie
    multivalued: true
  full name:
    name: full name
    description: a long-form human readable name for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    alias: full_name
    owner: icees study result
    domain_of:
    - named thing
    range: label type
  synonym:
    name: synonym
    description: Alternate human-readable names for a thing
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - alias
    narrow_mappings:
    - skos:altLabel
    - gff3:Alias
    - AGRKB:synonyms
    - gpi:DB_Object_Synonyms
    - HANCESTRO:0330
    - IAO:0000136
    - RXNORM:has_tradename
    rank: 1000
    is_a: node property
    domain: named thing
    owner: icees study result
    domain_of:
    - named thing
    - gene product mixin
    range: label type
    multivalued: true
  exact synonym:
    name: exact synonym
    description: An alternate label for an entity that denotes exactly the same meaning
      as the primary label and is interchangeable with it in all contexts.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - oboInOwl:hasExactSynonym
    rank: 1000
    is_a: synonym
    domain: named thing
    alias: exact_synonym
    owner: icees study result
    domain_of:
    - named thing
    range: label type
    multivalued: true
  broad synonym:
    name: broad synonym
    description: An alternate label for an entity whose meaning is broader (more general)
      than the primary label but is still useful as a lexical alternative.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - oboInOwl:hasBroadSynonym
    rank: 1000
    is_a: synonym
    domain: named thing
    alias: broad_synonym
    owner: icees study result
    domain_of:
    - named thing
    range: label type
    multivalued: true
  narrow synonym:
    name: narrow synonym
    description: An alternate label for an entity whose meaning is narrower (more
      specific) than the primary label, for example naming a particular sub-type.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - oboInOwl:hasNarrowSynonym
    rank: 1000
    is_a: synonym
    domain: named thing
    alias: narrow_synonym
    owner: icees study result
    domain_of:
    - named thing
    range: label type
    multivalued: true
  related synonym:
    name: related synonym
    description: An alternate label that is related to the primary label but is neither
      exactly synonymous nor cleanly broader or narrower; useful as a lexical pointer
      but not for strict equivalence. Corresponds to oboInOwl:hasRelatedSynonym.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - oboInOwl:hasRelatedSynonym
    rank: 1000
    is_a: synonym
    domain: named thing
    alias: related_synonym
    owner: icees study result
    domain_of:
    - named thing
    range: label type
    multivalued: true
  equivalent identifiers:
    name: equivalent identifiers
    description: A set of identifiers that are considered equivalent to the primary
      identifier of the entity. This attribute is used to represent a collection of
      identifiers that are considered equivalent to the primary identifier of an entity.
      These equivalent identifiers may come from different databases, ontologies,
      or naming conventions, but they all refer to the same underlying concept or
      entity. This attribute is particularly useful in data integration and interoperability
      scenarios, where it is important to recognize and link different representations
      of the same entity across various sources.
    from_schema: https://w3id.org/monarch-initiative/namo
    see_also:
    - biolink:xref
    - biolink:synonyms
    rank: 1000
    alias: equivalent_identifiers
    owner: icees study result
    domain_of:
    - named thing
    range: uriorcurie
    multivalued: true
  information content:
    name: information content
    description: Information content (IC) value for a term, primarily from Automats.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: information_content
    owner: icees study result
    domain_of:
    - named thing
    range: float
  taxon:
    name: taxon
    description: A property that indicates the taxonomic classification of an entity.
      Values for this slot should be from the NCBITaxon ontology.
    comments:
    - Note there is also a predicate 'in taxon' that can be used to instantiate an
      edge between a taxon entity and a thing with taxon entity.  This is an acceptable
      practice for KG construction, but for many applications it is more convenient
      to use this property slot to directly annotate the taxon on the entity itself.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    owner: icees study result
    domain_of:
    - named thing
    range: uriorcurie
  id:
    name: id
    description: A unique identifier for an entity. Must be either a CURIE shorthand
      for a URI or a complete URI
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - AGRKB:primaryId
    - gff3:ID
    - gpi:DB_Object_ID
    rank: 1000
    domain: entity
    identifier: true
    owner: icees study result
    domain_of:
    - Reference
    - ontology class
    - entity
    range: string
    required: true
  iri:
    name: iri
    description: An IRI for an entity. This is determined by the id using expansion
      rules.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - WIKIDATA_PROPERTY:P854
    rank: 1000
    owner: icees study result
    domain_of:
    - attribute
    - entity
    range: iri type
  category:
    name: category
    description: Name of the high level ontology class in which this entity is categorized.
      Corresponds to the label for the biolink entity type class. In a neo4j database
      this MAY correspond to the neo4j label tag. In an RDF database it should be
      a biolink model class URI. This field is multi-valued. It should include values
      for ancestors of the biolink class; for example, a protein such as Shh would
      have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`.
      In an RDF database, nodes will typically have an rdf:type triples. This can
      be to the most specific biolink class, or potentially to a class more specific
      than something in biolink. For example, a sequence feature `f` may have a rdf:type
      assertion to a SO class such as TF_binding_site, which is more specific than
      anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity,
      biolink:NamedThing}
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: type
    domain: entity
    designates_type: true
    owner: icees study result
    domain_of:
    - entity
    is_class_field: true
    range: uriorcurie
    required: true
    multivalued: true
  type:
    name: type
    description: An rdf:type property asserting that an entity is an instance of a
      particular class. In Biolink the value is typically used to indicate the most
      specific category of which the entity is an instance.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - gff3:type
    - gpi:DB_Object_Type
    rank: 1000
    domain: entity
    slot_uri: rdf:type
    owner: icees study result
    domain_of:
    - entity
    range: string
    multivalued: true
  name:
    name: name
    description: A human-readable name for an attribute or entity.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    rank: 1000
    domain: entity
    slot_uri: rdfs:label
    owner: icees study result
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: label type
  description:
    name: description
    description: a human-readable description of an entity
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - definition
    exact_mappings:
    - IAO:0000115
    - skos:definitions
    narrow_mappings:
    - gff3:Description
    rank: 1000
    slot_uri: dct:description
    owner: icees study result
    domain_of:
    - entity
    range: narrative text
  has attribute:
    name: has attribute
    description: connects any entity to an attribute
    in_subset:
    - samples
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - SIO:000008
    close_mappings:
    - OBI:0001927
    narrow_mappings:
    - OBAN:association_has_subject_property
    - OBAN:association_has_object_property
    - CPT:has_possibly_included_panel_element
    - DRUGBANK:category
    - EFO:is_executed_in
    - HANCESTRO:0301
    - LOINC:has_action_guidance
    - LOINC:has_adjustment
    - LOINC:has_aggregation_view
    - LOINC:has_approach_guidance
    - LOINC:has_divisor
    - LOINC:has_exam
    - LOINC:has_method
    - LOINC:has_modality_subtype
    - LOINC:has_object_guidance
    - LOINC:has_scale
    - LOINC:has_suffix
    - LOINC:has_time_aspect
    - LOINC:has_time_modifier
    - LOINC:has_timing_of
    - NCIT:R88
    - NCIT:eo_disease_has_property_or_attribute
    - NCIT:has_data_element
    - NCIT:has_pharmaceutical_administration_method
    - NCIT:has_pharmaceutical_basic_dose_form
    - NCIT:has_pharmaceutical_intended_site
    - NCIT:has_pharmaceutical_release_characteristics
    - NCIT:has_pharmaceutical_state_of_matter
    - NCIT:has_pharmaceutical_transformation
    - NCIT:is_qualified_by
    - NCIT:qualifier_applies_to
    - NCIT:role_has_domain
    - NCIT:role_has_range
    - INO:0000154
    - HANCESTRO:0308
    - orphanet:C016
    - orphanet:C017
    - RO:0000053
    - RO:0000086
    - RO:0000087
    - SNOMED:has_access
    - SNOMED:has_clinical_course
    - SNOMED:has_count_of_base_of_active_ingredient
    - SNOMED:has_dose_form_administration_method
    - SNOMED:has_dose_form_release_characteristic
    - SNOMED:has_dose_form_transformation
    - SNOMED:has_finding_context
    - SNOMED:has_finding_informer
    - SNOMED:has_inherent_attribute
    - SNOMED:has_intent
    - SNOMED:has_interpretation
    - SNOMED:has_laterality
    - SNOMED:has_measurement_method
    - SNOMED:has_method
    - SNOMED:has_priority
    - SNOMED:has_procedure_context
    - SNOMED:has_process_duration
    - SNOMED:has_property
    - SNOMED:has_revision_status
    - SNOMED:has_scale_type
    - SNOMED:has_severity
    - SNOMED:has_specimen
    - SNOMED:has_state_of_matter
    - SNOMED:has_subject_relationship_context
    - SNOMED:has_surgical_approach
    - SNOMED:has_technique
    - SNOMED:has_temporal_context
    - SNOMED:has_time_aspect
    - SNOMED:has_units
    - UMLS:has_structural_class
    - UMLS:has_supported_concept_property
    - UMLS:has_supported_concept_relationship
    - UMLS:may_be_qualified_by
    rank: 1000
    domain: entity
    alias: has_attribute
    owner: icees study result
    domain_of:
    - entity
    range: attribute
    multivalued: true
  deprecated:
    name: deprecated
    description: A boolean flag indicating that an entity is no longer considered
      current or valid.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - oboInOwl:ObsoleteClass
    rank: 1000
    owner: icees study result
    domain_of:
    - entity
    range: boolean

```
</details></div>