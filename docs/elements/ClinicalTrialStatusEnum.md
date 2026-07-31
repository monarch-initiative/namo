---
search:
  boost: 2.0
---


# Enum: ClinicalTrialStatusEnum 




_Enumeration of clinical trial statuses indicating the recruitment state, availability, or regulatory status of a clinical study or intervention._

__



<div data-search-exclude markdown="1">

URI: [namo:ClinicalTrialStatusEnum](https://w3id.org/monarch-initiative/namo/ClinicalTrialStatusEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ACTIVE_NOT_RECRUITING | None | The study is ongoing but not currently recruiting participants |
| APPROVED_FOR_MARKETING | None | The intervention has received regulatory approval for marketing |
| AVAILABLE | None | The intervention or data is available for use or distribution |
| COMPLETED | None | The study has ended normally and participants are no longer being examined or... |
| ENROLLING_BY_INVITATION | None | Participants are being enrolled by invitation only |
| NO_LONGER_AVAILABLE | None | The intervention or data is no longer available |
| NOT_YET_RECRUITING | None | The study has not yet started recruiting participants |
| RECRUITING | None | The study is currently recruiting participants |
| SUSPENDED | None | The study has been temporarily halted but may resume |
| TEMPORARILY_NOT_AVAILABLE | None | The intervention or data is not currently available but may become available ... |
| TERMINATED | None | The study has stopped prematurely and will not start again |
| UNKNOWN | None | The recruitment or availability status is unknown |
| WITHDRAWN | None | The study was halted before enrolling its first participant |




## Slots

| Name | Description |
| ---  | --- |
| [clinical_trial_overall_status](clinical_trial_overall_status.md) | The overall status of a clinical trial as determined by clinicaltrials |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: ClinicalTrialStatusEnum
description: 'Enumeration of clinical trial statuses indicating the recruitment state,
  availability, or regulatory status of a clinical study or intervention.

  '
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  ACTIVE_NOT_RECRUITING:
    text: ACTIVE_NOT_RECRUITING
    description: The study is ongoing but not currently recruiting participants.
  APPROVED_FOR_MARKETING:
    text: APPROVED_FOR_MARKETING
    description: The intervention has received regulatory approval for marketing.
  AVAILABLE:
    text: AVAILABLE
    description: The intervention or data is available for use or distribution.
  COMPLETED:
    text: COMPLETED
    description: The study has ended normally and participants are no longer being
      examined or treated.
  ENROLLING_BY_INVITATION:
    text: ENROLLING_BY_INVITATION
    description: Participants are being enrolled by invitation only.
  NO_LONGER_AVAILABLE:
    text: NO_LONGER_AVAILABLE
    description: The intervention or data is no longer available.
  NOT_YET_RECRUITING:
    text: NOT_YET_RECRUITING
    description: The study has not yet started recruiting participants.
  RECRUITING:
    text: RECRUITING
    description: The study is currently recruiting participants.
  SUSPENDED:
    text: SUSPENDED
    description: The study has been temporarily halted but may resume.
  TEMPORARILY_NOT_AVAILABLE:
    text: TEMPORARILY_NOT_AVAILABLE
    description: The intervention or data is not currently available but may become
      available later.
  TERMINATED:
    text: TERMINATED
    description: The study has stopped prematurely and will not start again.
  UNKNOWN:
    text: UNKNOWN
    description: The recruitment or availability status is unknown.
  WITHDRAWN:
    text: WITHDRAWN
    description: The study was halted before enrolling its first participant.

```
</details>

</div>