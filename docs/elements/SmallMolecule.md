---
search:
  boost: 10.0
---

# Class: SmallMolecule 


_A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion)._



<div data-search-exclude markdown="1">



URI: [namo:SmallMolecule](https://w3id.org/monarch-initiative/namo/SmallMolecule)





```mermaid
 classDiagram
    class SmallMolecule
    click SmallMolecule href "../SmallMolecule/"
      MolecularEntity <|-- SmallMolecule
        click MolecularEntity href "../MolecularEntity/"
      
      SmallMolecule : available_from
        
          
    
        
        
        SmallMolecule --> "*" DrugAvailabilityEnum : available_from
        click DrugAvailabilityEnum href "../DrugAvailabilityEnum/"
    

        
      SmallMolecule : broad_synonym
        
      SmallMolecule : category
        
      SmallMolecule : chembl_availability_type
        
      SmallMolecule : chembl_black_box_warning
        
      SmallMolecule : chembl_chirality
        
      SmallMolecule : chembl_drug_warning
        
      SmallMolecule : chembl_natural_product
        
      SmallMolecule : chembl_prodrug
        
      SmallMolecule : deprecated
        
      SmallMolecule : description
        
      SmallMolecule : equivalent_identifiers
        
      SmallMolecule : exact_synonym
        
      SmallMolecule : full_name
        
      SmallMolecule : has_attribute
        
          
    
        
        
        SmallMolecule --> "*" Attribute : has_attribute
        click Attribute href "../Attribute/"
    

        
      SmallMolecule : has_chemical_role
        
          
    
        
        
        SmallMolecule --> "*" ChemicalRole : has_chemical_role
        click ChemicalRole href "../ChemicalRole/"
    

        
      SmallMolecule : id
        
      SmallMolecule : information_content
        
      SmallMolecule : iri
        
      SmallMolecule : is_metabolite
        
      SmallMolecule : is_toxic
        
      SmallMolecule : max_tolerated_dose
        
      SmallMolecule : name
        
      SmallMolecule : narrow_synonym
        
      SmallMolecule : provided_by
        
      SmallMolecule : related_synonym
        
      SmallMolecule : routes_of_delivery
        
          
    
        
        
        SmallMolecule --> "*" DrugDeliveryEnum : routes_of_delivery
        click DrugDeliveryEnum href "../DrugDeliveryEnum/"
    

        
      SmallMolecule : subsets
        
      SmallMolecule : synonym
        
      SmallMolecule : taxon
        
      SmallMolecule : trade_name
        
      SmallMolecule : type
        
      SmallMolecule : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [ChemicalEntity](ChemicalEntity.md) [ [PhysicalEssence](PhysicalEssence.md) [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md) [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) [ChemicalEntityOrProteinOrPolypeptide](ChemicalEntityOrProteinOrPolypeptide.md)]
            * [MolecularEntity](MolecularEntity.md) [ [OntologyClass](OntologyClass.md)]
                * **SmallMolecule**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [is_metabolite](is_metabolite.md) | 0..1 <br/> [Boolean](Boolean.md) | indicates whether a molecular entity is a metabolite | [MolecularEntity](MolecularEntity.md) |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md), [OntologyClass](OntologyClass.md) |
| [subsets](subsets.md) | * <br/> [String](String.md) | The set of ontology subsets a term belongs to (e | [OntologyClass](OntologyClass.md) |
| [trade_name](trade_name.md) | 0..1 <br/> [String](String.md) | A proprietary brand or trade name under which a chemical entity (typically a ... | [ChemicalEntity](ChemicalEntity.md) |
| [available_from](available_from.md) | * <br/> [DrugAvailabilityEnum](DrugAvailabilityEnum.md) | The regulatory or commercial availability channel through which a drug or che... | [ChemicalEntity](ChemicalEntity.md) |
| [max_tolerated_dose](max_tolerated_dose.md) | 0..1 <br/> [String](String.md) | The highest dose of a drug or treatment that does not cause unacceptable side... | [ChemicalEntity](ChemicalEntity.md) |
| [is_toxic](is_toxic.md) | 0..1 <br/> [Boolean](Boolean.md) | A boolean flag indicating whether a chemical entity is toxic under ordinary c... | [ChemicalEntity](ChemicalEntity.md) |
| [has_chemical_role](has_chemical_role.md) | * <br/> [ChemicalRole](ChemicalRole.md) | A role is particular behaviour which a chemical entity may exhibit | [ChemicalEntity](ChemicalEntity.md) |
| [routes_of_delivery](routes_of_delivery.md) | * <br/> [DrugDeliveryEnum](DrugDeliveryEnum.md) | the method or process of administering a pharmaceutical compound to achieve a... | [ChemicalEntity](ChemicalEntity.md) |
| [chembl_prodrug](chembl_prodrug.md) | 0..1 <br/> [Boolean](Boolean.md) | Flag indicating if a drug is a prodrug that is active only after being metabo... | [ChemicalEntity](ChemicalEntity.md) |
| [chembl_black_box_warning](chembl_black_box_warning.md) | 0..1 <br/> [String](String.md) | Text describing black box warnings for use of chemicals as therapeutics | [ChemicalEntity](ChemicalEntity.md) |
| [chembl_natural_product](chembl_natural_product.md) | 0..1 <br/> [Boolean](Boolean.md) | Flag indicating if a chemical entity is a natural product | [ChemicalEntity](ChemicalEntity.md) |
| [chembl_availability_type](chembl_availability_type.md) | 0..1 <br/> [String](String.md) | Text indicating the availability type of the chemical entity | [ChemicalEntity](ChemicalEntity.md) |
| [chembl_chirality](chembl_chirality.md) | 0..1 <br/> [String](String.md) | Tern indicating the chirality of the chemical entity | [ChemicalEntity](ChemicalEntity.md) |
| [chembl_drug_warning](chembl_drug_warning.md) | 0..1 <br/> [String](String.md) | Text describing warnings for use of chemicals as therapeutics | [ChemicalEntity](ChemicalEntity.md) |
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
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md) |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | * <br/> [String](String.md) | An rdf:type property asserting that an entity is an instance of a particular ... | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | * <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |
| [deprecated](deprecated.md) | 0..1 <br/> [Boolean](Boolean.md) | A boolean flag indicating that an entity is no longer considered current or v... | [Entity](Entity.md) |











## In Subsets


* [ModelOrganismDatabase](ModelOrganismDatabase.md)
* [TranslatorMinimal](TranslatorMinimal.md)



## Aliases


* chemical substance




## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CHEBI

* UNII

* PUBCHEM.COMPOUND

* CHEMBL.COMPOUND

* DRUGBANK

* MESH

* CAS

* DrugCentral

* GTOPDB

* HMDB

* KEGG.COMPOUND

* PHARMGKB.DRUG

* ChemBank

* PUBCHEM.SUBSTANCE

* SIDER.DRUG

* INCHI

* INCHIKEY

* BIGG.METABOLITE

* foodb.compound

* KEGG.GLYCAN

* KEGG.DRUG

* KEGG.ENVIRON

* KEGG

* UMLS







### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:SmallMolecule |
| native | namo:SmallMolecule |
| narrow | STY:T196, CHEBI:59999, bioschemas:ChemicalSubstance, STY:T125, STY:T197, STY:T109, STY:T118, STY:T111, STY:T119, STY:T124, STY:T115, STY:T110, STY:T127 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: small molecule
id_prefixes:
- CHEBI
- UNII
- PUBCHEM.COMPOUND
- CHEMBL.COMPOUND
- DRUGBANK
- MESH
- CAS
- DrugCentral
- GTOPDB
- HMDB
- KEGG.COMPOUND
- PHARMGKB.DRUG
- ChemBank
- PUBCHEM.SUBSTANCE
- SIDER.DRUG
- INCHI
- INCHIKEY
- BIGG.METABOLITE
- foodb.compound
- KEGG.GLYCAN
- KEGG.DRUG
- KEGG.ENVIRON
- KEGG
- UMLS
description: A small molecule entity is a molecular entity characterized by availability
  in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation
  of its precise chemical structure; for convenience of representation, any valid
  chemical representation is included, even if it is not strictly molecular (e.g.,
  sodium ion).
in_subset:
- model_organism_database
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- chemical substance
narrow_mappings:
- STY:T196
- CHEBI:59999
- bioschemas:ChemicalSubstance
- STY:T125
- STY:T197
- STY:T109
- STY:T118
- STY:T111
- STY:T119
- STY:T124
- STY:T115
- STY:T110
- STY:T127
is_a: molecular entity

```
</details>

### Induced

<details>
```yaml
name: small molecule
id_prefixes:
- CHEBI
- UNII
- PUBCHEM.COMPOUND
- CHEMBL.COMPOUND
- DRUGBANK
- MESH
- CAS
- DrugCentral
- GTOPDB
- HMDB
- KEGG.COMPOUND
- PHARMGKB.DRUG
- ChemBank
- PUBCHEM.SUBSTANCE
- SIDER.DRUG
- INCHI
- INCHIKEY
- BIGG.METABOLITE
- foodb.compound
- KEGG.GLYCAN
- KEGG.DRUG
- KEGG.ENVIRON
- KEGG
- UMLS
description: A small molecule entity is a molecular entity characterized by availability
  in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation
  of its precise chemical structure; for convenience of representation, any valid
  chemical representation is included, even if it is not strictly molecular (e.g.,
  sodium ion).
in_subset:
- model_organism_database
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- chemical substance
narrow_mappings:
- STY:T196
- CHEBI:59999
- bioschemas:ChemicalSubstance
- STY:T125
- STY:T197
- STY:T109
- STY:T118
- STY:T111
- STY:T119
- STY:T124
- STY:T115
- STY:T110
- STY:T127
is_a: molecular entity
attributes:
  is metabolite:
    name: is metabolite
    description: indicates whether a molecular entity is a metabolite
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - CHEBI:25212
    rank: 1000
    is_a: node property
    domain: molecular entity
    alias: is_metabolite
    owner: small molecule
    domain_of:
    - molecular entity
    range: boolean
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
    owner: small molecule
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
    owner: small molecule
    domain_of:
    - ontology class
    range: string
    multivalued: true
  trade name:
    name: trade name
    description: A proprietary brand or trade name under which a chemical entity (typically
      a drug) is manufactured and marketed by a vendor.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: chemical entity
    alias: trade_name
    owner: small molecule
    domain_of:
    - chemical entity
    range: string
  available from:
    name: available from
    description: The regulatory or commercial availability channel through which a
      drug or chemical entity can be obtained, drawn from DrugAvailabilityEnum.
    examples:
    - value: over_the_counter
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    alias: available_from
    owner: small molecule
    domain_of:
    - chemical entity
    range: DrugAvailabilityEnum
    multivalued: true
  max tolerated dose:
    name: max tolerated dose
    description: The highest dose of a drug or treatment that does not cause unacceptable
      side effects. The maximum tolerated dose is determined in clinical trials by
      testing increasing doses on different groups of people until the highest dose
      with acceptable side effects is found. Also called MTD.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    alias: max_tolerated_dose
    owner: small molecule
    domain_of:
    - chemical entity
    range: string
    multivalued: false
  is toxic:
    name: is toxic
    description: A boolean flag indicating whether a chemical entity is toxic under
      ordinary conditions of exposure.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: node property
    domain: named thing
    alias: is_toxic
    owner: small molecule
    domain_of:
    - chemical entity
    range: boolean
    multivalued: false
  has chemical role:
    name: has chemical role
    id_prefixes:
    - CHEBI
    description: A role is particular behaviour which a chemical entity may exhibit.
    comments:
    - We expect primarily to use CHEBI chemical roles here; however, we are looking
      for a mapping between CHEBI And ATC codes to support this slot.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: related to at concept level
    domain: chemical entity
    inherited: true
    alias: has_chemical_role
    owner: small molecule
    domain_of:
    - chemical entity
    inverse: is chemical role of
    range: chemical role
    multivalued: true
  routes of delivery:
    name: routes of delivery
    description: the method or process of administering a pharmaceutical compound
      to achieve a therapeutic effect in humans or animals.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: routes_of_delivery
    owner: small molecule
    domain_of:
    - chemical entity
    range: DrugDeliveryEnum
    multivalued: true
  chembl prodrug:
    name: chembl prodrug
    description: Flag indicating if a drug is a prodrug that is active only after
      being metabolized by the body.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: chembl_prodrug
    owner: small molecule
    domain_of:
    - chemical entity
    range: boolean
  chembl black box warning:
    name: chembl black box warning
    description: Text describing black box warnings for use of chemicals as therapeutics.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: chembl_black_box_warning
    owner: small molecule
    domain_of:
    - chemical entity
    range: string
  chembl natural product:
    name: chembl natural product
    description: Flag indicating if a chemical entity is a natural product.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: chembl_natural_product
    owner: small molecule
    domain_of:
    - chemical entity
    range: boolean
  chembl availability type:
    name: chembl availability type
    description: Text indicating the availability type of the chemical entity.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: chembl_availability_type
    owner: small molecule
    domain_of:
    - chemical entity
    range: string
  chembl chirality:
    name: chembl chirality
    description: Tern indicating the chirality of the chemical entity.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: chembl_chirality
    owner: small molecule
    domain_of:
    - chemical entity
    range: string
  chembl drug warning:
    name: chembl drug warning
    description: Text describing warnings for use of chemicals as therapeutics.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: chembl_drug_warning
    owner: small molecule
    domain_of:
    - chemical entity
    range: string
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
    domain_of:
    - named thing
    range: uriorcurie
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
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
    owner: small molecule
    domain_of:
    - entity
    range: boolean

```
</details></div>