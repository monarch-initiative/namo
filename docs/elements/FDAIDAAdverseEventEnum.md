---
search:
  boost: 2.0
---


# Enum: FDAIDAAdverseEventEnum 




_please consult with the FDA guidelines as proposed in this document: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm?fr=312.32_



<div data-search-exclude markdown="1">

URI: [namo:FDAIDAAdverseEventEnum](https://w3id.org/monarch-initiative/namo/FDAIDAAdverseEventEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| life_threatening_adverse_event | None | An adverse event or suspected adverse reaction is considered 'life-threatenin... |
| serious_adverse_event | None | An adverse event or suspected adverse reaction is considered 'serious' if, in... |
| suspected_adverse_reaction | None | means any adverse event for which there is a reasonable possibility that the ... |
| unexpected_adverse_event | None | An adverse event or suspected adverse reaction is considered 'unexpected' if ... |




## Slots

| Name | Description |
| ---  | --- |
| [FDA_adverse_event_level](FDA_adverse_event_level.md) | The level or severity grade of an adverse event as classified by FDA adverse-... |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: FDAIDAAdverseEventEnum
description: 'please consult with the FDA guidelines as proposed in this document:
  https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm?fr=312.32'
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  life_threatening_adverse_event:
    text: life_threatening_adverse_event
    description: An adverse event or suspected adverse reaction is considered 'life-threatening'
      if, in the view of either the investigator or sponsor, its occurrence places
      the patient or subject at immediate risk of death. It does not include an adverse
      event or suspected adverse reaction that, had it occurred in a more severe form,
      might have caused death.
  serious_adverse_event:
    text: serious_adverse_event
    description: 'An adverse event or suspected adverse reaction is considered ''serious''
      if, in the view of either the investigator or sponsor, it results in any of
      the following outcomes: Death, a life-threatening adverse event, inpatient hospitalization
      or prolongation of existing hospitalization, a persistent or significant incapacity
      or substantial disruption of the ability to conduct normal life functions, or
      a congenital anomaly/birth defect. Important medical events that may not result
      in death, be life-threatening, or require hospitalization may be considered
      serious when, based upon appropriate medical judgment, they may jeopardize the
      patient or subject and may require medical or surgical intervention to prevent
      one of the outcomes listed in this definition. Examples of such medical events
      include allergic bronchospasm requiring intensive treatment in an emergency
      room or at home, blood dyscrasias or convulsions that do not result in inpatient
      hospitalization, or the development of drug dependency or drug abuse.'
  suspected_adverse_reaction:
    text: suspected_adverse_reaction
    description: means any adverse event for which there is a reasonable possibility
      that the drug caused the adverse event. For the purposes of IND safety reporting,
      'reasonable possibility' means there is evidence to suggest a causal relationship
      between the drug and the adverse event. Suspected adverse reaction implies a
      lesser degree of certainty about causality than adverse reaction, which means
      any adverse event caused by a drug.
  unexpected_adverse_event:
    text: unexpected_adverse_event
    description: An adverse event or suspected adverse reaction is considered 'unexpected'
      if it is not listed in the investigator brochure or is not listed at the specificity
      or severity that has been observed; or, if an investigator brochure is not required
      or available, is not consistent with the risk information described in the general
      investigational plan or elsewhere in the current application, as amended. For
      example, under this definition, hepatic necrosis would be unexpected (by virtue
      of greater severity) if the investigator brochure referred only to elevated
      hepatic enzymes or hepatitis. Similarly, cerebral thromboembolism and cerebral
      vasculitis would be unexpected (by virtue of greater specificity) if the investigator
      brochure listed only cerebral vascular accidents. 'Unexpected', as used in this
      definition, also refers to adverse events or suspected adverse reactions that
      are mentioned in the investigator brochure as occurring with a class of drugs
      or as anticipated from the pharmacological properties of the drug, but are not
      specifically mentioned as occurring with the particular drug under investigation.

```
</details>

</div>