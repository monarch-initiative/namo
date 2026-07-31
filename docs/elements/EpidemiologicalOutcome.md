---
search:
  boost: 10.0
---

# Class: EpidemiologicalOutcome 


_An epidemiological outcome, such as societal disease burden, resulting from an exposure event._



<div data-search-exclude markdown="1">



URI: [namo:EpidemiologicalOutcome](https://w3id.org/monarch-initiative/namo/EpidemiologicalOutcome)





```mermaid
 classDiagram
    class EpidemiologicalOutcome
    click EpidemiologicalOutcome href "../EpidemiologicalOutcome/"
      Outcome <|-- EpidemiologicalOutcome
        click Outcome href "../Outcome/"
      
      
```





## Inheritance
* **EpidemiologicalOutcome** [ [Outcome](Outcome.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:EpidemiologicalOutcome |
| native | namo:EpidemiologicalOutcome |
| related | NCIT:C19291 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: epidemiological outcome
description: An epidemiological outcome, such as societal disease burden, resulting
  from an exposure event.
from_schema: https://w3id.org/monarch-initiative/namo
related_mappings:
- NCIT:C19291
mixins:
- outcome

```
</details>

### Induced

<details>
```yaml
name: epidemiological outcome
description: An epidemiological outcome, such as societal disease burden, resulting
  from an exposure event.
from_schema: https://w3id.org/monarch-initiative/namo
related_mappings:
- NCIT:C19291
mixins:
- outcome

```
</details></div>