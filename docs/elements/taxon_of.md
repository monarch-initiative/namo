---
search:
  boost: 5.0
---

# Slot: taxon_of 

<div data-search-exclude markdown="1">



URI: [namo:taxon_of](https://w3id.org/monarch-initiative/namo/taxon_of)
Alias: taxon_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **taxon_of**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ThingWithTaxon](ThingWithTaxon.md) |
| Domain | [OrganismTaxon](OrganismTaxon.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [in_taxon](in_taxon.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:taxon_of |
| native | namo:taxon_of |




## LinkML Source

<details>
```yaml
name: taxon of
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: organism taxon
inherited: true
alias: taxon_of
inverse: in taxon
range: thing with taxon
multivalued: true

```
</details></div>