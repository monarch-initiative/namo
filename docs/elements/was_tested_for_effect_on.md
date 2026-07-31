---
search:
  boost: 0.5
---

# Slot: was_tested_for_effect_on  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 


_Reports that the subject was interrogated in an experiment to determine how it may affect the object. A relationship between some perturbing agent (usually a chemical compound) and some target entity, where the affect of the perturbing agent on the target entity was interrogated in a particular assay. The target might be a particular protein, tissue, phenotype, whole organism, cell line, or other type of biological entity._



<div data-search-exclude markdown="1">



URI: [namo:was_tested_for_effect_on](https://w3id.org/monarch-initiative/namo/was_tested_for_effect_on)
Alias: was_tested_for_effect_on


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **was_tested_for_effect_on**








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









## Aliases


* was assayed against
* was experimentally tested against




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
| self | namo:was_tested_for_effect_on |
| native | namo:was_tested_for_effect_on |




## LinkML Source

<details>
```yaml
name: was tested for effect on
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Reports that the subject was interrogated in an experiment to determine
  how it may affect the object. A relationship between some perturbing agent (usually
  a chemical compound) and some target entity, where the affect of the perturbing
  agent on the target entity was interrogated in a particular assay. The target might
  be a particular protein, tissue, phenotype, whole organism, cell line, or other
  type of biological entity.
deprecated: 'true'
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- was assayed against
- was experimentally tested against
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: was_tested_for_effect_on
range: named thing
multivalued: true

```
</details></div>