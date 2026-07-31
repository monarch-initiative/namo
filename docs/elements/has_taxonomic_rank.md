---
search:
  boost: 5.0
---

# Slot: has_taxonomic_rank 


_The taxonomic rank (e.g. species, genus, family, order, kingdom) assigned to an organism taxon._



<div data-search-exclude markdown="1">



URI: [namo:has_taxonomic_rank](https://w3id.org/monarch-initiative/namo/has_taxonomic_rank)
Alias: has_taxonomic_rank


## Inheritance

* [node_property](node_property.md)
    * **has_taxonomic_rank**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OrganismTaxon](OrganismTaxon.md) | A classification of a set of organisms |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TaxonomicRank](TaxonomicRank.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [OrganismTaxon](OrganismTaxon.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_taxonomic_rank |
| native | namo:has_taxonomic_rank |
| undefined | WIKIDATA:P105 |




## LinkML Source

<details>
```yaml
name: has taxonomic rank
description: The taxonomic rank (e.g. species, genus, family, order, kingdom) assigned
  to an organism taxon.
from_schema: https://w3id.org/monarch-initiative/namo
mappings:
- WIKIDATA:P105
rank: 1000
is_a: node property
domain: named thing
alias: has_taxonomic_rank
domain_of:
- organism taxon
range: taxonomic rank
multivalued: false

```
</details></div>