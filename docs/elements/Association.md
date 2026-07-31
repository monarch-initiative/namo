---
search:
  boost: 10.0
---

# Class: Association 


_A typed association between two entities, supported by evidence_



<div data-search-exclude markdown="1">



URI: [namo:Association](https://w3id.org/monarch-initiative/namo/Association)





```mermaid
 classDiagram
    class Association
    click Association href "../Association/"
      Entity <|-- Association
        click Entity href "../Entity/"
      

      Association <|-- DiseaseAssociatedWithResponseToChemicalEntityAssociation
        click DiseaseAssociatedWithResponseToChemicalEntityAssociation href "../DiseaseAssociatedWithResponseToChemicalEntityAssociation/"
      Association <|-- ChemicalEntityAssessesNamedThingAssociation
        click ChemicalEntityAssessesNamedThingAssociation href "../ChemicalEntityAssessesNamedThingAssociation/"
      Association <|-- ContributorAssociation
        click ContributorAssociation href "../ContributorAssociation/"
      Association <|-- GenotypeToGenotypePartAssociation
        click GenotypeToGenotypePartAssociation href "../GenotypeToGenotypePartAssociation/"
      Association <|-- GenotypeToGeneAssociation
        click GenotypeToGeneAssociation href "../GenotypeToGeneAssociation/"
      Association <|-- GenotypeToVariantAssociation
        click GenotypeToVariantAssociation href "../GenotypeToVariantAssociation/"
      Association <|-- GeneToGeneAssociation
        click GeneToGeneAssociation href "../GeneToGeneAssociation/"
      Association <|-- GeneToGeneFamilyAssociation
        click GeneToGeneFamilyAssociation href "../GeneToGeneFamilyAssociation/"
      Association <|-- GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation
        click GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation href "../GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation/"
      Association <|-- GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation
        click GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation href "../GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation/"
      Association <|-- BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation
        click BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation href "../BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation/"
      Association <|-- BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation
        click BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation href "../BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation/"
      Association <|-- CellLineToDiseaseOrPhenotypicFeatureAssociation
        click CellLineToDiseaseOrPhenotypicFeatureAssociation href "../CellLineToDiseaseOrPhenotypicFeatureAssociation/"
      Association <|-- ChemicalEntityToChemicalEntityAssociation
        click ChemicalEntityToChemicalEntityAssociation href "../ChemicalEntityToChemicalEntityAssociation/"
      Association <|-- ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation
        click ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation href "../ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation/"
      Association <|-- ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation
        click ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation href "../ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation/"
      Association <|-- ChemicalOrDrugOrTreatmentAdverseEventAssociation
        click ChemicalOrDrugOrTreatmentAdverseEventAssociation href "../ChemicalOrDrugOrTreatmentAdverseEventAssociation/"
      Association <|-- ChemicalOrDrugOrTreatmentSideEffectAssociation
        click ChemicalOrDrugOrTreatmentSideEffectAssociation href "../ChemicalOrDrugOrTreatmentSideEffectAssociation/"
      Association <|-- GeneToPathwayAssociation
        click GeneToPathwayAssociation href "../GeneToPathwayAssociation/"
      Association <|-- MolecularActivityToPathwayAssociation
        click MolecularActivityToPathwayAssociation href "../MolecularActivityToPathwayAssociation/"
      Association <|-- ChemicalEntityToPathwayAssociation
        click ChemicalEntityToPathwayAssociation href "../ChemicalEntityToPathwayAssociation/"
      Association <|-- ChemicalEntityToBiologicalProcessAssociation
        click ChemicalEntityToBiologicalProcessAssociation href "../ChemicalEntityToBiologicalProcessAssociation/"
      Association <|-- NamedThingAssociatedWithLikelihoodOfNamedThingAssociation
        click NamedThingAssociatedWithLikelihoodOfNamedThingAssociation href "../NamedThingAssociatedWithLikelihoodOfNamedThingAssociation/"
      Association <|-- ChemicalGeneInteractionAssociation
        click ChemicalGeneInteractionAssociation href "../ChemicalGeneInteractionAssociation/"
      Association <|-- MacromolecularMachineHasSubstrateAssociation
        click MacromolecularMachineHasSubstrateAssociation href "../MacromolecularMachineHasSubstrateAssociation/"
      Association <|-- GeneRegulatesGeneAssociation
        click GeneRegulatesGeneAssociation href "../GeneRegulatesGeneAssociation/"
      Association <|-- ProcessRegulatesProcessAssociation
        click ProcessRegulatesProcessAssociation href "../ProcessRegulatesProcessAssociation/"
      Association <|-- ChemicalAffectsBiologicalEntityAssociation
        click ChemicalAffectsBiologicalEntityAssociation href "../ChemicalAffectsBiologicalEntityAssociation/"
      Association <|-- ChemicalGeneSensitivityAssociation
        click ChemicalGeneSensitivityAssociation href "../ChemicalGeneSensitivityAssociation/"
      Association <|-- GeneAffectsChemicalAssociation
        click GeneAffectsChemicalAssociation href "../GeneAffectsChemicalAssociation/"
      Association <|-- DrugToGeneAssociation
        click DrugToGeneAssociation href "../DrugToGeneAssociation/"
      Association <|-- MaterialSampleDerivationAssociation
        click MaterialSampleDerivationAssociation href "../MaterialSampleDerivationAssociation/"
      Association <|-- MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
        click MaterialSampleToDiseaseOrPhenotypicFeatureAssociation href "../MaterialSampleToDiseaseOrPhenotypicFeatureAssociation/"
      Association <|-- DiseaseToExposureEventAssociation
        click DiseaseToExposureEventAssociation href "../DiseaseToExposureEventAssociation/"
      Association <|-- ExposureEventToOutcomeAssociation
        click ExposureEventToOutcomeAssociation href "../ExposureEventToOutcomeAssociation/"
      Association <|-- PhenotypicFeatureToPhenotypicFeatureAssociation
        click PhenotypicFeatureToPhenotypicFeatureAssociation href "../PhenotypicFeatureToPhenotypicFeatureAssociation/"
      Association <|-- InformationContentEntityToNamedThingAssociation
        click InformationContentEntityToNamedThingAssociation href "../InformationContentEntityToNamedThingAssociation/"
      Association <|-- DiseaseOrPhenotypicFeatureToLocationAssociation
        click DiseaseOrPhenotypicFeatureToLocationAssociation href "../DiseaseOrPhenotypicFeatureToLocationAssociation/"
      Association <|-- DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation
        click DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation href "../DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation/"
      Association <|-- GenotypeToPhenotypicFeatureAssociation
        click GenotypeToPhenotypicFeatureAssociation href "../GenotypeToPhenotypicFeatureAssociation/"
      Association <|-- ExposureEventToPhenotypicFeatureAssociation
        click ExposureEventToPhenotypicFeatureAssociation href "../ExposureEventToPhenotypicFeatureAssociation/"
      Association <|-- DiseaseToPhenotypicFeatureAssociation
        click DiseaseToPhenotypicFeatureAssociation href "../DiseaseToPhenotypicFeatureAssociation/"
      Association <|-- DiseaseToDiseaseAssociation
        click DiseaseToDiseaseAssociation href "../DiseaseToDiseaseAssociation/"
      Association <|-- CaseToPhenotypicFeatureAssociation
        click CaseToPhenotypicFeatureAssociation href "../CaseToPhenotypicFeatureAssociation/"
      Association <|-- CaseToDiseaseAssociation
        click CaseToDiseaseAssociation href "../CaseToDiseaseAssociation/"
      Association <|-- CaseToVariantAssociation
        click CaseToVariantAssociation href "../CaseToVariantAssociation/"
      Association <|-- CaseToGeneAssociation
        click CaseToGeneAssociation href "../CaseToGeneAssociation/"
      Association <|-- BehaviorToBehavioralFeatureAssociation
        click BehaviorToBehavioralFeatureAssociation href "../BehaviorToBehavioralFeatureAssociation/"
      Association <|-- GeneToPhenotypicFeatureAssociation
        click GeneToPhenotypicFeatureAssociation href "../GeneToPhenotypicFeatureAssociation/"
      Association <|-- GeneToDiseaseAssociation
        click GeneToDiseaseAssociation href "../GeneToDiseaseAssociation/"
      Association <|-- CausalGeneToDiseaseAssociation
        click CausalGeneToDiseaseAssociation href "../CausalGeneToDiseaseAssociation/"
      Association <|-- CorrelatedGeneToDiseaseAssociation
        click CorrelatedGeneToDiseaseAssociation href "../CorrelatedGeneToDiseaseAssociation/"
      Association <|-- PhenotypicFeatureToDiseaseAssociation
        click PhenotypicFeatureToDiseaseAssociation href "../PhenotypicFeatureToDiseaseAssociation/"
      Association <|-- VariantToGeneAssociation
        click VariantToGeneAssociation href "../VariantToGeneAssociation/"
      Association <|-- VariantToPopulationAssociation
        click VariantToPopulationAssociation href "../VariantToPopulationAssociation/"
      Association <|-- PopulationToPopulationAssociation
        click PopulationToPopulationAssociation href "../PopulationToPopulationAssociation/"
      Association <|-- VariantToPhenotypicFeatureAssociation
        click VariantToPhenotypicFeatureAssociation href "../VariantToPhenotypicFeatureAssociation/"
      Association <|-- VariantToDiseaseAssociation
        click VariantToDiseaseAssociation href "../VariantToDiseaseAssociation/"
      Association <|-- GenotypeToDiseaseAssociation
        click GenotypeToDiseaseAssociation href "../GenotypeToDiseaseAssociation/"
      Association <|-- OrganismalEntityAsAModelOfDiseaseAssociation
        click OrganismalEntityAsAModelOfDiseaseAssociation href "../OrganismalEntityAsAModelOfDiseaseAssociation/"
      Association <|-- OrganismToOrganismAssociation
        click OrganismToOrganismAssociation href "../OrganismToOrganismAssociation/"
      Association <|-- TaxonToTaxonAssociation
        click TaxonToTaxonAssociation href "../TaxonToTaxonAssociation/"
      Association <|-- GeneToExpressionSiteAssociation
        click GeneToExpressionSiteAssociation href "../GeneToExpressionSiteAssociation/"
      Association <|-- SequenceVariantModulatesTreatmentAssociation
        click SequenceVariantModulatesTreatmentAssociation href "../SequenceVariantModulatesTreatmentAssociation/"
      Association <|-- FunctionalAssociation
        click FunctionalAssociation href "../FunctionalAssociation/"
      Association <|-- MolecularActivityToChemicalEntityAssociation
        click MolecularActivityToChemicalEntityAssociation href "../MolecularActivityToChemicalEntityAssociation/"
      Association <|-- MolecularActivityToMolecularActivityAssociation
        click MolecularActivityToMolecularActivityAssociation href "../MolecularActivityToMolecularActivityAssociation/"
      Association <|-- EntityToDiseaseAssociation
        click EntityToDiseaseAssociation href "../EntityToDiseaseAssociation/"
      Association <|-- EntityToPhenotypicFeatureAssociation
        click EntityToPhenotypicFeatureAssociation href "../EntityToPhenotypicFeatureAssociation/"
      Association <|-- SequenceAssociation
        click SequenceAssociation href "../SequenceAssociation/"
      Association <|-- SequenceFeatureRelationship
        click SequenceFeatureRelationship href "../SequenceFeatureRelationship/"
      Association <|-- ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation
        click ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation href "../ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation/"
      Association <|-- AnatomicalEntityToAnatomicalEntityAssociation
        click AnatomicalEntityToAnatomicalEntityAssociation href "../AnatomicalEntityToAnatomicalEntityAssociation/"
      Association <|-- GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation
        click GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation href "../GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation/"
      Association <|-- BiologicalProcessOrActivityToAnatomicalEntityAssociation
        click BiologicalProcessOrActivityToAnatomicalEntityAssociation href "../BiologicalProcessOrActivityToAnatomicalEntityAssociation/"
      Association <|-- OrganismTaxonToOrganismTaxonAssociation
        click OrganismTaxonToOrganismTaxonAssociation href "../OrganismTaxonToOrganismTaxonAssociation/"
      Association <|-- OrganismTaxonToEnvironmentAssociation
        click OrganismTaxonToEnvironmentAssociation href "../OrganismTaxonToEnvironmentAssociation/"
      

      Association : adjusted_p_value
        
      Association : agent_type
        
          
    
        
        
        Association --> "1" AgentTypeEnum : agent_type
        click AgentTypeEnum href "../AgentTypeEnum/"
    

        
      Association : aggregator_knowledge_source
        
      Association : category
        
      Association : deprecated
        
      Association : description
        
      Association : elevate_to_prediction
        
      Association : evidence_count
        
      Association : has_attribute
        
          
    
        
        
        Association --> "*" Attribute : has_attribute
        click Attribute href "../Attribute/"
    

        
      Association : has_confidence_score
        
      Association : has_evidence
        
          
    
        
        
        Association --> "*" InformationContentEntity : has_evidence
        click InformationContentEntity href "../InformationContentEntity/"
    

        
      Association : has_evidence_of_type
        
          
    
        
        
        Association --> "*" EvidenceType : has_evidence_of_type
        click EvidenceType href "../EvidenceType/"
    

        
      Association : has_supporting_studies
        
          
    
        
        
        Association --> "*" Study : has_supporting_studies
        click Study href "../Study/"
    

        
      Association : id
        
      Association : iri
        
      Association : knowledge_level
        
          
    
        
        
        Association --> "1" KnowledgeLevelEnum : knowledge_level
        click KnowledgeLevelEnum href "../KnowledgeLevelEnum/"
    

        
      Association : knowledge_source
        
      Association : name
        
      Association : negated
        
      Association : object
        
          
    
        
        
        Association --> "1" NamedThing : object
        click NamedThing href "../NamedThing/"
    

        
      Association : object_category
        
          
    
        
        
        Association --> "0..1" OntologyClass : object_category
        click OntologyClass href "../OntologyClass/"
    

        
      Association : object_category_closure
        
          
    
        
        
        Association --> "*" OntologyClass : object_category_closure
        click OntologyClass href "../OntologyClass/"
    

        
      Association : object_closure
        
      Association : object_feature_name
        
      Association : object_label_closure
        
      Association : object_namespace
        
      Association : original_object
        
      Association : original_predicate
        
      Association : original_subject
        
      Association : p_value
        
      Association : predicate
        
      Association : primary_knowledge_source
        
      Association : publications
        
          
    
        
        
        Association --> "*" Publication : publications
        click Publication href "../Publication/"
    

        
      Association : qualifier
        
      Association : qualifiers
        
          
    
        
        
        Association --> "*" OntologyClass : qualifiers
        click OntologyClass href "../OntologyClass/"
    

        
      Association : retrieval_source_ids
        
          
    
        
        
        Association --> "*" RetrievalSource : retrieval_source_ids
        click RetrievalSource href "../RetrievalSource/"
    

        
      Association : semmed_agreement_count
        
      Association : sources
        
          
    
        
        
        Association --> "*" RetrievalSource : sources
        click RetrievalSource href "../RetrievalSource/"
    

        
      Association : subject
        
          
    
        
        
        Association --> "1" NamedThing : subject
        click NamedThing href "../NamedThing/"
    

        
      Association : subject_category
        
          
    
        
        
        Association --> "0..1" OntologyClass : subject_category
        click OntologyClass href "../OntologyClass/"
    

        
      Association : subject_category_closure
        
          
    
        
        
        Association --> "*" OntologyClass : subject_category_closure
        click OntologyClass href "../OntologyClass/"
    

        
      Association : subject_closure
        
      Association : subject_feature_name
        
      Association : subject_label_closure
        
      Association : subject_namespace
        
      Association : supporting_text
        
      Association : timepoint
        
      Association : type
        
      Association : update_date
        
      
```





## Inheritance
* [Entity](Entity.md)
    * **Association**
        * [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md)
        * [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md)
        * [ContributorAssociation](ContributorAssociation.md)
        * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)
        * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)
        * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)
        * [GeneToGeneAssociation](GeneToGeneAssociation.md)
        * [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md)
        * [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md)
        * [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md)
        * [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md)
        * [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md)
        * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) [ [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)]
        * [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md)
        * [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) [ [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)]
        * [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) [ [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md)]
        * [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) [ [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md)]
        * [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) [ [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md)]
        * [GeneToPathwayAssociation](GeneToPathwayAssociation.md) [ [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)]
        * [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md)
        * [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md)
        * [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md)
        * [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md)
        * [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md)
        * [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md)
        * [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md)
        * [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md)
        * [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md)
        * [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md)
        * [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md)
        * [DrugToGeneAssociation](DrugToGeneAssociation.md) [ [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md)]
        * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md)
        * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) [ [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)]
        * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) [ [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md)]
        * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) [ [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md)]
        * [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) [ [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)]
        * [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md)
        * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) [ [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md)]
        * [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) [ [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md)]
        * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md)]
        * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)]
        * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) [ [FrequencyQuantifier](FrequencyQuantifier.md) [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md)]
        * [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) [ [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md)]
        * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md)]
        * [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) [ [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md)]
        * [CaseToVariantAssociation](CaseToVariantAssociation.md) [ [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md)]
        * [CaseToGeneAssociation](CaseToGeneAssociation.md) [ [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md)]
        * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)]
        * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)]
        * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) [ [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)]
        * [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) [ [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)]
        * [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) [ [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)]
        * [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) [ [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md)]
        * [VariantToGeneAssociation](VariantToGeneAssociation.md) [ [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md)]
        * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) [ [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) [FrequencyQuantifier](FrequencyQuantifier.md) [FrequencyQualifierMixin](FrequencyQualifierMixin.md)]
        * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)
        * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) [ [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)]
        * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) [ [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md)]
        * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) [ [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md) [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md)]
        * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) [ [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md)]
        * [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md)
        * [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md)
        * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)
        * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)
        * [FunctionalAssociation](FunctionalAssociation.md)
        * [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md)
        * [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md)
        * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md)
        * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
        * [SequenceAssociation](SequenceAssociation.md)
        * [SequenceFeatureRelationship](SequenceFeatureRelationship.md)
        * [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md)
        * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
        * [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md)
        * [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md)
        * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) [ [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md)]
        * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) [ [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 1 <br/> [NamedThing](NamedThing.md) | connects an association to the subject of the association | direct |
| [predicate](predicate.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Has a value from the Biolink 'related_to' hierarchy | direct |
| [object](object.md) | 1 <br/> [NamedThing](NamedThing.md) | connects an association to the object of the association | direct |
| [negated](negated.md) | 0..1 <br/> [Boolean](Boolean.md) | if set to true, then the association is negated i | direct |
| [qualifier](qualifier.md) | 0..1 <br/> [String](String.md) | grouping slot for all qualifiers on an edge | direct |
| [qualifiers](qualifiers.md) | * <br/> [OntologyClass](OntologyClass.md) | connects an association to qualifiers that modify or qualify the meaning of t... | direct |
| [publications](publications.md) | * <br/> [Publication](Publication.md) | One or more publications that report the statement expressed in an Associatio... | direct |
| [sources](sources.md) | * <br/> [RetrievalSource](RetrievalSource.md) | A set of RetrievalSources, which traces where the statement expressed in an A... | direct |
| [has_evidence_of_type](has_evidence_of_type.md) | * <br/> [EvidenceType](EvidenceType.md) | Connects an association to an evidence type ontology term | direct |
| [has_evidence](has_evidence.md) | * <br/> [InformationContentEntity](InformationContentEntity.md) | Connects an association to detailed information providing supporting evidence | direct |
| [knowledge_source](knowledge_source.md) | 0..1 <br/> [String](String.md) | An Information Resource from which the knowledge expressed in an Association ... | direct |
| [primary_knowledge_source](primary_knowledge_source.md) | 0..1 <br/> [String](String.md) | The most upstream source of the knowledge expressed in an Association that an... | direct |
| [aggregator_knowledge_source](aggregator_knowledge_source.md) | * <br/> [String](String.md) | An intermediate aggregator resource from which knowledge expressed in an Asso... | direct |
| [knowledge_level](knowledge_level.md) | 1 <br/> [KnowledgeLevelEnum](KnowledgeLevelEnum.md) | Describes the level of knowledge expressed in a statement, based on the reaso... | direct |
| [agent_type](agent_type.md) | 1 <br/> [AgentTypeEnum](AgentTypeEnum.md) | Describes the high-level category of agent who originally generated a stateme... | direct |
| [timepoint](timepoint.md) | 0..1 <br/> [TimeType](TimeType.md) | a point in time | direct |
| [original_subject](original_subject.md) | 0..1 <br/> [String](String.md) | used to hold the original subject of a relation (or predicate) that an extern... | direct |
| [original_predicate](original_predicate.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | used to hold the original relation/predicate that an external knowledge sourc... | direct |
| [original_object](original_object.md) | 0..1 <br/> [String](String.md) | used to hold the original object of a relation (or predicate) that an externa... | direct |
| [subject_feature_name](subject_feature_name.md) | 0..1 <br/> [String](String.md) | Used to describe a subordinate feature of the associated subject for example,... | direct |
| [object_feature_name](object_feature_name.md) | 0..1 <br/> [String](String.md) | Used to describe a subordinate feature of the associated object for example, ... | direct |
| [subject_category](subject_category.md) | 0..1 <br/> [OntologyClass](OntologyClass.md) | Used to hold the biolink class/category of an association | direct |
| [object_category](object_category.md) | 0..1 <br/> [OntologyClass](OntologyClass.md) | Used to hold the biolink class/category of an association | direct |
| [subject_closure](subject_closure.md) | * <br/> [String](String.md) | Used to hold the subject closure of an association | direct |
| [object_closure](object_closure.md) | * <br/> [String](String.md) | Used to hold the object closure of an association | direct |
| [subject_category_closure](subject_category_closure.md) | * <br/> [OntologyClass](OntologyClass.md) | Used to hold the subject category closure of an association | direct |
| [object_category_closure](object_category_closure.md) | * <br/> [OntologyClass](OntologyClass.md) | Used to hold the object category closure of an association | direct |
| [subject_namespace](subject_namespace.md) | 0..1 <br/> [String](String.md) | Used to hold the subject namespace of an association | direct |
| [object_namespace](object_namespace.md) | 0..1 <br/> [String](String.md) | Used to hold the object namespace of an association | direct |
| [subject_label_closure](subject_label_closure.md) | * <br/> [String](String.md) | Used to hold the subject label closure of an association | direct |
| [object_label_closure](object_label_closure.md) | * <br/> [String](String.md) | Used to hold the object label closure of an association | direct |
| [retrieval_source_ids](retrieval_source_ids.md) | * <br/> [RetrievalSource](RetrievalSource.md) | A list of retrieval sources that served as a source of knowledge expressed in... | direct |
| [p_value](p_value.md) | 0..1 <br/> [Float](Float.md) | A quantitative confidence value that represents the probability of obtaining ... | direct |
| [adjusted_p_value](adjusted_p_value.md) | 0..1 <br/> [Float](Float.md) | The adjusted p-value is the probability of obtaining test results at least as... | direct |
| [supporting_text](supporting_text.md) | * <br/> [String](String.md) | The segment of text from a document that supports the mined assertion | direct |
| [has_supporting_studies](has_supporting_studies.md) | * <br/> [Study](Study.md) | Studies that produced information used as evidence to generate the knowledge ... | direct |
| [update_date](update_date.md) | 0..1 <br/> [Date](Date.md) | date on which an entity was updated | direct |
| [has_confidence_score](has_confidence_score.md) | 0..1 <br/> [Float](Float.md) | connects an association to a quantitative (numeric) value that can be interpr... | direct |
| [elevate_to_prediction](elevate_to_prediction.md) | 0..1 <br/> [Boolean](Boolean.md) | A boolean flag indicating whether a clinical trial finding should be elevated... | direct |
| [evidence_count](evidence_count.md) | 0..1 <br/> [Integer](Integer.md) | The number of evidence instances that are connected to an association | direct |
| [semmed_agreement_count](semmed_agreement_count.md) | 0..1 <br/> [Integer](Integer.md) | The number of times this concept has been asserted in the SemMedDB literature... | direct |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md) |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md) |
| [category](category.md) | * <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | * <br/> [String](String.md) | rdf:type of biolink:Association should be fixed at rdf:Statement | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | * <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |
| [deprecated](deprecated.md) | 0..1 <br/> [Boolean](Boolean.md) | A boolean flag indicating that an entity is no longer considered current or v... | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [KnowledgeGraph](KnowledgeGraph.md) | [edges](edges.md) | range | [Association](Association.md) |
| [KnowledgeGraph](KnowledgeGraph.md) | [edges](edges.md) | range | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_derivative_qualifier](object_derivative_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [TextMiningStudyResult](TextMiningStudyResult.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [TextMiningStudyResult](TextMiningStudyResult.md) | [subject_location_in_text](subject_location_in_text.md) | domain | [Association](Association.md) |
| [TextMiningStudyResult](TextMiningStudyResult.md) | [object_location_in_text](object_location_in_text.md) | domain | [Association](Association.md) |
| [TextMiningStudyResult](TextMiningStudyResult.md) | [extraction_confidence_score](extraction_confidence_score.md) | domain | [Association](Association.md) |
| [TextMiningStudyResult](TextMiningStudyResult.md) | [supporting_document_type](supporting_document_type.md) | domain | [Association](Association.md) |
| [TextMiningStudyResult](TextMiningStudyResult.md) | [supporting_document_year](supporting_document_year.md) | domain | [Association](Association.md) |
| [TextMiningStudyResult](TextMiningStudyResult.md) | [supporting_text_section_type](supporting_text_section_type.md) | domain | [Association](Association.md) |
| [IceesStudyResult](IceesStudyResult.md) | [chi_squared_statistic](chi_squared_statistic.md) | domain | [Association](Association.md) |
| [IceesStudyResult](IceesStudyResult.md) | [chi_squared_dof](chi_squared_dof.md) | domain | [Association](Association.md) |
| [IceesStudyResult](IceesStudyResult.md) | [chi_squared_p](chi_squared_p.md) | domain | [Association](Association.md) |
| [IceesStudyResult](IceesStudyResult.md) | [total_sample_size](total_sample_size.md) | domain | [Association](Association.md) |
| [IceesStudyResult](IceesStudyResult.md) | [fisher_exact_odds_ratio](fisher_exact_odds_ratio.md) | domain | [Association](Association.md) |
| [IceesStudyResult](IceesStudyResult.md) | [fisher_exact_p](fisher_exact_p.md) | domain | [Association](Association.md) |
| [IceesStudyResult](IceesStudyResult.md) | [log_odds_ratio](log_odds_ratio.md) | domain | [Association](Association.md) |
| [IceesStudyResult](IceesStudyResult.md) | [log_odds_ratio_95_ci](log_odds_ratio_95_ci.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object](object.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [response_context_qualifier](response_context_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [response_target_context_qualifier](response_target_context_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_activity_qualifier](subject_activity_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_process_qualifier](subject_process_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_activity_qualifier](object_activity_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_process_qualifier](object_process_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_activity_qualifier](subject_activity_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_process_qualifier](subject_process_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_activity_qualifier](object_activity_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_process_qualifier](object_process_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | [Association](Association.md) |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [expression_site](expression_site.md) | domain | [Association](Association.md) |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [stage_qualifier](stage_qualifier.md) | domain | [Association](Association.md) |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [phenotypic_state](phenotypic_state.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [expression_site](expression_site.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [stage_qualifier](stage_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [phenotypic_state](phenotypic_state.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_activity_qualifier](subject_activity_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_process_qualifier](subject_process_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_activity_qualifier](object_activity_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_process_qualifier](object_process_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_activity_qualifier](subject_activity_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_process_qualifier](subject_process_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object](object.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_activity_qualifier](object_activity_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_process_qualifier](object_process_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [interacting_molecules_category](interacting_molecules_category.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_activity_qualifier](subject_activity_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_process_qualifier](subject_process_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object](object.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_activity_qualifier](object_activity_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_process_qualifier](object_process_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_specialization_qualifier](subject_specialization_qualifier.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_specialization_qualifier](object_specialization_qualifier.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [stoichiometry](stoichiometry.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [reaction_direction](reaction_direction.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [reaction_side](reaction_side.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [stoichiometry](stoichiometry.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [reaction_direction](reaction_direction.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [reaction_side](reaction_side.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [catalyst_qualifier](catalyst_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [clinical_approval_status](clinical_approval_status.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [max_research_phase](max_research_phase.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_specialization_qualifier](subject_specialization_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [object_specialization_qualifier](object_specialization_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_specialization_qualifier](subject_specialization_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_specialization_qualifier](object_specialization_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [FDA_adverse_event_level](FDA_adverse_event_level.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject_specialization_qualifier](subject_specialization_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object_specialization_qualifier](object_specialization_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject_specialization_qualifier](subject_specialization_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object_specialization_qualifier](object_specialization_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [population_context_qualifier](population_context_qualifier.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [has_affinity](has_affinity.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [supporting_documents](supporting_documents.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_derivative_qualifier](object_derivative_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [supporting_documents](supporting_documents.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_derivative_qualifier](object_derivative_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_specialization_qualifier](subject_specialization_qualifier.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_specialization_qualifier](object_specialization_qualifier.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [population_context_qualifier](population_context_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [temporal_context_qualifier](temporal_context_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrVariantQualifiersMixin](EntityToFeatureOrVariantQualifiersMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrGeneQualifiersMixin](EntityToFeatureOrGeneQualifiersMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [FeatureOrDiseaseQualifiersToEntityMixin](FeatureOrDiseaseQualifiersToEntityMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) | [subject_specialization_qualifier](subject_specialization_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) | [object_specialization_qualifier](object_specialization_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [allelic_requirement](allelic_requirement.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [allelic_requirement](allelic_requirement.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [allelic_requirement](allelic_requirement.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [z_score](z_score.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [allelic_requirement](allelic_requirement.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [allelic_requirement](allelic_requirement.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [expression_site](expression_site.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [stage_qualifier](stage_qualifier.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [phenotypic_state](phenotypic_state.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [allelic_requirement](allelic_requirement.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_specialization_qualifier](subject_specialization_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_specialization_qualifier](object_specialization_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [disease_context_qualifier](disease_context_qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [allelic_requirement](allelic_requirement.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [stage_qualifier](stage_qualifier.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_specialization_qualifier](object_specialization_qualifier.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToEntityAssociationMixin](MacromolecularMachineToEntityAssociationMixin.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToEntityAssociationMixin](MacromolecularMachineToEntityAssociationMixin.md) | [object](object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToEntityAssociationMixin](MacromolecularMachineToEntityAssociationMixin.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [clinical_approval_status](clinical_approval_status.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [max_research_phase](max_research_phase.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [clinical_approval_status](clinical_approval_status.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [max_research_phase](max_research_phase.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object](object.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object](object.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object](object.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [associated_environmental_context](associated_environmental_context.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [qualifier](qualifier.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [sources](sources.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_evidence_of_type](has_evidence_of_type.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [knowledge_level](knowledge_level.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [agent_type](agent_type.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_feature_name](subject_feature_name.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_feature_name](object_feature_name.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [p_value](p_value.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [adjusted_p_value](adjusted_p_value.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [supporting_text](supporting_text.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_supporting_studies](has_supporting_studies.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_confidence_score](has_confidence_score.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [evidence_count](evidence_count.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [semmed_agreement_count](semmed_agreement_count.md) | domain | [Association](Association.md) |











## Examples

| Value |
| --- |
| None |
| None |
| None |

## Comments

* This is roughly the model used by biolink and ontobio at the moment



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:Association |
| native | namo:Association |
| exact | OBAN:association, rdf:Statement, owl:Axiom |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: association
description: A typed association between two entities, supported by evidence
comments:
- This is roughly the model used by biolink and ontobio at the moment
examples:
- object:
    subject: NCBIGene:6910
    predicate: biolink:acts_upstream_of
    object: GO:1901846
    category: biolink:Association
    knowledge_level: knowledge_assertion
    agent_type: manual_agent
    publications:
    - PMID:15289437
- object:
    subject: NCBIGene:4357
    predicate: biolink:enables
    object: GO:0005515
    category: biolink:Association
    knowledge_level: knowledge_assertion
    agent_type: manual_agent
    publications:
    - PMID:32296183
- object:
    subject: CHEBI:114566
    predicate: biolink:subclass_of
    object: CHEBI:38166
    category: biolink:Association
    knowledge_level: knowledge_assertion
    agent_type: manual_agent
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- OBAN:association
- rdf:Statement
- owl:Axiom
is_a: entity
slots:
- subject
- predicate
- object
- negated
- qualifier
- qualifiers
- publications
- sources
- has evidence of type
- has evidence
- knowledge source
- primary knowledge source
- aggregator knowledge source
- knowledge level
- agent type
- timepoint
- original subject
- original predicate
- original object
- subject feature name
- object feature name
- subject category
- object category
- subject closure
- object closure
- subject category closure
- object category closure
- subject namespace
- object namespace
- subject label closure
- object label closure
- retrieval source ids
- p value
- adjusted p value
- supporting text
- has supporting studies
- update date
- has confidence score
- elevate to prediction
- evidence count
- semmed agreement count
slot_usage:
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
  category:
    name: category
    range: uriorcurie
    required: false
  sources:
    name: sources
    inlined_as_list: true
  has supporting studies:
    name: has supporting studies
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: association
description: A typed association between two entities, supported by evidence
comments:
- This is roughly the model used by biolink and ontobio at the moment
examples:
- object:
    subject: NCBIGene:6910
    predicate: biolink:acts_upstream_of
    object: GO:1901846
    category: biolink:Association
    knowledge_level: knowledge_assertion
    agent_type: manual_agent
    publications:
    - PMID:15289437
- object:
    subject: NCBIGene:4357
    predicate: biolink:enables
    object: GO:0005515
    category: biolink:Association
    knowledge_level: knowledge_assertion
    agent_type: manual_agent
    publications:
    - PMID:32296183
- object:
    subject: CHEBI:114566
    predicate: biolink:subclass_of
    object: CHEBI:38166
    category: biolink:Association
    knowledge_level: knowledge_assertion
    agent_type: manual_agent
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- OBAN:association
- rdf:Statement
- owl:Axiom
is_a: entity
slot_usage:
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
  category:
    name: category
    range: uriorcurie
    required: false
  sources:
    name: sources
    inlined_as_list: true
  has supporting studies:
    name: has supporting studies
    inlined: true
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
    description: connects an association to the subject of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedSource
    - OBAN:association_has_subject
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    owner: association
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
    range: named thing
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
    description: Has a value from the Biolink 'related_to' hierarchy. In RDF,  this
      corresponds to rdf:predicate and in Neo4j this corresponds to the relationship
      type. The convention is for an edge label in snake_case form. For example, biolink:related_to,
      biolink:causes, biolink:treats
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedProperty
    - OBAN:association_has_predicate
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:predicate
    owner: association
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
    range: uriorcurie
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
    description: connects an association to the object of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedTarget
    - OBAN:association_has_object
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:object
    owner: association
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
    range: named thing
    required: true
  negated:
    name: negated
    description: if set to true, then the association is negated i.e. is not true
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: association slot
    domain: association
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
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
    owner: association
    domain_of:
    - entity
    range: boolean

```
</details></div>