---
search:
  boost: 2.0
---


# Enum: ResearchPhaseEnum 




_An enumeration of research phases describing the stage of investigation for a drug or therapy, spanning preclinical research through clinical trial phases 1 through 4 (including phase 1/2 and phase 2/3 combinations)._



<div data-search-exclude markdown="1">

URI: [namo:ResearchPhaseEnum](https://w3id.org/monarch-initiative/namo/ResearchPhaseEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| pre_clinical_research_phase | None | Biolink 'pre_clinical_research' is the union of both the `FDA discovery and d... ||
| clinical_trial_phase | None | Clinical research involves trials of the drug on people, and it is one of the... ||
| clinical_trial_phase_1 | None | In the FDA Clinical Trial Phase, the Clinical Trial Phase 1 involves 20 – 100... | Is-A: NONE<br>|
| clinical_trial_phase_1_to_2 | None | A study that tests the safety, side effects, and best dose of a new treatment | Is-A: NONE<br>|
| clinical_trial_phase_2 | None | In the FDA Clinical Trial Phase, the Clinical Trial Phase 2 involves up to se... | Is-A: NONE<br>|
| clinical_trial_phase_2_to_3 | None | A study that tests how well a new treatment works for a certain type of cance... | Is-A: NONE<br>|
| clinical_trial_phase_3 | None | In the FDA Clinical Trial Phase, the Clinical Trial Phase 3 involves 300 – 30... | Is-A: NONE<br>|
| clinical_trial_phase_4 | None | In the FDA Clinical Trial Phase, the Clinical Trial Phase 4 involves several ... | Is-A: NONE<br>|
| not_provided | None |  ||




## Slots

| Name | Description |
| ---  | --- |
| [clinical_trial_phase](clinical_trial_phase.md) | The phase that a clinical trials study represents |
| [max_research_phase](max_research_phase.md) | The maximum research phase reached for a specific chemical-disease pair, indi... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: ResearchPhaseEnum
description: An enumeration of research phases describing the stage of investigation
  for a drug or therapy, spanning preclinical research through clinical trial phases
  1 through 4 (including phase 1/2 and phase 2/3 combinations).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  pre_clinical_research_phase:
    text: pre_clinical_research_phase
    description: 'Biolink ''pre_clinical_research'' is the union of both the `FDA
      discovery and development phase` and `FDA preclinical research phase`. Discovery
      involves researchers finding new possibilities for medication through testing
      molecular compounds, noting unexpected effects from existing treatments, or
      the creation of new technology that allows novel ways of targeting medical products
      to sites in the body. Drug development occurs after researchers identify potential
      compounds for experiments Preclinical Research Phase. Once researchers have
      examined the possibilities a new drug may contain, they must do preliminary
      research to determine its potential for harm (toxicity). This is categorized
      as preclinical research and can be one of two types: in vitro or in vivo.'
    notes:
    - DrugBank calls this 'experimental'.
  clinical_trial_phase:
    text: clinical_trial_phase
    description: Clinical research involves trials of the drug on people, and it is
      one of the most involved stages in the drug development and approval process.
      Clinical trials must answer specific questions and follow a protocol determined
      by the drug researcher or manufacturer.
  clinical_trial_phase_1:
    text: clinical_trial_phase_1
    description: In the FDA Clinical Trial Phase, the Clinical Trial Phase 1 involves
      20 – 100 study participants and lasts several months. This phase is used to
      determine the safety and dosage of the drug, and about 70% of these drugs move
      on to the next clinical research phase.
    is_a: clinical_trial_phase
  clinical_trial_phase_1_to_2:
    text: clinical_trial_phase_1_to_2
    description: A study that tests the safety, side effects, and best dose of a new
      treatment. Phase I/II clinical trials also test how well a certain type of cancer
      or other disease responds to a new treatment. In the phase II part of the clinical
      trial, patients usually receive the highest dose of treatment that did not cause
      harmful side effects in the phase I part of the clinical trial. Combining phases
      I and II may allow research questions to be answered more quickly or with fewer
      patients. Also called phase 1/phase 2 clinical trial.
    is_a: clinical_trial_phase
    see_also:
    - https://www.cancer.gov/publications/dictionaries/cancer-terms/def/phase-i-ii-clinical-trial
  clinical_trial_phase_2:
    text: clinical_trial_phase_2
    description: In the FDA Clinical Trial Phase, the Clinical Trial Phase 2 involves
      up to several hundred people, who must have the disease or condition the drug
      supposes to treat. This phase can last from a few months to two years, and its
      purpose is to monitor the efficacy of the drug, as well as note side effects
      that may occur.
    is_a: clinical_trial_phase
  clinical_trial_phase_2_to_3:
    text: clinical_trial_phase_2_to_3
    description: A study that tests how well a new treatment works for a certain type
      of cancer or other disease and compares the new treatment with a standard treatment.
      Phase II/III clinical trials may also provide more information about the safety
      and side effects of the new treatment. Combining phases II and III may allow
      research questions to be answered more quickly or with fewer patients. Also
      called phase 2/phase 3 clinical trial.
    is_a: clinical_trial_phase
    see_also:
    - https://www.cancer.gov/publications/dictionaries/cancer-terms/def/phase-ii-iii-clinical-trial
  clinical_trial_phase_3:
    text: clinical_trial_phase_3
    description: In the FDA Clinical Trial Phase, the Clinical Trial Phase 3 involves
      300 – 3000 volunteers and can last up to four years. It is used to continue
      monitoring the efficacy of the drug, as well as exploring any longer-term adverse
      reactions.
    is_a: clinical_trial_phase
  clinical_trial_phase_4:
    text: clinical_trial_phase_4
    description: In the FDA Clinical Trial Phase, the Clinical Trial Phase 4 involves
      several thousands of volunteers who have the disease or condition and continues
      to monitor safety and efficacy. If a drug passes this phase, it goes on to FDA
      review.
    is_a: clinical_trial_phase
  not_provided:
    text: not_provided

```
</details>

</div>