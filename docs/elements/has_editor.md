---
search:
  boost: 5.0
---

# Slot: has_editor 

<div data-search-exclude markdown="1">



URI: [namo:has_editor](https://w3id.org/monarch-initiative/namo/has_editor)
Alias: has_editor


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_contributor](has_contributor.md)
            * **has_editor**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain | [Publication](Publication.md) |

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
| Inverse | [editor](editor.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_editor |
| native | namo:has_editor |




## LinkML Source

<details>
```yaml
name: has editor
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has contributor
domain: publication
inherited: true
alias: has_editor
inverse: editor
range: agent
multivalued: true

```
</details></div>