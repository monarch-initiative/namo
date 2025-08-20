

# Class: FunctionalAssay 


_A functional assay used to assess biological capabilities._





URI: [namo:FunctionalAssay](https://w3id.org/monarch-initiative/namo/FunctionalAssay)





```mermaid
 classDiagram
    class FunctionalAssay
    click FunctionalAssay href "../FunctionalAssay/"
      NamedThing <|-- FunctionalAssay
        click NamedThing href "../NamedThing/"
      
      FunctionalAssay : assay_result
        
      FunctionalAssay : assay_type
        
      FunctionalAssay : description
        
      FunctionalAssay : id
        
      FunctionalAssay : methodology
        
      FunctionalAssay : name
        
      FunctionalAssay : reference_value
        
      FunctionalAssay : type
        
      FunctionalAssay : units
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **FunctionalAssay**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [assay_type](assay_type.md) | 0..1 <br/> [String](String.md) | Type of functional assay (e | direct |
| [assay_result](assay_result.md) | 0..1 <br/> [Float](Float.md) | Quantitative result of the assay | direct |
| [reference_value](reference_value.md) | 0..1 <br/> [Float](Float.md) | Reference or control value for comparison | direct |
| [units](units.md) | 0..1 <br/> [String](String.md) | Units of measurement for the assay result | direct |
| [methodology](methodology.md) | 0..1 <br/> [String](String.md) | Detailed methodology for the assay | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [NamedThing](NamedThing.md) |
| [type](type.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [FunctionalParity](FunctionalParity.md) | [functional_assays](functional_assays.md) | range | [FunctionalAssay](FunctionalAssay.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:FunctionalAssay |
| native | namo:FunctionalAssay |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FunctionalAssay
description: A functional assay used to assess biological capabilities.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: NamedThing
attributes:
  assay_type:
    name: assay_type
    description: Type of functional assay (e.g., TEER, permeability, metabolic activity).
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - FunctionalAssay
  assay_result:
    name: assay_result
    description: Quantitative result of the assay.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - FunctionalAssay
    range: float
  reference_value:
    name: reference_value
    description: Reference or control value for comparison.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - FunctionalAssay
    range: float
  units:
    name: units
    description: Units of measurement for the assay result.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - FunctionalAssay
  methodology:
    name: methodology
    description: Detailed methodology for the assay.
    from_schema: https://w3id.org/monarch-initiative/namo
    domain_of:
    - MolecularSimilarity
    - FunctionalAssay

```
</details>

### Induced

<details>
```yaml
name: FunctionalAssay
description: A functional assay used to assess biological capabilities.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: NamedThing
attributes:
  assay_type:
    name: assay_type
    description: Type of functional assay (e.g., TEER, permeability, metabolic activity).
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: assay_type
    owner: FunctionalAssay
    domain_of:
    - FunctionalAssay
    range: string
  assay_result:
    name: assay_result
    description: Quantitative result of the assay.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: assay_result
    owner: FunctionalAssay
    domain_of:
    - FunctionalAssay
    range: float
  reference_value:
    name: reference_value
    description: Reference or control value for comparison.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: reference_value
    owner: FunctionalAssay
    domain_of:
    - FunctionalAssay
    range: float
  units:
    name: units
    description: Units of measurement for the assay result.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: units
    owner: FunctionalAssay
    domain_of:
    - FunctionalAssay
    range: string
  methodology:
    name: methodology
    description: Detailed methodology for the assay.
    from_schema: https://w3id.org/monarch-initiative/namo
    alias: methodology
    owner: FunctionalAssay
    domain_of:
    - MolecularSimilarity
    - FunctionalAssay
    range: string
  id:
    name: id
    description: A unique identifier for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: FunctionalAssay
    domain_of:
    - NamedThing
    - Reference
    range: uriorcurie
    required: true
  name:
    name: name
    description: A human-readable name for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: FunctionalAssay
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: FunctionalAssay
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: FunctionalAssay
    domain_of:
    - NamedThing
    range: string

```
</details>