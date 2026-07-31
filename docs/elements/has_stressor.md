---
search:
  boost: 5.0
---

# Slot: has_stressor 


_An agent, stimulus, activity, or event that causes stress or tension on an organism and interacts with an exposure_receptor during an exposure event._



<div data-search-exclude markdown="1">



URI: [namo:has_stressor](https://w3id.org/monarch-initiative/namo/has_stressor)
Alias: has_stressor


## Inheritance

* [node_property](node_property.md)
    * **has_stressor**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [ExposureEvent](ExposureEvent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* has stimulus




## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* ExO







### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_stressor |
| native | namo:has_stressor |
| exact | ExO:0000000 |




## LinkML Source

<details>
```yaml
name: has stressor
id_prefixes:
- ExO
description: An agent, stimulus, activity, or event that causes stress or tension
  on an organism and interacts with an exposure_receptor during an exposure event.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- has stimulus
exact_mappings:
- ExO:0000000
rank: 1000
is_a: node property
domain: exposure event
alias: has_stressor
range: string

```
</details></div>