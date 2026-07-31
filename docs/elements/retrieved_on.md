---
search:
  boost: 5.0
---

# Slot: retrieved_on 


_The date on which a dataset was retrieved or harvested from its original source, following pav:retrievedOn._



<div data-search-exclude markdown="1">



URI: [namo:retrieved_on](https://w3id.org/monarch-initiative/namo/retrieved_on)
Alias: retrieved_on


## Inheritance

* [node_property](node_property.md)
    * **retrieved_on**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain | [Dataset](Dataset.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:retrieved_on |
| native | namo:retrieved_on |
| exact | pav:retrievedOn |




## LinkML Source

<details>
```yaml
name: retrieved on
description: The date on which a dataset was retrieved or harvested from its original
  source, following pav:retrievedOn.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- pav:retrievedOn
rank: 1000
is_a: node property
domain: dataset
alias: retrieved_on
range: date

```
</details></div>