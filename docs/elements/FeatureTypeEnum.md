# Enum: FeatureTypeEnum 



URI: [namo:FeatureTypeEnum](https://w3id.org/monarch-initiative/namo/FeatureTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| MOLECULAR | None | Molecular descriptors and chemical features |
| PHENOTYPIC | None | Phenotypic and physiological features |
| GENOMIC | None | Genomic and genetic features |
| TRANSCRIPTOMIC | EDAM:3308 | Gene expression features |
| PROTEOMIC | EDAM:0121 | Protein abundance and modification features |
| METABOLOMIC | EDAM:3172 | Metabolite concentration features |
| IMAGING | EDAM:3382 | Image-derived features |
| CLINICAL | None | Clinical and demographic features |
| TEMPORAL | None | Time-series and temporal features |




## Slots

| Name | Description |
| ---  | --- |
| [feature_types](feature_types.md) | Types of features used (molecular, phenotypic, imaging, etc |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: FeatureTypeEnum
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  MOLECULAR:
    text: MOLECULAR
    description: Molecular descriptors and chemical features
  PHENOTYPIC:
    text: PHENOTYPIC
    description: Phenotypic and physiological features
  GENOMIC:
    text: GENOMIC
    description: Genomic and genetic features
  TRANSCRIPTOMIC:
    text: TRANSCRIPTOMIC
    description: Gene expression features
    meaning: EDAM:3308
  PROTEOMIC:
    text: PROTEOMIC
    description: Protein abundance and modification features
    meaning: EDAM:0121
  METABOLOMIC:
    text: METABOLOMIC
    description: Metabolite concentration features
    meaning: EDAM:3172
  IMAGING:
    text: IMAGING
    description: Image-derived features
    meaning: EDAM:3382
  CLINICAL:
    text: CLINICAL
    description: Clinical and demographic features
  TEMPORAL:
    text: TEMPORAL
    description: Time-series and temporal features

```
</details>