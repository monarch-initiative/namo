---
search:
  boost: 10.0
---

# Class: RelationshipQuantifier 


_A mixin for quantifying aspects of the strength, frequency, or specificity of a relationship between two entities._



<div data-search-exclude markdown="1">



URI: [namo:RelationshipQuantifier](https://w3id.org/monarch-initiative/namo/RelationshipQuantifier)





```mermaid
 classDiagram
    class RelationshipQuantifier
    click RelationshipQuantifier href "../RelationshipQuantifier/"
      RelationshipQuantifier <|-- SensitivityQuantifier
        click SensitivityQuantifier href "../SensitivityQuantifier/"
      RelationshipQuantifier <|-- SpecificityQuantifier
        click SpecificityQuantifier href "../SpecificityQuantifier/"
      RelationshipQuantifier <|-- FrequencyQuantifier
        click FrequencyQuantifier href "../FrequencyQuantifier/"
      
      
```





## Inheritance
* **RelationshipQuantifier**
    * [SensitivityQuantifier](SensitivityQuantifier.md)
    * [SpecificityQuantifier](SpecificityQuantifier.md)
    * [FrequencyQuantifier](FrequencyQuantifier.md)


## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:RelationshipQuantifier |
| native | namo:RelationshipQuantifier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: relationship quantifier
description: A mixin for quantifying aspects of the strength, frequency, or specificity
  of a relationship between two entities.
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true

```
</details>

### Induced

<details>
```yaml
name: relationship quantifier
description: A mixin for quantifying aspects of the strength, frequency, or specificity
  of a relationship between two entities.
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true

```
</details></div>