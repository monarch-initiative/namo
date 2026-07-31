---
search:
  boost: 10.0
---

# Class: PathologicalEntityMixin 


_A pathological (abnormal) structure or process._



<div data-search-exclude markdown="1">



URI: [namo:PathologicalEntityMixin](https://w3id.org/monarch-initiative/namo/PathologicalEntityMixin)





```mermaid
 classDiagram
    class PathologicalEntityMixin
    click PathologicalEntityMixin href "../PathologicalEntityMixin/"
      PathologicalEntityMixin <|-- PathologicalProcess
        click PathologicalProcess href "../PathologicalProcess/"
      PathologicalEntityMixin <|-- PathologicalAnatomicalStructure
        click PathologicalAnatomicalStructure href "../PathologicalAnatomicalStructure/"
      PathologicalEntityMixin <|-- DiseaseOrPhenotypicFeatureExposure
        click DiseaseOrPhenotypicFeatureExposure href "../DiseaseOrPhenotypicFeatureExposure/"
      
      
```




<!-- no inheritance hierarchy -->

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
| [PathologicalProcess](PathologicalProcess.md) | A biologic function or a process having an abnormal or deleterious effect at ... |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | An anatomical structure with the potential of have an abnormal or deleterious... |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | A disease or phenotypic feature state, when viewed as an exposure, represente... |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:PathologicalEntityMixin |
| native | namo:PathologicalEntityMixin |
| exact | MPATH:0 |
| narrow | HP:0000118 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: pathological entity mixin
description: A pathological (abnormal) structure or process.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- MPATH:0
narrow_mappings:
- HP:0000118
mixin: true

```
</details>

### Induced

<details>
```yaml
name: pathological entity mixin
description: A pathological (abnormal) structure or process.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- MPATH:0
narrow_mappings:
- HP:0000118
mixin: true

```
</details></div>