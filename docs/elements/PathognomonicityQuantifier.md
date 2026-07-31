---
search:
  boost: 10.0
---

# Class: PathognomonicityQuantifier 


_A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease_



<div data-search-exclude markdown="1">



URI: [namo:PathognomonicityQuantifier](https://w3id.org/monarch-initiative/namo/PathognomonicityQuantifier)





```mermaid
 classDiagram
    class PathognomonicityQuantifier
    click PathognomonicityQuantifier href "../PathognomonicityQuantifier/"
      SpecificityQuantifier <|-- PathognomonicityQuantifier
        click SpecificityQuantifier href "../SpecificityQuantifier/"
      
      
```





## Inheritance
* [RelationshipQuantifier](RelationshipQuantifier.md)
    * [SpecificityQuantifier](SpecificityQuantifier.md)
        * **PathognomonicityQuantifier**


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
| self | namo:PathognomonicityQuantifier |
| native | namo:PathognomonicityQuantifier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: pathognomonicity quantifier
description: A relationship quantifier between a variant or symptom and a disease,
  which is high when the presence of the feature implies the existence of the disease
from_schema: https://w3id.org/monarch-initiative/namo
is_a: specificity quantifier
mixin: true

```
</details>

### Induced

<details>
```yaml
name: pathognomonicity quantifier
description: A relationship quantifier between a variant or symptom and a disease,
  which is high when the presence of the feature implies the existence of the disease
from_schema: https://w3id.org/monarch-initiative/namo
is_a: specificity quantifier
mixin: true

```
</details></div>