---
search:
  boost: 10.0
---

# Class: DiseaseToEntityAssociationMixin 


_A mixin applied to any association whose subject (source node) is a disease._



<div data-search-exclude markdown="1">



URI: [namo:DiseaseToEntityAssociationMixin](https://w3id.org/monarch-initiative/namo/DiseaseToEntityAssociationMixin)





```mermaid
 classDiagram
    class DiseaseToEntityAssociationMixin
    click DiseaseToEntityAssociationMixin href "../DiseaseToEntityAssociationMixin/"
      DiseaseToEntityAssociationMixin <|-- DiseaseToExposureEventAssociation
        click DiseaseToExposureEventAssociation href "../DiseaseToExposureEventAssociation/"
      DiseaseToEntityAssociationMixin <|-- DiseaseToPhenotypicFeatureAssociation
        click DiseaseToPhenotypicFeatureAssociation href "../DiseaseToPhenotypicFeatureAssociation/"
      DiseaseToEntityAssociationMixin <|-- DiseaseToDiseaseAssociation
        click DiseaseToDiseaseAssociation href "../DiseaseToDiseaseAssociation/"
      
      DiseaseToEntityAssociationMixin : object
        
          
    
        
        
        DiseaseToEntityAssociationMixin --> "1" NamedThing : object
        click NamedThing href "../NamedThing/"
    

        
      DiseaseToEntityAssociationMixin : predicate
        
      DiseaseToEntityAssociationMixin : subject
        
          
    
        
        
        DiseaseToEntityAssociationMixin --> "1" Disease : subject
        click Disease href "../Disease/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 1 <br/> [Disease](Disease.md) | disease class | direct |
| [predicate](predicate.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Has a value from the Biolink 'related_to' hierarchy | direct |
| [object](object.md) | 1 <br/> [NamedThing](NamedThing.md) | connects an association to the object of the association | direct |

## Defining Slots

This class is defined by the following slots:


* [subject](subject.md)



## Mixin Usage

| mixed into | description |
| --- | --- |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | An association between an exposure event and a disease |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenot... |
| [DiseaseToDiseaseAssociation](DiseaseToDiseaseAssociation.md) | An association between two diseases |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:DiseaseToEntityAssociationMixin |
| native | namo:DiseaseToEntityAssociationMixin |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: disease to entity association mixin
description: A mixin applied to any association whose subject (source node) is a disease.
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
slots:
- subject
- predicate
- object
slot_usage:
  subject:
    name: subject
    description: disease class
    examples:
    - value: MONDO:0017314
      description: Ehlers-Danlos syndrome, vascular type
    values_from:
    - mondo
    - omim
    - orphanet
    - ncit
    - doid
    range: disease
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: disease to entity association mixin
description: A mixin applied to any association whose subject (source node) is a disease.
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
slot_usage:
  subject:
    name: subject
    description: disease class
    examples:
    - value: MONDO:0017314
      description: Ehlers-Danlos syndrome, vascular type
    values_from:
    - mondo
    - omim
    - orphanet
    - ncit
    - doid
    range: disease
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
    description: disease class
    examples:
    - value: MONDO:0017314
      description: Ehlers-Danlos syndrome, vascular type
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedSource
    - OBAN:association_has_subject
    rank: 1000
    is_a: association slot
    values_from:
    - mondo
    - omim
    - orphanet
    - ncit
    - doid
    domain: association
    slot_uri: rdf:subject
    owner: disease to entity association mixin
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
    owner: disease to entity association mixin
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
    owner: disease to entity association mixin
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
defining_slots:
- subject

```
</details></div>