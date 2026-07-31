---
search:
  boost: 2.0
---


# Enum: ApprovalStatusEnum 




_An enumeration of regulatory and development milestones for a drug or therapeutic, spanning discovery, preclinical research, FDA clinical trial phases (1-4), special review designations (e.g., fast track, breakthrough therapy, priority review), regular FDA approval, and post-approval withdrawal._



<div data-search-exclude markdown="1">

URI: [namo:ApprovalStatusEnum](https://w3id.org/monarch-initiative/namo/ApprovalStatusEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| discovery_and_development_phase | None | Discovery & Development Phase |
| preclinical_research_phase | None | Preclinical Research Phase |
| fda_clinical_research_phase | None | Clinical Research Phase |
| fda_review_phase_4 | None | FDA Review |
| fda_post_market_safety_review | None | FDA Post-Market Safety Monitoring |
| fda_clinical_research_phase_1 | None | In the FDA Clinical Research Phase, the Clinical Research Phase 1 involves 20... |
| fda_clinical_research_phase_2 | None | In the FDA Clinical Research Phase, the Clinical Research Phase 2 involves up... |
| fda_clinical_research_phase_3 | None | In the FDA Clinical Research Phase, the Clinical Research Phase 3 involves 30... |
| fda_clinical_research_phase_4 | None | In the FDA Clinical Research Phase, the Clinical Research Phase 4 involves se... |
| fda_fast_track | None | Fast track is a process designed to facilitate the development, and expedite ... |
| fda_breakthrough_therapy | None | Breakthrough Therapy designation is a process designed to expedite the develo... |
| fda_accelerated_approval | None | When studying a new drug, it can sometimes take many years to learn whether a... |
| fda_priority_review | None | Prior to approval, each drug marketed in the United States must go through a ... |
| regular_fda_approval | None | Regular FDA Approval |
| post_approval_withdrawal | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [highest_FDA_approval_status](highest_FDA_approval_status.md) | Should be the highest level of FDA approval this chemical entity or device ha... |
| [drug_regulatory_status_world_wide](drug_regulatory_status_world_wide.md) | An agglomeration of drug regulatory status worldwide |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: ApprovalStatusEnum
description: An enumeration of regulatory and development milestones for a drug or
  therapeutic, spanning discovery, preclinical research, FDA clinical trial phases
  (1-4), special review designations (e.g., fast track, breakthrough therapy, priority
  review), regular FDA approval, and post-approval withdrawal.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  discovery_and_development_phase:
    text: discovery_and_development_phase
    description: Discovery & Development Phase. Discovery involves researchers finding
      new possibilities for medication through testing molecular compounds, noting
      unexpected effects from existing treatments, or the creation of new technology
      that allows novel ways of targeting medical products to sites in the body. Drug
      development occurs after researchers identify potential compounds for experiments.
  preclinical_research_phase:
    text: preclinical_research_phase
    description: 'Preclinical Research Phase.  Once researchers have examined the
      possibilities a new drug may contain, they must do preliminary research to determine
      its potential for harm (toxicity). This is categorized as preclinical research
      and can be one of two types: in vitro or in vivo.'
  fda_clinical_research_phase:
    text: fda_clinical_research_phase
    description: Clinical Research Phase. Clinical research involves trials of the
      drug on people, and it is one of the most involved stages in the drug development
      and approval process. Clinical trials must answer specific questions and follow
      a protocol determined by the drug researcher or manufacturer.
  fda_review_phase_4:
    text: fda_review_phase_4
    description: FDA Review
  fda_post_market_safety_review:
    text: fda_post_market_safety_review
    description: FDA Post-Market Safety Monitoring.  The last phase of drug approval
      is an ongoing one while the drug is on the marketplace. If a developer wants
      to change anything about the drug formulation or approve it for a new use, they
      must apply with the FDA. The FDA also frequently reviews the drug’s advertising
      and its manufacturing facility to make sure everything involved in its creation
      and marketing is in compliance with regulations.
  fda_clinical_research_phase_1:
    text: fda_clinical_research_phase_1
    description: In the FDA Clinical Research Phase, the Clinical Research Phase 1
      involves 20 – 100 study participants and lasts several months. This phase is
      used to determine the safety and dosage of the drug, and about 70% of these
      drugs move on to the next clinical research phase.
  fda_clinical_research_phase_2:
    text: fda_clinical_research_phase_2
    description: In the FDA Clinical Research Phase, the Clinical Research Phase 2
      involves up to several hundred people, who must have the disease or condition
      the drug supposes to treat. This phase can last from a few months to two years,
      and its purpose is to monitor the efficacy of the drug, as well as note side
      effects that may occur.
  fda_clinical_research_phase_3:
    text: fda_clinical_research_phase_3
    description: In the FDA Clinical Research Phase, the Clinical Research Phase 3
      involves 300 – 3000 volunteers and can last up to four years. It is used to
      continue monitoring the efficacy of the drug, as well as exploring any longer-term
      adverse reactions.
  fda_clinical_research_phase_4:
    text: fda_clinical_research_phase_4
    description: In the FDA Clinical Research Phase, the Clinical Research Phase 4
      involves several thousands of volunteers who have the disease or condition and
      continues to monitor safety and efficacy. If a drug passes this phase, it goes
      on to FDA review.
  fda_fast_track:
    text: fda_fast_track
    description: Fast track is a process designed to facilitate the development, and
      expedite the review of drugs to treat serious conditions and fill an unmet medical
      need. The purpose is to get important new drugs to the patient earlier. Fast
      Track addresses a broad range of serious conditions. For more information https://www.fda.gov/patients/fast-track-breakthrough-therapy-accelerated-approval-priority-review/fast-track
  fda_breakthrough_therapy:
    text: fda_breakthrough_therapy
    description: Breakthrough Therapy designation is a process designed to expedite
      the development and review of drugs that are intended to treat a serious condition
      and preliminary clinical evidence indicates that the drug may demonstrate substantial
      improvement over available therapy on a clinically significant endpoint(s).
      For more information https://www.fda.gov/patients/fast-track-breakthrough-therapy-accelerated-approval-priority-review/breakthrough-therapy
  fda_accelerated_approval:
    text: fda_accelerated_approval
    description: When studying a new drug, it can sometimes take many years to learn
      whether a drug actually provides a real effect on how a patient survives, feels,
      or functions. A positive therapeutic effect that is clinically meaningful in
      the context of a given disease is known as “clinical benefit”. Mindful of the
      fact that it may take an extended period of time to measure a drug’s intended
      clinical benefit, in 1992 FDA instituted the Accelerated Approval regulations.
      These regulations allowed drugs for serious conditions that filled an unmet
      medical need to be approved based on a surrogate endpoint. Using a surrogate
      endpoint enabled the FDA to approve these drugs faster. For more information
      https://www.fda.gov/patients/fast-track-breakthrough-therapy-accelerated-approval-priority-review/accelerated-approval
  fda_priority_review:
    text: fda_priority_review
    description: Prior to approval, each drug marketed in the United States must go
      through a detailed FDA review process. In 1992, under the Prescription Drug
      User Act (PDUFA), FDA agreed to specific goals for improving the drug review
      time and created a two-tiered system of review times – Standard Review and Priority
      Review. A Priority Review designation means FDA’s goal is to take action on
      an application within 6 months (compared to 10 months under standard review).
      For more information https://www.fda.gov/patients/fast-track-breakthrough-therapy-accelerated-approval-priority-review/priority-review
  regular_fda_approval:
    text: regular_fda_approval
    description: Regular FDA Approval.  The last phase of drug approval is an ongoing
      one while the drug is on the marketplace. If a developer wants to change anything
      about the drug formulation or approve it for a new use, they must apply with
      the FDA. The FDA also frequently reviews the drug’s advertising and its manufacturing
      facility to make sure everything involved in its creation and marketing is in
      compliance with regulations.
  post_approval_withdrawal:
    text: post_approval_withdrawal

```
</details>

</div>