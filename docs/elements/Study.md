---
search:
  boost: 10.0
---

# Class: Study 


_a detailed investigation and/or analysis_



<div data-search-exclude markdown="1">



URI: [namo:Study](https://w3id.org/monarch-initiative/namo/Study)





```mermaid
 classDiagram
    class Study
    click Study href "../Study/"
      Activity <|-- Study
        click Activity href "../Activity/"
      

      Study <|-- NAMStudy
        click NAMStudy href "../NAMStudy/"
      Study <|-- ClinicalTrial
        click ClinicalTrial href "../ClinicalTrial/"
      

      Study : broad_synonym
        
      Study : category
        
      Study : deprecated
        
      Study : description
        
      Study : equivalent_identifiers
        
      Study : exact_synonym
        
      Study : full_name
        
      Study : has_attribute
        
          
    
        
        
        Study --> "*" Attribute : has_attribute
        click Attribute href "../Attribute/"
    

        
      Study : has_study_results
        
          
    
        
        
        Study --> "*" StudyResult : has_study_results
        click StudyResult href "../StudyResult/"
    

        
      Study : id
        
      Study : information_content
        
      Study : iri
        
      Study : name
        
      Study : narrow_synonym
        
      Study : provided_by
        
      Study : related_synonym
        
      Study : synonym
        
      Study : taxon
        
      Study : type
        
      Study : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [Activity](Activity.md) [ [ActivityAndBehavior](ActivityAndBehavior.md)]
            * **Study**
                * [NAMStudy](NAMStudy.md)
                * [ClinicalTrial](ClinicalTrial.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_study_results](has_study_results.md) | * <br/> [StudyResult](StudyResult.md) | Connects an study to instances of its study result | direct |
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





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NAMStudy](NAMStudy.md) | [has_study_results](has_study_results.md) | domain | [Study](Study.md) |
| [Study](Study.md) | [has_study_results](has_study_results.md) | domain | [Study](Study.md) |
| [ClinicalTrial](ClinicalTrial.md) | [has_study_results](has_study_results.md) | domain | [Study](Study.md) |
| [Association](Association.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ContributorAssociation](ContributorAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [SequenceAssociation](SequenceAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | range | [Study](Study.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:Study |
| native | namo:Study |
| exact | NCIT:C63536 |
| narrow | SIO:000994 |
| close | SIO:001066, SEPIO:0000004 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: study
description: a detailed investigation and/or analysis
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- NCIT:C63536
close_mappings:
- SIO:001066
- SEPIO:0000004
narrow_mappings:
- SIO:000994
is_a: activity
slots:
- has study results

```
</details>

### Induced

<details>
```yaml
name: study
description: a detailed investigation and/or analysis
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- NCIT:C63536
close_mappings:
- SIO:001066
- SEPIO:0000004
narrow_mappings:
- SIO:000994
is_a: activity
attributes:
  has study results:
    name: has study results
    description: Connects an study to instances of its study result
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: study
    alias: has_study_results
    owner: study
    domain_of:
    - study
    range: study result
    multivalued: true
    inlined: true
    inlined_as_list: true
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
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
    owner: study
    domain_of:
    - entity
    range: boolean

```
</details></div>