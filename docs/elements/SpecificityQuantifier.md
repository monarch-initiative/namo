---
search:
  boost: 10.0
---

# Class: SpecificityQuantifier 


_A relationship quantifier that measures the specificity of a relationship, such as the proportion of true negatives correctly identified in a diagnostic or association context._



<div data-search-exclude markdown="1">



URI: [namo:SpecificityQuantifier](https://w3id.org/monarch-initiative/namo/SpecificityQuantifier)





```mermaid
 classDiagram
    class SpecificityQuantifier
    click SpecificityQuantifier href "../SpecificityQuantifier/"
      RelationshipQuantifier <|-- SpecificityQuantifier
        click RelationshipQuantifier href "../RelationshipQuantifier/"
      

      SpecificityQuantifier <|-- PathognomonicityQuantifier
        click PathognomonicityQuantifier href "../PathognomonicityQuantifier/"
      

      
```





## Inheritance
* [RelationshipQuantifier](RelationshipQuantifier.md)
    * **SpecificityQuantifier**
        * [PathognomonicityQuantifier](PathognomonicityQuantifier.md)


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
| self | namo:SpecificityQuantifier |
| native | namo:SpecificityQuantifier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: specificity quantifier
description: A relationship quantifier that measures the specificity of a relationship,
  such as the proportion of true negatives correctly identified in a diagnostic or
  association context.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: relationship quantifier
mixin: true

```
</details>

### Induced

<details>
```yaml
name: specificity quantifier
description: A relationship quantifier that measures the specificity of a relationship,
  such as the proportion of true negatives correctly identified in a diagnostic or
  association context.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: relationship quantifier
mixin: true

```
</details></div>