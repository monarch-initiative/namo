# ARRIVE 2.0 Guidelines

## Overview

ARRIVE (Animal Research: Reporting of In Vivo Experiments) 2.0 provides essential information for evaluating the rigor, reproducibility and reliability of animal research studies. While focused on animal studies, it provides important context for NAM validation.

## Standard Information

- **Full Name**: Animal Research: Reporting of In Vivo Experiments
- **Version**: 2.0 (2020)
- **Organization**: NC3Rs (National Centre for the Replacement, Refinement and Reduction)
- **Focus**: Animal study reporting
- **Relevance to NAMs**: Comparison and validation standards

## NAMO Implementation

### Animal Model Context

```yaml
AnimalModel:
  attributes:
    arrive_compliance:
      essential_10: boolean  # Core ARRIVE items
      recommended_set: boolean  # Additional items

    experimental_details:
      study_design: string
      sample_size: integer
      inclusion_criteria: string
      exclusion_criteria: string
      randomization: string
      blinding: string
      outcome_measures: []
      statistical_methods: string
```

### NAM Validation Against Animal Models

```yaml
ValidationStudy:
  attributes:
    animal_comparison:
      animal_model: AnimalModel
      nam_model: NAMModel
      concordance_metrics:
        phenotypic: percentage
        molecular: percentage
        pharmacological: percentage

    arrive_reporting:
      animal_arm_compliant: boolean
      nam_arm_documented: boolean
```

## Essential 10 Items

| ARRIVE Item | NAMO Mapping | Purpose |
|-------------|--------------|---------|
| Study design | `Study.experimental_design` | Experimental groups |
| Sample size | `Study.sample_size` | Power calculation |
| Inclusion criteria | `selection_criteria` | Subject selection |
| Randomization | `randomization_method` | Bias reduction |
| Blinding | `blinding_protocol` | Objective assessment |
| Outcome measures | `Study.endpoints` | Primary/secondary |
| Statistical methods | `statistical_analysis` | Analysis plan |
| Animals | `AnimalModel` details | Species/strain |
| Experimental procedures | `Study.methods` | Timeline/interventions |
| Results | `Study.results` | Data presentation |

## NAM-Specific Adaptations

### Replacement Context

```yaml
replacement_justification:
  animal_model_limitations: []
  nam_advantages: []
  validation_evidence: []
  regulatory_acceptance: string
```

### Comparative Reporting

```yaml
comparative_study:
  animal_data:
    arrive_compliant: boolean
    historical_data: references

  nam_data:
    givrest_compliant: boolean  # NAM equivalent
    validation_metrics: []
```

## Integration with 3Rs

```yaml
three_rs_assessment:
  replacement:
    nam_type: NAMModel reference
    replacement_scope: partial/full

  refinement:
    reduced_severity: boolean
    improved_welfare: string

  reduction:
    animals_saved: integer
    statistical_efficiency: percentage
```

## Validation Examples

### ARRIVE Compliance Checker

```python
from namo.standards import ARRIVEChecker

checker = ARRIVEChecker()
animal_study = load_study("animal_toxicity.yaml")

# Check ARRIVE 2.0 compliance
report = checker.check_compliance(animal_study)

# Essential 10
print(f"Essential items: {report.essential_score}/10")

# Recommended items
print(f"Recommended items: {report.recommended_score}/11")

# Generate report
report.to_pdf("arrive_compliance.pdf")
```

### NAM-Animal Comparison

```python
from namo.validation import ComparisonValidator

validator = ComparisonValidator()

# Load studies
animal_study = load_study("mouse_hepatotox.yaml")
organoid_study = load_study("liver_organoid_tox.yaml")

# Compare outcomes
comparison = validator.compare(
    animal_study,
    organoid_study,
    standards=["ARRIVE", "GIVReST"]
)

print(f"Concordance: {comparison.overall_concordance}%")
```

## Benefits for NAM Development

1. **Validation Framework**: Structure for comparing NAMs to animal data
2. **Quality Benchmark**: Standard for robust experimental design
3. **Regulatory Bridge**: Familiar framework for regulators
4. **3Rs Documentation**: Evidence for replacement claims
5. **Meta-Analysis**: Enables systematic reviews

## References

- Percie du Sert N, et al. The ARRIVE guidelines 2.0. PLoS Biol. 2020;18(7):e3000410.
- Percie du Sert N, et al. Reporting animal research: Explanation and elaboration for the ARRIVE guidelines 2.0. PLoS Biol. 2020;18(7):e3000411.

## Related NAMO Classes

- [AnimalModel](../elements/AnimalModel.md)
- [ValidationStudy](../elements/ValidationStudy.md)
- [Study](../elements/Study.md)
- [ComparisonMetrics](../elements/ComparisonMetrics.md)