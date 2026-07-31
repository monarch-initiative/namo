---
search:
  boost: 10.0
---

# Class: ModelToDiseaseAssociationMixin 


_This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease_



<div data-search-exclude markdown="1">



URI: [namo:ModelToDiseaseAssociationMixin](https://w3id.org/monarch-initiative/namo/ModelToDiseaseAssociationMixin)





```mermaid
 classDiagram
    class ModelToDiseaseAssociationMixin
    click ModelToDiseaseAssociationMixin href "../ModelToDiseaseAssociationMixin/"
      ModelToDiseaseAssociationMixin <|-- GeneAsAModelOfDiseaseAssociation
        click GeneAsAModelOfDiseaseAssociation href "../GeneAsAModelOfDiseaseAssociation/"
      ModelToDiseaseAssociationMixin <|-- VariantAsAModelOfDiseaseAssociation
        click VariantAsAModelOfDiseaseAssociation href "../VariantAsAModelOfDiseaseAssociation/"
      ModelToDiseaseAssociationMixin <|-- GenotypeAsAModelOfDiseaseAssociation
        click GenotypeAsAModelOfDiseaseAssociation href "../GenotypeAsAModelOfDiseaseAssociation/"
      ModelToDiseaseAssociationMixin <|-- CellLineAsAModelOfDiseaseAssociation
        click CellLineAsAModelOfDiseaseAssociation href "../CellLineAsAModelOfDiseaseAssociation/"
      ModelToDiseaseAssociationMixin <|-- OrganismalEntityAsAModelOfDiseaseAssociation
        click OrganismalEntityAsAModelOfDiseaseAssociation href "../OrganismalEntityAsAModelOfDiseaseAssociation/"
      
      ModelToDiseaseAssociationMixin : object
        
          
    
        
        
        ModelToDiseaseAssociationMixin --> "1" NamedThing : object
        click NamedThing href "../NamedThing/"
    

        
      ModelToDiseaseAssociationMixin : predicate
        
      ModelToDiseaseAssociationMixin : subject
        
          
    
        
        
        ModelToDiseaseAssociationMixin --> "1" NamedThing : subject
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
| [subject](subject.md) | 1 <br/> [NamedThing](NamedThing.md) | The entity that serves as the model of the disease | direct |
| [predicate](predicate.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | The relationship to the disease | direct |
| [object](object.md) | 1 <br/> [NamedThing](NamedThing.md) | connects an association to the object of the association | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | An association in which a gene (e |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | An association in which a sequence variant serves as a model of a disease, re... |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | An association in which a genotype serves as a model of a disease, recapitula... |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | An association in which a cell line - typically derived from an organismal en... |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | An association in which an organismal entity (e |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:ModelToDiseaseAssociationMixin |
| native | namo:ModelToDiseaseAssociationMixin |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: model to disease association mixin
description: This mixin is used for any association class for which the subject (source
  node) plays the role of a 'model', in that it recapitulates some features of the
  disease in a way that is useful for studying the disease outside a patient carrying
  the disease
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
slots:
- subject
- predicate
- object
slot_usage:
  subject:
    name: subject
    description: The entity that serves as the model of the disease. This may be an
      organism, a strain of organism, a genotype or variant that exhibits similar
      features, or a gene that when mutated exhibits features of the disease
  predicate:
    name: predicate
    description: The relationship to the disease
    subproperty_of: model of

```
</details>

### Induced

<details>
```yaml
name: model to disease association mixin
description: This mixin is used for any association class for which the subject (source
  node) plays the role of a 'model', in that it recapitulates some features of the
  disease in a way that is useful for studying the disease outside a patient carrying
  the disease
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
slot_usage:
  subject:
    name: subject
    description: The entity that serves as the model of the disease. This may be an
      organism, a strain of organism, a genotype or variant that exhibits similar
      features, or a gene that when mutated exhibits features of the disease
  predicate:
    name: predicate
    description: The relationship to the disease
    subproperty_of: model of
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
    description: The entity that serves as the model of the disease. This may be an
      organism, a strain of organism, a genotype or variant that exhibits similar
      features, or a gene that when mutated exhibits features of the disease
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedSource
    - OBAN:association_has_subject
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    owner: model to disease association mixin
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
    description: The relationship to the disease
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedProperty
    - OBAN:association_has_predicate
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:predicate
    owner: model to disease association mixin
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
    owner: model to disease association mixin
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

```
</details></div>