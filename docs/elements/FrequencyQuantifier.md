---
search:
  boost: 10.0
---

# Class: FrequencyQuantifier 


_A relationship quantifier that expresses how often a relationship holds, using count, total, quotient, or percentage measures._



<div data-search-exclude markdown="1">



URI: [namo:FrequencyQuantifier](https://w3id.org/monarch-initiative/namo/FrequencyQuantifier)





```mermaid
 classDiagram
    class FrequencyQuantifier
    click FrequencyQuantifier href "../FrequencyQuantifier/"
      RelationshipQuantifier <|-- FrequencyQuantifier
        click RelationshipQuantifier href "../RelationshipQuantifier/"
      

      FrequencyQuantifier <|-- EntityToPhenotypicFeatureAssociationMixin
        click EntityToPhenotypicFeatureAssociationMixin href "../EntityToPhenotypicFeatureAssociationMixin/"
      FrequencyQuantifier <|-- PhenotypicFeatureToEntityAssociationMixin
        click PhenotypicFeatureToEntityAssociationMixin href "../PhenotypicFeatureToEntityAssociationMixin/"
      FrequencyQuantifier <|-- DiseaseToPhenotypicFeatureAssociation
        click DiseaseToPhenotypicFeatureAssociation href "../DiseaseToPhenotypicFeatureAssociation/"
      FrequencyQuantifier <|-- VariantToPopulationAssociation
        click VariantToPopulationAssociation href "../VariantToPopulationAssociation/"
      

      FrequencyQuantifier : has_count
        
      FrequencyQuantifier : has_percentage
        
      FrequencyQuantifier : has_quotient
        
      FrequencyQuantifier : has_total
        
      
```





## Inheritance
* [RelationshipQuantifier](RelationshipQuantifier.md)
    * **FrequencyQuantifier**


## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_count](has_count.md) | 0..1 <br/> [Integer](Integer.md) | number of things with a particular property | direct |
| [has_total](has_total.md) | 0..1 <br/> [Integer](Integer.md) | total number of things in a particular reference set | direct |
| [has_quotient](has_quotient.md) | 0..1 <br/> [Double](Double.md) |  | direct |
| [has_percentage](has_percentage.md) | 0..1 <br/> [Double](Double.md) | equivalent to has quotient multiplied by 100 | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | A mixin applied to any association whose object (target node) is a phenotypic... |
| [PhenotypicFeatureToEntityAssociationMixin](PhenotypicFeatureToEntityAssociationMixin.md) | A mixin applied to any association whose subject (source node) is a phenotypi... |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenot... |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |













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
| self | namo:FrequencyQuantifier |
| native | namo:FrequencyQuantifier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: frequency quantifier
description: A relationship quantifier that expresses how often a relationship holds,
  using count, total, quotient, or percentage measures.
examples:
- object:
    has_count: 42
    has_total: 100
    has_quotient: 0.42
    has_percentage: 42.0
from_schema: https://w3id.org/monarch-initiative/namo
is_a: relationship quantifier
mixin: true
slots:
- has count
- has total
- has quotient
- has percentage

```
</details>

### Induced

<details>
```yaml
name: frequency quantifier
description: A relationship quantifier that expresses how often a relationship holds,
  using count, total, quotient, or percentage measures.
examples:
- object:
    has_count: 42
    has_total: 100
    has_quotient: 0.42
    has_percentage: 42.0
from_schema: https://w3id.org/monarch-initiative/namo
is_a: relationship quantifier
mixin: true
attributes:
  has count:
    name: has count
    description: number of things with a particular property
    from_schema: https://w3id.org/monarch-initiative/namo
    exact_mappings:
    - LOINC:has_count
    rank: 1000
    is_a: aggregate statistic
    domain: named thing
    alias: has_count
    owner: frequency quantifier
    domain_of:
    - frequency quantifier
    range: integer
  has total:
    name: has total
    description: total number of things in a particular reference set
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: aggregate statistic
    domain: named thing
    alias: has_total
    owner: frequency quantifier
    domain_of:
    - frequency quantifier
    range: integer
  has quotient:
    name: has quotient
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: aggregate statistic
    domain: named thing
    alias: has_quotient
    owner: frequency quantifier
    domain_of:
    - frequency quantifier
    range: double
  has percentage:
    name: has percentage
    description: equivalent to has quotient multiplied by 100
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    is_a: aggregate statistic
    domain: named thing
    alias: has_percentage
    owner: frequency quantifier
    domain_of:
    - frequency quantifier
    range: double

```
</details></div>