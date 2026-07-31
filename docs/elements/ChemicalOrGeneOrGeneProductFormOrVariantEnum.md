---
search:
  boost: 2.0
---


# Enum: ChemicalOrGeneOrGeneProductFormOrVariantEnum 




_An enumeration used as a qualifier to indicate a specific form or variant of a chemical, gene, or gene product involved in an association (e.g., modified form, loss-of-function variant, gain-of-function variant, dominant-negative variant, polymorphic form, SNP form, mutant form, or analog form)._



<div data-search-exclude markdown="1">

URI: [namo:ChemicalOrGeneOrGeneProductFormOrVariantEnum](https://w3id.org/monarch-initiative/namo/ChemicalOrGeneOrGeneProductFormOrVariantEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| genetic_variant_form | None |  | Is-A: NONE<br>|
| modified_form | None |  ||
| loss_of_function_variant_form | None |  | Is-A: NONE<br>|
| non_loss_of_function_variant_form | None |  | Is-A: NONE<br>|
| gain_of_function_variant_form | None |  | Is-A: NONE<br>|
| dominant_negative_variant_form | None |  | Is-A: NONE<br>|
| polymorphic_form | None |  | Is-A: NONE<br>|
| snp_form | None |  | Is-A: NONE<br>|
| mutant_form | None |  | Is-A: NONE<br>|
| analog_form | None |  | Is-A: NONE<br>|




## Slots

| Name | Description |
| ---  | --- |
| [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) |  |
| [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: ChemicalOrGeneOrGeneProductFormOrVariantEnum
description: An enumeration used as a qualifier to indicate a specific form or variant
  of a chemical, gene, or gene product involved in an association (e.g., modified
  form, loss-of-function variant, gain-of-function variant, dominant-negative variant,
  polymorphic form, SNP form, mutant form, or analog form).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  genetic_variant_form:
    text: genetic_variant_form
    is_a: modified_form
  modified_form:
    text: modified_form
  loss_of_function_variant_form:
    text: loss_of_function_variant_form
    is_a: genetic_variant_form
  non_loss_of_function_variant_form:
    text: non_loss_of_function_variant_form
    is_a: genetic_variant_form
  gain_of_function_variant_form:
    text: gain_of_function_variant_form
    is_a: non_loss_of_function_variant_form
  dominant_negative_variant_form:
    text: dominant_negative_variant_form
    is_a: non_loss_of_function_variant_form
  polymorphic_form:
    text: polymorphic_form
    is_a: genetic_variant_form
  snp_form:
    text: snp_form
    is_a: polymorphic_form
  mutant_form:
    text: mutant_form
    is_a: genetic_variant_form
  analog_form:
    text: analog_form
    is_a: modified_form

```
</details>

</div>