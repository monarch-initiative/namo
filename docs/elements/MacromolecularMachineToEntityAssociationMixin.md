---
search:
  boost: 10.0
---

# Class: MacromolecularMachineToEntityAssociationMixin 


_an association which has a macromolecular machine mixin as a subject_



<div data-search-exclude markdown="1">



URI: [namo:MacromolecularMachineToEntityAssociationMixin](https://w3id.org/monarch-initiative/namo/MacromolecularMachineToEntityAssociationMixin)





```mermaid
 classDiagram
    class MacromolecularMachineToEntityAssociationMixin
    click MacromolecularMachineToEntityAssociationMixin href "../MacromolecularMachineToEntityAssociationMixin/"
      MacromolecularMachineToEntityAssociationMixin <|-- MacromolecularMachineToMolecularActivityAssociation
        click MacromolecularMachineToMolecularActivityAssociation href "../MacromolecularMachineToMolecularActivityAssociation/"
      MacromolecularMachineToEntityAssociationMixin <|-- MacromolecularMachineToBiologicalProcessAssociation
        click MacromolecularMachineToBiologicalProcessAssociation href "../MacromolecularMachineToBiologicalProcessAssociation/"
      MacromolecularMachineToEntityAssociationMixin <|-- MacromolecularMachineToCellularComponentAssociation
        click MacromolecularMachineToCellularComponentAssociation href "../MacromolecularMachineToCellularComponentAssociation/"
      
      MacromolecularMachineToEntityAssociationMixin : object
        
          
    
        
        
        MacromolecularMachineToEntityAssociationMixin --> "1" NamedThing : object
        click NamedThing href "../NamedThing/"
    

        
      MacromolecularMachineToEntityAssociationMixin : predicate
        
      MacromolecularMachineToEntityAssociationMixin : species_context_qualifier
        
          
    
        
        
        MacromolecularMachineToEntityAssociationMixin --> "0..1" OrganismTaxon : species_context_qualifier
        click OrganismTaxon href "../OrganismTaxon/"
    

        
      MacromolecularMachineToEntityAssociationMixin : subject
        
          
    
        
        
        MacromolecularMachineToEntityAssociationMixin --> "1" NamedThing : subject
        click NamedThing href "../NamedThing/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 1 <br/> [NamedThing](NamedThing.md) | connects an association to the subject of the association | direct |
| [predicate](predicate.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Has a value from the Biolink 'related_to' hierarchy | direct |
| [object](object.md) | 1 <br/> [NamedThing](NamedThing.md) | connects an association to the object of the association | direct |
| [species_context_qualifier](species_context_qualifier.md) | 0..1 <br/> [OrganismTaxon](OrganismTaxon.md) | A statement qualifier representing a taxonomic category of species in which a... | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:MacromolecularMachineToEntityAssociationMixin |
| native | namo:MacromolecularMachineToEntityAssociationMixin |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: macromolecular machine to entity association mixin
description: an association which has a macromolecular machine mixin as a subject
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
slots:
- subject
- predicate
- object
- species context qualifier
slot_usage:
  subject:
    name: subject
    domain: macromolecular machine mixin

```
</details>

### Induced

<details>
```yaml
name: macromolecular machine to entity association mixin
description: an association which has a macromolecular machine mixin as a subject
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
slot_usage:
  subject:
    name: subject
    domain: macromolecular machine mixin
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
    domain: macromolecular machine mixin
    slot_uri: rdf:subject
    owner: macromolecular machine to entity association mixin
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
    owner: macromolecular machine to entity association mixin
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
    owner: macromolecular machine to entity association mixin
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
  species context qualifier:
    name: species context qualifier
    description: A statement qualifier representing a taxonomic category of species
      in which a relationship expressed in an association took place.
    notes:
    - Ontology CURIEs are expected as values here, the examples below are intended
      to help clarify the content of the CURIEs.
    examples:
    - value: NCBITaxon:7955
      description: zebrafish
    - value: NCBITaxon:9606
      description: human
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: statement qualifier
    domain: association
    alias: species_context_qualifier
    owner: macromolecular machine to entity association mixin
    domain_of:
    - predicate mapping
    - gene to gene association
    - chemical entity to chemical entity association
    - chemical entity to biological process association
    - chemical gene interaction association
    - macromolecular machine has substrate association
    - gene regulates gene association
    - chemical affects biological entity association
    - chemical gene sensitivity association
    - gene affects chemical association
    - macromolecular machine to entity association mixin
    range: organism taxon

```
</details></div>