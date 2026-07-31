---
search:
  boost: 5.0
---

# Slot: aggregate_statistic 


_An abstract grouping for summary numerical measures (e.g. count, total, quotient, percentage, rate) computed over a set of observations or a reference population, used to describe a property of an aggregated entity rather than an individual instance._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:aggregate_statistic](https://w3id.org/monarch-initiative/namo/aggregate_statistic)
Alias: aggregate_statistic


## Inheritance

* [node_property](node_property.md)
    * **aggregate_statistic**
        * [has_count](has_count.md)
        * [has_total](has_total.md)
        * [has_quotient](has_quotient.md)
        * [has_percentage](has_percentage.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [NamedThing](NamedThing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:aggregate_statistic |
| native | namo:aggregate_statistic |




## LinkML Source

<details>
```yaml
name: aggregate statistic
description: An abstract grouping for summary numerical measures (e.g. count, total,
  quotient, percentage, rate) computed over a set of observations or a reference population,
  used to describe a property of an aggregated entity rather than an individual instance.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
abstract: true
domain: named thing
alias: aggregate_statistic
range: string

```
</details></div>