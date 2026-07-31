---
search:
  boost: 5.0
---

# Slot: bonferonni_adjusted_p_value 


_The Bonferroni correction is an adjustment made to P values when several dependent or independent statistical tests are being performed simultaneously on a single data set. To perform a Bonferroni correction, divide the critical P value (α) by the number of comparisons being made.  P is always italicized and capitalized. The actual P value* should be expressed (P=. 04) rather than expressing a statement of inequality (P<. 05), unless P<._



<div data-search-exclude markdown="1">



URI: [namo:bonferonni_adjusted_p_value](https://w3id.org/monarch-initiative/namo/bonferonni_adjusted_p_value)
Alias: bonferonni_adjusted_p_value


## Inheritance

* [association_slot](association_slot.md)
    * [p_value](p_value.md)
        * [adjusted_p_value](adjusted_p_value.md)
            * **bonferonni_adjusted_p_value**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain | [Association](Association.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 0.018 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:bonferonni_adjusted_p_value |
| native | namo:bonferonni_adjusted_p_value |




## LinkML Source

<details>
```yaml
name: bonferonni adjusted p value
description: The Bonferroni correction is an adjustment made to P values when several
  dependent or independent statistical tests are being performed simultaneously on
  a single data set. To perform a Bonferroni correction, divide the critical P value
  (α) by the number of comparisons being made.  P is always italicized and capitalized.
  The actual P value* should be expressed (P=. 04) rather than expressing a statement
  of inequality (P<. 05), unless P<.
examples:
- value: '0.018'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: adjusted p value
domain: association
alias: bonferonni_adjusted_p_value
range: float

```
</details></div>