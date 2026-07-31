---
search:
  boost: 10.0
---

# Class: Outcome 


_An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of various categories of possible biological or non-biological outcomes._



<div data-search-exclude markdown="1">



URI: [namo:Outcome](https://w3id.org/monarch-initiative/namo/Outcome)





```mermaid
 classDiagram
    class Outcome
    click Outcome href "../Outcome/"
      Outcome <|-- PathologicalProcessOutcome
        click PathologicalProcessOutcome href "../PathologicalProcessOutcome/"
      Outcome <|-- PathologicalAnatomicalOutcome
        click PathologicalAnatomicalOutcome href "../PathologicalAnatomicalOutcome/"
      Outcome <|-- DiseaseOrPhenotypicFeatureOutcome
        click DiseaseOrPhenotypicFeatureOutcome href "../DiseaseOrPhenotypicFeatureOutcome/"
      Outcome <|-- BehavioralOutcome
        click BehavioralOutcome href "../BehavioralOutcome/"
      Outcome <|-- HospitalizationOutcome
        click HospitalizationOutcome href "../HospitalizationOutcome/"
      Outcome <|-- MortalityOutcome
        click MortalityOutcome href "../MortalityOutcome/"
      Outcome <|-- EpidemiologicalOutcome
        click EpidemiologicalOutcome href "../EpidemiologicalOutcome/"
      Outcome <|-- SocioeconomicOutcome
        click SocioeconomicOutcome href "../SocioeconomicOutcome/"
      
      
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
| [PathologicalProcessOutcome](PathologicalProcessOutcome.md) | An outcome resulting from an exposure event which is the manifestation of a p... |
| [PathologicalAnatomicalOutcome](PathologicalAnatomicalOutcome.md) | An outcome resulting from an exposure event which is the manifestation of an ... |
| [DiseaseOrPhenotypicFeatureOutcome](DiseaseOrPhenotypicFeatureOutcome.md) | Physiological outcomes resulting from an exposure event which is the manifest... |
| [BehavioralOutcome](BehavioralOutcome.md) | An outcome resulting from an exposure event which is the manifestation of hum... |
| [HospitalizationOutcome](HospitalizationOutcome.md) | An outcome resulting from an exposure event which is the increased manifestat... |
| [MortalityOutcome](MortalityOutcome.md) | An outcome of death from resulting from an exposure event |
| [EpidemiologicalOutcome](EpidemiologicalOutcome.md) | An epidemiological outcome, such as societal disease burden, resulting from a... |
| [SocioeconomicOutcome](SocioeconomicOutcome.md) | An general social or economic outcome, such as healthcare costs, utilization,... |




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) | [object](object.md) | range | [Outcome](Outcome.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object](object.md) | range | [Outcome](Outcome.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:Outcome |
| native | namo:Outcome |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: outcome
description: An entity that has the role of being the consequence of an exposure event.
  This is an abstract mixin grouping of various categories of possible biological
  or non-biological outcomes.
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true

```
</details>

### Induced

<details>
```yaml
name: outcome
description: An entity that has the role of being the consequence of an exposure event.
  This is an abstract mixin grouping of various categories of possible biological
  or non-biological outcomes.
from_schema: https://w3id.org/monarch-initiative/namo
mixin: true

```
</details></div>