---
search:
  boost: 10.0
---

# Class: Attribute 


_A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material._



<div data-search-exclude markdown="1">



URI: [namo:Attribute](https://w3id.org/monarch-initiative/namo/Attribute)





```mermaid
 classDiagram
    class Attribute
    click Attribute href "../Attribute/"
      OntologyClass <|-- Attribute
        click OntologyClass href "../OntologyClass/"
      NamedThing <|-- Attribute
        click NamedThing href "../NamedThing/"
      

      Attribute <|-- ChemicalRole
        click ChemicalRole href "../ChemicalRole/"
      Attribute <|-- BiologicalSex
        click BiologicalSex href "../BiologicalSex/"
      Attribute <|-- SeverityValue
        click SeverityValue href "../SeverityValue/"
      Attribute <|-- OrganismAttribute
        click OrganismAttribute href "../OrganismAttribute/"
      Attribute <|-- Zygosity
        click Zygosity href "../Zygosity/"
      Attribute <|-- ClinicalAttribute
        click ClinicalAttribute href "../ClinicalAttribute/"
      Attribute <|-- SocioeconomicAttribute
        click SocioeconomicAttribute href "../SocioeconomicAttribute/"
      

      Attribute : broad_synonym
        
      Attribute : category
        
      Attribute : deprecated
        
      Attribute : description
        
      Attribute : equivalent_identifiers
        
      Attribute : exact_synonym
        
      Attribute : full_name
        
      Attribute : has_attribute
        
          
    
        
        
        Attribute --> "*" Attribute : has_attribute
        click Attribute href "../Attribute/"
    

        
      Attribute : has_attribute_type
        
          
    
        
        
        Attribute --> "1" OntologyClass : has_attribute_type
        click OntologyClass href "../OntologyClass/"
    

        
      Attribute : has_qualitative_value
        
          
    
        
        
        Attribute --> "0..1" NamedThing : has_qualitative_value
        click NamedThing href "../NamedThing/"
    

        
      Attribute : has_quantitative_value
        
          
    
        
        
        Attribute --> "*" QuantityValue : has_quantitative_value
        click QuantityValue href "../QuantityValue/"
    

        
      Attribute : id
        
      Attribute : information_content
        
      Attribute : iri
        
      Attribute : name
        
      Attribute : narrow_synonym
        
      Attribute : provided_by
        
      Attribute : related_synonym
        
      Attribute : subsets
        
      Attribute : synonym
        
      Attribute : taxon
        
      Attribute : type
        
      Attribute : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * **Attribute** [ [OntologyClass](OntologyClass.md)]
            * [ChemicalRole](ChemicalRole.md)
            * [BiologicalSex](BiologicalSex.md)
            * [SeverityValue](SeverityValue.md)
            * [OrganismAttribute](OrganismAttribute.md)
            * [Zygosity](Zygosity.md)
            * [ClinicalAttribute](ClinicalAttribute.md)
            * [SocioeconomicAttribute](SocioeconomicAttribute.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | The human-readable 'attribute name' can be set to a string which reflects its... | direct |
| [has_attribute_type](has_attribute_type.md) | 1 <br/> [OntologyClass](OntologyClass.md) | connects an attribute to a class that describes it | direct |
| [has_quantitative_value](has_quantitative_value.md) | * <br/> [QuantityValue](QuantityValue.md) | connects an attribute to a value | direct |
| [has_qualitative_value](has_qualitative_value.md) | 0..1 <br/> [NamedThing](NamedThing.md) | connects an attribute to a value | direct |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | direct |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md), [OntologyClass](OntologyClass.md) |
| [subsets](subsets.md) | * <br/> [String](String.md) | The set of ontology subsets a term belongs to (e | [OntologyClass](OntologyClass.md) |
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
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | * <br/> [String](String.md) | An rdf:type property asserting that an entity is an instance of a particular ... | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | * <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |
| [deprecated](deprecated.md) | 0..1 <br/> [Boolean](Boolean.md) | A boolean flag indicating that an entity is no longer considered current or v... | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NAMDataset](NAMDataset.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NAMStudy](NAMStudy.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ModelSystem](ModelSystem.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnimalModel](AnimalModel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NAMModel](NAMModel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellularSystem](CellularSystem.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TwoDCellCulture](TwoDCellCulture.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ThreeDCellCulture](ThreeDCellCulture.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CoCulture](CoCulture.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Organoid](Organoid.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellLineModel](CellLineModel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MicrophysiologicalSystem](MicrophysiologicalSystem.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganOnChip](OrganOnChip.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TissueOnChip](TissueOnChip.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [InSilicoModel](InSilicoModel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [QSARModel](QSARModel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PBPKModel](PBPKModel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DigitalTwin](DigitalTwin.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MLModel](MLModel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MetabolicModel](MetabolicModel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PBPKCompartment](PBPKCompartment.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MicrofluidicDesign](MicrofluidicDesign.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MechanicalStimulation](MechanicalStimulation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalSystem](BiologicalSystem.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularSimilarity](MolecularSimilarity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathwayConcordance](PathwayConcordance.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhenotypeOverlap](PhenotypeOverlap.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellTypeCoverage](CellTypeCoverage.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [FunctionalParity](FunctionalParity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Reproducibility](Reproducibility.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneExpressionResult](GeneExpressionResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathwayActivityResult](PathwayActivityResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [FunctionalAssay](FunctionalAssay.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Attribute](Attribute.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [Attribute](Attribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [Attribute](Attribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [Attribute](Attribute.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalRole](ChemicalRole.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ChemicalRole](ChemicalRole.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ChemicalRole](ChemicalRole.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ChemicalRole](ChemicalRole.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalSex](BiologicalSex.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [BiologicalSex](BiologicalSex.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [BiologicalSex](BiologicalSex.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [BiologicalSex](BiologicalSex.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhenotypicSex](PhenotypicSex.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicSex](PhenotypicSex.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicSex](PhenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicSex](PhenotypicSex.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypicSex](GenotypicSex.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [GenotypicSex](GenotypicSex.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [GenotypicSex](GenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [GenotypicSex](GenotypicSex.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SeverityValue](SeverityValue.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [SeverityValue](SeverityValue.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [SeverityValue](SeverityValue.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [SeverityValue](SeverityValue.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Entity](Entity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NamedThing](NamedThing.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxon](OrganismTaxon.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Event](Event.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AdministrativeEntity](AdministrativeEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [StudyResult](StudyResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [LogOddsAnalysisResult](LogOddsAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TextMiningStudyResult](TextMiningStudyResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [IceesStudyResult](IceesStudyResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Study](Study.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [StudyVariable](StudyVariable.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CommonDataElement](CommonDataElement.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Agent](Agent.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [InformationContentEntity](InformationContentEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Dataset](Dataset.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DatasetDistribution](DatasetDistribution.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DatasetVersion](DatasetVersion.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DatasetSummary](DatasetSummary.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ConfidenceLevel](ConfidenceLevel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EvidenceType](EvidenceType.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Evidence](Evidence.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Publication](Publication.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Book](Book.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BookChapter](BookChapter.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Serial](Serial.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Article](Article.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [JournalArticle](JournalArticle.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Patent](Patent.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [WebPage](WebPage.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PreprintPublication](PreprintPublication.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DrugLabel](DrugLabel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RetrievalSource](RetrievalSource.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhysicalEntity](PhysicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Activity](Activity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Procedure](Procedure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Phenomenon](Phenomenon.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Device](Device.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiagnosticAid](DiagnosticAid.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [StudyPopulation](StudyPopulation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MaterialSample](MaterialSample.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PlanetaryEntity](PlanetaryEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeographicLocation](GeographicLocation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalEntity](BiologicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularEntity](MolecularEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntity](ChemicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AffinityMeasurement](AffinityMeasurement.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SmallMolecule](SmallMolecule.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalMixture](ChemicalMixture.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RegulatoryRegion](RegulatoryRegion.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularMixture](MolecularMixture.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularActivity](MolecularActivity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalProcess](BiologicalProcess.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Pathway](Pathway.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Behavior](Behavior.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Drug](Drug.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [FoodAdditive](FoodAdditive.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Food](Food.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismAttribute](OrganismAttribute.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [OrganismAttribute](OrganismAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [OrganismAttribute](OrganismAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [OrganismAttribute](OrganismAttribute.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneticInheritance](GeneticInheritance.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismalEntity](OrganismalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Bacterium](Bacterium.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Virus](Virus.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellularOrganism](CellularOrganism.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Mammal](Mammal.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Human](Human.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Plant](Plant.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Invertebrate](Invertebrate.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Vertebrate](Vertebrate.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Fungus](Fungus.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [LifeStage](LifeStage.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [IndividualOrganism](IndividualOrganism.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Disease](Disease.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhenotypicFeature](PhenotypicFeature.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BehavioralFeature](BehavioralFeature.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnatomicalEntity](AnatomicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellularComponent](CellularComponent.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Cell](Cell.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellLine](CellLine.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Gene](Gene.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MacromolecularComplex](MacromolecularComplex.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NucleosomeModification](NucleosomeModification.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Genome](Genome.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Exon](Exon.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Transcript](Transcript.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CodingSequence](CodingSequence.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Polypeptide](Polypeptide.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Protein](Protein.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ProteinIsoform](ProteinIsoform.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ProteinDomain](ProteinDomain.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PosttranslationalModification](PosttranslationalModification.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ProteinFamily](ProteinFamily.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RNAProduct](RNAProduct.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MicroRNA](MicroRNA.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SiRNA](SiRNA.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneFamily](GeneFamily.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Zygosity](Zygosity.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [Zygosity](Zygosity.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [Zygosity](Zygosity.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [Zygosity](Zygosity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Genotype](Genotype.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Haplotype](Haplotype.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SequenceVariant](SequenceVariant.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Snv](Snv.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalModifier](ClinicalModifier.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ClinicalModifier](ClinicalModifier.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalModifier](ClinicalModifier.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalModifier](ClinicalModifier.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalCourse](ClinicalCourse.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ClinicalCourse](ClinicalCourse.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalCourse](ClinicalCourse.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalCourse](ClinicalCourse.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Onset](Onset.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [Onset](Onset.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [Onset](Onset.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [Onset](Onset.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalEntity](ClinicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalTrial](ClinicalTrial.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalIntervention](ClinicalIntervention.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Hospitalization](Hospitalization.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Case](Case.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Cohort](Cohort.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ExposureEvent](ExposureEvent.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathologicalProcess](PathologicalProcess.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalExposure](ChemicalExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ChemicalExposure](ChemicalExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DrugExposure](DrugExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [DrugExposure](DrugExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Treatment](Treatment.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BioticExposure](BioticExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeographicExposure](GeographicExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BehavioralExposure](BehavioralExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Association](Association.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ContributorAssociation](ContributorAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation](GeneFamilyToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation](GeneOrGeneProductOrGeneFamilyToBiologicalProcessOrActivityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation](BiologicalProcessOrActivityToGeneOrGeneProductOrGeneFamilyAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation](BiologicalProcessOrActivityToBiologicalProcessOrActivityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntityToChemicalEntityAssociation](ChemicalEntityToChemicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntityToChemicalDerivationAssociation](ChemicalEntityToChemicalDerivationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ProcessRegulatesProcessAssociation](ProcessRegulatesProcessAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhenotypicFeatureToPhenotypicFeatureAssociation](PhenotypicFeatureToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CaseToDiseaseAssociation](CaseToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CaseToVariantAssociation](CaseToVariantAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CaseToGeneAssociation](CaseToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhenotypicFeatureToDiseaseAssociation](PhenotypicFeatureToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SequenceAssociation](SequenceAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnatomicalEntityHasPartAnatomicalEntityAssociation](AnatomicalEntityHasPartAnatomicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnatomicalEntityPartOfAnatomicalEntityAssociation](AnatomicalEntityPartOfAnatomicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation](GeneOrGeneProductOrGeneFamilyToAnatomicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalProcessOrActivityToAnatomicalEntityAssociation](BiologicalProcessOrActivityToAnatomicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |








## In Subsets


* [Samples](Samples.md)






## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* EDAM-DATA

* EDAM-FORMAT

* EDAM-OPERATION

* EDAM-TOPIC







### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:Attribute |
| native | namo:Attribute |
| exact | SIO:000614 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: attribute
id_prefixes:
- EDAM-DATA
- EDAM-FORMAT
- EDAM-OPERATION
- EDAM-TOPIC
description: A property or characteristic of an entity. For example, an apple may
  have properties such as color, shape, age, crispiness. An environmental sample may
  have attributes such as depth, lat, long, material.
in_subset:
- samples
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- SIO:000614
is_a: named thing
mixins:
- ontology class
slots:
- name
- has attribute type
- has quantitative value
- has qualitative value
- iri
slot_usage:
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.

```
</details>

### Induced

<details>
```yaml
name: attribute
id_prefixes:
- EDAM-DATA
- EDAM-FORMAT
- EDAM-OPERATION
- EDAM-TOPIC
description: A property or characteristic of an entity. For example, an apple may
  have properties such as color, shape, age, crispiness. An environmental sample may
  have attributes such as depth, lat, long, material.
in_subset:
- samples
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- SIO:000614
is_a: named thing
mixins:
- ontology class
slot_usage:
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.
attributes:
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.
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
    owner: attribute
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: label type
  has attribute type:
    name: has attribute type
    description: connects an attribute to a class that describes it
    in_subset:
    - samples
    from_schema: https://w3id.org/monarch-initiative/namo
    narrow_mappings:
    - LOINC:has_modality_type
    - LOINC:has_view_type
    rank: 1000
    domain: attribute
    alias: has_attribute_type
    owner: attribute
    domain_of:
    - attribute
    range: ontology class
    required: true
    multivalued: false
  has quantitative value:
    name: has quantitative value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - qud:quantityValue
    narrow_mappings:
    - SNOMED:has_concentration_strength_numerator_value
    - SNOMED:has_presentation_strength_denominator_value
    - SNOMED:has_presentation_strength_numerator_value
    rank: 1000
    domain: attribute
    alias: has_quantitative_value
    owner: attribute
    domain_of:
    - attribute
    - chemical exposure
    range: quantity value
    multivalued: true
  has qualitative value:
    name: has qualitative value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain: attribute
    alias: has_qualitative_value
    owner: attribute
    domain_of:
    - attribute
    range: named thing
    multivalued: false
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
    owner: attribute
    domain_of:
    - attribute
    - entity
    range: iri type
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
    owner: attribute
    domain_of:
    - Reference
    - ontology class
    - entity
    range: string
    required: true
  subsets:
    name: subsets
    description: The set of ontology subsets a term belongs to (e.g. GO slim subsets,
      MONDO rare disease subset). Carries the values of `oboInOwl:inSubset` annotations
      from source ontologies through to downstream knowledge graphs.
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - oboInOwl:inSubset
    rank: 1000
    is_a: node property
    domain: named thing
    owner: attribute
    domain_of:
    - ontology class
    range: string
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
    domain_of:
    - named thing
    range: uriorcurie
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
    owner: attribute
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
    owner: attribute
    domain_of:
    - entity
    range: string
    multivalued: true
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
    owner: attribute
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
    owner: attribute
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
    owner: attribute
    domain_of:
    - entity
    range: boolean

```
</details></div>