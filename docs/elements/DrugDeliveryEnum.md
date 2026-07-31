---
search:
  boost: 2.0
---


# Enum: DrugDeliveryEnum 




_An enumeration of routes by which a drug is administered or delivered to a patient, including inhalation, oral, transdermal absorption, and various forms of injection (intravenous, subcutaneous, intramuscular)._



<div data-search-exclude markdown="1">

URI: [namo:DrugDeliveryEnum](https://w3id.org/monarch-initiative/namo/DrugDeliveryEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| inhalation | None |  ||
| oral | None |  ||
| absorption_through_the_skin | None |  ||
| injection | None |  ||
| intravenous_injection | None |  | Is-A: NONE<br>|
| subcutaneous_injection | None |  | Is-A: NONE<br>|
| intramuscular_injection | None |  | Is-A: NONE<br>|




## Slots

| Name | Description |
| ---  | --- |
| [routes_of_delivery](routes_of_delivery.md) | the method or process of administering a pharmaceutical compound to achieve a... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: DrugDeliveryEnum
description: An enumeration of routes by which a drug is administered or delivered
  to a patient, including inhalation, oral, transdermal absorption, and various forms
  of injection (intravenous, subcutaneous, intramuscular).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  inhalation:
    text: inhalation
  oral:
    text: oral
  absorption_through_the_skin:
    text: absorption_through_the_skin
  injection:
    text: injection
  intravenous_injection:
    text: intravenous_injection
    is_a: injection
  subcutaneous_injection:
    text: subcutaneous_injection
    is_a: injection
  intramuscular_injection:
    text: intramuscular_injection
    is_a: injection

```
</details>

</div>