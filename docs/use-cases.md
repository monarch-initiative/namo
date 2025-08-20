# NAMO Use Cases and Implementation Patterns

This document outlines practical applications and implementation scenarios for the NAMO schema, demonstrating how different organizations and research communities can leverage NAMO to address real-world challenges in alternative methodology research.

## Use Case 1: Integrated NAM Database for Regulatory Science

### Scenario
A regulatory agency needs to build a comprehensive database of validated alternative methods to support evidence-based decision making for safety assessment and replace animal testing requirements.

### Implementation
```yaml
# Regulatory validation package
dataset:
  model_systems:
    - id: "reg_validated_001"
      name: "3D Hepatotoxicity Screening Platform"
      type: "CoCulture"
      validation_status: "OECD_GUIDELINE_ACCEPTED"
      cell_types:
        - id: "CL:0000182"
          name: "hepatocyte"
        - id: "CL:0002145" 
          name: "hepatic stellate cell"
      models:
        - biological_system_modeled: "liver_toxicity"
          concordance:
            sensitivity: 0.89
            specificity: 0.92
            positive_predictive_value: 0.87
          structured_concordance:
            reproducibility:
              inter_laboratory_consistency: 0.94
              replicate_count: 156
              quality_control_metrics:
                - metric_name: "Cell viability"
                  metric_value: 0.93
                  threshold: 0.85
                  pass_fail_status: true
```

### Benefits
- **Standardized evidence packages** for regulatory submissions
- **Cross-study reproducibility tracking** across multiple laboratories
- **Clear acceptance criteria** with quantitative performance thresholds
- **Harmonized validation metrics** across different NAM types

## Use Case 2: Pharmaceutical R&D Model Selection Platform

### Scenario
A pharmaceutical company needs an intelligent platform to recommend optimal alternative models for specific drug development questions across different therapeutic areas and development stages.

### Implementation
```python
from namo.datamodel import Dataset, QSARModel, OrganOnChip, MLModel
import pandas as pd

class NAMRecommendationEngine:
    def __init__(self, namo_database):
        self.database = namo_database
    
    def recommend_models(self, disease_context, endpoint_type, complexity_requirement):
        """Find models matching research requirements"""
        candidates = []
        
        for model in self.database.model_systems:
            # Check disease relevance
            if self._matches_disease_context(model, disease_context):
                # Evaluate concordance scores
                score = self._calculate_fitness_score(model, endpoint_type)
                candidates.append((model, score))
        
        return sorted(candidates, key=lambda x: x[1], reverse=True)
    
    def _calculate_fitness_score(self, model, endpoint_type):
        """Calculate model fitness based on concordance metrics"""
        if hasattr(model, 'models') and model.models:
            concordance = model.models[0].structured_concordance
            if concordance:
                return (
                    concordance.molecular_similarity.similarity_score * 0.3 +
                    concordance.functional_parity.functional_similarity_score * 0.4 +
                    concordance.reproducibility.reproducibility_score * 0.3
                )
        return 0.0

# Example usage
recommendations = engine.recommend_models(
    disease_context="MONDO:0005061",  # cystic fibrosis
    endpoint_type="inflammatory_response",
    complexity_requirement="HIGH"
)
```

### Benefits
- **Data-driven model selection** based on quantitative performance metrics
- **Reduced development timelines** through optimal model matching
- **Risk mitigation** via validated concordance assessments
- **Cost optimization** by avoiding unsuitable model systems

## Use Case 3: Academic Research Consortium Data Sharing

### Scenario
A multi-institution research consortium studying neurological diseases needs to standardize and share data about organoid models across participating laboratories.

### Implementation
```yaml
# Consortium data sharing schema
dataset:
  consortium_id: "neuro_consortium_2024"
  participating_institutions:
    - "Stanford University"
    - "MIT"
    - "Johns Hopkins"
  
  model_systems:
    - id: "stanford_brain_org_001"
      name: "Alzheimer's Disease Brain Organoid"
      type: "Organoid"
      institution: "Stanford University"
      organ_modeled:
        id: "UBERON:0000955"
        name: "brain"
      cell_types:
        - id: "CL:0000540"
          name: "neuron"
        - id: "CL:0000127"
          name: "astrocyte"
        - id: "CL:0002063"
          name: "oligodendrocyte precursor cell"
      
      models:
        - biological_system_modeled: "alzheimers_disease"
          structured_concordance:
            molecular_similarity:
              methodology: "Single-cell RNA sequencing with Alzheimer's patient tissue comparison"
              data_source: "ROSMAP cohort temporal cortex samples"
              correlation_coefficient: 0.78
              
            phenotype_overlap:
              shared_phenotypes:
                - id: "HP:0002180"
                  name: "Neurodegeneration"
                - id: "HP:0000726" 
                  name: "Dementia"
              
            cell_type_coverage:
              coverage_percentage: 82.3
              represented_cell_types:
                - id: "CL:0000540"
                  name: "neuron"
              missing_cell_types:
                - id: "CL:0000129"
                  name: "microglial cell"
      
      references:
        - id: "doi:10.1038/s41586-2024-xxxxx"
          title: "Modeling Alzheimer's pathology in human brain organoids"
          authors: ["Smith, J.", "Johnson, A."]
          year: 2024
```

### Benefits
- **Standardized metadata** enabling cross-institutional comparisons
- **Reproducibility tracking** across different laboratory conditions
- **Collaborative benchmarking** of model performance
- **Shared validation standards** for publication and grant applications

## Use Case 4: AI/ML Training Data Curation

### Scenario
A biotech company developing AI models for drug discovery needs high-quality, structured training data that captures the relationship between chemical structures, biological activities, and model system responses.

### Implementation
```python
# AI training data pipeline
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from namo.datamodel import QSARModel, MLModel

class NAMAITrainingPipeline:
    def __init__(self, namo_dataset):
        self.dataset = namo_dataset
        
    def extract_features(self):
        """Extract structured features for ML training"""
        features = []
        labels = []
        
        for model in self.dataset.model_systems:
            if isinstance(model, (QSARModel, MLModel)):
                # Extract performance metrics as features
                if model.model_performance:
                    feature_vector = [
                        model.model_performance.accuracy,
                        model.model_performance.sensitivity,
                        model.model_performance.specificity,
                        model.model_performance.auc
                    ]
                    
                    # Add concordance metrics if available
                    if hasattr(model, 'models') and model.models:
                        concordance = model.models[0].structured_concordance
                        if concordance:
                            feature_vector.extend([
                                concordance.molecular_similarity.similarity_score,
                                concordance.functional_parity.functional_similarity_score,
                                concordance.reproducibility.reproducibility_score
                            ])
                    
                    features.append(feature_vector)
                    
                    # Binary label: high-performing model vs. low-performing
                    performance_score = np.mean(feature_vector[:4])  # Average of basic metrics
                    labels.append(1 if performance_score > 0.8 else 0)
        
        return np.array(features), np.array(labels)
    
    def train_performance_predictor(self):
        """Train a model to predict NAM performance"""
        X, y = self.extract_features()
        
        # Train classifier to predict high-performing models
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X, y)
        
        # Feature importance analysis
        feature_names = [
            'accuracy', 'sensitivity', 'specificity', 'auc',
            'molecular_similarity', 'functional_parity', 'reproducibility'
        ]
        
        importance_scores = dict(zip(feature_names, clf.feature_importances_))
        return clf, importance_scores

# Usage example
pipeline = NAMAITrainingPipeline(namo_database)
model, feature_importance = pipeline.train_performance_predictor()
```

### Benefits
- **Structured training data** with rich metadata annotations
- **Quality-controlled datasets** with validation metrics
- **Ontology-mapped features** enabling semantic understanding
- **Reproducible ML pipelines** with standardized input formats

## Use Case 5: Commercial Model Marketplace

### Scenario
A technology company wants to create a marketplace where researchers can discover, compare, and access commercial alternative method platforms and services.

### Implementation
```yaml
# Commercial marketplace catalog
marketplace_catalog:
  vendors:
    - vendor_id: "emulate_inc"
      name: "Emulate Inc."
      model_systems:
        - id: "emulate_lung_chip_v3"
          name: "Lung-on-Chip Platform v3.0"
          type: "OrganOnChip"
          commercial_status: "AVAILABLE"
          pricing_model: "PER_EXPERIMENT"
          
          organ_modeled:
            id: "UBERON:0002048"
            name: "lung"
            
          microfluidic_design:
            architecture_type: "TWO_CHANNEL"
            membrane_type: "POROUS_POLYMER"
            sensors_integrated: ["TEER", "OXYGEN", "PH"]
            
          validated_applications:
            - "respiratory_toxicity_screening"
            - "drug_permeability_testing"
            - "inflammatory_response_modeling"
            
          performance_benchmarks:
            throughput: "96_wells_per_day"
            reproducibility_cv: 0.12
            dynamic_range: "3_orders_magnitude"
            
          regulatory_acceptance:
            - agency: "FDA"
              status: "QUALIFIED_BIOMARKER"
              context_of_use: "pulmonary_toxicity_screening"
              
          support_services:
            - "protocol_development"
            - "data_analysis"
            - "regulatory_consultation"
            
          models:
            - biological_system_modeled: "healthy_lung_physiology"
              structured_concordance:
                functional_parity:
                  functional_assays:
                    - assay_type: "Barrier integrity (TEER)"
                      assay_result: 1200.0
                      reference_value: 1150.0
                      units: "ohm*cm²"
                    - assay_type: "Ciliary beat frequency"
                      assay_result: 850.0
                      reference_value: 900.0  
                      units: "beats/min"
```

### Benefits
- **Standardized product descriptions** enabling direct comparisons
- **Performance benchmarking** across different vendor platforms
- **Regulatory status tracking** for compliance requirements
- **Service integration** with standardized APIs and data formats

## Use Case 6: Multi-Organ System Integration

### Scenario
A research institute studying systemic drug effects needs to integrate data from multiple organ-on-chip systems to model whole-body pharmacokinetics and toxicity.

### Implementation
```yaml
# Multi-organ system study
multi_organ_study:
  study_id: "systemic_cardiotox_2024"
  study_design: "PARALLEL_ORGAN_EXPOSURE"
  
  model_systems:
    - id: "heart_chip_001"
      name: "Cardiac Contractility Chip"
      type: "OrganOnChip"
      organ_modeled:
        id: "UBERON:0000948"
        name: "heart"
      
      endpoints_measured:
        - "beat_rate_variability"
        - "contractile_force"
        - "action_potential_duration"
        
    - id: "liver_chip_001" 
      name: "Hepatic Metabolism Chip"
      type: "OrganOnChip"
      organ_modeled:
        id: "UBERON:0002107"
        name: "liver"
        
      endpoints_measured:
        - "cytochrome_p450_activity"
        - "albumin_synthesis"
        - "lactate_dehydrogenase_release"
        
    - id: "kidney_chip_001"
      name: "Renal Clearance Chip" 
      type: "OrganOnChip"
      organ_modeled:
        id: "UBERON:0002113"
        name: "kidney"
        
      endpoints_measured:
        - "glomerular_filtration_rate"
        - "tubular_secretion_rate"
        - "creatinine_clearance"
  
  # PBPK model integration
  computational_models:
    - id: "pbpk_integration_001"
      name: "Multi-Organ PBPK Model"
      type: "PBPKModel"
      
      compartments:
        - compartment_type: "HEART"
          volume: 0.33
          blood_flow: 0.24
        - compartment_type: "LIVER" 
          volume: 1.8
          blood_flow: 0.25
        - compartment_type: "KIDNEY"
          volume: 0.31
          blood_flow: 0.19
          
      validation_data:
        experimental_chips: ["heart_chip_001", "liver_chip_001", "kidney_chip_001"]
        correlation_coefficients:
          heart_chip: 0.85
          liver_chip: 0.91
          kidney_chip: 0.78
```

### Benefits
- **Systems-level understanding** of drug effects across organs
- **Integrated experimental design** with coordinated endpoints
- **Computational model validation** using multi-organ chip data  
- **Reduced animal use** for systemic toxicity studies

## Use Case 7: Precision Medicine Model Development

### Scenario
A clinical research organization needs to develop patient-specific models using iPSC-derived organoids to predict individual drug responses and optimize treatment selection.

### Implementation
```yaml
# Patient-specific organoid study
precision_medicine_cohort:
  study_id: "personalized_cf_treatment_2024"
  patient_cohort_size: 25
  
  model_systems:
    - id: "patient_001_lung_org"
      name: "CF Patient 001 Lung Organoid"
      type: "Organoid"
      patient_derived: true
      
      patient_metadata:
        age_at_sampling: 28
        sex: "female"
        genotype: "CFTR_F508del/F508del"
        clinical_phenotype:
          - id: "HP:0002205"
            name: "Recurrent respiratory infections"
          - id: "HP:0006528"
            name: "Chronic airway obstruction"
            
      organ_modeled:
        id: "UBERON:0001004"
        name: "respiratory system"
        
      cell_source: "Patient iPSC-derived airway epithelial cells"
      
      models:
        - biological_system_modeled: "patient_001_cf_phenotype"
          structured_concordance:
            molecular_similarity:
              patient_tissue_correlation: 0.89
              methodology: "scRNA-seq comparison with patient bronchial biopsy"
              
            functional_parity:
              functional_assays:
                - assay_type: "CFTR function (forskolin swelling)"
                  assay_result: 15.2
                  reference_value: 45.8  # healthy control
                  units: "percent_swelling"
                  
                - assay_type: "Mucus viscosity"
                  assay_result: 8.9
                  reference_value: 3.2   # healthy control
                  units: "cP"
      
      drug_testing_results:
        - compound: "ivacaftor"
          functional_improvement: 0.23
          molecular_markers:
            cftr_surface_expression_fold_change: 1.8
            
        - compound: "lumacaftor_ivacaftor"
          functional_improvement: 0.67
          molecular_markers:
            cftr_surface_expression_fold_change: 3.2
            
      clinical_correlation:
        treatment_response_prediction: "lumacaftor_ivacaftor"
        confidence_score: 0.87
        
      references:
        - id: "clinical_trial:NCT04xxxxxxx"
          title: "Personalized CF Treatment Selection Using Patient Organoids"
          status: "ongoing"
```

### Benefits
- **Personalized treatment selection** based on individual patient biology
- **Reduced clinical trial failures** through pre-screening
- **Patient stratification** for targeted therapy development
- **Predictive biomarker identification** for treatment response

## Implementation Guidelines

### Data Quality Standards
- **Ontology term validation** using established vocabularies (CL, UBERON, MONDO)
- **Mandatory provenance tracking** with literature references and DOIs
- **Quantitative metrics** with statistical significance testing
- **Reproducibility documentation** across experimental replicates

### Technical Integration
- **API-first design** with OpenAPI/GraphQL specifications
- **Version control** for evolving model systems and validation data
- **Interoperability testing** with existing biomedical databases
- **Validation pipelines** for data integrity and schema compliance

### Community Engagement
- **Working groups** for domain-specific extensions
- **Feedback mechanisms** for schema evolution
- **Training materials** and implementation examples
- **Certification programs** for data quality assurance

These use cases demonstrate NAMO's versatility in addressing diverse needs across regulatory science, pharmaceutical R&D, academic research, commercial applications, and clinical translation. The schema's flexibility and extensibility enable adaptation to emerging technologies and evolving research paradigms while maintaining data quality and interoperability standards.