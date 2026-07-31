---
search:
  boost: 5.0
---

# Slot: is_input_of 

<div data-search-exclude markdown="1">



URI: [namo:is_input_of](https://w3id.org/monarch-initiative/namo/is_input_of)
Alias: is_input_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [participates_in](participates_in.md)
            * **is_input_of**
                * [consumed_by](consumed_by.md)








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
| Inverse | [has_input](has_input.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_input_of |
| native | namo:is_input_of |
| exact | RO:0002352 |




## LinkML Source

<details>
```yaml
name: is input of
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002352
rank: 1000
is_a: participates in
domain: named thing
inherited: true
alias: is_input_of
inverse: has input
range: biological process or activity
multivalued: true

```
</details></div>