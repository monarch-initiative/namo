---
search:
  boost: 10.0
---

# Class: RetrievalSource 


_Provides information about how a particular InformationResource served as a source from which knowledge expressed in an Edge, or data used to generate this knowledge, was retrieved._



<div data-search-exclude markdown="1">



URI: [namo:RetrievalSource](https://w3id.org/monarch-initiative/namo/RetrievalSource)





```mermaid
 classDiagram
    class RetrievalSource
    click RetrievalSource href "../RetrievalSource/"
      InformationContentEntity <|-- RetrievalSource
        click InformationContentEntity href "../InformationContentEntity/"
      
      RetrievalSource : broad_synonym
        
      RetrievalSource : category
        
      RetrievalSource : creation_date
        
      RetrievalSource : deprecated
        
      RetrievalSource : description
        
      RetrievalSource : equivalent_identifiers
        
      RetrievalSource : exact_synonym
        
      RetrievalSource : format
        
      RetrievalSource : full_name
        
      RetrievalSource : has_attribute
        
          
    
        
        
        RetrievalSource --> "*" Attribute : has_attribute
        click Attribute href "../Attribute/"
    

        
      RetrievalSource : id
        
      RetrievalSource : information_content
        
      RetrievalSource : iri
        
      RetrievalSource : license
        
      RetrievalSource : name
        
      RetrievalSource : narrow_synonym
        
      RetrievalSource : provided_by
        
      RetrievalSource : related_synonym
        
      RetrievalSource : resource_id
        
      RetrievalSource : resource_role
        
          
    
        
        
        RetrievalSource --> "1" ResourceRoleEnum : resource_role
        click ResourceRoleEnum href "../ResourceRoleEnum/"
    

        
      RetrievalSource : rights
        
      RetrievalSource : source_record_urls
        
      RetrievalSource : synonym
        
      RetrievalSource : taxon
        
      RetrievalSource : type
        
      RetrievalSource : upstream_resource_ids
        
      RetrievalSource : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [InformationContentEntity](InformationContentEntity.md)
            * **RetrievalSource**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [resource_id](resource_id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | The InformationResource that served as a source for the knowledge expressed i... | direct |
| [resource_role](resource_role.md) | 1 <br/> [ResourceRoleEnum](ResourceRoleEnum.md) | The role of the InformationResource in the retrieval of the knowledge express... | direct |
| [upstream_resource_ids](upstream_resource_ids.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A list of upstream InformationResources from which the resource being describ... | direct |
| [source_record_urls](source_record_urls.md) | * <br/> [Uriorcurie](Uriorcurie.md) | One or more URLs that link to a specific web page or document provided by the... | direct |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge... | direct |
| [license](license.md) | 0..1 <br/> [String](String.md) | A legal instrument under which the information content entity is made availab... | [InformationContentEntity](InformationContentEntity.md) |
| [rights](rights.md) | 0..1 <br/> [String](String.md) | A statement describing rights held in or over the information content entity,... | [InformationContentEntity](InformationContentEntity.md) |
| [format](format.md) | 0..1 <br/> [String](String.md) | The file format, physical medium, or representational form of the information... | [InformationContentEntity](InformationContentEntity.md) |
| [creation_date](creation_date.md) | 0..1 <br/> [Date](Date.md) | date on which an entity was created | [InformationContentEntity](InformationContentEntity.md) |
| [provided_by](provided_by.md) | * <br/> [String](String.md) | The value in this node property represents the knowledge provider that create... | [NamedThing](NamedThing.md) |
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





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RetrievalSource](RetrievalSource.md) | [resource_id](resource_id.md) | domain | [RetrievalSource](RetrievalSource.md) |
| [RetrievalSource](RetrievalSource.md) | [resource_role](resource_role.md) | domain | [RetrievalSource](RetrievalSource.md) |
| [RetrievalSource](RetrievalSource.md) | [upstream_resource_ids](upstream_resource_ids.md) | domain | [RetrievalSource](RetrievalSource.md) |
| [RetrievalSource](RetrievalSource.md) | [source_record_urls](source_record_urls.md) | domain | [RetrievalSource](RetrievalSource.md) |
| [Association](Association.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [Association](Association.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ContributorAssociation](ContributorAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ContributorAssociation](ContributorAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [SequenceAssociation](SequenceAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [SequenceAssociation](SequenceAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [sources](sources.md) | range | [RetrievalSource](RetrievalSource.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [retrieval_source_ids](retrieval_source_ids.md) | range | [RetrievalSource](RetrievalSource.md) |











## Examples

| Value |
| --- |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:RetrievalSource |
| native | namo:RetrievalSource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: retrieval source
description: Provides information about how a particular InformationResource served
  as a source from which knowledge expressed in an Edge, or data used to generate
  this knowledge, was retrieved.
examples:
- object:
    id: urn:uuid:id
    category: biolink:RetrievalSource
    resource_id: infores:text-mining-provider-targeted
    resource_role: primary_knowledge_source
    upstream_resource_ids:
    - infores:pubmed
from_schema: https://w3id.org/monarch-initiative/namo
is_a: information content entity
slots:
- resource id
- resource role
- upstream resource ids
- source record urls
- xref
slot_usage:
  resource id:
    name: resource id
    description: The InformationResource that served as a source for the knowledge
      expressed in an Edge, or data used to generate this knowledge.
    required: true
  resource role:
    name: resource role
    description: The role of the InformationResource in the retrieval of the knowledge
      expressed in an Edge, or data used to generate this knowledge.
    required: true
  upstream resource ids:
    name: upstream resource ids
    description: A list of upstream InformationResources from which the resource being
      described directly retrieved a record of the knowledge expressed in the Edge,
      or data used to generate this knowledge.
  source record urls:
    name: source record urls
    description: One or more URLs that link to a specific web page or document provided
      by the InformationResource, that contains a record of the knowledge expressed
      in the Edge.

```
</details>

### Induced

<details>
```yaml
name: retrieval source
description: Provides information about how a particular InformationResource served
  as a source from which knowledge expressed in an Edge, or data used to generate
  this knowledge, was retrieved.
examples:
- object:
    id: urn:uuid:id
    category: biolink:RetrievalSource
    resource_id: infores:text-mining-provider-targeted
    resource_role: primary_knowledge_source
    upstream_resource_ids:
    - infores:pubmed
from_schema: https://w3id.org/monarch-initiative/namo
is_a: information content entity
slot_usage:
  resource id:
    name: resource id
    description: The InformationResource that served as a source for the knowledge
      expressed in an Edge, or data used to generate this knowledge.
    required: true
  resource role:
    name: resource role
    description: The role of the InformationResource in the retrieval of the knowledge
      expressed in an Edge, or data used to generate this knowledge.
    required: true
  upstream resource ids:
    name: upstream resource ids
    description: A list of upstream InformationResources from which the resource being
      described directly retrieved a record of the knowledge expressed in the Edge,
      or data used to generate this knowledge.
  source record urls:
    name: source record urls
    description: One or more URLs that link to a specific web page or document provided
      by the InformationResource, that contains a record of the knowledge expressed
      in the Edge.
attributes:
  resource id:
    name: resource id
    description: The InformationResource that served as a source for the knowledge
      expressed in an Edge, or data used to generate this knowledge.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: retrieval source
    alias: resource_id
    owner: retrieval source
    domain_of:
    - retrieval source
    range: uriorcurie
    required: true
  resource role:
    name: resource role
    description: The role of the InformationResource in the retrieval of the knowledge
      expressed in an Edge, or data used to generate this knowledge.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: retrieval source
    alias: resource_role
    owner: retrieval source
    domain_of:
    - retrieval source
    range: ResourceRoleEnum
    required: true
  upstream resource ids:
    name: upstream resource ids
    description: A list of upstream InformationResources from which the resource being
      described directly retrieved a record of the knowledge expressed in the Edge,
      or data used to generate this knowledge.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: retrieval source
    alias: upstream_resource_ids
    owner: retrieval source
    domain_of:
    - retrieval source
    range: uriorcurie
    multivalued: true
  source record urls:
    name: source record urls
    description: One or more URLs that link to a specific web page or document provided
      by the InformationResource, that contains a record of the knowledge expressed
      in the Edge.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: retrieval source
    alias: source_record_urls
    owner: retrieval source
    domain_of:
    - retrieval source
    range: uriorcurie
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
    owner: retrieval source
    domain_of:
    - named thing
    - publication
    - retrieval source
    - gene
    - gene product mixin
    range: uriorcurie
    multivalued: true
  license:
    name: license
    description: A legal instrument under which the information content entity is
      made available, typically identified by a URL or CURIE pointing to a license
      document.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - dct:license
    narrow_mappings:
    - WIKIDATA_PROPERTY:P275
    rank: 1000
    is_a: node property
    domain: information content entity
    owner: retrieval source
    domain_of:
    - information content entity
    range: string
  rights:
    name: rights
    description: A statement describing rights held in or over the information content
      entity, such as copyright, intellectual property, or access and usage rights.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - dct:rights
    rank: 1000
    is_a: node property
    domain: information content entity
    owner: retrieval source
    domain_of:
    - information content entity
    range: string
  format:
    name: format
    description: The file format, physical medium, or representational form of the
      information content entity; for digital resources typically a MIME type or format
      identifier. Corresponds to dct:format.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - dct:format
    - WIKIDATA_PROPERTY:P2701
    rank: 1000
    is_a: node property
    domain: information content entity
    owner: retrieval source
    domain_of:
    - information content entity
    range: string
  creation date:
    name: creation date
    description: date on which an entity was created. This can be applied to nodes
      or edges
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - publication date
    - date started
    exact_mappings:
    - dct:createdOn
    - WIKIDATA_PROPERTY:P577
    rank: 1000
    is_a: node property
    domain: named thing
    alias: creation_date
    owner: retrieval source
    domain_of:
    - information content entity
    - clinical trial
    range: date
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
    owner: retrieval source
    domain_of:
    - named thing
    range: string
    multivalued: true
  full name:
    name: full name
    description: a long-form human readable name for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    alias: full_name
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
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
    owner: retrieval source
    domain_of:
    - entity
    range: boolean

```
</details></div>