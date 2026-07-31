---
search:
  boost: 10.0
---

# Class: ActivityAndBehavior 


_Activity or behavior of any independent integral living, organization or mechanical actor in the world_



<div data-search-exclude markdown="1">



URI: [namo:ActivityAndBehavior](https://w3id.org/monarch-initiative/namo/ActivityAndBehavior)





```mermaid
 classDiagram
    class ActivityAndBehavior
    click ActivityAndBehavior href "../ActivityAndBehavior/"
      Occurrent <|-- ActivityAndBehavior
        click Occurrent href "../Occurrent/"
      

      ActivityAndBehavior <|-- Activity
        click Activity href "../Activity/"
      ActivityAndBehavior <|-- Procedure
        click Procedure href "../Procedure/"
      ActivityAndBehavior <|-- Behavior
        click Behavior href "../Behavior/"
      

      
```





## Inheritance
* [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md)
    * [Occurrent](Occurrent.md)
        * **ActivityAndBehavior**


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
| [Activity](Activity.md) | An activity is something that occurs over a period of time and acts upon or w... |
| [Procedure](Procedure.md) | A series of actions conducted in a certain order or manner |
| [Behavior](Behavior.md) | The internally coordinated responses (actions or inactions) of organisms (ind... |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:ActivityAndBehavior |
| native | namo:ActivityAndBehavior |
| exact | UMLSSG:ACTI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: activity and behavior
description: Activity or behavior of any independent integral living, organization
  or mechanical actor in the world
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- UMLSSG:ACTI
is_a: occurrent
mixin: true

```
</details>

### Induced

<details>
```yaml
name: activity and behavior
description: Activity or behavior of any independent integral living, organization
  or mechanical actor in the world
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- UMLSSG:ACTI
is_a: occurrent
mixin: true

```
</details></div>