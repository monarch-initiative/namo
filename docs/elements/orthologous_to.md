---
search:
  boost: 5.0
---

# Slot: orthologous_to 


_a homology relationship between entities (typically genes) that diverged after a speciation event._



<div data-search-exclude markdown="1">



URI: [namo:orthologous_to](https://w3id.org/monarch-initiative/namo/orthologous_to)
Alias: orthologous_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [similar_to](similar_to.md)
            * [homologous_to](homologous_to.md)
                * **orthologous_to**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [NamedThing](NamedThing.md) |

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
| Symmetric | Yes |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:orthologous_to |
| native | namo:orthologous_to |
| exact | RO:HOM0000017, WIKIDATA_PROPERTY:P684 |




## LinkML Source

<details>
```yaml
name: orthologous to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: a homology relationship between entities (typically genes) that diverged
  after a speciation event.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:HOM0000017
- WIKIDATA_PROPERTY:P684
rank: 1000
is_a: homologous to
domain: named thing
inherited: true
alias: orthologous_to
symmetric: true
range: named thing
multivalued: true

```
</details></div>