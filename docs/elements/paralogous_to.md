---
search:
  boost: 5.0
---

# Slot: paralogous_to 


_a homology relationship that holds between entities (typically genes) that diverged after a duplication event._



<div data-search-exclude markdown="1">



URI: [namo:paralogous_to](https://w3id.org/monarch-initiative/namo/paralogous_to)
Alias: paralogous_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [similar_to](similar_to.md)
            * [homologous_to](homologous_to.md)
                * **paralogous_to**








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
| self | namo:paralogous_to |
| native | namo:paralogous_to |
| exact | RO:HOM0000011 |




## LinkML Source

<details>
```yaml
name: paralogous to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: a homology relationship that holds between entities (typically genes)
  that diverged after a duplication event.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:HOM0000011
rank: 1000
is_a: homologous to
domain: named thing
inherited: true
alias: paralogous_to
symmetric: true
range: named thing
multivalued: true

```
</details></div>