---
search:
  boost: 2.0
---


# Enum: ClinicalApprovalStatusEnum 




_An enumeration describing whether a chemical or therapy is approved for use in treating a specific condition (e.g., FDA-approved for a condition, not approved, off-label use, or withdrawn following approval)._



<div data-search-exclude markdown="1">

URI: [namo:ClinicalApprovalStatusEnum](https://w3id.org/monarch-initiative/namo/ClinicalApprovalStatusEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| approved_for_condition | None |  ||
| fda_approved_for_condition | None |  | Is-A: NONE<br>|
| not_approved_for_condition | None |  ||
| post_approval_withdrawal | None |  | Is-A: NONE<br>|
| off_label_use | None |  | Is-A: NONE<br>|
| not_provided | None |  ||




## Slots

| Name | Description |
| ---  | --- |
| [clinical_approval_status](clinical_approval_status.md) | The clinical approval status of a chemical entity for treating a specific dis... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: ClinicalApprovalStatusEnum
description: An enumeration describing whether a chemical or therapy is approved for
  use in treating a specific condition (e.g., FDA-approved for a condition, not approved,
  off-label use, or withdrawn following approval).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  approved_for_condition:
    text: approved_for_condition
  fda_approved_for_condition:
    text: fda_approved_for_condition
    is_a: approved_for_condition
  not_approved_for_condition:
    text: not_approved_for_condition
  post_approval_withdrawal:
    text: post_approval_withdrawal
    is_a: not_approved_for_condition
  off_label_use:
    text: off_label_use
    is_a: not_approved_for_condition
  not_provided:
    text: not_provided

```
</details>

</div>