# OECD OHT210 Harmonised Template

## Overview

OECD Harmonised Template 201 (OHT210) structures and reports mechanistic information to foster integration of new approach methodologies for hazard and risk assessment of chemicals.

## Standard Information

- **Full Name**: OECD Harmonised Template 201
- **Organization**: OECD
- **Focus**: Chemical risk assessment using NAMs
- **Purpose**: Regulatory data harmonization
- **Application**: Toxicological endpoints

## NAMO Implementation

### Chemical Testing Context

```yaml
Study:
  attributes:
    oecd_compliance:
      template: OHT210
      guideline: string  # e.g., "TG 442D"

    chemical_testing:
      test_substance: ChEBI term
      concentrations: []
      exposure_duration: hours/days

    regulatory_endpoints:
      skin_sensitization: boolean
      eye_irritation: boolean
      genotoxicity: boolean
```

## Key Elements

| OHT210 Element | NAMO Mapping | Purpose |
|----------------|--------------|---------|
| Test chemical | `perturbations.chemical` | Substance identity |
| Test system | `NAMModel` type | Model description |
| Endpoint | `Study.endpoints` | Measured outcome |
| Prediction model | `MLModel` | QSAR/AI component |
| Applicability domain | `prediction_scope` | Model limitations |

## Regulatory Endpoints

OECD-relevant toxicity endpoints in NAMO:
- Skin sensitization
- Eye irritation/corrosion
- Genotoxicity
- Endocrine disruption
- Repeated dose toxicity

## References

- Carnesecchi E, et al. OECD harmonised template 201. Regul Toxicol Pharmacol. 2023;142:105426.

## Related NAMO Classes

- [Study](../elements/Study.md)
- [NAMModel](../elements/NAMModel.md)
- [InSilicoModel](../elements/InSilicoModel.md)