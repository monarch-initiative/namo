---
search:
  boost: 10.0
---

# Class: VariantToEntityAssociationMixin 

<div data-search-exclude markdown="1">



URI: [namo:VariantToEntityAssociationMixin](https://w3id.org/monarch-initiative/namo/VariantToEntityAssociationMixin)





```mermaid
 classDiagram
    class VariantToEntityAssociationMixin
    click VariantToEntityAssociationMixin href "../VariantToEntityAssociationMixin/"
      VariantToEntityAssociationMixin <|-- VariantToGeneAssociation
        click VariantToGeneAssociation href "../VariantToGeneAssociation/"
      VariantToEntityAssociationMixin <|-- VariantToPopulationAssociation
        click VariantToPopulationAssociation href "../VariantToPopulationAssociation/"
      VariantToEntityAssociationMixin <|-- VariantToPhenotypicFeatureAssociation
        click VariantToPhenotypicFeatureAssociation href "../VariantToPhenotypicFeatureAssociation/"
      VariantToEntityAssociationMixin <|-- VariantToDiseaseAssociation
        click VariantToDiseaseAssociation href "../VariantToDiseaseAssociation/"
      
      VariantToEntityAssociationMixin : object
        
          
    
        
        
        VariantToEntityAssociationMixin --> "1" NamedThing : object
        click NamedThing href "../NamedThing/"
    

        
      VariantToEntityAssociationMixin : predicate
        
      VariantToEntityAssociationMixin : subject
        
          
    
        
        
        VariantToEntityAssociationMixin --> "1" SequenceVariant : subject
        click SequenceVariant href "../SequenceVariant/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 1 <br/> [SequenceVariant](SequenceVariant.md) | a sequence variant in which the allele state is associated with some other en... | direct |
| [predicate](predicate.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Has a value from the Biolink 'related_to' hierarchy | direct |
| [object](object.md) | 1 <br/> [NamedThing](NamedThing.md) | connects an association to the object of the association | direct |

## Defining Slots

This class is defined by the following slots:


* [subject](subject.md)



## Mixin Usage

| mixed into | description |
| --- | --- |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | An association between a variant and a gene, where the variant has a genetic ... |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | An association between a sequence variant and a phenotypic feature, in which ... |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | An association between a sequence variant and a disease, in which the allele ... |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:VariantToEntityAssociationMixin |
| native | namo:VariantToEntityAssociationMixin |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: variant to entity association mixin
local_names:
  ga4gh:
    local_name_source: ga4gh
    local_name_value: variant annotation
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
slots:
- subject
- predicate
- object
slot_usage:
  subject:
    name: subject
    description: a sequence variant in which the allele state is associated with some
      other entity
    examples:
    - value: CLINVAR:38077
      description: CLINVAR representation of NM_000059.3(BRCA2):c.7007G>A (p.Arg2336His)
    - value: ClinGen:CA024716
      description: chr13:g.32921033G>C (hg19) in ClinGen
    range: sequence variant
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: variant to entity association mixin
local_names:
  ga4gh:
    local_name_source: ga4gh
    local_name_value: variant annotation
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true
slot_usage:
  subject:
    name: subject
    description: a sequence variant in which the allele state is associated with some
      other entity
    examples:
    - value: CLINVAR:38077
      description: CLINVAR representation of NM_000059.3(BRCA2):c.7007G>A (p.Arg2336His)
    - value: ClinGen:CA024716
      description: chr13:g.32921033G>C (hg19) in ClinGen
    range: sequence variant
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
    description: a sequence variant in which the allele state is associated with some
      other entity
    examples:
    - value: CLINVAR:38077
      description: CLINVAR representation of NM_000059.3(BRCA2):c.7007G>A (p.Arg2336His)
    - value: ClinGen:CA024716
      description: chr13:g.32921033G>C (hg19) in ClinGen
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - owl:annotatedSource
    - OBAN:association_has_subject
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    owner: variant to entity association mixin
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
    range: sequence variant
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
    owner: variant to entity association mixin
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
    owner: variant to entity association mixin
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