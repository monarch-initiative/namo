---
search:
  boost: 10.0
---

# Class: Annotation 


_Biolink Model root class for entity annotations._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [namo:Annotation](https://w3id.org/monarch-initiative/namo/Annotation)





```mermaid
 classDiagram
    class Annotation
    click Annotation href "../Annotation/"
      Annotation <|-- QuantityValue
        click QuantityValue href "../QuantityValue/"
      
      
```





## Inheritance
* **Annotation**
    * [QuantityValue](QuantityValue.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:Annotation |
| native | namo:Annotation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: annotation
description: Biolink Model root class for entity annotations.
from_schema: https://w3id.org/monarch-initiative/namo
abstract: true

```
</details>

### Induced

<details>
```yaml
name: annotation
description: Biolink Model root class for entity annotations.
from_schema: https://w3id.org/monarch-initiative/namo
abstract: true

```
</details></div>