

# Class: Pathway 


_A biological pathway with activity and enrichment information._





URI: [namo:Pathway](https://w3id.org/monarch-initiative/namo/Pathway)





```mermaid
 classDiagram
    class Pathway
    click Pathway href "../Pathway/"
      NamedThing <|-- Pathway
        click NamedThing href "../NamedThing/"
      
      Pathway : activity_score
        
      Pathway : description
        
      Pathway : enrichment_score
        
      Pathway : id
        
      Pathway : name
        
      Pathway : pathway_database
        
      Pathway : pathway_id
        
      Pathway : type
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **Pathway**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [pathway_database](pathway_database.md) | 0..1 <br/> [String](String.md) | Source database (e | direct |
| [pathway_id](pathway_id.md) | 0..1 <br/> [String](String.md) | Database-specific pathway identifier | direct |
| [activity_score](activity_score.md) | 0..1 <br/> [Float](Float.md) | Quantitative measure of pathway activity | direct |
| [enrichment_score](enrichment_score.md) | 0..1 <br/> [Float](Float.md) | Statistical enrichment score for the pathway | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [NamedThing](NamedThing.md) |
| [type](type.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PathwayConcordance](PathwayConcordance.md) | [active_pathways](active_pathways.md) | range | [Pathway](Pathway.md) |
| [PathwayConcordance](PathwayConcordance.md) | [divergent_pathways](divergent_pathways.md) | range | [Pathway](Pathway.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:Pathway |
| native | namo:Pathway |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Pathway
description: A biological pathway with activity and enrichment information.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: NamedThing
attributes:
  pathway_database:
    name: pathway_database
    description: Source database (e.g., KEGG, Reactome, GO).
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - Pathway
  pathway_id:
    name: pathway_id
    description: Database-specific pathway identifier.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - Pathway
  activity_score:
    name: activity_score
    description: Quantitative measure of pathway activity.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - Pathway
    range: float
  enrichment_score:
    name: enrichment_score
    description: Statistical enrichment score for the pathway.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    domain_of:
    - Pathway
    - EnrichmentStatistics
    range: float

```
</details>

### Induced

<details>
```yaml
name: Pathway
description: A biological pathway with activity and enrichment information.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: NamedThing
attributes:
  pathway_database:
    name: pathway_database
    description: Source database (e.g., KEGG, Reactome, GO).
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: pathway_database
    owner: Pathway
    domain_of:
    - Pathway
    range: string
  pathway_id:
    name: pathway_id
    description: Database-specific pathway identifier.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: pathway_id
    owner: Pathway
    domain_of:
    - Pathway
    range: string
  activity_score:
    name: activity_score
    description: Quantitative measure of pathway activity.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: activity_score
    owner: Pathway
    domain_of:
    - Pathway
    range: float
  enrichment_score:
    name: enrichment_score
    description: Statistical enrichment score for the pathway.
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    alias: enrichment_score
    owner: Pathway
    domain_of:
    - Pathway
    - EnrichmentStatistics
    range: float
  id:
    name: id
    description: A unique identifier for a thing
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: Pathway
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
    owner: Pathway
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
    owner: Pathway
    domain_of:
    - NamedThing
    range: string
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/namo
    rank: 1000
    designates_type: true
    alias: type
    owner: Pathway
    domain_of:
    - NamedThing
    range: string

```
</details>