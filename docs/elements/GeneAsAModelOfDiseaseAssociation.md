---
search:
  boost: 10.0
---

# Class: GeneAsAModelOfDiseaseAssociation 


_An association in which a gene (e.g., a model-organism ortholog of a known disease gene) serves as a model of a human disease - for example, because mutants of the gene recapitulate core features of the disease._



<div data-search-exclude markdown="1">



URI: [namo:GeneAsAModelOfDiseaseAssociation](https://w3id.org/monarch-initiative/namo/GeneAsAModelOfDiseaseAssociation)





```mermaid
 classDiagram
    class GeneAsAModelOfDiseaseAssociation
    click GeneAsAModelOfDiseaseAssociation href "../GeneAsAModelOfDiseaseAssociation/"
      ModelToDiseaseAssociationMixin <|-- GeneAsAModelOfDiseaseAssociation
        click ModelToDiseaseAssociationMixin href "../ModelToDiseaseAssociationMixin/"
      EntityToDiseaseAssociationMixin <|-- GeneAsAModelOfDiseaseAssociation
        click EntityToDiseaseAssociationMixin href "../EntityToDiseaseAssociationMixin/"
      GeneToDiseaseAssociation <|-- GeneAsAModelOfDiseaseAssociation
        click GeneToDiseaseAssociation href "../GeneToDiseaseAssociation/"
      
      GeneAsAModelOfDiseaseAssociation : adjusted_p_value
        
      GeneAsAModelOfDiseaseAssociation : agent_type
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "1" AgentTypeEnum : agent_type
        click AgentTypeEnum href "../AgentTypeEnum/"
    

        
      GeneAsAModelOfDiseaseAssociation : aggregator_knowledge_source
        
      GeneAsAModelOfDiseaseAssociation : allelic_requirement
        
      GeneAsAModelOfDiseaseAssociation : category
        
      GeneAsAModelOfDiseaseAssociation : deprecated
        
      GeneAsAModelOfDiseaseAssociation : description
        
      GeneAsAModelOfDiseaseAssociation : disease_context_qualifier
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "0..1" Disease : disease_context_qualifier
        click Disease href "../Disease/"
    

        
      GeneAsAModelOfDiseaseAssociation : diseases_confidence_score
        
      GeneAsAModelOfDiseaseAssociation : elevate_to_prediction
        
      GeneAsAModelOfDiseaseAssociation : evidence_count
        
      GeneAsAModelOfDiseaseAssociation : frequency_qualifier
        
      GeneAsAModelOfDiseaseAssociation : gene2phenotype_confidence_category
        
      GeneAsAModelOfDiseaseAssociation : has_attribute
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" Attribute : has_attribute
        click Attribute href "../Attribute/"
    

        
      GeneAsAModelOfDiseaseAssociation : has_confidence_score
        
      GeneAsAModelOfDiseaseAssociation : has_evidence
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" InformationContentEntity : has_evidence
        click InformationContentEntity href "../InformationContentEntity/"
    

        
      GeneAsAModelOfDiseaseAssociation : has_evidence_of_type
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" EvidenceType : has_evidence_of_type
        click EvidenceType href "../EvidenceType/"
    

        
      GeneAsAModelOfDiseaseAssociation : has_supporting_studies
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" Study : has_supporting_studies
        click Study href "../Study/"
    

        
      GeneAsAModelOfDiseaseAssociation : id
        
      GeneAsAModelOfDiseaseAssociation : iri
        
      GeneAsAModelOfDiseaseAssociation : knowledge_level
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "1" KnowledgeLevelEnum : knowledge_level
        click KnowledgeLevelEnum href "../KnowledgeLevelEnum/"
    

        
      GeneAsAModelOfDiseaseAssociation : knowledge_source
        
      GeneAsAModelOfDiseaseAssociation : name
        
      GeneAsAModelOfDiseaseAssociation : negated
        
      GeneAsAModelOfDiseaseAssociation : object
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "1" Disease : object
        click Disease href "../Disease/"
    

        
      GeneAsAModelOfDiseaseAssociation : object_aspect_qualifier
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "0..1" GeneOrGeneProductOrChemicalEntityAspectEnum : object_aspect_qualifier
        click GeneOrGeneProductOrChemicalEntityAspectEnum href "../GeneOrGeneProductOrChemicalEntityAspectEnum/"
    

        
      GeneAsAModelOfDiseaseAssociation : object_category
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "0..1" OntologyClass : object_category
        click OntologyClass href "../OntologyClass/"
    

        
      GeneAsAModelOfDiseaseAssociation : object_category_closure
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" OntologyClass : object_category_closure
        click OntologyClass href "../OntologyClass/"
    

        
      GeneAsAModelOfDiseaseAssociation : object_closure
        
      GeneAsAModelOfDiseaseAssociation : object_direction_qualifier
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "0..1" DirectionQualifierEnum : object_direction_qualifier
        click DirectionQualifierEnum href "../DirectionQualifierEnum/"
    

        
      GeneAsAModelOfDiseaseAssociation : object_feature_name
        
      GeneAsAModelOfDiseaseAssociation : object_label_closure
        
      GeneAsAModelOfDiseaseAssociation : object_namespace
        
      GeneAsAModelOfDiseaseAssociation : original_object
        
      GeneAsAModelOfDiseaseAssociation : original_predicate
        
      GeneAsAModelOfDiseaseAssociation : original_subject
        
      GeneAsAModelOfDiseaseAssociation : p_value
        
      GeneAsAModelOfDiseaseAssociation : predicate
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "1" GeneToDiseasePredicateEnum : predicate
        click GeneToDiseasePredicateEnum href "../GeneToDiseasePredicateEnum/"
    

        
      GeneAsAModelOfDiseaseAssociation : primary_knowledge_source
        
      GeneAsAModelOfDiseaseAssociation : publications
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" Publication : publications
        click Publication href "../Publication/"
    

        
      GeneAsAModelOfDiseaseAssociation : qualified_predicate
        
      GeneAsAModelOfDiseaseAssociation : qualifier
        
      GeneAsAModelOfDiseaseAssociation : qualifiers
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" OntologyClass : qualifiers
        click OntologyClass href "../OntologyClass/"
    

        
      GeneAsAModelOfDiseaseAssociation : retrieval_source_ids
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" RetrievalSource : retrieval_source_ids
        click RetrievalSource href "../RetrievalSource/"
    

        
      GeneAsAModelOfDiseaseAssociation : semmed_agreement_count
        
      GeneAsAModelOfDiseaseAssociation : sources
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" RetrievalSource : sources
        click RetrievalSource href "../RetrievalSource/"
    

        
      GeneAsAModelOfDiseaseAssociation : subject
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "1" GeneOrGeneProduct : subject
        click GeneOrGeneProduct href "../GeneOrGeneProduct/"
    

        
      GeneAsAModelOfDiseaseAssociation : subject_aspect_qualifier
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "0..1" GeneOrGeneProductOrChemicalEntityAspectEnum : subject_aspect_qualifier
        click GeneOrGeneProductOrChemicalEntityAspectEnum href "../GeneOrGeneProductOrChemicalEntityAspectEnum/"
    

        
      GeneAsAModelOfDiseaseAssociation : subject_category
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "0..1" OntologyClass : subject_category
        click OntologyClass href "../OntologyClass/"
    

        
      GeneAsAModelOfDiseaseAssociation : subject_category_closure
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "*" OntologyClass : subject_category_closure
        click OntologyClass href "../OntologyClass/"
    

        
      GeneAsAModelOfDiseaseAssociation : subject_closure
        
      GeneAsAModelOfDiseaseAssociation : subject_direction_qualifier
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "0..1" DirectionQualifierEnum : subject_direction_qualifier
        click DirectionQualifierEnum href "../DirectionQualifierEnum/"
    

        
      GeneAsAModelOfDiseaseAssociation : subject_feature_name
        
      GeneAsAModelOfDiseaseAssociation : subject_form_or_variant_qualifier
        
          
    
        
        
        GeneAsAModelOfDiseaseAssociation --> "0..1" ChemicalOrGeneOrGeneProductFormOrVariantEnum : subject_form_or_variant_qualifier
        click ChemicalOrGeneOrGeneProductFormOrVariantEnum href "../ChemicalOrGeneOrGeneProductFormOrVariantEnum/"
    

        
      GeneAsAModelOfDiseaseAssociation : subject_label_closure
        
      GeneAsAModelOfDiseaseAssociation : subject_namespace
        
      GeneAsAModelOfDiseaseAssociation : supporting_text
        
      GeneAsAModelOfDiseaseAssociation : timepoint
        
      GeneAsAModelOfDiseaseAssociation : type
        
      GeneAsAModelOfDiseaseAssociation : update_date
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [Association](Association.md)
        * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) [ [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)]
            * **GeneAsAModelOfDiseaseAssociation** [ [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 1 <br/> [GeneOrGeneProduct](GeneOrGeneProduct.md) | A gene that has a role in modeling the disease | [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md), [FrequencyQualifierMixin](FrequencyQualifierMixin.md), [Association](Association.md), [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) |
| [predicate](predicate.md) | 1 <br/> [GeneToDiseasePredicateEnum](GeneToDiseasePredicateEnum.md) | The relationship to the disease | [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md), [FrequencyQualifierMixin](FrequencyQualifierMixin.md), [Association](Association.md), [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) |
| [object](object.md) | 1 <br/> [Disease](Disease.md) | disease | [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md), [FrequencyQualifierMixin](FrequencyQualifierMixin.md), [Association](Association.md), [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) |
| [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | 0..1 <br/> [ChemicalOrGeneOrGeneProductFormOrVariantEnum](ChemicalOrGeneOrGeneProductFormOrVariantEnum.md) | A qualifier that composes with a core subject/object concept to define a spec... | [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |
| [subject_aspect_qualifier](subject_aspect_qualifier.md) | 0..1 <br/> [GeneOrGeneProductOrChemicalEntityAspectEnum](GeneOrGeneProductOrChemicalEntityAspectEnum.md) | Composes with the core concept to describe new concepts of a different ontolo... | [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md), [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |
| [object_direction_qualifier](object_direction_qualifier.md) | 0..1 <br/> [DirectionQualifierEnum](DirectionQualifierEnum.md) | Composes with the core concept (+ aspect if provided) to describe a change in... | [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md), [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |
| [allelic_requirement](allelic_requirement.md) | 0..1 <br/> [String](String.md) | The allele configuration of a particular gene or variant required for the exp... | [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |
| [qualified_predicate](qualified_predicate.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Predicate to be used in an association when subject and object qualifiers are... | [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md), [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |
| [diseases_confidence_score](diseases_confidence_score.md) | 0..1 <br/> [Float](Float.md) | A score defined by Jensen Lab Diseases that reports confidence level in an as... | [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |
| [gene2phenotype_confidence_category](gene2phenotype_confidence_category.md) | 0..1 <br/> [String](String.md) | A term used by EBI Gene2Phenotype to describe the confidence that the associa... | [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |
| [negated](negated.md) | 0..1 <br/> [Boolean](Boolean.md) | if set to true, then the association is negated i | [Association](Association.md) |
| [qualifier](qualifier.md) | 0..1 <br/> [String](String.md) | grouping slot for all qualifiers on an edge | [Association](Association.md) |
| [qualifiers](qualifiers.md) | * <br/> [OntologyClass](OntologyClass.md) | connects an association to qualifiers that modify or qualify the meaning of t... | [Association](Association.md) |
| [publications](publications.md) | * <br/> [Publication](Publication.md) | One or more publications that report the statement expressed in an Associatio... | [Association](Association.md) |
| [sources](sources.md) | * <br/> [RetrievalSource](RetrievalSource.md) | A set of RetrievalSources, which traces where the statement expressed in an A... | [Association](Association.md) |
| [has_evidence_of_type](has_evidence_of_type.md) | * <br/> [EvidenceType](EvidenceType.md) | Connects an association to an evidence type ontology term | [Association](Association.md) |
| [has_evidence](has_evidence.md) | * <br/> [InformationContentEntity](InformationContentEntity.md) | Connects an association to detailed information providing supporting evidence | [Association](Association.md) |
| [knowledge_source](knowledge_source.md) | 0..1 <br/> [String](String.md) | An Information Resource from which the knowledge expressed in an Association ... | [Association](Association.md) |
| [primary_knowledge_source](primary_knowledge_source.md) | 0..1 <br/> [String](String.md) | The most upstream source of the knowledge expressed in an Association that an... | [Association](Association.md) |
| [aggregator_knowledge_source](aggregator_knowledge_source.md) | * <br/> [String](String.md) | An intermediate aggregator resource from which knowledge expressed in an Asso... | [Association](Association.md) |
| [knowledge_level](knowledge_level.md) | 1 <br/> [KnowledgeLevelEnum](KnowledgeLevelEnum.md) | Describes the level of knowledge expressed in a statement, based on the reaso... | [Association](Association.md) |
| [agent_type](agent_type.md) | 1 <br/> [AgentTypeEnum](AgentTypeEnum.md) | Describes the high-level category of agent who originally generated a stateme... | [Association](Association.md) |
| [timepoint](timepoint.md) | 0..1 <br/> [TimeType](TimeType.md) | a point in time | [Association](Association.md) |
| [original_subject](original_subject.md) | 0..1 <br/> [String](String.md) | used to hold the original subject of a relation (or predicate) that an extern... | [Association](Association.md) |
| [original_predicate](original_predicate.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | used to hold the original relation/predicate that an external knowledge sourc... | [Association](Association.md) |
| [original_object](original_object.md) | 0..1 <br/> [String](String.md) | used to hold the original object of a relation (or predicate) that an externa... | [Association](Association.md) |
| [subject_feature_name](subject_feature_name.md) | 0..1 <br/> [String](String.md) | Used to describe a subordinate feature of the associated subject for example,... | [Association](Association.md) |
| [object_feature_name](object_feature_name.md) | 0..1 <br/> [String](String.md) | Used to describe a subordinate feature of the associated object for example, ... | [Association](Association.md) |
| [subject_category](subject_category.md) | 0..1 <br/> [OntologyClass](OntologyClass.md) | Used to hold the biolink class/category of an association | [Association](Association.md) |
| [object_category](object_category.md) | 0..1 <br/> [OntologyClass](OntologyClass.md) | Used to hold the biolink class/category of an association | [Association](Association.md) |
| [subject_closure](subject_closure.md) | * <br/> [String](String.md) | Used to hold the subject closure of an association | [Association](Association.md) |
| [object_closure](object_closure.md) | * <br/> [String](String.md) | Used to hold the object closure of an association | [Association](Association.md) |
| [subject_category_closure](subject_category_closure.md) | * <br/> [OntologyClass](OntologyClass.md) | Used to hold the subject category closure of an association | [Association](Association.md) |
| [object_category_closure](object_category_closure.md) | * <br/> [OntologyClass](OntologyClass.md) | Used to hold the object category closure of an association | [Association](Association.md) |
| [subject_namespace](subject_namespace.md) | 0..1 <br/> [String](String.md) | Used to hold the subject namespace of an association | [Association](Association.md) |
| [object_namespace](object_namespace.md) | 0..1 <br/> [String](String.md) | Used to hold the object namespace of an association | [Association](Association.md) |
| [subject_label_closure](subject_label_closure.md) | * <br/> [String](String.md) | Used to hold the subject label closure of an association | [Association](Association.md) |
| [object_label_closure](object_label_closure.md) | * <br/> [String](String.md) | Used to hold the object label closure of an association | [Association](Association.md) |
| [retrieval_source_ids](retrieval_source_ids.md) | * <br/> [RetrievalSource](RetrievalSource.md) | A list of retrieval sources that served as a source of knowledge expressed in... | [Association](Association.md) |
| [p_value](p_value.md) | 0..1 <br/> [Float](Float.md) | A quantitative confidence value that represents the probability of obtaining ... | [Association](Association.md) |
| [adjusted_p_value](adjusted_p_value.md) | 0..1 <br/> [Float](Float.md) | The adjusted p-value is the probability of obtaining test results at least as... | [Association](Association.md) |
| [supporting_text](supporting_text.md) | * <br/> [String](String.md) | The segment of text from a document that supports the mined assertion | [Association](Association.md) |
| [has_supporting_studies](has_supporting_studies.md) | * <br/> [Study](Study.md) | Studies that produced information used as evidence to generate the knowledge ... | [Association](Association.md) |
| [update_date](update_date.md) | 0..1 <br/> [Date](Date.md) | date on which an entity was updated | [Association](Association.md) |
| [has_confidence_score](has_confidence_score.md) | 0..1 <br/> [Float](Float.md) | connects an association to a quantitative (numeric) value that can be interpr... | [Association](Association.md) |
| [elevate_to_prediction](elevate_to_prediction.md) | 0..1 <br/> [Boolean](Boolean.md) | A boolean flag indicating whether a clinical trial finding should be elevated... | [Association](Association.md) |
| [evidence_count](evidence_count.md) | 0..1 <br/> [Integer](Integer.md) | The number of evidence instances that are connected to an association | [Association](Association.md) |
| [semmed_agreement_count](semmed_agreement_count.md) | 0..1 <br/> [Integer](Integer.md) | The number of times this concept has been asserted in the SemMedDB literature... | [Association](Association.md) |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md) |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md) |
| [category](category.md) | * <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | * <br/> [String](String.md) | rdf:type of biolink:Association should be fixed at rdf:Statement | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | * <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |
| [deprecated](deprecated.md) | 0..1 <br/> [Boolean](Boolean.md) | A boolean flag indicating that an entity is no longer considered current or v... | [Entity](Entity.md) |
| [subject_direction_qualifier](subject_direction_qualifier.md) | 0..1 <br/> [DirectionQualifierEnum](DirectionQualifierEnum.md) | Composes with the core concept (+ aspect if provided) to describe a change in... | [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) |
| [object_aspect_qualifier](object_aspect_qualifier.md) | 0..1 <br/> [GeneOrGeneProductOrChemicalEntityAspectEnum](GeneOrGeneProductOrChemicalEntityAspectEnum.md) | Composes with the core concept to describe new concepts of a different ontolo... | [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) |
| [disease_context_qualifier](disease_context_qualifier.md) | 0..1 <br/> [Disease](Disease.md) | A context qualifier representing a disease or condition in which a relationsh... | [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) |
| [frequency_qualifier](frequency_qualifier.md) | 0..1 <br/> [FrequencyValue](FrequencyValue.md) | a qualifier used in a phenotypic association to state how frequent the phenot... | [FrequencyQualifierMixin](FrequencyQualifierMixin.md) |

## Defining Slots

This class is defined by the following slots:


* [subject](subject.md)
* [predicate](predicate.md)
* [object](object.md)















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:GeneAsAModelOfDiseaseAssociation |
| native | namo:GeneAsAModelOfDiseaseAssociation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene as a model of disease association
description: An association in which a gene (e.g., a model-organism ortholog of a
  known disease gene) serves as a model of a human disease - for example, because
  mutants of the gene recapitulate core features of the disease.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: gene to disease association
mixins:
- model to disease association mixin
- entity to disease association mixin
slot_usage:
  subject:
    name: subject
    description: A gene that has a role in modeling the disease. This may be a model
      organism ortholog of a known disease gene, or it may be a gene whose mutants
      recapitulate core features of the disease.
    range: gene or gene product
defining_slots:
- subject
- predicate
- object

```
</details>

### Induced

<details>
```yaml
name: gene as a model of disease association
description: An association in which a gene (e.g., a model-organism ortholog of a
  known disease gene) serves as a model of a human disease - for example, because
  mutants of the gene recapitulate core features of the disease.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: gene to disease association
mixins:
- model to disease association mixin
- entity to disease association mixin
slot_usage:
  subject:
    name: subject
    description: A gene that has a role in modeling the disease. This may be a model
      organism ortholog of a known disease gene, or it may be a gene whose mutants
      recapitulate core features of the disease.
    range: gene or gene product
attributes:
  subject:
    name: subject
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation subject
      neo4j:
        local_name_source: neo4j
        local_name_value: node with outgoing relationship
    description: A gene that has a role in modeling the disease. This may be a model
      organism ortholog of a known disease gene, or it may be a gene whose mutants
      recapitulate core features of the disease.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedSource
    - OBAN:association_has_subject
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    owner: gene as a model of disease association
    domain_of:
    - association
    - gene to gene association
    - cell line to entity association mixin
    - chemical entity to entity association mixin
    - drug to entity association mixin
    - chemical to entity association mixin
    - case to entity association mixin
    - chemical entity to chemical entity association
    - named thing associated with likelihood of named thing association
    - material sample to entity association mixin
    - material sample derivation association
    - disease to entity association mixin
    - entity to exposure event association mixin
    - entity to outcome association mixin
    - frequency qualifier mixin
    - entity to phenotypic feature association mixin
    - disease or phenotypic feature to entity association mixin
    - entity to disease or phenotypic feature association mixin
    - genotype to entity association mixin
    - case to disease association
    - case to variant association
    - case to gene association
    - gene to entity association mixin
    - variant to entity association mixin
    - model to disease association mixin
    - macromolecular machine to entity association mixin
    - organism taxon to entity association
    range: gene or gene product
    required: true
  predicate:
    name: predicate
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation predicate
      translator:
        local_name_source: translator
        local_name_value: predicate
    description: The relationship to the disease
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedProperty
    - OBAN:association_has_predicate
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:predicate
    owner: gene as a model of disease association
    domain_of:
    - predicate mapping
    - association
    - gene to gene association
    - cell line to entity association mixin
    - chemical entity to entity association mixin
    - drug to entity association mixin
    - chemical to entity association mixin
    - case to entity association mixin
    - chemical entity to chemical entity association
    - named thing associated with likelihood of named thing association
    - material sample to entity association mixin
    - material sample derivation association
    - disease to entity association mixin
    - entity to exposure event association mixin
    - entity to outcome association mixin
    - frequency qualifier mixin
    - entity to phenotypic feature association mixin
    - disease or phenotypic feature to entity association mixin
    - entity to disease or phenotypic feature association mixin
    - genotype to entity association mixin
    - case to disease association
    - case to variant association
    - case to gene association
    - gene to entity association mixin
    - variant to entity association mixin
    - model to disease association mixin
    - macromolecular machine to entity association mixin
    - organism taxon to entity association
    subproperty_of: model of
    range: GeneToDiseasePredicateEnum
    required: true
  object:
    name: object
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: descriptor
      neo4j:
        local_name_source: neo4j
        local_name_value: node with incoming relationship
    description: disease
    examples:
    - value: MONDO:0020066
      description: Ehlers-Danlos syndrome
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedTarget
    - OBAN:association_has_object
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:object
    owner: gene as a model of disease association
    domain_of:
    - association
    - gene to gene association
    - cell line to entity association mixin
    - chemical entity to entity association mixin
    - drug to entity association mixin
    - chemical to entity association mixin
    - case to entity association mixin
    - chemical entity to chemical entity association
    - named thing associated with likelihood of named thing association
    - material sample to entity association mixin
    - material sample derivation association
    - disease to entity association mixin
    - entity to exposure event association mixin
    - entity to outcome association mixin
    - frequency qualifier mixin
    - entity to phenotypic feature association mixin
    - disease or phenotypic feature to entity association mixin
    - entity to disease or phenotypic feature association mixin
    - genotype to entity association mixin
    - case to disease association
    - case to variant association
    - case to gene association
    - gene to entity association mixin
    - variant to entity association mixin
    - model to disease association mixin
    - macromolecular machine to entity association mixin
    - organism taxon to entity association
    range: disease
    required: true
  subject form or variant qualifier:
    name: subject form or variant qualifier
    description: 'A qualifier that composes with a core subject/object concept to
      define a specific type, variant, alternative version of this concept. The composed
      concept remains a subtype or instance of the core concept. For example, the
      qualifier ‘mutation’ combines with the core concept ‘Gene X’ to express the
      compose concept ‘a mutation of Gene X’.  This qualifier specifies a change in
      the subject of an association (aka: statement).'
    examples:
    - value: mutation
    - value: late stage
    - value: severe
    - value: transplant
    - value: chemical analog
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: form or variant qualifier
    domain: association
    alias: subject_form_or_variant_qualifier
    owner: gene as a model of disease association
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - macromolecular machine has substrate association
    - chemical affects biological entity association
    - chemical gene sensitivity association
    - gene affects chemical association
    - gene to phenotypic feature association
    - gene to disease association
    - causal gene to disease association
    - correlated gene to disease association
    - gene has variant that contributes to disease association
    range: ChemicalOrGeneOrGeneProductFormOrVariantEnum
  subject aspect qualifier:
    name: subject aspect qualifier
    description: 'Composes with the core concept to describe new concepts of a different
      ontological type. e.g. a process in which the core concept participates, a function/activity/role
      held by the core concept, or a characteristic/quality that inheres in the core
      concept.  The purpose of the aspect slot is to indicate what aspect is being
      affected in an ''affects'' association.  This qualifier specifies a change in
      the subject of an association (aka: statement).'
    examples:
    - value: stability
    - value: abundance
    - value: expression
    - value: exposure
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: aspect qualifier
    domain: association
    alias: subject_aspect_qualifier
    owner: gene as a model of disease association
    domain_of:
    - predicate mapping
    - gene to gene association
    - named thing associated with likelihood of named thing association
    - macromolecular machine has substrate association
    - chemical affects biological entity association
    - chemical gene sensitivity association
    - gene affects chemical association
    - entity to feature or disease qualifiers mixin
    - entity to feature or variant qualifiers mixin
    - entity to feature or gene qualifiers mixin
    - feature or disease qualifiers to entity mixin
    - gene to phenotypic feature association
    - gene to disease association
    - causal gene to disease association
    - correlated gene to disease association
    range: GeneOrGeneProductOrChemicalEntityAspectEnum
  object direction qualifier:
    name: object direction qualifier
    description: 'Composes with the core concept (+ aspect if provided) to describe
      a change in its direction or degree. This qualifier qualifies the object of
      an association (aka: statement).'
    examples:
    - value: increased
    - value: downregulated
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: direction qualifier
    domain: association
    alias: object_direction_qualifier
    owner: gene as a model of disease association
    domain_of:
    - predicate mapping
    - gene to gene association
    - chemical entity to biological process association
    - chemical gene interaction association
    - macromolecular machine has substrate association
    - gene regulates gene association
    - chemical affects biological entity association
    - chemical gene sensitivity association
    - gene affects chemical association
    - entity to feature or disease qualifiers mixin
    - entity to feature or variant qualifiers mixin
    - entity to feature or gene qualifiers mixin
    - feature or disease qualifiers to entity mixin
    - gene to phenotypic feature association
    - gene to disease association
    - causal gene to disease association
    - correlated gene to disease association
    - chemical entity or gene or gene product regulates gene association
    range: DirectionQualifierEnum
  allelic requirement:
    name: allelic requirement
    description: The allele configuration of a particular gene or variant required
      for the expression of a disease or phenotype in a specific patient or instance.
    comments:
    - This edge property may be used by associations between Genes or SequenceVariants
      and DiseaseOrPhenotypicFeatures to provide the inheritance pattern and genetic
      context of the relationship. Terms from the HP mode of inheritance sub-ontology
      (HP:0000005) should be used in the value of this slot. This slot differs from
      the predicate "has_mode_of_inheritance", in that the predicate is used to link
      a disease or phenotype with its general inheritance pattern (how it is typically
      transmitted from one generation to the next, regardless of the specific genetic
      variant that is present in an individual or instance).
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: allelic_requirement
    owner: gene as a model of disease association
    domain_of:
    - gene to phenotypic feature association
    - gene to disease association
    - causal gene to disease association
    - correlated gene to disease association
    range: string
    pattern: ^HP:\d{7}$
  qualified predicate:
    name: qualified predicate
    description: Predicate to be used in an association when subject and object qualifiers
      are present and the full reading of the statement requires a qualification to
      the predicate in use in order to refine or increase the specificity of the full
      statement reading.  Has a value from the Biolink 'related_to' hierarchy, for
      example, biolink:related_to, biolink:causes, biolink:treats This qualifier holds
      a relationship to be used instead of that expressed by the primary predicate,
      in a ‘full statement’ reading of the association, where qualifier-based semantics
      are included. This is necessary only in cases where the primary predicate does
      not work in a full statement reading.
    notes:
    - 'to express the statement that “Chemical X causes increased expression of Gene
      Y”, the core triple is read using the fields subject:ChemX, predicate:affects,
      object:GeneY . . . and the full statement is read using the fields subject:ChemX,
      qualified_predicate:causes, object:GeneY, object_aspect: expression, object_direction:increased.
      The predicate ‘affects’ is needed for the core triple reading, but does not
      make sense in the full statement reading  (because “Chemical X affects increased
      expression of Gene Y'''' is not what we mean to say here: it causes increased
      expression of Gene Y)'
    examples:
    - value: biolink:causes
      description: used with `affects` predicate to express causal statements
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: qualifier
    domain: association
    alias: qualified_predicate
    owner: gene as a model of disease association
    domain_of:
    - predicate mapping
    - gene to gene association
    - chemical entity to biological process association
    - chemical gene interaction association
    - macromolecular machine has substrate association
    - gene regulates gene association
    - chemical affects biological entity association
    - chemical gene sensitivity association
    - gene affects chemical association
    - entity to feature or disease qualifiers mixin
    - entity to feature or variant qualifiers mixin
    - entity to feature or gene qualifiers mixin
    - feature or disease qualifiers to entity mixin
    - gene to disease association
    - causal gene to disease association
    - correlated gene to disease association
    range: uriorcurie
  diseases confidence score:
    name: diseases confidence score
    description: A score defined by Jensen Lab Diseases that reports confidence level
      in an association on a scale of 1-5 stars.  It is based on different inputs
      for curated knowledge associations vs text-mined associations vs experimental/GWAS
      based associations, but adjusts/caps scores for these types of knowledge such
      that they are comparable on a single scale.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: diseases_confidence_score
    owner: gene as a model of disease association
    domain_of:
    - gene to disease association
    - correlated gene to disease association
    range: float
  gene2phenotype confidence category:
    name: gene2phenotype confidence category
    description: A term used by EBI Gene2Phenotype to describe the confidence that
      the association is real. GenCC confidence terms are used for different levels
      of confidence (enum).  See https://www.ebi.ac.uk/gene2phenotype/about/terminology#g2p-confidence-section.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: gene2phenotype_confidence_category
    owner: gene as a model of disease association
    domain_of:
    - gene to disease association
    range: string
  negated:
    name: negated
    description: if set to true, then the association is negated i.e. is not true
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    owner: gene as a model of disease association
    domain_of:
    - association
    - case to phenotypic feature association
    range: boolean
  qualifier:
    name: qualifier
    description: grouping slot for all qualifiers on an edge.  useful for testing
      compliance with association classes
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
  qualifiers:
    name: qualifiers
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation qualifier
    description: connects an association to qualifiers that modify or qualify the
      meaning of that association
    deprecated: 'true'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    owner: gene as a model of disease association
    domain_of:
    - association
    range: ontology class
    multivalued: true
  publications:
    name: publications
    description: One or more publications that report the statement expressed in an
      Association, or provide information used as evidence supporting this statement.
    comments:
    - The notion of a ‘Publication’ is considered broadly to include any document
      made available for public consumption. It covers journal issues, individual
      articles, and books - and also things like article pre-prints, white papers,
      patents, drug labels, web pages, protocol documents, etc.
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - supporting publications
    - supporting documents
    rank: 1000
    is_a: association slot
    domain: association
    owner: gene as a model of disease association
    domain_of:
    - association
    range: publication
    multivalued: true
  sources:
    name: sources
    description: A set of RetrievalSources, which traces where the statement expressed
      in an Association came from. For example, the provenance of a Gene-Chemical
      Edge might be traced through the Translator Resource that provided it (e.g.
      MolePro) to one or more intermediate aggregator resources (e.g. ChEMBL), and
      finally to the resource that originally created/curated it (e.g. ClinicalTrials.org).
    comments:
    - Note that source retrieval provenance concerns the mechanical retrieval and
      transformation of data between web accessible information systems. It does not
      trace the source of knowledge back to specific publications or data sets. And
      it is not concerned with the reasoning, inference or analysis activities that
      generate knowledge in the first place (this is instead covered by 'knowledge
      level' and 'agent type' properties).
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - source retrieval provenance
    rank: 1000
    is_a: association slot
    domain: association
    owner: gene as a model of disease association
    domain_of:
    - association
    range: retrieval source
    multivalued: true
    inlined: true
    inlined_as_list: true
  has evidence of type:
    name: has evidence of type
    description: Connects an association to an evidence type ontology term. Generally
      represents terms from the ECO ontology.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: has_evidence_of_type
    owner: gene as a model of disease association
    domain_of:
    - association
    range: evidence type
    multivalued: true
  has evidence:
    name: has evidence
    description: Connects an association to detailed information providing supporting
      evidence.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - RO:0002558
    rank: 1000
    is_a: association slot
    domain: association
    alias: has_evidence
    owner: gene as a model of disease association
    domain_of:
    - association
    range: information content entity
    multivalued: true
    inlined: false
  knowledge source:
    name: knowledge source
    description: An Information Resource from which the knowledge expressed in an
      Association was retrieved, directly or indirectly. This can be any resource
      through which the knowledge passed on its way to its currently serialized form.
      In practice, implementers should use one of the more specific subtypes of this
      generic property.
    from_schema: https://w3id.org/monarch-initiative/namo
    close_mappings:
    - pav:providedBy
    rank: 1000
    is_a: association slot
    domain: association
    alias: knowledge_source
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
  primary knowledge source:
    name: primary knowledge source
    description: The most upstream source of the knowledge expressed in an Association
      that an implementer can identify.  Performing a rigorous analysis of upstream
      data providers is expected; every effort is made to catalog the most upstream
      source of data in this property.  Only one data source should be declared primary
      in any association.  "aggregator knowledge source" can be used to capture non-primary
      sources.
    notes:
    - 'For example: a single ChemicalToGene Edge originally curated by ClinicalTrials.org,
      is aggregated by ChEMBL, then incorporated into the MolePro KP, then sent via
      TRAPI message to the ARAGORN ARA, and finally sent to the NCATS ARS. The retrieval
      path for this Edge is as follows: ARS--retrieved_from-->  ARAGORN  --retrieved_from-->   MolePro  --retrieved_from-->
      ChEMBL --retrieved_from-->  ClinicalTrials.gov The "primary knowledge source"
      for this edge is "infores:clinical-trials-gov".  "infores:chembl" and "infores:molecular_data_provider"
      are listed in the "aggregator knowledge source" property.'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: knowledge source
    domain: association
    alias: primary_knowledge_source
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
    multivalued: false
  aggregator knowledge source:
    name: aggregator knowledge source
    description: An intermediate aggregator resource from which knowledge expressed
      in an Association was retrieved downstream of the original source, on its path
      to its current serialized form.
    notes:
    - 'For example, in this Feature Variable Association Edge generated by the Exposure
      Agent’s ICEES KP, through statistical analysis of clinical and environmental
      data supplied by the UNC Clinical Data Warehouse, the Edge is passed to the
      Ranking Agent’s ARAGORN ARA, and then on to the ARS. The retrieval path for
      this Edge is as follows: ARS--retrieved_from-->  ARAGORN  --retrieved_from-->   ICEES
      --supporting_data_from-->  UNC Data Warehouse This example illustrates how to
      represent the source provenance of KP-generated knowledge, including the source
      of data from which the knowledge was derived. The "primary knowledge source"
      for this edge is "infores:icees-asthma". A "supporting data source" for this
      KP- generated knowledge is "infores:unc-cdw-health."  The "aggregator knowledge
      source" for this data is "infores:aragorn-ara"'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: knowledge source
    domain: association
    alias: aggregator_knowledge_source
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
    multivalued: true
  knowledge level:
    name: knowledge level
    description: Describes the level of knowledge expressed in a statement, based
      on the reasoning or analysis methods used to generate the statement, or the
      scope or specificity of what the statement expresses to be true.
    notes:
    - The notion of a 'level' of knowledge can in one sense relate to the strength
      of a statement - i.e. how confident we are that it says something true about
      our domain of discourse. Here, we can generally consider Assertions to be stronger
      than Entailments to be stronger than Predictions. But in another sense, 'level'
      of knowledge can refer to the scope or specificity of what a statement expresses
      - on a spectrum from context-specific results of a data analysis, to generalized
      assertions of knowledge or fact. Here, Statistical Associations and  Observations
      represent more foundational statements that are only slightly removed from the
      data on which they are based (the former reporting the direct results of  an
      analysis in terms of correlations between variables in the data, and the latter
      describing phenomena that were observed/reported to have occurred).
    examples:
    - value: knowledge_assertion
    - value: prediction
    - value: statistical_association
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - knowledge type
    rank: 1000
    is_a: association slot
    domain: association
    alias: knowledge_level
    owner: gene as a model of disease association
    domain_of:
    - association
    range: KnowledgeLevelEnum
    required: true
    multivalued: false
  agent type:
    name: agent type
    description: Describes the high-level category of agent who originally generated
      a statement of knowledge or other type of information.
    notes:
    - Note that this property indicates the type of agent who produced a final statement
      of knowledge, which is often different from the agent oragents who produced
      information used as evidence to support generation of this knowledge. For example,
      if a human curator concludes that a particular gene variant causes a medical
      condition - based on their interpretation of information produced by computational
      modeling tools, automated data analysis pipelines, and robotic laboratory assay
      systems - the agent_type for this statement is 'manual agent' - despite all
      of the evidence being created by automated agents. But if any of these systems
      is programmed to generate knowledge statements directly and without human assistance,
      the statement would be attributed to an 'automated_agent'.
    examples:
    - value: manual_agent
    - value: automated_agent
    - value: computational_model
    - value: text_mining_agent
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: agent_type
    owner: gene as a model of disease association
    domain_of:
    - association
    range: AgentTypeEnum
    required: true
    multivalued: false
  timepoint:
    name: timepoint
    description: a point in time
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - duration
    rank: 1000
    owner: gene as a model of disease association
    domain_of:
    - geographic location at time
    - exposure event
    - association
    range: time type
  original subject:
    name: original subject
    description: used to hold the original subject of a relation (or predicate) that
      an external knowledge source uses before transformation to match the biolink-model
      specification.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: original_subject
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
  original predicate:
    name: original predicate
    id_prefixes:
    - RO
    - BSPO
    - SIO
    description: used to hold the original relation/predicate that an external knowledge
      source uses before transformation to match the biolink-model specification.
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - original relation
    - relation
    rank: 1000
    is_a: association slot
    domain: association
    alias: original_predicate
    owner: gene as a model of disease association
    domain_of:
    - association
    range: uriorcurie
  original object:
    name: original object
    description: used to hold the original object of a relation (or predicate) that
      an external knowledge source uses before transformation to match the biolink-model
      specification.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: original_object
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
  subject feature name:
    name: subject feature name
    description: Used to describe a subordinate feature of the associated subject
      for example, a particular sequence variant of a gene
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: subject_feature_name
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
  object feature name:
    name: object feature name
    description: Used to describe a subordinate feature of the associated object for
      example, a symptom diagnosis of a disease
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: object_feature_name
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
  subject category:
    name: subject category
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the biolink class/category of an association. This is
      a denormalized field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: biolink:Gene
      description: The subject category of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'biolink:Gene'.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: subject_category
    owner: gene as a model of disease association
    domain_of:
    - association
    range: ontology class
    multivalued: false
  object category:
    name: object category
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the biolink class/category of an association. This is
      a denormalized field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: biolink:Disease
      description: The object category of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'biolink:Disease'.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: object_category
    owner: gene as a model of disease association
    domain_of:
    - association
    range: ontology class
    multivalued: false
  subject closure:
    name: subject closure
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the subject closure of an association. This is a denormalized
      field used primarily in the SQL serialization of a knowledge graph via KGX.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: subject_closure
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
    multivalued: true
  object closure:
    name: object closure
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the object closure of an association. This is a denormalized
      field used primarily in the SQL serialization of a knowledge graph via KGX.
    examples:
    - value: '[''MONDO:0000167'', ''MONDO:0005395'']'
      description: 'The object closure of the association between the gene ''BRCA1''
        and the disease ''breast cancer'' is the set of all diseases that are ancestors
        of ''breast cancer'' in the MONDO ontology.  Note: typically the "subclass
        of" and "part of" relations are used to construct the closure, but other relations
        may be used as well.'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: object_closure
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
    multivalued: true
  subject category closure:
    name: subject category closure
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the subject category closure of an association. This
      is a denormalized field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''biolink:Gene'', ''biolink:NamedThing'']'
      description: 'The subject category closure of the association between the gene
        ''BRCA1'' and the disease ''breast cancer'' is the set of all biolink classes
        that are ancestors of ''biolink:Gene'' in the biolink model.  Note: typically
        the "subclass of" and "part of" relations are used to construct the closure,
        but other relations may be used as well.'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: subject_category_closure
    owner: gene as a model of disease association
    domain_of:
    - association
    range: ontology class
    multivalued: true
  object category closure:
    name: object category closure
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the object category closure of an association. This
      is a denormalized field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''biolink:Disease'', ''biolink:NamedThing'']'
      description: 'The object category closure of the association between the gene
        ''BRCA1'' and the disease ''breast cancer'' is the set of all biolink classes
        that are ancestors of ''biolink:Disease'' in the biolink model.  Note: typically
        the "subclass of" and "part of" relations are used to construct the closure,
        but other relations may be used as well.'
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: object_category_closure
    owner: gene as a model of disease association
    domain_of:
    - association
    range: ontology class
    multivalued: true
  subject namespace:
    name: subject namespace
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the subject namespace of an association. This is a denormalized
      field used primarily in the SQL serialization of a knowledge graph via KGX.
    examples:
    - value: NCBIGene
      description: The subject namespace of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'NCBIGene'.
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - subject prefix
    rank: 1000
    is_a: association slot
    domain: association
    alias: subject_namespace
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
    multivalued: false
  object namespace:
    name: object namespace
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the object namespace of an association. This is a denormalized
      field used primarily in the SQL serialization of a knowledge graph via KGX.
    examples:
    - value: MONDO
      description: The object namespace of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'MONDO'.
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - object prefix
    rank: 1000
    is_a: association slot
    domain: association
    alias: object_namespace
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
    multivalued: false
  subject label closure:
    name: subject label closure
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the subject label closure of an association. This is
      a denormalized field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''BRCA1'']'
      description: The subject label closure of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is the set of all labels that are ancestors
        of 'BRCA1' in the biolink model.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: subject_label_closure
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
    multivalued: true
  object label closure:
    name: object label closure
    annotations:
      denormalized:
        tag: denormalized
        value: true
    description: Used to hold the object label closure of an association. This is
      a denormalized field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: breast cancer
      description: The object label closure of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is the set of all labels that are ancestors
        of 'breast cancer' in the biolink model.
    - value: cancer
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: object_label_closure
    owner: gene as a model of disease association
    domain_of:
    - association
    range: string
    multivalued: true
  retrieval source ids:
    name: retrieval source ids
    description: A list of retrieval sources that served as a source of knowledge
      expressed in an Edge, or a source of data used to generate this knowledge.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: retrieval_source_ids
    owner: gene as a model of disease association
    domain_of:
    - association
    range: retrieval source
    multivalued: true
  p value:
    name: p value
    description: A quantitative confidence value that represents the probability of
      obtaining a result at least as extreme as that actually obtained, assuming that
      the actual value was the result of chance alone.
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - unadjusted p value
    exact_mappings:
    - OBI:0000175
    - NCIT:C44185
    - EDAM-DATA:1669
    rank: 1000
    is_a: association slot
    domain: association
    alias: p_value
    owner: gene as a model of disease association
    domain_of:
    - association
    range: float
  adjusted p value:
    name: adjusted p value
    description: The adjusted p-value is the probability of obtaining test results
      at least as extreme as the results actually observed, under the assumption that
      the null hypothesis is correct, adjusted for multiple comparisons. P is always
      italicized and capitalized. The actual P value* should be expressed (P=. 04)
      rather than expressing a statement of inequality (P<. 05), unless P<.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: p value
    domain: association
    alias: adjusted_p_value
    owner: gene as a model of disease association
    domain_of:
    - association
    range: float
  supporting text:
    name: supporting text
    description: The segment of text from a document that supports the mined assertion.
    examples:
    - value: Here, we report two new cases of rivaroxaban-induced hepatitis.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: supporting_text
    owner: gene as a model of disease association
    domain_of:
    - text mining study result
    - association
    range: string
    multivalued: true
  has supporting studies:
    name: has supporting studies
    description: Studies that produced information used as evidence to generate the
      knowledge expressed in an Association.
    from_schema: https://w3id.org/monarch-initiative/namo
    close_mappings:
    - OBAN:has_study_id
    rank: 1000
    is_a: association slot
    domain: association
    alias: has_supporting_studies
    owner: gene as a model of disease association
    domain_of:
    - association
    range: study
    multivalued: true
    inlined: true
  update date:
    name: update date
    description: date on which an entity was updated. This can be applied to nodes
      or edges
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    alias: update_date
    owner: gene as a model of disease association
    domain_of:
    - association
    range: date
  has confidence score:
    name: has confidence score
    description: connects an association to a quantitative (numeric) value that can
      be interpreted as an indicator of the degree of confidence that a piece of information
      is true, and accurately reflects the aspect of reality it is about.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - SEPIO:0000168
    close_mappings:
    - SEPIO:0000187
    - SEPIO:0000167
    rank: 1000
    is_a: association slot
    domain: association
    alias: has_confidence_score
    owner: gene as a model of disease association
    domain_of:
    - association
    range: float
  elevate to prediction:
    name: elevate to prediction
    description: A boolean flag indicating whether a clinical trial finding should
      be elevated to a prediction.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    alias: elevate_to_prediction
    owner: gene as a model of disease association
    domain_of:
    - association
    range: boolean
  evidence count:
    name: evidence count
    description: The number of evidence instances that are connected to an association.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: evidence_count
    owner: gene as a model of disease association
    domain_of:
    - association
    - chemical affects gene association
    - chemical gene sensitivity association
    range: integer
  semmed agreement count:
    name: semmed agreement count
    description: The number of times this concept has been asserted in the SemMedDB
      literature database.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    alias: semmed_agreement_count
    owner: gene as a model of disease association
    domain_of:
    - association
    range: integer
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
    owner: gene as a model of disease association
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
    owner: gene as a model of disease association
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
    owner: gene as a model of disease association
    domain_of:
    - entity
    is_class_field: true
    range: uriorcurie
    required: false
    multivalued: true
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - gff3:type
    - gpi:DB_Object_Type
    rank: 1000
    domain: entity
    slot_uri: rdf:type
    owner: gene as a model of disease association
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
    owner: gene as a model of disease association
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
    owner: gene as a model of disease association
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
    owner: gene as a model of disease association
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
    owner: gene as a model of disease association
    domain_of:
    - entity
    range: boolean
  subject direction qualifier:
    name: subject direction qualifier
    description: 'Composes with the core concept (+ aspect if provided) to describe
      a change in its direction or degree. This qualifier qualifies the subject of
      an association (aka: statement).'
    examples:
    - value: increased
    - value: downregulated
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: direction qualifier
    domain: association
    alias: subject_direction_qualifier
    owner: gene as a model of disease association
    domain_of:
    - predicate mapping
    - gene to gene association
    - macromolecular machine has substrate association
    - chemical affects biological entity association
    - chemical gene sensitivity association
    - gene affects chemical association
    - entity to feature or disease qualifiers mixin
    - entity to feature or variant qualifiers mixin
    - entity to feature or gene qualifiers mixin
    - feature or disease qualifiers to entity mixin
    range: DirectionQualifierEnum
  object aspect qualifier:
    name: object aspect qualifier
    description: 'Composes with the core concept to describe new concepts of a different
      ontological type. e.g. a process in which the core concept participates, a function/activity/role
      held by the core concept, or a characteristic/quality that inheres in the core
      concept.  The purpose of the aspect slot is to indicate what aspect is being
      affected in an ''affects'' association.  This qualifier specifies a change in
      the object of an association (aka: statement).'
    examples:
    - value: stability
    - value: abundance
    - value: expression
    - value: exposure
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: aspect qualifier
    domain: association
    alias: object_aspect_qualifier
    owner: gene as a model of disease association
    domain_of:
    - predicate mapping
    - gene to gene association
    - named thing associated with likelihood of named thing association
    - chemical gene interaction association
    - macromolecular machine has substrate association
    - gene regulates gene association
    - chemical affects biological entity association
    - chemical gene sensitivity association
    - gene affects chemical association
    - entity to feature or disease qualifiers mixin
    - entity to feature or variant qualifiers mixin
    - entity to feature or gene qualifiers mixin
    - feature or disease qualifiers to entity mixin
    range: GeneOrGeneProductOrChemicalEntityAspectEnum
  disease context qualifier:
    name: disease context qualifier
    description: A context qualifier representing a disease or condition in which
      a relationship expressed in an association took place.
    examples:
    - value: MONDO:0004979
      description: asthma
    - value: MONDO:0005148
      description: type 2 diabetes mellitus
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: context qualifier
    domain: association
    alias: disease_context_qualifier
    owner: gene as a model of disease association
    domain_of:
    - entity to feature or disease qualifiers mixin
    - entity to disease or phenotypic feature association mixin
    range: disease
  frequency qualifier:
    name: frequency qualifier
    description: a qualifier used in a phenotypic association to state how frequent
      the phenotype is observed in the subject
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: qualifier
    domain: association
    alias: frequency_qualifier
    owner: gene as a model of disease association
    domain_of:
    - frequency qualifier mixin
    range: frequency value
defining_slots:
- subject
- predicate
- object

```
</details></div>