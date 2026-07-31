---
search:
  boost: 5.0
---

# Slot: is_output_of 

<div data-search-exclude markdown="1">



URI: [namo:is_output_of](https://w3id.org/monarch-initiative/namo/is_output_of)
Alias: is_output_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [participates_in](participates_in.md)
            * **is_output_of**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) |
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
| Inverse | [has_output](has_output.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_output_of |
| native | namo:is_output_of |
| exact | RO:0002353 |
| narrow | RO:0002354 |




## LinkML Source

<details>
```yaml
name: is output of
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002353
narrow_mappings:
- RO:0002354
rank: 1000
is_a: participates in
domain: named thing
inherited: true
alias: is_output_of
inverse: has output
range: biological process or activity
multivalued: true

```
</details></div>