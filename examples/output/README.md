## Organoid-example-003
### Input
```yaml
cell_source: Human small intestinal crypts isolated from biopsy samples
cell_types:
- id: CL:0000584
  name: enterocyte
- id: CL:0000160
  name: goblet cell
- id: CL:0000510
  name: paneth cell
- id: CL:1001516
  name: intestinal enteroendocrine cell
- id: CL:0002250
  name: intestinal crypt stem cell
culture_system: "Matrigel dome culture in 24-well plates with IntestiCult Organoid\
  \  Growth Medium. Cultures maintained at 37\xB0C with 5% CO2, passaged  every 7-10\
  \ days by mechanical dissociation."
description: A 3D intestinal organoid derived from human intestinal stem cells that  recapitulates
  the architecture and function of the small intestine.  Contains crypt-villus structures
  with stem cells, Paneth cells,  enterocytes, and goblet cells. Exhibits barrier
  function, nutrient  absorption, and antimicrobial peptide secretion.
differentiation_method: Intestinal stem cells are embedded in Matrigel and cultured
  in  IntestiCult medium containing Wnt3a, R-spondin1, Noggin, and EGF.  Organoids
  develop crypt-villus architecture through self-organization  over 5-7 days.
id: organoid:003
models:
- biological_system_modeled: intestinal_barrier:001
  concordance:
    cell_type_coverage: Contains all major intestinal epithelial cell types
    functional_parity: Demonstrates nutrient transport and antimicrobial secretion
    molecular_similarity: High expression of intestinal markers LGR5, OLFM4, MUC2
    pathway_concordance: Active Wnt signaling and Notch pathways
    phenotype_overlap: Exhibits tight junction formation and barrier function
    reproducibility: Consistent organoid formation efficiency >80%
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.7
        cell_type:
          id: CL:0000584
          name: enterocyte
        model_proportion: 0.65
        proportion_ratio: 0.93
      - biological_proportion: 0.12
        cell_type:
          id: CL:0000160
          name: goblet cell
        model_proportion: 0.15
        proportion_ratio: 1.25
      coverage_percentage: 88.5
      description: Single-cell analysis of intestinal epithelial cell diversity
      id: cellcov:003
      missing_cell_types:
      - id: CL:0009019
        name: tuft cell
      name: Intestinal Cell Type Representation
      represented_cell_types:
      - id: CL:0000584
        name: enterocyte
      - id: CL:0000160
        name: goblet cell
      - id: CL:0000510
        name: paneth cell
      - id: CL:0002250
        name: intestinal crypt stem cell
      single_cell_method: scRNA-seq with intestinal lineage markers
    functional_parity:
      conserved_functions:
      - Tight junction barrier formation
      - Mucus production and secretion
      - Antimicrobial peptide secretion
      description: Evaluation of intestinal barrier integrity and transport
      functional_assays:
      - assay_result: 1.8e-06
        assay_type: Permeability assay
        id: assay:016
        methodology: FITC-dextran permeability measurement
        name: Barrier permeability
        reference_value: 1.5e-06
        units: cm/s
      - assay_result: 42.5
        assay_type: Protein quantification
        id: assay:017
        methodology: Alcian blue staining quantification
        name: Mucin production
        reference_value: 50.2
        units: "\u03BCg/mg protein"
      functional_similarity_score: 0.79
      id: funcpar:008
      impaired_functions:
      - Immune cell interaction
      - Microbiome response
      name: Intestinal Barrier Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.523
        ensembl_id: ENSG00000163347
        fold_change: 1.1
        gene_symbol: CLDN1
        id: gene:019
        name: CLDN1
        p_value: 0.456
      correlation_coefficient: 0.81
      data_source: Human small intestine biopsy reference data
      description: RNA-seq comparison with human small intestine tissue
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000139292
        fold_change: 3.2
        gene_symbol: LGR5
        id: gene:017
        name: LGR5
        p_value: 0.0001
      - adjusted_p_value: 0.002
        ensembl_id: ENSG00000198788
        fold_change: 2.8
        gene_symbol: MUC2
        id: gene:018
        name: MUC2
        p_value: 0.0002
      id: molsim:008
      methodology: Single-cell RNA sequencing with intestinal lineage analysis
      name: Intestinal Organoid Expression Profile
      similarity_score: 0.85
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.78
        confidence_interval_upper: 0.88
        p_value: 0.0001
        statistical_test: Spearman correlation
    pathway_concordance:
      active_pathways:
      - activity_score: 0.91
        enrichment_score: 3.5
        id: pathway:005
        name: Wnt signaling pathway
        pathway_database: KEGG
        pathway_id: hsa04310
      - activity_score: 0.83
        enrichment_score: 2.7
        id: pathway:006
        name: Notch signaling pathway
        pathway_database: KEGG
        pathway_id: hsa04330
      description: Analysis of key intestinal development and maintenance pathways
      enrichment_statistics:
      - enrichment_score: 3.5
        genes_in_dataset: 102
        genes_in_pathway: 167
        p_value: 0.0001
        q_value: 0.001
      id: pathconcord:003
      name: Intestinal Signaling Pathway Analysis
      pathway_analysis_method: Gene Set Enrichment Analysis (GSEA)
      pathway_overlap_score: 0.87
    reproducibility:
      batch_to_batch_variation: 0.15
      coefficient_of_variation: 0.12
      description: Consistency of organoid formation and differentiation
      id: repro:008
      inter_laboratory_consistency: 0.82
      name: Intestinal Organoid Reproducibility
      quality_control_metrics:
      - metric_name: Formation efficiency
        metric_value: 0.85
        pass_fail_status: true
        threshold: 0.75
      - metric_name: Crypt-villus organization
        metric_value: 0.91
        pass_fail_status: true
        threshold: 0.8
      replicate_count: 32
      reproducibility_score: 0.88
name: Human Intestinal Organoid
organ_modeled:
  id: UBERON:0002108
  name: small intestine
type: Organoid

```
## QSARModel-example-002
### Input
```yaml
activity_endpoint: Hepatotoxicity and multi-organ ADMET properties
biological_organization_level: SUBCELLULAR
complexity_level: HIGH
description: A deep neural network model for predicting multiple ADMET (Absorption,
  Distribution,  Metabolism, Excretion, Toxicity) endpoints using molecular descriptors
  and fingerprints.  The model integrates multiple data sources and uses transfer
  learning from large  chemical databases to predict drug-drug interactions, cytotoxicity,
  and  pharmacokinetic properties across multiple species.
id: qsarmodel:002
model_performance:
  accuracy: 0.87
  auc: 0.91
  r_squared: 0.82
  sensitivity: 0.89
  specificity: 0.84
models:
- biological_system_modeled: hepatotoxicity_prediction:002
  concordance:
    functional_parity: Accurate prediction of hepatotoxic mechanisms
    molecular_similarity: High correlation with experimental cytotoxicity data
    reproducibility: Consistent performance across validation sets
  is_computed: true
  structured_concordance:
    functional_parity:
      conserved_functions:
      - Cytochrome P450 metabolism prediction
      - Drug-drug interaction identification
      - Acute toxicity classification
      description: Multi-endpoint toxicity prediction accuracy assessment
      dose_response_similarity:
        compound_tested: Acetaminophen hepatotoxicity dose-response
        correlation_coefficient: 0.83
        ec50_ratio: 1.18
        max_response_ratio: 0.91
      functional_assays:
      - assay_result: 0.87
        assay_type: Binary classification
        id: assay:035
        methodology: Random forest benchmark on DILIrank dataset
        name: Hepatotoxicity classification
        reference_value: 0.85
        units: accuracy
      - assay_result: 0.82
        assay_type: IC50 regression
        id: assay:036
        methodology: Gradient boosting regression with molecular descriptors
        name: CYP inhibition prediction
        reference_value: 0.8
        units: "R\xB2"
      - assay_result: 0.76
        assay_type: Pharmacokinetic modeling
        id: assay:037
        methodology: Multi-species allometric scaling with machine learning
        name: Drug clearance prediction
        reference_value: 0.74
        units: "R\xB2"
      functional_similarity_score: 0.89
      id: funcpar:015
      impaired_functions:
      - Chronic toxicity mechanisms
      - Individual variation modeling
      name: ADMET Prediction Performance
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.512
        ensembl_id: ENSG00000163631
        fold_change: 1.1
        gene_symbol: ALB
        id: gene:043
        name: ALB
        p_value: 0.423
      correlation_coefficient: 0.88
      data_source: ChEMBL hepatotoxicity annotations and ToxCast assay data
      description: Molecular similarity analysis for hepatotoxicity prediction
      differentially_expressed_genes:
      - adjusted_p_value: 0.01
        ensembl_id: ENSG00000160868
        fold_change: 2.8
        gene_symbol: CYP3A4
        id: gene:041
        name: CYP3A4
        p_value: 0.001
      - adjusted_p_value: 0.005
        ensembl_id: ENSG00000084207
        fold_change: 3.2
        gene_symbol: GSTP1
        id: gene:042
        name: GSTP1
        p_value: 0.0005
      id: molsim:015
      methodology: Tanimoto coefficient analysis with Morgan fingerprints
      name: Chemical Structure-Activity Relationship
      similarity_score: 0.91
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.85
        confidence_interval_upper: 0.93
        p_value: 0.0001
        statistical_test: Permutation test
    reproducibility:
      batch_to_batch_variation: 0.05
      coefficient_of_variation: 0.08
      description: Cross-validation and external test set performance
      id: repro:015
      inter_laboratory_consistency: 0.88
      name: Model Validation Reproducibility
      quality_control_metrics:
      - metric_name: Cross-validation stability
        metric_value: 0.91
        pass_fail_status: true
        threshold: 0.85
      - metric_name: External validation performance
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Feature importance consistency
        metric_value: 0.94
        pass_fail_status: true
        threshold: 0.9
      replicate_count: 50
      reproducibility_score: 0.92
molecular_descriptors:
- MORGAN_FINGERPRINTS
- RDKIT_DESCRIPTORS
- MACCS_KEYS
- PHARMACOPHORE_FEATURES
name: Deep Learning ADMET Prediction Model
references:
- authors:
  - Yang K
  - Swanson K
  - Jin W
  - Coley C
  - Eiden P
  - Gao H
  id: doi:10.1021/acs.jcim.4c00123
  journal: Journal of Chemical Information and Modeling
  title: 'Deep learning approaches for comprehensive ADMET prediction: integrating
    multi-task learning and transfer learning'
  url: https://pubs.acs.org/doi/10.1021/acs.jcim.4c00123
  year: 2024
- authors:
  - Chen H
  - Wang Y
  - Liu Z
  - Zhang S
  - Li X
  id: PMID:38445678
  journal: Nature Machine Intelligence
  title: Transformer-based molecular property prediction for drug discovery applications
  url: https://pubmed.ncbi.nlm.nih.gov/38445678/
  year: 2024
spatial_context: Chemical space defined by molecular descriptors and pharmacophore
  features
training_dataset_size: 45000
type: QSARModel

```
## OrganOnChip-example-zhu-2024
### Input
```yaml
biological_organization_level: SYSTEM
cell_types:
- id: CL:0000066
  name: epithelial cell
- id: CL:0002062
  name: type I pneumocyte
- id: CL:0000182
  name: hepatocyte
- id: CL:0000746
  name: cardiac muscle cell
complexity_level: HIGH
description: Dynamic microphysiological system chip platform with 4x4 microwell arrays
  supporting 304 spheroids for high-throughput, multi-dimensional drug screening.
  Integrates lung, liver, heart, and intestine models with microvalve-controlled flow
  for comprehensive drug evaluation and toxicity assessment.
id: mps:zhu_2024
microfluidic_design:
  architecture_type: LAYERED
  channel_configuration:
  - PARALLEL
  - BRANCHING
  channel_dimensions:
  - channel_name: micropillar_array
    height: 50
    length: 10.0
    width: 100
  - channel_name: microwell_array
    height: 100
    length: 10.0
    width: 200
  description: Three-layer platform with valve control and microwell arrays
  flow_control_method:
  - SYRINGE_PUMP
  - PRESSURE_DRIVEN
  id: microfluidic:zhu_001
  material:
  - PDMS
  name: Dynamic MSCP Multi-Layer Design
  number_of_channels: 16
models:
- biological_system_modeled: multi_organ_drug_screening:001
  concordance:
    functional_parity: Integrated drug absorption, distribution, and toxicity assessment
    molecular_similarity: Multi-organ spheroid models with preserved cellular characteristics
    reproducibility: High-throughput parallel testing with consistent results across
      304 spheroids
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.3
        cell_type:
          id: CL:0002062
          name: type I pneumocyte
        model_proportion: 0.25
        proportion_ratio: 0.83
      - biological_proportion: 0.22
        cell_type:
          id: CL:0000182
          name: hepatocyte
        model_proportion: 0.25
        proportion_ratio: 1.14
      coverage_percentage: 80.0
      description: Cell type diversity across four organ spheroid models
      id: cellcov:012
      missing_cell_types:
      - id: CL:0000071
        name: blood vessel endothelial cell
      - id: CL:0000115
        name: endothelial cell
      name: Multi-Organ Cell Type Representation
      represented_cell_types:
      - id: CL:0000066
        name: epithelial cell
      - id: CL:0002062
        name: type I pneumocyte
      - id: CL:0000182
        name: hepatocyte
      - id: CL:0000746
        name: cardiac muscle cell
      single_cell_method: Spheroid-specific cell type markers
    functional_parity:
      conserved_functions:
      - Drug absorption simulation
      - Multi-organ toxicity assessment
      - Dose-response modeling
      - IC50 determination
      description: High-throughput assessment of four anti-lung cancer drugs
      dose_response_similarity:
        compound_tested: Cisplatin multi-organ response
        correlation_coefficient: 0.85
        ec50_ratio: 0.9
        max_response_ratio: 0.92
      functional_assays:
      - assay_result: 0.45
        assay_type: Cell viability
        id: assay:071
        methodology: Live/dead staining with microscopy analysis
        name: Cisplatin cytotoxicity
        reference_value: 0.5
        units: "IC50 (\u03BCM)"
      - assay_result: 304
        assay_type: Pharmacokinetics
        id: assay:072
        methodology: Parallel screening across organ models
        name: Multi-organ drug distribution
        reference_value: 304
        units: spheroids analyzed
      - assay_result: 0.12
        assay_type: Drug efficacy
        id: assay:073
        methodology: High-throughput viability assessment
        name: Docetaxel screening
        reference_value: 0.15
        units: "IC50 (\u03BCM)"
      functional_similarity_score: 0.88
      id: funcpar:zhu_001
      impaired_functions:
      - Immune system interactions
      - Vascular perfusion dynamics
      name: Multi-Drug Screening Performance
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.743
        ensembl_id: ENSG00000111640
        fold_change: 1.0
        gene_symbol: GAPDH
        id: gene:090
        name: GAPDH
        p_value: 0.678
      correlation_coefficient: 0.81
      data_source: Multi-organ reference datasets for lung, liver, heart, intestine
      description: Comparison of spheroid models with native organ tissues
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000085563
        fold_change: 3.2
        gene_symbol: ABCB1
        id: gene:087
        name: ABCB1
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000160868
        fold_change: 4.8
        gene_symbol: CYP3A4
        id: gene:088
        name: CYP3A4
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000118194
        fold_change: 5.1
        gene_symbol: TNNT2
        id: gene:089
        name: TNNT2
        p_value: 0.0001
      id: molsim:zhu_001
      methodology: Multi-organ gene expression analysis of spheroid models
      name: Multi-Organ Spheroid Molecular Profile
      similarity_score: 0.84
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.78
        confidence_interval_upper: 0.88
        p_value: 0.0001
        statistical_test: Multi-organ differential expression analysis
    reproducibility:
      batch_to_batch_variation: 0.08
      coefficient_of_variation: 0.09
      description: Consistency across 304 spheroids and multiple drug screening runs
      id: repro:zhu_001
      inter_laboratory_consistency: 0.87
      name: High-Throughput Platform Reproducibility
      quality_control_metrics:
      - metric_name: Spheroid formation efficiency
        metric_value: 0.95
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Flow control stability
        metric_value: 0.93
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Multi-organ response consistency
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.75
      replicate_count: 304
      reproducibility_score: 0.91
name: Dynamic High-Throughput Multi-Organ Drug Screening Platform
organ_modeled:
  id: UBERON:0002048
  name: lung
perfusion_system: "Dynamic flow control with microvalve arrays at 100 \u03BCm/s initial\
  \ velocity. Differential flow rates: micropillar array at 9 \xD7 10\u207B\xB3 \u03BC\
  L/min and microwell array at 0.63 \u03BCL/min optimize spheroid culture and drug\
  \ delivery."
references:
- authors:
  - Zhu Y
  - Wang J
  - Li H
  - Chen X
  id: doi:10.1016/j.bioactmat.2024.05.028
  journal: Bioactive Materials
  title: Dynamic microphysiological system chip platform for high-throughput, customizable,
    and multi-dimensional drug screening
  url: https://www.sciencedirect.com/science/article/pii/S2452199X24001853
  year: 2024
sensor_integration:
- OPTICAL
spatial_context: Multi-layer microfluidic platform with interconnected organ spheroids
type: OrganOnChip

```
## ThreeDCellCulture-example-002
### Input
```yaml
biological_organization_level: CELLULAR_NEIGHBORHOOD
cell_source: Primary ovarian cancer cells, cancer-associated fibroblasts, and endothelial
  cells
cell_types:
- id: CL:0002418
  name: epithelial cell of ovary
- id: CL:0002548
  name: fibroblast of cardiac tissue
- id: CL:0000071
  name: blood vessel endothelial cell
complexity_level: MODERATE
description: A three-dimensional multicellular tumor spheroid model that recapitulates
  the  complex heterogeneity of ovarian cancer tumors. The spheroid contains cancer
  cells,  cancer-associated fibroblasts, and endothelial cells to mimic the tumor  microenvironment.
  Used for high-throughput drug screening and studying  drug resistance mechanisms
  in ovarian cancer.
id: spheroid:001
matrix_composition: Self-assembled cell aggregates in ultra-low attachment conditions
models:
- biological_system_modeled: ovarian_cancer:001
  concordance:
    functional_parity: Recapitulates chemotherapy resistance patterns
    molecular_similarity: High expression of ovarian cancer markers and drug resistance
      genes
    reproducibility: Consistent spheroid formation and drug response
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.65
        cell_type:
          id: CL:0002418
          name: epithelial cell of ovary
        model_proportion: 0.7
        proportion_ratio: 1.08
      - biological_proportion: 0.25
        cell_type:
          id: CL:0002548
          name: fibroblast of cardiac tissue
        model_proportion: 0.2
        proportion_ratio: 0.8
      coverage_percentage: 75.0
      description: Analysis of cell type diversity in cancer spheroids
      id: cellcov:008
      missing_cell_types:
      - id: CL:0000576
        name: monocyte
      - id: CL:0000084
        name: T cell
      name: Tumor Microenvironment Cell Representation
      represented_cell_types:
      - id: CL:0002418
        name: epithelial cell of ovary
      - id: CL:0002548
        name: fibroblast of cardiac tissue
      - id: CL:0000071
        name: blood vessel endothelial cell
      single_cell_method: Flow cytometry with cancer cell markers
    functional_parity:
      conserved_functions:
      - Cisplatin resistance development
      - Hypoxia-induced gene expression
      - Cell-cell adhesion maintenance
      description: Evaluation of chemotherapy sensitivity and resistance mechanisms
      dose_response_similarity:
        compound_tested: Paclitaxel sensitivity
        correlation_coefficient: 0.82
        ec50_ratio: 1.09
        max_response_ratio: 0.91
      functional_assays:
      - assay_result: 0.35
        assay_type: Cell viability
        id: assay:041
        methodology: ATP-based cell viability assay after 72h treatment
        name: Cisplatin cytotoxicity
        reference_value: 0.32
        units: "IC50 (\u03BCM)"
      - assay_result: 3.8
        assay_type: Protein quantification
        id: assay:042
        methodology: "HIF-1\u03B1 immunofluorescence quantification"
        name: Hypoxia marker expression
        reference_value: 4.2
        units: fold change
      - assay_result: 1.24
        assay_type: Volume measurement
        id: assay:043
        methodology: Automated imaging and volume analysis
        name: Spheroid growth rate
        reference_value: 1.18
        units: "mm\xB3/day"
      functional_similarity_score: 0.86
      id: funcpar:017
      impaired_functions:
      - Vascular invasion capacity
      - Metastatic spread simulation
      name: Cancer Drug Response Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.901
        ensembl_id: ENSG00000075624
        fold_change: 1.0
        gene_symbol: ACTB
        id: gene:050
        name: ACTB
        p_value: 0.823
      correlation_coefficient: 0.81
      data_source: The Cancer Genome Atlas ovarian adenocarcinoma dataset
      description: RNA-seq comparison with patient ovarian tumor samples
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000141510
        fold_change: 0.3
        gene_symbol: TP53
        id: gene:047
        name: TP53
        p_value: 0.0001
      - adjusted_p_value: 0.002
        ensembl_id: ENSG00000012048
        fold_change: 2.8
        gene_symbol: BRCA1
        id: gene:048
        name: BRCA1
        p_value: 0.0002
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000085563
        fold_change: 4.5
        gene_symbol: ABCB1
        id: gene:049
        name: ABCB1
        p_value: 0.0001
      id: molsim:017
      methodology: Single-cell RNA sequencing with tumor microenvironment analysis
      name: Ovarian Cancer Spheroid Expression Profile
      similarity_score: 0.84
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.77
        confidence_interval_upper: 0.89
        p_value: 0.0001
        statistical_test: Pearson correlation
    reproducibility:
      batch_to_batch_variation: 0.15
      coefficient_of_variation: 0.13
      description: Inter-batch consistency and drug response variability
      id: repro:017
      inter_laboratory_consistency: 0.83
      name: Spheroid Formation Reproducibility
      quality_control_metrics:
      - metric_name: Spheroid size uniformity
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Cell viability
        metric_value: 0.94
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Drug response consistency
        metric_value: 0.86
        pass_fail_status: true
        threshold: 0.75
      replicate_count: 48
      reproducibility_score: 0.87
name: 3D Multicellular Ovarian Cancer Spheroid Model
references:
- authors:
  - Smith JA
  - Johnson MD
  - Brown KL
  - Davis RT
  id: doi:10.1038/s41598-024-73680-6
  journal: Scientific Reports
  title: 'Multicellular ovarian cancer spheroids: novel 3D model to mimic tumour complexity'
  url: https://www.nature.com/articles/s41598-024-73680-6
  year: 2024
- authors:
  - Sharma P
  - Kumar A
  - Singh R
  id: doi:10.1002/cai2.102
  journal: Cancer Innovation
  title: A comprehensive review of 3D cancer models for drug screening and translational
    research
  url: https://onlinelibrary.wiley.com/doi/10.1002/cai2.102
  year: 2024
size_range: 200-500 micrometers diameter
spatial_context: 3D tumor microenvironment with hypoxic core and proliferative outer
  layers
three_d_architecture: SPHEROID
type: ThreeDCellCulture

```
## Organoid-example-002
### Input
```yaml
cell_source: Primary human hepatocytes and cholangiocytes isolated from donor liver
  tissue
cell_types:
- id: CL:0000182
  name: hepatocyte
- id: CL:0000183
  name: cholangiocyte
- id: CL:0002138
  name: hepatic stellate cell
- id: CL:0000091
  name: Kupffer cell
culture_system: "Low-attachment plates with hepatocyte organoid medium containing\
  \  Wnt3a, R-spondin, and Noggin. Cultures maintained at 37\xB0C with 5% CO2  and\
  \ medium changed every 2-3 days."
description: A liver organoid system derived from human hepatocytes and cholangiocytes  that
  recapitulates key hepatic functions including albumin production,  urea synthesis,
  and cytochrome P450 metabolism. The organoid maintains  hepatocyte polarity and
  bile canaliculi formation, making it suitable  for drug metabolism and hepatotoxicity
  studies.
differentiation_method: Co-culture of primary hepatocytes and cholangiocytes in hepatocyte  culture
  medium supplemented with hepatocyte growth factor (HGF) and  epidermal growth factor
  (EGF). Organoids form through self-organization  over 7-10 days.
id: organoid:002
models:
- biological_system_modeled: hepatic_function:001
  concordance:
    cell_type_coverage: Contains primary hepatic cell types with maintained polarity
    functional_parity: Exhibits drug-metabolizing enzyme activity comparable to primary
      hepatocytes
    molecular_similarity: High expression of hepatic markers CYP3A4, ALB, AFP
    pathway_concordance: Active Phase I and Phase II drug metabolism pathways
    phenotype_overlap: Maintains key hepatic functions including albumin and urea
      production
    reproducibility: Consistent albumin production across biological replicates
  is_computed: false
  structured_concordance:
    functional_parity:
      conserved_functions:
      - Albumin synthesis and secretion
      - Urea cycle activity
      - Glucose metabolism
      description: Evaluation of liver-specific metabolic and synthetic functions
      functional_assays:
      - assay_result: 28.5
        assay_type: Protein secretion
        id: assay:014
        methodology: ELISA-based albumin quantification
        name: Albumin production rate
        reference_value: 45.2
        units: "\u03BCg/mg protein/24h"
      - assay_result: 12.8
        assay_type: Metabolic function
        id: assay:015
        methodology: Colorimetric urea assay
        name: Urea synthesis capacity
        reference_value: 18.5
        units: "\u03BCg/mg protein/24h"
      functional_similarity_score: 0.71
      id: funcpar:007
      impaired_functions:
      - CYP450 enzyme activity
      - Bile acid synthesis
      name: Hepatic Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.634
        ensembl_id: ENSG00000101076
        fold_change: 1.1
        gene_symbol: HNF4A
        id: gene:016
        name: HNF4A
        p_value: 0.567
      correlation_coefficient: 0.78
      data_source: Primary human hepatocyte reference transcriptomes
      description: RNA-seq comparison with primary human hepatocytes
      differentially_expressed_genes:
      - adjusted_p_value: 0.345
        ensembl_id: ENSG00000163631
        fold_change: 0.8
        gene_symbol: ALB
        id: gene:014
        name: ALB
        p_value: 0.234
      - adjusted_p_value: 0.01
        ensembl_id: ENSG00000160868
        fold_change: -3.2
        gene_symbol: CYP3A4
        id: gene:015
        name: CYP3A4
        p_value: 0.001
      id: molsim:007
      methodology: Bulk RNA sequencing with hepatic marker analysis
      name: Hepatic Organoid Gene Expression
      similarity_score: 0.81
      statistical_significance:
        adjusted_p_value: 0.005
        confidence_interval_lower: 0.74
        confidence_interval_upper: 0.86
        p_value: 0.001
        statistical_test: Pearson correlation
    reproducibility:
      batch_to_batch_variation: 0.19
      coefficient_of_variation: 0.16
      description: Inter-batch consistency of hepatic organoid generation
      id: repro:007
      inter_laboratory_consistency: 0.78
      name: Hepatic Organoid Reproducibility
      quality_control_metrics:
      - metric_name: Organoid size
        metric_value: 380.0
        pass_fail_status: true
        threshold: 300.0
      - metric_name: Hepatocyte marker expression
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      replicate_count: 24
      reproducibility_score: 0.84
name: Hepatic Organoid Model
organ_modeled:
  id: UBERON:0002107
  name: liver
type: Organoid

```
## OrganOnChip-example-001
### Input
```yaml
cell_source: "Primary human CF bronchial epithelial cells (CFTR \u0394F508 mutation)"
cell_types:
- id: CL:0002632
  name: epithelial cell of lower respiratory tract
- id: CL:0002139
  name: endothelial cell of vascular tree
- id: CL:0000775
  name: neutrophil
description: A microfluidic airway-on-chip model of cystic fibrosis using primary
  human CF  bronchial epithelial cells cultured at air-liquid interface, interfaced
  with  microvascular endothelium. This chip faithfully reproduces hallmarks of CF
  airways  including excess mucus accumulation, increased ciliary beat frequency,
  and  hyperinflammatory responses with elevated IL-8 secretion leading to robust  neutrophil
  adhesion and transmigration.
id: organonchip:001
mechanical_forces:
  cyclic_stretch_percent: 5
  description: Mechanical forces mimicking physiological breathing
  duration_minutes: 10080
  frequency_hz: 0.2
  id: mechanical:001
  name: Breathing simulation forces
  shear_stress: 0.5
  stimulation_type:
  - BREATHING_MOTION
  - SHEAR_STRESS
microfluidic_design:
  architecture_type: TWO_CHANNEL
  channel_configuration:
  - PARALLEL
  channel_dimensions:
  - channel_name: apical
    height: 1000
    length: 16.7
    width: 1000
  - channel_name: basolateral
    height: 200
    length: 16.7
    width: 1000
  description: Two-channel microfluidic device optimized for airway modeling
  flow_control_method:
  - SYRINGE_PUMP
  - GRAVITY_DRIVEN
  id: microfluidic:001
  interface_type:
  - AIR_LIQUID
  - VASCULAR_EPITHELIAL
  material:
  - PDMS
  membrane_pore_size: 0.4
  membrane_thickness: 10
  membrane_type: POROUS_POLYMER
  name: CF Airway Chip Design
  number_of_channels: 2
  sensors_integrated:
  - TEER
  special_features:
  - Transparent for imaging
  - Removable membrane for cell recovery
  surface_treatment:
  - COLLAGEN
  - FIBRONECTIN
models:
- biological_system_modeled: cf_airway:001
  concordance:
    functional_parity: Recapitulates CF airway phenotypes including mucus accumulation
    molecular_similarity: High expression of CF-related genes and markers
    reproducibility: Consistent CF phenotype across experimental replicates
  is_computed: false
  structured_concordance:
    functional_parity:
      conserved_functions:
      - Mucus hypersecretion
      - Impaired ciliary clearance
      - Inflammatory response
      description: Evaluation of CF-specific airway dysfunction
      functional_assays:
      - assay_result: 3.8
        assay_type: Histological analysis
        id: assay:018
        methodology: Alcian blue/PAS staining quantification
        name: Mucus accumulation
        reference_value: 1.2
        units: mucus thickness score
      - assay_result: 750.0
        assay_type: High-speed microscopy
        id: assay:019
        methodology: High-speed video microscopy analysis
        name: Ciliary beat frequency
        reference_value: 600.0
        units: beats/min
      - assay_result: 185.2
        assay_type: Cytokine assay
        id: assay:020
        methodology: ELISA-based cytokine quantification
        name: IL-8 secretion
        reference_value: 150.5
        units: pg/mL
      functional_similarity_score: 0.82
      id: funcpar:009
      impaired_functions:
      - CFTR-mediated chloride transport
      - Antimicrobial peptide activity
      name: CF Airway Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.345
        ensembl_id: ENSG00000129654
        fold_change: 1.3
        gene_symbol: FOXJ1
        id: gene:022
        name: FOXJ1
        p_value: 0.234
      correlation_coefficient: 0.73
      data_source: CF patient bronchial epithelial cell reference data
      description: RNA-seq comparison with CF patient airway samples
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000001626
        fold_change: -8.5
        gene_symbol: CFTR
        id: gene:020
        name: CFTR
        p_value: 0.0001
      - adjusted_p_value: 0.002
        ensembl_id: ENSG00000215182
        fold_change: 4.2
        gene_symbol: MUC5AC
        id: gene:021
        name: MUC5AC
        p_value: 0.0002
      id: molsim:009
      methodology: Bulk RNA sequencing with CF-specific gene panel analysis
      name: CF Airway Expression Analysis
      similarity_score: 0.76
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.68
        confidence_interval_upper: 0.81
        p_value: 0.0001
        statistical_test: Pearson correlation
    reproducibility:
      batch_to_batch_variation: 0.13
      coefficient_of_variation: 0.11
      description: Inter-chip consistency of CF phenotype
      id: repro:009
      inter_laboratory_consistency: 0.84
      name: CF Airway Chip Reproducibility
      quality_control_metrics:
      - metric_name: Cell viability
        metric_value: 0.94
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Barrier integrity
        metric_value: 0.88
        pass_fail_status: true
        threshold: 0.8
      - metric_name: CF phenotype penetrance
        metric_value: 0.92
        pass_fail_status: true
        threshold: 0.85
      replicate_count: 18
      reproducibility_score: 0.89
name: CF Airway-on-Chip
organ_modeled:
  id: UBERON:0001005
  name: respiratory airway
type: OrganOnChip

```
## Organoid-example-005
### Input
```yaml
biological_organization_level: ORGAN
cell_source: Human induced pluripotent stem cells (iPSCs) from healthy donors and
  cardiac disease patients
cell_types:
- id: CL:0000746
  name: cardiac muscle cell
- id: CL:0002494
  name: cardiocyte
- id: CL:0002548
  name: fibroblast of cardiac tissue
- id: CL:0000071
  name: blood vessel endothelial cell
complexity_level: HIGH
culture_system: Hanging drop culture followed by suspension culture in cardiac differentiation  medium.
  Organoids maintained for 14-21 days with regular medium changes and  monitoring
  of spontaneous contractile activity.
description: A 3D cardiac organoid derived from human induced pluripotent stem cells
  that  recapitulates key aspects of human heart development and function. The organoid  contains
  cardiomyocytes, cardiac fibroblasts, and endothelial cells organized  in chamber-like
  structures with spontaneous contractile activity. Used for  cardiotoxicity screening,
  particularly doxorubicin-induced cardiomyopathy  and drug safety assessment.
differentiation_method: Cardiac differentiation protocol using temporal modulation
  of Wnt signaling  with CHIR99021 and IWP2, followed by metabolic selection with
  lactate medium  to enrich for cardiomyocytes. Self-assembly into 3D organoids through  hanging
  drop aggregation.
id: organoid:005
models:
- biological_system_modeled: cardiac_toxicity:001
  concordance:
    functional_parity: Recapitulates doxorubicin-induced cardiomyopathy
    molecular_similarity: High expression of cardiac-specific markers and cardiotoxicity
      genes
    reproducibility: Consistent cardiotoxic response across experimental batches
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.7
        cell_type:
          id: CL:0000746
          name: cardiac muscle cell
        model_proportion: 0.75
        proportion_ratio: 1.07
      - biological_proportion: 0.2
        cell_type:
          id: CL:0002548
          name: fibroblast of cardiac tissue
        model_proportion: 0.15
        proportion_ratio: 0.75
      coverage_percentage: 82.5
      description: Analysis of cardiac cell type diversity and organization
      id: cellcov:006
      missing_cell_types:
      - id: CL:0000182
        name: hepatocyte
      - id: CL:0002072
        name: nodal myocyte
      name: Cardiac Cell Type Representation
      represented_cell_types:
      - id: CL:0000746
        name: cardiac muscle cell
      - id: CL:0002548
        name: fibroblast of cardiac tissue
      - id: CL:0000071
        name: blood vessel endothelial cell
      single_cell_method: scRNA-seq with cardiac lineage markers
    functional_parity:
      conserved_functions:
      - Spontaneous contractile activity
      - Calcium handling mechanisms
      - Drug-induced injury response
      description: Evaluation of cardiac contractile function and drug-induced injury
      dose_response_similarity:
        compound_tested: Doxorubicin cardiotoxicity
        correlation_coefficient: 0.78
        ec50_ratio: 1.25
        max_response_ratio: 0.89
      functional_assays:
      - assay_result: 0.58
        assay_type: Mechanical function
        id: assay:029
        methodology: Video-based motion tracking analysis of organoid contraction
        name: Contractile force measurement
        reference_value: 0.75
        units: relative force
      - assay_result: 45.2
        assay_type: Electrophysiology
        id: assay:030
        methodology: Optical mapping of calcium transients
        name: Beat frequency analysis
        reference_value: 60.8
        units: beats per minute
      - assay_result: 125.6
        assay_type: Biomarker quantification
        id: assay:031
        methodology: ELISA-based troponin I quantification in culture medium
        name: Troponin I release
        reference_value: 98.2
        units: ng/mL
      functional_similarity_score: 0.81
      id: funcpar:013
      impaired_functions:
      - Complex electrophysiological patterns
      - Metabolic stress response
      name: Cardiotoxicity Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.567
        ensembl_id: ENSG00000159251
        fold_change: 1.2
        gene_symbol: ACTC1
        id: gene:036
        name: ACTC1
        p_value: 0.456
      correlation_coefficient: 0.83
      data_source: Human heart biopsy samples and doxorubicin cardiomyopathy patients
      description: RNA-seq comparison with human heart samples and cardiomyopathy
        patients
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000118194
        fold_change: 5.8
        gene_symbol: TNNT2
        id: gene:033
        name: TNNT2
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000092054
        fold_change: 4.2
        gene_symbol: MYH7
        id: gene:034
        name: MYH7
        p_value: 0.0001
      - adjusted_p_value: 0.005
        ensembl_id: ENSG00000087088
        fold_change: 3.1
        gene_symbol: BAX
        id: gene:035
        name: BAX
        p_value: 0.0005
      id: molsim:013
      methodology: Bulk RNA sequencing with cardiac-specific gene panel analysis
      name: Cardiac Organoid Cardiotoxicity Gene Expression
      similarity_score: 0.86
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.79
        confidence_interval_upper: 0.91
        p_value: 0.0001
        statistical_test: Pearson correlation
    reproducibility:
      batch_to_batch_variation: 0.13
      coefficient_of_variation: 0.11
      description: Inter-batch and inter-laboratory consistency assessment
      id: repro:013
      inter_laboratory_consistency: 0.86
      name: Cardiac Organoid Reproducibility
      quality_control_metrics:
      - metric_name: Contractile activity onset
        metric_value: 0.94
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Cardiac marker expression
        metric_value: 0.91
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Organoid morphology score
        metric_value: 0.87
        pass_fail_status: true
        threshold: 0.75
      replicate_count: 42
      reproducibility_score: 0.89
name: Human Cardiac Organoid Cardiotoxicity Model
organ_modeled:
  id: UBERON:0000948
  name: heart
references:
- authors:
  - Chen X
  - Li Y
  - Wang H
  - Zhang L
  id: PMID:37879593
  journal: Heliyon
  title: 'Assessment of doxorubicin toxicity using human cardiac organoids: A novel
    model for evaluating drug cardiotoxicity'
  url: https://pubmed.ncbi.nlm.nih.gov/37879593/
  year: 2023
- authors:
  - Rodriguez-Gonzalez M
  - Martinez-Sanchez A
  id: doi:10.3389/fcvm.2025.1537730
  journal: Frontiers in Cardiovascular Medicine
  title: 'Cardiac organoids: a new tool for disease modeling and drug screening applications'
  url: https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2025.1537730/full
  year: 2025
spatial_context: 3D cardiac chamber-like structures with organized sarcomeric architecture
type: Organoid

```
## DigitalTwin-example-001
### Input
```yaml
biological_organization_level: SYSTEM
complexity_level: HIGH
description: A digital twin model integrating gut-liver-placenta microphysiological
  systems  to simulate drug pharmacokinetics in pregnant women. The model combines
  real-time  physiological data with mechanistic simulations to predict drug absorption,  distribution,
  metabolism, and placental transfer. Used for personalized dosing  recommendations
  and fetal safety assessment during pregnancy.
id: digitaltwin:001
models:
- biological_system_modeled: maternal_fetal_pharmacokinetics:001
  concordance:
    functional_parity: Accurate prediction of drug disposition in pregnancy
    molecular_similarity: High fidelity physiological parameter modeling
    reproducibility: Consistent predictive performance across patient populations
  is_computed: true
  structured_concordance:
    functional_parity:
      conserved_functions:
      - Maternal drug clearance
      - Placental drug transfer
      - Fetal drug exposure
      - First-pass metabolism
      description: Digital twin accuracy in predicting drug disposition
      dose_response_similarity:
        compound_tested: Prednisone maternal-fetal pharmacokinetics
        correlation_coefficient: 0.91
        ec50_ratio: 1.05
        max_response_ratio: 0.97
      functional_assays:
      - assay_result: 0.94
        assay_type: Pharmacokinetic prediction
        id: assay:062
        methodology: Comparison with clinical PK data for prednisone
        name: Maternal plasma concentration
        reference_value: 0.91
        units: "R\xB2"
      - assay_result: 0.87
        assay_type: Drug transport prediction
        id: assay:063
        methodology: Maternal-fetal concentration ratio prediction
        name: Placental transfer ratio
        reference_value: 0.84
        units: correlation coefficient
      - assay_result: 0.89
        assay_type: Metabolism prediction
        id: assay:064
        methodology: Prednisolone formation from prednisone
        name: Metabolite formation
        reference_value: 0.86
        units: "R\xB2"
      functional_similarity_score: 0.92
      id: funcpar:024
      impaired_functions:
      - Individual genetic variation
      - Disease state modifications
      name: Pharmacokinetic Prediction Performance
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.678
        ensembl_id: ENSG00000163631
        fold_change: 1.0
        gene_symbol: ALB
        id: gene:078
        name: ALB
        p_value: 0.567
      correlation_coefficient: 0.91
      data_source: Maternal-fetal pharmacokinetic studies database
      description: Digital twin parameter calibration against clinical pharmacokinetic
        data
      differentially_expressed_genes:
      - adjusted_p_value: 0.01
        ensembl_id: ENSG00000160868
        fold_change: 1.8
        gene_symbol: CYP3A4
        id: gene:075
        name: CYP3A4
        p_value: 0.001
      - adjusted_p_value: 0.005
        ensembl_id: ENSG00000085563
        fold_change: 2.3
        gene_symbol: ABCB1
        id: gene:076
        name: ABCB1
        p_value: 0.0005
      - adjusted_p_value: 0.02
        ensembl_id: ENSG00000134538
        fold_change: 1.5
        gene_symbol: SLCO1B1
        id: gene:077
        name: SLCO1B1
        p_value: 0.002
      id: molsim:024
      methodology: Bayesian parameter estimation with clinical PK data
      name: Physiological Parameter Concordance
      similarity_score: 0.94
      statistical_significance:
        adjusted_p_value: 0.005
        confidence_interval_lower: 0.88
        confidence_interval_upper: 0.96
        p_value: 0.0005
        statistical_test: Bayesian credible intervals
    reproducibility:
      batch_to_batch_variation: 0.08
      coefficient_of_variation: 0.1
      description: Cross-patient and cross-study validation performance
      id: repro:024
      inter_laboratory_consistency: 0.88
      name: Digital Twin Reproducibility
      quality_control_metrics:
      - metric_name: Parameter estimation convergence
        metric_value: 0.96
        pass_fail_status: true
        threshold: 0.9
      - metric_name: Real-time data integration
        metric_value: 0.92
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Clinical validation accuracy
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      replicate_count: 75
      reproducibility_score: 0.9
name: Maternal-Fetal Pharmacokinetic Digital Twin
personalization_parameters:
- Maternal weight and BMI
- Gestational age
- Placental blood flow
- Hepatic enzyme activity
- Gastrointestinal transit time
real_time_data_sources:
- Maternal vital signs monitoring
- Drug concentration measurements
- IoT sensor data
- Clinical monitoring systems
references:
- authors:
  - Zhang L
  - Chen M
  - Wang Y
  - Liu X
  id: doi:10.3389/fphar.2025.1528748
  journal: Frontiers in Pharmacology
  title: Digital twin-enhanced three-organ microphysiological system for studying
    drug pharmacokinetics in pregnant women
  url: https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1528748/full
  year: 2025
- authors:
  - Kumar A
  - Smith R
  - Johnson K
  - Davis M
  id: doi:10.1038/s41746-024-01402-3
  journal: npj Digital Medicine
  title: Challenges and opportunities for digital twins in precision medicine from
    a complex systems perspective
  url: https://www.nature.com/articles/s41746-024-01402-3
  year: 2024
spatial_context: Multi-organ system with maternal circulation and fetal compartments
twin_scope: PATIENT
type: DigitalTwin
update_frequency: Continuous real-time updating with clinical data integration

```
## CellLineModel-example-001
### Input
```yaml
authentication_method: STR profiling and mycoplasma testing performed quarterly
cell_source: Immortalized human hepatocellular carcinoma cell line (ATCC HB-8065)
cell_types:
- id: CL:0000182
  name: hepatocyte
culture_conditions: "DMEM + 10% FBS, 37\xB0C, 5% CO2, sub-confluent passage every\
  \ 2-3 days"
description: HepG2 human hepatocellular carcinoma cell line used as an in vitro model
  for drug-induced liver injury (DILI) screening and hepatotoxicity assessment. While
  not recapitulating all aspects of primary hepatocytes, it provides a standardized,
  reproducible platform for initial toxicity screening.
id: cellline:001
models:
- biological_system_modeled: hepatotoxicity:001
  concordance:
    functional_parity: Limited drug metabolism capacity
    molecular_similarity: Moderate similarity to primary hepatocytes
    reproducibility: High reproducibility across laboratories
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.78
        cell_type:
          id: CL:0000182
          name: hepatocyte
        model_proportion: 1.0
        proportion_ratio: 1.28
      coverage_percentage: 62.0
      description: Analysis of hepatocyte-like characteristics in HepG2 cells
      id: cellcov:004
      missing_cell_types:
      - id: CL:0000091
        name: Kupffer cell
      - id: CL:0002138
        name: hepatic stellate cell
      name: HepG2 Hepatocyte Representation
      represented_cell_types:
      - id: CL:0000182
        name: hepatocyte
      single_cell_method: Flow cytometry with hepatocyte markers
    functional_parity:
      conserved_functions:
      - Albumin production
      - Basic glucose metabolism
      - Cell viability assessment
      description: Evaluation of drug metabolism and hepatic functions
      dose_response_similarity:
        compound_tested: Acetaminophen
        correlation_coefficient: 0.73
        ec50_ratio: 2.1
        max_response_ratio: 0.85
      functional_assays:
      - assay_result: 0.15
        assay_type: Enzymatic activity
        id: assay:002
        methodology: Luciferin-IPA substrate conversion assay
        name: CYP3A4 activity assay
        reference_value: 2.8
        units: pmol/min/mg protein
      - assay_result: 12.5
        assay_type: Protein secretion
        id: assay:003
        methodology: ELISA-based albumin quantification
        name: Albumin production
        reference_value: 45.2
        units: "\u03BCg/mg protein/24h"
      functional_similarity_score: 0.45
      id: funcpar:002
      impaired_functions:
      - Phase I drug metabolism
      - Phase II conjugation reactions
      - Bile acid synthesis
      name: Hepatic Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.723
        ensembl_id: ENSG00000163631
        fold_change: 0.9
        gene_symbol: ALB
        id: gene:006
        name: ALB
        p_value: 0.678
      correlation_coefficient: 0.58
      data_source: RNA-seq comparison with freshly isolated primary hepatocytes
      description: Transcriptomic comparison with primary human hepatocytes
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000160868
        fold_change: -15.2
        gene_symbol: CYP3A4
        id: gene:004
        name: CYP3A4
        p_value: 0.0001
      - adjusted_p_value: 0.002
        ensembl_id: ENSG00000140505
        fold_change: -8.7
        gene_symbol: CYP1A2
        id: gene:005
        name: CYP1A2
        p_value: 0.0002
      id: molsim:002
      methodology: Bulk RNA sequencing with DESeq2 analysis
      name: HepG2 vs Primary Hepatocyte Comparison
      similarity_score: 0.62
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.52
        confidence_interval_upper: 0.67
        p_value: 0.0001
        statistical_test: Pearson correlation
    reproducibility:
      batch_to_batch_variation: 0.12
      coefficient_of_variation: 0.08
      description: Inter-laboratory and inter-passage consistency
      id: repro:002
      inter_laboratory_consistency: 0.89
      name: HepG2 Model Reproducibility
      quality_control_metrics:
      - metric_name: Cell confluence
        metric_value: 85.0
        pass_fail_status: true
        threshold: 80.0
      - metric_name: Passage number
        metric_value: 15.0
        pass_fail_status: true
        threshold: 25.0
      - metric_name: Doubling time
        metric_value: 22.5
        pass_fail_status: true
        threshold: 30.0
      replicate_count: 48
      reproducibility_score: 0.91
name: HepG2 Hepatotoxicity Model
passage_range: 5-25 passages recommended for experimental use
type: CellLineModel

```
## PBPKModel-example-001
### Input
```yaml
biological_organization_level: SYSTEM
compartments:
- blood_flow: 90.0
  compartment_type: LIVER
  id: pbpk_liver:001
  name: Liver compartment
  partition_coefficient: 0.8
  volume: 1.8
- blood_flow: 60.0
  compartment_type: KIDNEY
  id: pbpk_kidney:001
  name: Kidney compartment
  partition_coefficient: 0.7
  volume: 0.31
- blood_flow: 12.0
  compartment_type: MUSCLE
  id: pbpk_muscle:001
  name: Muscle compartment
  partition_coefficient: 0.6
  volume: 35.0
- blood_flow: 5.0
  compartment_type: FAT
  id: pbpk_fat:001
  name: Fat compartment
  partition_coefficient: 0.4
  volume: 14.0
complexity_level: HIGH
computational_method: Ordinary differential equations with physiological parameters
description: A physiologically-based pharmacokinetic model for acetaminophen in humans,  incorporating
  hepatic metabolism, renal clearance, and tissue distribution.  The model predicts
  plasma concentrations and hepatotoxicity risk following  oral administration across
  different dosing regimens.
drug_properties:
  clearance: 18.0
  logp: 0.46
  molecular_weight: 151.16
  pka: 9.38
  protein_binding: 0.1
elimination_pathways:
- Hepatic glucuronidation (UGT1A1, UGT1A6)
- Hepatic sulfation (SULT1A1)
- CYP2E1-mediated oxidation to NAPQI
- Renal clearance
id: pbpk:001
models:
- biological_system_modeled: acetaminophen_pk:001
  concordance:
    functional_parity: Predicts clinical PK profiles within 2-fold
    molecular_similarity: Mechanistic representation of drug metabolism
    reproducibility: Validated across multiple clinical studies
  is_computed: true
  structured_concordance:
    functional_parity:
      conserved_functions:
      - Plasma concentration-time profiles
      - Hepatic metabolism prediction
      - Renal clearance modeling
      description: Evaluation of PBPK model performance in predicting clinical outcomes
      dose_response_similarity:
        compound_tested: Acetaminophen dose range 325-1000mg
        correlation_coefficient: 0.89
        ec50_ratio: 1.12
        max_response_ratio: 0.96
      functional_assays:
      - assay_result: 1.8
        assay_type: Pharmacokinetic parameter
        id: assay:011
        methodology: Predicted/observed Cmax ratio analysis
        name: Cmax prediction accuracy
        reference_value: 2.0
        units: fold error
      - assay_result: 1.3
        assay_type: Pharmacokinetic parameter
        id: assay:012
        methodology: Predicted/observed AUC ratio analysis
        name: AUC prediction accuracy
        reference_value: 2.0
        units: fold error
      - assay_result: 16.5
        assay_type: Pharmacokinetic parameter
        id: assay:013
        methodology: Total body clearance prediction validation
        name: Clearance prediction
        reference_value: 18.0
        units: L/h
      functional_similarity_score: 0.84
      id: funcpar:006
      impaired_functions:
      - Inter-individual variability
      - Drug-drug interaction prediction
      name: Pharmacokinetic Prediction Performance
    molecular_similarity:
      correlation_coefficient: 0.82
      data_source: Clinical pharmacokinetic studies and in vitro metabolism data
      description: Comparison of predicted vs observed pharmacokinetic parameters
      id: molsim:006
      methodology: Physiological parameter validation against clinical data
      name: PBPK Mechanistic Similarity
      similarity_score: 0.76
      statistical_significance:
        adjusted_p_value: 0.005
        confidence_interval_lower: 0.71
        confidence_interval_upper: 0.89
        p_value: 0.001
        statistical_test: Linear regression of predicted vs observed
    reproducibility:
      batch_to_batch_variation: 0.08
      coefficient_of_variation: 0.15
      description: Model consistency across different populations and scenarios
      id: repro:006
      inter_laboratory_consistency: 0.91
      name: PBPK Model Reproducibility
      quality_control_metrics:
      - metric_name: Model convergence
        metric_value: 1.0
        pass_fail_status: true
        threshold: 0.95
      - metric_name: Parameter sensitivity
        metric_value: 0.85
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Clinical validation score
        metric_value: 0.82
        pass_fail_status: true
        threshold: 0.75
      replicate_count: 150
      reproducibility_score: 0.87
name: Human Acetaminophen PBPK Model
prediction_scope: Plasma and tissue concentrations, hepatotoxicity biomarkers
software_platform: MATLAB with SimBiology toolbox
spatial_context: Whole-body physiological representation with organ-specific kinetics
species_modeled:
  id: NCBITaxon:9606
  name: Homo sapiens
type: PBPKModel
validation_datasets:
- Clinical pharmacokinetic studies (n=120 subjects)
- Hepatotoxicity biomarker data
- Pediatric dosing studies

```
## TissueOnChip-example-001
### Input
```yaml
barrier_functions:
- Selective molecular transport
- Tight junction integrity
- P-glycoprotein efflux activity
biological_organization_level: TISSUE
complexity_level: HIGH
description: A microfluidic tissue-on-chip model that recreates the blood-brain barrier
  (BBB)  using human brain microvascular endothelial cells, pericytes, and astrocytes.  The
  model features physiological shear stress, tight junction formation, and  selective
  permeability for drug transport studies.
id: tissueonchip:001
mechanical_forces:
  description: Shear stress mimicking cerebral blood flow
  duration_minutes: 1440
  frequency_hz: 1.0
  id: mechanical:003
  name: Physiological BBB shear stress
  shear_stress: 1.2
  stimulation_type:
  - SHEAR_STRESS
microfluidic_design:
  architecture_type: MULTI_CHANNEL
  channel_configuration:
  - PARALLEL
  channel_dimensions:
  - channel_name: vascular
    height: 200
    length: 12.0
    width: 1000
  - channel_name: brain
    height: 200
    length: 12.0
    width: 1000
  - channel_name: astrocyte
    height: 100
    length: 12.0
    width: 1000
  description: Three-channel microfluidic device with permeable membranes
  flow_control_method:
  - SYRINGE_PUMP
  id: microfluidic:003
  interface_type:
  - LIQUID_LIQUID
  - CELL_CELL
  material:
  - PDMS
  membrane_pore_size: 0.4
  membrane_thickness: 10
  membrane_type: POROUS_POLYMER
  name: BBB Chip Design
  number_of_channels: 3
  sensors_integrated:
  - TEER
  - IMPEDANCE
  surface_treatment:
  - FIBRONECTIN
  - COLLAGEN
models:
- biological_system_modeled: bbb_transport:001
  concordance:
    functional_parity: Physiological TEER values and selective permeability
    molecular_similarity: Expression of BBB-specific transporters
    reproducibility: Consistent barrier formation across batches
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.7
        cell_type:
          id: CL:0000071
          name: blood vessel endothelial cell
        model_proportion: 0.65
        proportion_ratio: 0.93
      - biological_proportion: 0.3
        cell_type:
          id: CL:0000669
          name: pericyte
        model_proportion: 0.35
        proportion_ratio: 1.17
      coverage_percentage: 75.0
      description: Analysis of BBB-relevant cell types in the tissue chip
      id: cellcov:002
      missing_cell_types:
      - id: CL:0000129
        name: microglial cell
      name: BBB Cell Type Representation
      represented_cell_types:
      - id: CL:0000071
        name: blood vessel endothelial cell
      - id: CL:0000669
        name: pericyte
      single_cell_method: Immunofluorescence with cell-specific markers
    functional_parity:
      conserved_functions:
      - Tight junction barrier formation
      - P-glycoprotein efflux activity
      - Selective paracellular transport
      description: Evaluation of blood-brain barrier integrity and transport
      dose_response_similarity:
        compound_tested: Mannitol permeability marker
        correlation_coefficient: 0.81
        ec50_ratio: 1.15
        max_response_ratio: 0.94
      functional_assays:
      - assay_result: 1850.0
        assay_type: Electrical impedance
        id: assay:008
        methodology: EVOM2 epithelial voltohmmeter measurement
        name: Trans-epithelial electrical resistance
        reference_value: 2000.0
        units: "\u03A9\u22C5cm\xB2"
      - assay_result: 2.1e-06
        assay_type: Permeability
        id: assay:009
        methodology: Transwell permeability assay with fluorescent tracer
        name: Sodium fluorescein permeability
        reference_value: 1.8e-06
        units: cm/s
      - assay_result: 3.8
        assay_type: Efflux transport
        id: assay:010
        methodology: Rhodamine 123 bidirectional transport assay
        name: P-glycoprotein efflux activity
        reference_value: 4.2
        units: efflux ratio
      functional_similarity_score: 0.88
      id: funcpar:005
      impaired_functions:
      - Dynamic regulation by astrocytes
      - Immune cell trafficking
      name: BBB Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.345
        ensembl_id: ENSG00000213937
        fold_change: 1.2
        gene_symbol: CLDN5
        id: gene:013
        name: CLDN5
        p_value: 0.234
      correlation_coefficient: 0.79
      data_source: Human brain microvascular endothelial cell reference data
      description: RNA-seq comparison with human blood-brain barrier samples
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000085563
        fold_change: 8.5
        gene_symbol: ABCB1
        id: gene:011
        name: ABCB1
        p_value: 0.0001
      - adjusted_p_value: 0.002
        ensembl_id: ENSG00000117394
        fold_change: 4.2
        gene_symbol: SLC2A1
        id: gene:012
        name: SLC2A1
        p_value: 0.0002
      id: molsim:005
      methodology: Single-cell RNA sequencing with transporter-focused analysis
      name: BBB Transporter Expression Profile
      similarity_score: 0.83
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.75
        confidence_interval_upper: 0.87
        p_value: 0.0001
        statistical_test: Pearson correlation
    reproducibility:
      batch_to_batch_variation: 0.12
      coefficient_of_variation: 0.09
      description: Inter-chip and inter-batch consistency assessment
      id: repro:005
      inter_laboratory_consistency: 0.85
      name: BBB Chip Reproducibility
      quality_control_metrics:
      - metric_name: TEER baseline
        metric_value: 1850.0
        pass_fail_status: true
        threshold: 1500.0
      - metric_name: Barrier integrity
        metric_value: 0.95
        pass_fail_status: true
        threshold: 0.9
      - metric_name: Cell viability
        metric_value: 0.93
        pass_fail_status: true
        threshold: 0.85
      replicate_count: 36
      reproducibility_score: 0.91
name: Blood-Brain Barrier Tissue Chip
perfusion_system: "Continuous perfusion with physiological flow rates (2 \u03BCL/min)"
sensor_integration:
- TEER
- IMPEDANCE
spatial_context: 3D tissue architecture with vascular and neural compartments separated
  by BBB
tissue_architecture: Trilayer structure with endothelial cells, pericytes, and astrocytes
  in spatial arrangement
tissue_modeled:
  id: UBERON:0000120
  name: blood-brain barrier
type: TissueOnChip

```
## Organoid-example-004
### Input
```yaml
biological_organization_level: ORGAN
cell_source: Human induced pluripotent stem cells (iPSCs) from healthy donors
cell_types:
- id: CL:0000653
  name: podocyte
- id: CL:1000849
  name: kidney proximal tubule epithelial cell
- id: CL:1001431
  name: kidney distal tubule epithelial cell
- id: CL:0000071
  name: blood vessel endothelial cell
- id: CL:1000507
  name: kidney interstitial fibroblast
complexity_level: HIGH
culture_system: Suspension culture in ultra-low attachment plates with nephron differentiation  medium.
  Organoids maintained for 18-25 days with medium changes every 2-3 days  to allow
  full nephron maturation.
description: A 3D kidney organoid derived from human pluripotent stem cells that recapitulates  key
  aspects of human kidney development and function. The organoid contains podocytes,  proximal
  tubule cells, distal tubule cells, and endothelial cells organized in  nephron-like
  structures. Used for nephrotoxicity screening and modeling acute  kidney injury,
  particularly cisplatin-induced nephrotoxicity.
differentiation_method: Protocol based on developmental kidney organogenesis using
  sequential growth  factor treatment including activating canonical Wnt signaling,
  followed by  FGF9 and BMP signaling to induce metanephric mesenchyme and nephron
  progenitors.
id: organoid:004
models:
- biological_system_modeled: kidney_nephrotoxicity:001
  concordance:
    functional_parity: Recapitulates cisplatin-induced acute kidney injury
    molecular_similarity: High expression of kidney-specific markers and nephrotoxicity
      genes
    reproducibility: Consistent nephrotoxicity response across experimental batches
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.12
        cell_type:
          id: CL:0000653
          name: podocyte
        model_proportion: 0.15
        proportion_ratio: 1.25
      - biological_proportion: 0.62
        cell_type:
          id: CL:1000849
          name: kidney proximal tubule epithelial cell
        model_proportion: 0.55
        proportion_ratio: 0.89
      coverage_percentage: 85.2
      description: Analysis of nephron cell type diversity and organization
      id: cellcov:005
      missing_cell_types:
      - id: CL:1000452
        name: kidney collecting duct principal cell
      - id: CL:1000453
        name: kidney collecting duct intercalated cell
      name: Kidney Cell Type Representation
      represented_cell_types:
      - id: CL:0000653
        name: podocyte
      - id: CL:1000849
        name: kidney proximal tubule epithelial cell
      - id: CL:1001431
        name: kidney distal tubule epithelial cell
      - id: CL:0000071
        name: blood vessel endothelial cell
      single_cell_method: scRNA-seq with kidney lineage markers
    functional_parity:
      conserved_functions:
      - Glomerular filtration barrier formation
      - Proximal tubule transport function
      - Drug-induced injury response
      description: Evaluation of kidney-specific functions and drug-induced injury
      functional_assays:
      - assay_result: 0.42
        assay_type: Cell viability
        id: assay:026
        methodology: ATP-based cell viability assay after 72h cisplatin treatment
        name: Cisplatin cytotoxicity
        reference_value: 0.45
        units: viability fraction
      - assay_result: 185.2
        assay_type: Biomarker quantification
        id: assay:027
        methodology: ELISA-based KIM-1 quantification in culture medium
        name: KIM-1 biomarker release
        reference_value: 200.5
        units: pg/mL
      - assay_result: 2.5e-06
        assay_type: Permeability assay
        id: assay:028
        methodology: FITC-albumin permeability across organoid barrier
        name: Filtration barrier integrity
        reference_value: 2.1e-06
        units: cm/s
      functional_similarity_score: 0.84
      id: funcpar:012
      impaired_functions:
      - Urine concentration ability
      - Complex ion homeostasis
      name: Nephrotoxicity Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.234
        ensembl_id: ENSG00000184937
        fold_change: 1.3
        gene_symbol: WT1
        id: gene:032
        name: WT1
        p_value: 0.123
      correlation_coefficient: 0.79
      data_source: Human kidney biopsy samples and AKI patient data
      description: RNA-seq comparison with human kidney samples and AKI patients
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000161270
        fold_change: 3.5
        gene_symbol: NPHS1
        id: gene:029
        name: NPHS1
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000081479
        fold_change: 4.2
        gene_symbol: LRP2
        id: gene:030
        name: LRP2
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000113249
        fold_change: 8.5
        gene_symbol: HAVCR1
        id: gene:031
        name: KIM1
        p_value: 0.0001
      id: molsim:012
      methodology: Single-cell RNA sequencing with nephron segment-specific analysis
      name: Kidney Organoid Nephrotoxicity Gene Expression
      similarity_score: 0.82
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.75
        confidence_interval_upper: 0.87
        p_value: 0.0001
        statistical_test: Spearman correlation
    reproducibility:
      batch_to_batch_variation: 0.14
      coefficient_of_variation: 0.12
      description: Inter-batch and inter-laboratory consistency assessment
      id: repro:012
      inter_laboratory_consistency: 0.84
      name: Kidney Organoid Reproducibility
      quality_control_metrics:
      - metric_name: Nephron formation efficiency
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Podocyte marker expression
        metric_value: 0.92
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Organoid size consistency
        metric_value: 0.86
        pass_fail_status: true
        threshold: 0.8
      replicate_count: 36
      reproducibility_score: 0.88
name: Human Kidney Organoid Nephrotoxicity Model
organ_modeled:
  id: UBERON:0002113
  name: kidney
references:
- authors:
  - Nakanoh S
  - Takasato M
  - Little MH
  id: doi:10.1101/2025.04.30.651410
  journal: bioRxiv
  title: Development and Validation of a Stem Cell-Based Kidney Organoid Platform
    for Nephrotoxicity Assessment
  url: https://www.biorxiv.org/content/10.1101/2025.04.30.651410v1
  year: 2025
- authors:
  - Ramzy A
  - Tomov ML
  - Tran TT
  - Sharma AD
  - Feric NT
  id: PMID:38547531
  journal: Cell Reports Medicine
  title: Advancing preclinical drug evaluation through automated 3D imaging for high-throughput
    screening with kidney organoids
  url: https://pubmed.ncbi.nlm.nih.gov/38547531/
  year: 2024
spatial_context: 3D nephron-like structures with tubular organization and glomerular-like
  domains
type: Organoid

```
## CoCulture-example-001
### Input
```yaml
biological_organization_level: CELLULAR_NEIGHBORHOOD
cell_ratios:
- cell_type:
    id: CL:0000182
    name: hepatocyte
  ratio: 0.8
  ratio_type: PERCENTAGE
- cell_type:
    id: CL:0002138
    name: hepatic stellate cell
  ratio: 0.2
  ratio_type: PERCENTAGE
cell_source: Primary human hepatocytes and hepatic stellate cells from liver donors
cell_types:
- id: CL:0000182
  name: hepatocyte
- id: CL:0002138
  name: hepatic stellate cell
coculture_configuration: TRANSWELL
complexity_level: MODERATE
culture_conditions: "Williams E medium + hepatocyte supplements, 37\xB0C, 5% CO2"
description: A co-culture model combining primary human hepatocytes with hepatic stellate  cells
  to study liver fibrosis development. The model captures paracrine  signaling between
  cell types and enables investigation of fibrosis mechanisms  and potential therapeutic
  interventions.
id: coculture:001
interaction_mechanisms:
- "Paracrine signaling via TGF-\u03B2 and PDGF"
- Extracellular matrix deposition
- Cytokine-mediated inflammation response
models:
- biological_system_modeled: liver_fibrosis:001
  concordance:
    functional_parity: Recapitulates key fibrosis pathways
    molecular_similarity: High expression of fibrosis markers
    reproducibility: Consistent activation across replicates
  is_computed: false
  structured_concordance:
    functional_parity:
      conserved_functions:
      - Collagen deposition
      - Stellate cell activation
      - "TGF-\u03B2 responsiveness"
      description: Evaluation of key fibrotic processes and responses
      functional_assays:
      - assay_result: 180.5
        assay_type: Protein quantification
        id: assay:004
        methodology: Hydroxyproline assay for total collagen
        name: Collagen production assay
        reference_value: 210.2
        units: "\u03BCg/mg protein"
      - assay_result: 78.2
        assay_type: Immunofluorescence
        id: assay:005
        methodology: "Anti-\u03B1-SMA antibody staining"
        name: "\u03B1-SMA expression"
        reference_value: 85.6
        units: '% positive cells'
      functional_similarity_score: 0.75
      id: funcpar:003
      impaired_functions:
      - Matrix metalloproteinase regulation
      - Immune cell infiltration
      name: Fibrosis Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.005
        ensembl_id: ENSG00000105329
        fold_change: 2.1
        gene_symbol: TGFB1
        id: gene:009
        name: TGFB1
        p_value: 0.001
      correlation_coefficient: 0.74
      data_source: Comparison with human liver biopsy samples from fibrosis patients
      description: RNA-seq comparison with human liver fibrosis samples
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000108821
        fold_change: 5.2
        gene_symbol: COL1A1
        id: gene:007
        name: COL1A1
        p_value: 0.0001
      - adjusted_p_value: 0.002
        ensembl_id: ENSG00000107796
        fold_change: 3.8
        gene_symbol: ACTA2
        id: gene:008
        name: ACTA2
        p_value: 0.0002
      id: molsim:003
      methodology: Bulk RNA sequencing with pathway enrichment analysis
      name: Fibrosis Marker Expression Analysis
      similarity_score: 0.78
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.71
        confidence_interval_upper: 0.82
        p_value: 0.0001
        statistical_test: Spearman correlation
    pathway_concordance:
      active_pathways:
      - activity_score: 0.89
        enrichment_score: 3.2
        id: pathway:003
        name: "TGF-\u03B2 signaling pathway"
        pathway_database: KEGG
        pathway_id: hsa04350
      - activity_score: 0.76
        enrichment_score: 2.8
        id: pathway:004
        name: ECM-receptor interaction
        pathway_database: KEGG
        pathway_id: hsa04512
      description: Analysis of fibrosis-related signaling pathways
      enrichment_statistics:
      - enrichment_score: 3.2
        genes_in_dataset: 52
        genes_in_pathway: 84
        p_value: 0.0001
        q_value: 0.001
      id: pathconcord:002
      name: Fibrosis Pathway Activation
      pathway_analysis_method: Ingenuity Pathway Analysis (IPA)
      pathway_overlap_score: 0.82
    reproducibility:
      batch_to_batch_variation: 0.18
      coefficient_of_variation: 0.14
      description: Inter-experimental and inter-laboratory consistency
      id: repro:003
      inter_laboratory_consistency: 0.79
      name: Co-culture Reproducibility
      quality_control_metrics:
      - metric_name: Cell viability
        metric_value: 0.91
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Co-culture ratio
        metric_value: 0.82
        pass_fail_status: true
        threshold: 0.75
      replicate_count: 18
      reproducibility_score: 0.86
name: Hepatocyte-Stellate Cell Co-culture
spatial_context: Hepatocytes and stellate cells in defined spatial arrangement with
  paracrine interactions
type: CoCulture

```
## CoCulture-example-002
### Input
```yaml
biological_organization_level: CELLULAR_NEIGHBORHOOD
cell_ratios:
- cell_type:
    id: CL:0000540
    name: neuron
  ratio: 0.4
  ratio_type: PERCENTAGE
- cell_type:
    id: CL:0000127
    name: astrocyte
  ratio: 0.6
  ratio_type: PERCENTAGE
cell_source: Primary human neurons and astrocytes derived from fetal brain tissue
cell_types:
- id: CL:0000540
  name: neuron
- id: CL:0000127
  name: astrocyte
coculture_configuration: DIRECT_CONTACT
complexity_level: MODERATE
description: A two-dimensional co-culture system containing primary human neurons
  and  astrocytes to model neuron-glial interactions and assess neurotoxicity of  environmental
  chemicals and pharmaceuticals. The model maintains physiological  ratios of cell
  types and demonstrates synaptic activity for mechanistic  neurotoxicity studies.
id: coculture:002
interaction_mechanisms:
- Gap junction communication
- Neurotrophic factor secretion
- Glutamate uptake by astrocytes
- Synaptic support and maintenance
models:
- biological_system_modeled: neurotoxicity:001
  concordance:
    functional_parity: Physiological neuron-glia communication
    molecular_similarity: Expression of synaptic and glial markers
    reproducibility: Consistent co-culture establishment and toxicity responses
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.45
        cell_type:
          id: CL:0000540
          name: neuron
        model_proportion: 0.4
        proportion_ratio: 0.89
      - biological_proportion: 0.55
        cell_type:
          id: CL:0000127
          name: astrocyte
        model_proportion: 0.6
        proportion_ratio: 1.09
      coverage_percentage: 70.0
      description: Analysis of neural cell type interactions in co-culture
      id: cellcov:013
      missing_cell_types:
      - id: CL:0000128
        name: oligodendrocyte
      - id: CL:0000129
        name: microglial cell
      name: Neuron-Glia Cell Type Representation
      represented_cell_types:
      - id: CL:0000540
        name: neuron
      - id: CL:0000127
        name: astrocyte
      single_cell_method: Immunofluorescence with neural markers
    functional_parity:
      conserved_functions:
      - Synaptic transmission
      - Glutamate clearance
      - Neurotrophic support
      - Calcium homeostasis
      description: Evaluation of synaptic function and neurotoxic responses
      dose_response_similarity:
        compound_tested: MPTP neurotoxicity
        correlation_coefficient: 0.76
        ec50_ratio: 1.18
        max_response_ratio: 0.84
      functional_assays:
      - assay_result: 8.5
        assay_type: Electrophysiology
        id: assay:056
        methodology: Patch-clamp recording of spontaneous synaptic currents
        name: Synaptic activity measurement
        reference_value: 10.2
        units: Hz
      - assay_result: 0.31
        assay_type: Neurotoxicity screening
        id: assay:057
        methodology: MTT viability assay after 48h rotenone exposure
        name: Rotenone neurotoxicity
        reference_value: 0.28
        units: viability fraction
      - assay_result: 42.5
        assay_type: Transporter function
        id: assay:058
        methodology: Radioactive glutamate uptake assay
        name: Glutamate uptake
        reference_value: 48.2
        units: pmol/min/mg protein
      functional_similarity_score: 0.81
      id: funcpar:022
      impaired_functions:
      - Blood-brain barrier interactions
      - Microglial immune responses
      name: Neurotoxicity Assessment Function
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.456
        ensembl_id: ENSG00000258947
        fold_change: 1.2
        gene_symbol: TUBB3
        id: gene:070
        name: TUBB3
        p_value: 0.345
      correlation_coefficient: 0.79
      data_source: Human brain cortex reference dataset
      description: RNA-seq analysis of neuron-glial interactions
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000008056
        fold_change: 5.2
        gene_symbol: SYN1
        id: gene:067
        name: SYN1
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000131095
        fold_change: 7.8
        gene_symbol: GFAP
        id: gene:068
        name: GFAP
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000110436
        fold_change: 4.5
        gene_symbol: SLC1A2
        id: gene:069
        name: SLC1A2
        p_value: 0.0001
      id: molsim:022
      methodology: Single-cell RNA sequencing with cell-type deconvolution
      name: Neuron-Glia Co-Culture Expression Profile
      similarity_score: 0.83
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.76
        confidence_interval_upper: 0.87
        p_value: 0.0001
        statistical_test: DESeq2 analysis
    reproducibility:
      batch_to_batch_variation: 0.2
      coefficient_of_variation: 0.18
      description: Inter-batch consistency of co-culture establishment
      id: repro:022
      inter_laboratory_consistency: 0.78
      name: Co-Culture Reproducibility
      quality_control_metrics:
      - metric_name: Synaptic marker expression
        metric_value: 0.84
        pass_fail_status: true
        threshold: 0.75
      - metric_name: Cell viability
        metric_value: 0.91
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Astrocyte functionality
        metric_value: 0.86
        pass_fail_status: true
        threshold: 0.8
      replicate_count: 24
      reproducibility_score: 0.82
name: Neuron-Glial Co-Culture Neurotoxicity Model
references:
- authors:
  - Kim YH
  - Park SJ
  - Lee JH
  - Choi MK
  id: doi:10.1007/s43188-025-00279-y
  journal: Toxicological Research
  title: 'Toxicity assessment using neural organoids: innovative approaches and challenges'
  url: https://link.springer.com/article/10.1007/s43188-025-00279-y
  year: 2025
- authors:
  - Roberts AL
  - Thompson K
  - Martinez R
  id: doi:10.3389/ftox.2024.1402630
  journal: Frontiers in Toxicology
  title: Stem cell-based approaches for developmental neurotoxicity testing
  url: https://www.frontiersin.org/journals/toxicology/articles/10.3389/ftox.2024.1402630/full
  year: 2024
spatial_context: 2D co-culture with neuron-astrocyte cellular interactions and communication
type: CoCulture

```
## TissueOnChip-example-002
### Input
```yaml
barrier_functions:
- Selective nutrient absorption
- Tight junction integrity
- Mucus barrier formation
- Antimicrobial peptide secretion
biological_organization_level: TISSUE
complexity_level: HIGH
description: A microfluidic intestinal barrier model that recreates the human small
  intestine  environment using primary human intestinal epithelial cells and immune
  cells.  The model features physiological peristalsis-like motion, mucus production,
  and  intestinal barrier function for drug permeability and inflammation studies.
id: tissueonchip:002
mechanical_forces:
  cyclic_stretch_percent: 15.0
  description: Cyclic mechanical stretch mimicking intestinal peristalsis
  duration_minutes: 1440
  frequency_hz: 0.15
  id: mechanical:004
  name: Peristalsis-like motion
  stimulation_type:
  - CYCLIC_STRETCH
microfluidic_design:
  architecture_type: TWO_CHANNEL
  channel_configuration:
  - PARALLEL
  channel_dimensions:
  - channel_name: apical
    height: 1000
    length: 18.0
    width: 1000
  - channel_name: basolateral
    height: 1000
    length: 18.0
    width: 1000
  description: Dual-channel microfluidic device with flexible membranes for peristalsis
  flow_control_method:
  - PRESSURE_DRIVEN
  id: microfluidic:004
  interface_type:
  - LIQUID_LIQUID
  - CELL_CELL
  material:
  - PDMS
  membrane_pore_size: 0.4
  membrane_thickness: 50
  membrane_type: POROUS_POLYMER
  name: Gut-On-Chip Design
  number_of_channels: 2
  sensors_integrated:
  - TEER
  - OXYGEN
  surface_treatment:
  - MATRIGEL
  - COLLAGEN
models:
- biological_system_modeled: intestinal_absorption:001
  concordance:
    functional_parity: Physiological permeability to nutrients and drugs
    molecular_similarity: Expression of intestinal transporters and tight junction
      proteins
    reproducibility: Consistent barrier function across chips
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.85
        cell_type:
          id: CL:0000584
          name: enterocyte
        model_proportion: 0.8
        proportion_ratio: 0.94
      - biological_proportion: 0.15
        cell_type:
          id: CL:0000160
          name: goblet cell
        model_proportion: 0.2
        proportion_ratio: 1.33
      coverage_percentage: 78.5
      description: Analysis of intestinal cell type diversity in gut chip
      id: cellcov:007
      missing_cell_types:
      - id: CL:0000510
        name: paneth cell
      - id: CL:0009019
        name: tuft cell
      name: Intestinal Epithelial Cell Representation
      represented_cell_types:
      - id: CL:0000584
        name: enterocyte
      - id: CL:0000160
        name: goblet cell
      - id: CL:1001516
        name: intestinal enteroendocrine cell
      single_cell_method: Immunofluorescence with lineage-specific markers
    functional_parity:
      conserved_functions:
      - Glucose transport via SGLT1
      - Peptide absorption via PEPT1
      - Tight junction barrier maintenance
      - Mucus secretion
      description: Assessment of nutrient transport and barrier integrity
      dose_response_similarity:
        compound_tested: Caffeine absorption
        correlation_coefficient: 0.84
        ec50_ratio: 1.12
        max_response_ratio: 0.92
      functional_assays:
      - assay_result: 3.5e-05
        assay_type: Transport assay
        id: assay:032
        methodology: 14C-glucose bidirectional transport measurement
        name: Glucose permeability
        reference_value: 3.2e-05
        units: cm/s
      - assay_result: 8.0e-07
        assay_type: Paracellular marker
        id: assay:033
        methodology: 14C-mannitol paracellular transport assay
        name: Mannitol permeability
        reference_value: 6.0e-07
        units: cm/s
      - assay_result: 890.0
        assay_type: Electrical resistance
        id: assay:034
        methodology: Chopstick electrode TEER measurement
        name: TEER measurement
        reference_value: 950.0
        units: "\u03A9\u22C5cm\xB2"
      functional_similarity_score: 0.87
      id: funcpar:014
      impaired_functions:
      - Complex immune responses
      - Microbiome interactions
      name: Intestinal Absorption Function
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.634
        ensembl_id: ENSG00000163347
        fold_change: 1.1
        gene_symbol: CLDN1
        id: gene:040
        name: CLDN1
        p_value: 0.567
      correlation_coefficient: 0.85
      data_source: Human duodenal biopsy reference samples
      description: Transcriptomic comparison with human small intestine tissue
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000100170
        fold_change: 6.2
        gene_symbol: SLC5A1
        id: gene:037
        name: SGLT1
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000088386
        fold_change: 4.8
        gene_symbol: SLC15A1
        id: gene:038
        name: PEPT1
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000198788
        fold_change: 7.3
        gene_symbol: MUC2
        id: gene:039
        name: MUC2
        p_value: 0.0001
      id: molsim:014
      methodology: Bulk RNA sequencing with intestinal transporter analysis
      name: Intestinal Barrier Gene Expression
      similarity_score: 0.89
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.82
        confidence_interval_upper: 0.94
        p_value: 0.0001
        statistical_test: Spearman correlation
    reproducibility:
      batch_to_batch_variation: 0.16
      coefficient_of_variation: 0.14
      description: Inter-chip consistency and functional stability
      id: repro:014
      inter_laboratory_consistency: 0.82
      name: Gut Chip Reproducibility
      quality_control_metrics:
      - metric_name: Barrier formation time
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Transport function
        metric_value: 0.85
        pass_fail_status: true
        threshold: 0.75
      - metric_name: Cell differentiation markers
        metric_value: 0.91
        pass_fail_status: true
        threshold: 0.85
      replicate_count: 28
      reproducibility_score: 0.86
name: Human Intestinal Barrier Gut-On-Chip
perfusion_system: "Bidirectional flow with nutrient gradients (30 \u03BCL/hr)"
references:
- authors:
  - Kim HJ
  - Li H
  - Collins JJ
  - Ingber DE
  id: PMID:38112345
  journal: Nature Protocols
  title: Gut-on-chip models for investigating intestinal drug absorption and barrier
    function
  url: https://pubmed.ncbi.nlm.nih.gov/38112345/
  year: 2024
- authors:
  - Workman MJ
  - Gleeson JP
  - Troisi EJ
  - Estrada HQ
  - Kerns SJ
  id: doi:10.1038/s41587-024-02156-x
  journal: Nature Biotechnology
  title: Human organ-on-chip models of intestinal inflammation and drug transport
  url: https://www.nature.com/articles/s41587-024-02156-x
  year: 2024
sensor_integration:
- TEER
- OXYGEN
- PH
spatial_context: 3D intestinal villus-like architecture with apical-basal polarity
  and tight junctions
tissue_architecture: Villus-like epithelial layer with crypt-like invaginations and
  basal immune compartment
tissue_modeled:
  id: UBERON:0001555
  name: digestive tract
type: TissueOnChip

```
## PBPKModel-example-002
### Input
```yaml
biological_organization_level: SYSTEM
compartments:
- blood_flow: 5.0
  description: Maternal circulatory system compartment
  id: pbpk_comp:001
  name: Maternal Blood
  volume: 3.5
- blood_flow: 1.5
  description: Maternal hepatic compartment with metabolism
  id: pbpk_comp:002
  name: Maternal Liver
  volume: 1.8
- blood_flow: 0.7
  description: Placental barrier compartment
  id: pbpk_comp:003
  name: Placenta
  volume: 0.5
- blood_flow: 0.2
  description: Fetal circulatory system
  id: pbpk_comp:004
  name: Fetal Circulation
  volume: 0.3
complexity_level: HIGH
description: A physiologically-based pharmacokinetic model for predicting developmental  toxicity
  across multiple species (human, rat, rabbit) during pregnancy.  The model incorporates
  maternal-fetal transfer, placental metabolism, and  developmental stage-specific
  pharmacokinetics to predict teratogenic risk  for pharmaceutical compounds and environmental
  chemicals.
id: pbpkmodel:002
models:
- biological_system_modeled: developmental_toxicity:001
  concordance:
    functional_parity: Accurate prediction of maternal-fetal drug distribution
    molecular_similarity: Physiological parameter scaling across species
    reproducibility: Consistent performance across validation compounds
  is_computed: true
  structured_concordance:
    functional_parity:
      conserved_functions:
      - Maternal-fetal drug transfer
      - Developmental stage-specific clearance
      - Placental barrier modeling
      description: PBPK model performance for teratogenicity prediction
      dose_response_similarity:
        compound_tested: Thalidomide developmental toxicity
        correlation_coefficient: 0.77
        ec50_ratio: 1.32
        max_response_ratio: 0.88
      functional_assays:
      - assay_result: 0.79
        assay_type: Pharmacokinetic modeling
        id: assay:038
        methodology: Comparison with experimental fetal tissue data
        name: Fetal tissue concentration prediction
        reference_value: 0.75
        units: "R\xB2"
      - assay_result: 0.81
        assay_type: Binary classification
        id: assay:039
        methodology: ROC analysis against known teratogens
        name: Teratogenic risk classification
        reference_value: 0.78
        units: accuracy
      - assay_result: 0.74
        assay_type: Temporal modeling
        id: assay:040
        methodology: Developmental stage-specific exposure modeling
        name: Critical window prediction
        reference_value: 0.7
        units: temporal correlation
      functional_similarity_score: 0.83
      id: funcpar:016
      impaired_functions:
      - Individual genetic variation
      - Complex multi-generational effects
      name: Developmental Toxicity Prediction
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.923
        ensembl_id: ENSG00000163631
        fold_change: 1.0
        gene_symbol: ALB
        id: gene:046
        name: ALB
        p_value: 0.856
      correlation_coefficient: 0.82
      data_source: Published physiological parameters and pregnancy-specific changes
      description: Cross-species physiological parameter correlation analysis
      differentially_expressed_genes:
      - adjusted_p_value: 0.01
        ensembl_id: ENSG00000140505
        fold_change: 0.6
        gene_symbol: CYP1A2
        id: gene:044
        name: CYP1A2
        p_value: 0.001
      - adjusted_p_value: 0.02
        ensembl_id: ENSG00000241635
        fold_change: 1.8
        gene_symbol: UGT1A1
        id: gene:045
        name: UGT1A1
        p_value: 0.002
      id: molsim:016
      methodology: Allometric scaling with physiological compartment analysis
      name: Physiological Parameter Concordance
      similarity_score: 0.86
      statistical_significance:
        adjusted_p_value: 0.01
        confidence_interval_lower: 0.78
        confidence_interval_upper: 0.9
        p_value: 0.001
        statistical_test: Linear regression analysis
    reproducibility:
      batch_to_batch_variation: 0.12
      coefficient_of_variation: 0.15
      description: Cross-study validation and parameter sensitivity analysis
      id: repro:016
      inter_laboratory_consistency: 0.81
      name: PBPK Model Reproducibility
      quality_control_metrics:
      - metric_name: Parameter sensitivity stability
        metric_value: 0.88
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Cross-species extrapolation accuracy
        metric_value: 0.82
        pass_fail_status: true
        threshold: 0.75
      - metric_name: Model convergence reliability
        metric_value: 0.95
        pass_fail_status: true
        threshold: 0.9
      replicate_count: 25
      reproducibility_score: 0.85
name: Multi-Species Developmental Toxicity PBPK Model
references:
- authors:
  - Kapraun DF
  - Wambaugh JF
  - Ring CL
  - Tornero-Velez R
  id: doi:10.1016/j.reprotox.2024.108456
  journal: Reproductive Toxicology
  title: 'PBPK modeling for developmental and reproductive toxicity: recent advances
    and regulatory applications'
  url: https://www.sciencedirect.com/science/article/pii/S0890623824001023
  year: 2024
- authors:
  - Zhang Q
  - Fisher JW
  - Louisse J
  - Bois FY
  id: PMID:38234567
  journal: Critical Reviews in Toxicology
  title: 'Maternal-fetal PBPK models for risk assessment: a comprehensive review and
    future directions'
  url: https://pubmed.ncbi.nlm.nih.gov/38234567/
  year: 2024
spatial_context: Multi-compartment maternal-fetal physiological model with placental
  barrier
species_modeled:
  id: NCBITaxon:9606
  name: Homo sapiens
type: PBPKModel

```
## OrganOnChip-example-003
### Input
```yaml
cell_source: Primary human small airway epithelial cells from healthy or COPD donors
cell_types:
- id: CL:0002633
  name: respiratory basal cell
- id: CL:0002145
  name: ciliated epithelial cell
- id: CL:0002370
  name: respiratory goblet cell
- id: CL:0019018
  name: blood vessel smooth muscle cell
description: A smoking airway-on-chip model for chronic obstructive pulmonary disease
  (COPD)  research. Contains living human small-airway epithelium from healthy or
  COPD donors  cultured at air-liquid interface, coupled to a mechanical respirator
  that breathes  whole cigarette smoke in and out. The model demonstrates COPD-specific
  pathological  changes including ciliary dysfunction, micropathologies, and distinct
  molecular  signatures matching those seen in COPD patient airways. Also captures
  inflammatory  cytokine release and tissue-level damage responses under smoke exposure,
  providing  molecular, cellular, and tissue-level analysis capabilities.
id: organonchip:003
mechanical_forces:
  description: Rhythmic air flow simulating breathing with cigarette smoke
  frequency_hz: 0.25
  id: mechanical:003
  name: Breathing with smoke exposure
  stimulation_type:
  - BREATHING_MOTION
  - PULSATILE_FLOW
microfluidic_design:
  architecture_type: TWO_CHANNEL
  channel_configuration:
  - PARALLEL
  channel_dimensions:
  - channel_name: airway
    height: 1000
    length: 20
    width: 1000
  - channel_name: vascular
    height: 200
    length: 20
    width: 1000
  description: Airway chip with air-liquid interface and integrated smoking machine
  flow_control_method:
  - PNEUMATIC_VALVES
  - SYRINGE_PUMP
  id: microfluidic:003
  interface_type:
  - AIR_LIQUID
  material:
  - PDMS
  membrane_pore_size: 0.4
  membrane_thickness: 10
  membrane_type: POROUS_POLYMER
  name: Smoking COPD Airway Chip Design
  number_of_channels: 2
  sensors_integrated:
  - TEER
  - FLOW_RATE
  special_features:
  - Integrated smoking machine for controlled smoke delivery
  - Real-time TEER monitoring
  - Compatible with cigarette smoke exposure
  surface_treatment:
  - COLLAGEN
  - FIBRONECTIN
models:
- biological_system_modeled: copd_bronchiole:001
  concordance:
    functional_parity: Recapitulates smoke-induced airway damage and COPD phenotype
    molecular_similarity: Expression of COPD-related inflammatory and damage markers
    reproducibility: Consistent smoke exposure response across replicates
  is_computed: false
  structured_concordance:
    functional_parity:
      conserved_functions:
      - Inflammatory cytokine production
      - Matrix metalloproteinase activity
      - Epithelial barrier disruption
      description: Evaluation of smoke-induced airway dysfunction
      functional_assays:
      - assay_result: 2.8
        assay_type: Enzymatic activity
        id: assay:023
        methodology: Fluorogenic MMP substrate assay
        name: MMP activity
        reference_value: 2.1
        units: fold increase vs control
      - assay_result: 3.2e-05
        assay_type: Permeability
        id: assay:024
        methodology: FITC-dextran permeability measurement
        name: Barrier function
        reference_value: 1.8e-05
        units: cm/s
      - assay_result: 425.6
        assay_type: Cytokine assay
        id: assay:025
        methodology: "ELISA-based TNF-\u03B1 quantification"
        name: "TNF-\u03B1 release"
        reference_value: 380.2
        units: pg/mL
      functional_similarity_score: 0.76
      id: funcpar:011
      impaired_functions:
      - Ciliary clearance function
      - Antioxidant response
      name: COPD Bronchiole Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.01
        ensembl_id: ENSG00000197249
        fold_change: -2.1
        gene_symbol: SERPINA1
        id: gene:028
        name: SERPINA1
        p_value: 0.002
      correlation_coefficient: 0.71
      data_source: COPD patient bronchial biopsy and sputum cell data
      description: RNA-seq comparison with COPD patient bronchiole samples
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000100985
        fold_change: 4.8
        gene_symbol: MMP9
        id: gene:026
        name: MMP9
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000125538
        fold_change: 6.2
        gene_symbol: IL1B
        id: gene:027
        name: IL1B
        p_value: 0.0001
      id: molsim:011
      methodology: Bulk RNA sequencing with COPD biomarker panel
      name: COPD Bronchiole Expression Analysis
      similarity_score: 0.74
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.66
        confidence_interval_upper: 0.79
        p_value: 0.0001
        statistical_test: Pearson correlation
    pathway_concordance:
      active_pathways:
      - activity_score: 0.86
        enrichment_score: 3.1
        id: pathway:009
        name: TNF signaling pathway
        pathway_database: KEGG
        pathway_id: hsa04668
      - activity_score: 0.82
        enrichment_score: 2.8
        id: pathway:010
        name: NF-kappa B signaling pathway
        pathway_database: KEGG
        pathway_id: hsa04064
      description: Analysis of smoking-induced inflammatory and damage pathways
      enrichment_statistics:
      - enrichment_score: 3.1
        genes_in_dataset: 78
        genes_in_pathway: 112
        p_value: 0.0001
        q_value: 0.001
      id: pathconcord:005
      name: COPD Inflammatory Pathway Analysis
      pathway_analysis_method: KEGG pathway enrichment analysis
      pathway_overlap_score: 0.78
    reproducibility:
      batch_to_batch_variation: 0.18
      coefficient_of_variation: 0.15
      description: Consistency of smoke exposure model
      id: repro:011
      inter_laboratory_consistency: 0.79
      name: COPD Bronchiole Chip Reproducibility
      quality_control_metrics:
      - metric_name: Smoke exposure efficiency
        metric_value: 0.92
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Cell viability post-exposure
        metric_value: 0.74
        pass_fail_status: true
        threshold: 0.7
      - metric_name: COPD phenotype penetrance
        metric_value: 0.88
        pass_fail_status: true
        threshold: 0.8
      replicate_count: 20
      reproducibility_score: 0.85
name: Smoking COPD Airway-on-Chip
organ_modeled:
  id: UBERON:0002186
  name: bronchiole
type: OrganOnChip

```
## OrganOnChip-example-002
### Input
```yaml
cell_source: Primary human alveolar epithelial cells and lung microvascular endothelial
  cells
cell_types:
- id: CL:0002063
  name: type II pneumocyte
- id: CL:0002062
  name: type I pneumocyte
- id: CL:0002543
  name: vein endothelial cell
description: A human lung alveolus-on-chip model designed to study SARS-CoV-2 infection
  and  viral pneumonia. Features alveolar epithelial cells (enriched in AT2 cells
  expressing  ACE2 receptor) interfaced with pulmonary microvascular endothelium.
  The chip  incorporates cyclic mechanical strain to simulate breathing motions, which
  amplifies  innate immune responses via mechanosensitive pathways (TRPV4 and RAGE
  signaling).  Upon infection, the model exhibits cytokine storm-like responses and
  transcriptomic  changes closely resembling severe viral infections in human lungs.
id: organonchip:002
mechanical_forces:
  cyclic_stretch_percent: 10
  description: Cyclic mechanical strain mimicking breathing motions
  frequency_hz: 0.2
  id: mechanical:002
  name: Alveolar breathing forces
  stimulation_type:
  - CYCLIC_STRETCH
  - BREATHING_MOTION
microfluidic_design:
  architecture_type: TWO_CHANNEL
  channel_configuration:
  - PARALLEL
  channel_dimensions:
  - channel_name: alveolar
    height: 1000
    length: 10
    width: 1000
  - channel_name: vascular
    height: 200
    length: 10
    width: 1000
  description: Biomimetic alveolar-capillary interface with flexible PDMS membrane
  flow_control_method:
  - SYRINGE_PUMP
  id: microfluidic:002
  interface_type:
  - AIR_LIQUID
  - VASCULAR_EPITHELIAL
  material:
  - PDMS
  membrane_pore_size: 0.4
  membrane_thickness: 10
  membrane_type: PDMS
  name: Lung Alveolus Chip Design
  number_of_channels: 2
  special_features:
  - Flexible membrane for strain application
  - Transparent for real-time imaging
  surface_treatment:
  - COLLAGEN
models:
- biological_system_modeled: covid_lung:001
  concordance:
    functional_parity: Recapitulates SARS-CoV-2 infection and inflammatory response
    molecular_similarity: Viral response gene expression similar to COVID-19 patients
    reproducibility: Consistent viral infection model across experiments
  is_computed: false
  structured_concordance:
    functional_parity:
      conserved_functions:
      - SARS-CoV-2 viral entry
      - Cytokine storm response
      - Barrier dysfunction
      description: Evaluation of viral infection effects on lung function
      functional_assays:
      - assay_result: 8500000
        assay_type: qPCR
        id: assay:021
        methodology: SARS-CoV-2 N gene qPCR
        name: Viral replication
        reference_value: 7200000
        units: viral copies/mL
      - assay_result: 2850.0
        assay_type: Multiplex immunoassay
        id: assay:022
        methodology: Luminex cytokine panel
        name: Cytokine release
        reference_value: 2200.0
        units: pg/mL total cytokines
      functional_similarity_score: 0.79
      id: funcpar:010
      impaired_functions:
      - Gas exchange efficiency
      - Surfactant production
      name: COVID-19 Lung Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.245
        ensembl_id: ENSG00000184012
        fold_change: 1.4
        gene_symbol: TMPRSS2
        id: gene:025
        name: TMPRSS2
        p_value: 0.156
      correlation_coefficient: 0.77
      data_source: COVID-19 patient lung autopsy and BAL fluid data
      description: RNA-seq comparison with COVID-19 patient lung samples
      differentially_expressed_genes:
      - adjusted_p_value: 0.01
        ensembl_id: ENSG00000130234
        fold_change: 2.8
        gene_symbol: ACE2
        id: gene:023
        name: ACE2
        p_value: 0.001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000136244
        fold_change: 12.5
        gene_symbol: IL6
        id: gene:024
        name: IL6
        p_value: 0.0001
      id: molsim:010
      methodology: Single-cell RNA sequencing with viral response analysis
      name: COVID-19 Lung Response Analysis
      similarity_score: 0.81
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.73
        confidence_interval_upper: 0.85
        p_value: 0.0001
        statistical_test: Spearman correlation
    pathway_concordance:
      active_pathways:
      - activity_score: 0.92
        enrichment_score: 4.1
        id: pathway:007
        name: Cytokine signaling in immune system
        pathway_database: Reactome
        pathway_id: R-HSA-1280215
      - activity_score: 0.88
        enrichment_score: 3.7
        id: pathway:008
        name: Interferon signaling
        pathway_database: Reactome
        pathway_id: R-HSA-913531
      description: Analysis of viral infection and inflammatory response pathways
      enrichment_statistics:
      - enrichment_score: 4.1
        genes_in_dataset: 145
        genes_in_pathway: 234
        p_value: 0.0001
        q_value: 0.001
      id: pathconcord:004
      name: COVID-19 Inflammatory Pathway Analysis
      pathway_analysis_method: Reactome pathway enrichment analysis
      pathway_overlap_score: 0.84
    reproducibility:
      batch_to_batch_variation: 0.16
      coefficient_of_variation: 0.13
      description: Consistency of viral infection model
      id: repro:010
      inter_laboratory_consistency: 0.81
      name: COVID-19 Lung Chip Reproducibility
      quality_control_metrics:
      - metric_name: Infection efficiency
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Cell viability post-infection
        metric_value: 0.78
        pass_fail_status: true
        threshold: 0.7
      replicate_count: 24
      reproducibility_score: 0.87
name: Human Lung Alveolus Chip for COVID-19
organ_modeled:
  id: UBERON:0002299
  name: alveolus of lung
type: OrganOnChip

```
## Organoid-example-006
### Input
```yaml
biological_organization_level: ORGAN
cell_source: Human induced pluripotent stem cells from healthy donors and neurodevelopmental
  disorder patients
cell_types:
- id: CL:0000540
  name: neuron
- id: CL:0000127
  name: astrocyte
- id: CL:0000128
  name: oligodendrocyte
- id: CL:0000129
  name: microglial cell
- id: CL:0011020
  name: neural progenitor cell
complexity_level: HIGH
culture_system: Spinner flask culture with neural differentiation medium containing
  BDNF, GDNF,  and other neurotrophic factors. Organoids maintained in controlled
  oxygen environment  (5% O2) to prevent oxidative stress and support physiological
  development.
description: A three-dimensional brain organoid derived from human induced pluripotent
  stem cells  that recapitulates early human brain development and neural circuit
  formation.  The organoid contains multiple brain cell types including neurons, astrocytes,  oligodendrocytes,
  and microglia. Used for developmental neurotoxicity testing,  organoid intelligence
  research, and screening environmental chemicals for  neurodevelopmental effects.
differentiation_method: Dual SMAD inhibition protocol using Dorsomorphin and SB431542
  to promote neural  induction, followed by 3D aggregation and long-term culture with
  growth factors  to promote regional specification and maturation. Organoids cultured
  for 60-120 days  to achieve neural network formation.
id: organoid:006
models:
- biological_system_modeled: neurodevelopmental_toxicity:001
  concordance:
    functional_parity: Recapitulates developmental neurotoxicity patterns
    molecular_similarity: High expression of neural development and plasticity genes
    reproducibility: Consistent neural network formation and toxicity responses
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.65
        cell_type:
          id: CL:0000540
          name: neuron
        model_proportion: 0.6
        proportion_ratio: 0.92
      - biological_proportion: 0.2
        cell_type:
          id: CL:0000127
          name: astrocyte
        model_proportion: 0.25
        proportion_ratio: 1.25
      coverage_percentage: 78.5
      description: Single-cell analysis of neural cell diversity in organoids
      id: cellcov:010
      missing_cell_types:
      - id: CL:0000129
        name: microglial cell
      - id: CL:0000071
        name: blood vessel endothelial cell
      name: Brain Cell Type Representation
      represented_cell_types:
      - id: CL:0000540
        name: neuron
      - id: CL:0000127
        name: astrocyte
      - id: CL:0000128
        name: oligodendrocyte
      - id: CL:0011020
        name: neural progenitor cell
      single_cell_method: scRNA-seq with neural lineage markers
    functional_parity:
      conserved_functions:
      - Spontaneous neural activity
      - Synaptic plasticity
      - Neurotransmitter signaling
      - Glial cell support functions
      description: Evaluation of neural network activity and developmental milestones
      dose_response_similarity:
        compound_tested: Methylmercury developmental neurotoxicity
        correlation_coefficient: 0.81
        ec50_ratio: 1.14
        max_response_ratio: 0.87
      functional_assays:
      - assay_result: 12.5
        assay_type: Electrophysiology
        id: assay:047
        methodology: Microelectrode array recording of neural networks
        name: Spontaneous electrical activity
        reference_value: 15.2
        units: spikes/min
      - assay_result: 0.28
        assay_type: Neurotoxicity screening
        id: assay:048
        methodology: Cell viability assay after 7-day lead exposure
        name: Lead neurotoxicity
        reference_value: 0.32
        units: viability fraction
      - assay_result: 3.8
        assay_type: Protein quantification
        id: assay:049
        methodology: Immunofluorescence quantification of PSD95
        name: Synaptic protein expression
        reference_value: 4.1
        units: fold increase
      functional_similarity_score: 0.85
      id: funcpar:019
      impaired_functions:
      - Blood-brain barrier formation
      - Immune system interactions
      name: Neurodevelopmental Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.567
        ensembl_id: ENSG00000078018
        fold_change: 1.1
        gene_symbol: MAP2
        id: gene:058
        name: MAP2
        p_value: 0.456
      correlation_coefficient: 0.84
      data_source: Human fetal brain reference dataset and autism spectrum disorder
        samples
      description: Single-cell RNA-seq comparison with human fetal brain samples
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000162992
        fold_change: 6.8
        gene_symbol: NEUROD1
        id: gene:055
        name: NEUROD1
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000131095
        fold_change: 4.2
        gene_symbol: GFAP
        id: gene:056
        name: GFAP
        p_value: 0.0001
      - adjusted_p_value: 0.002
        ensembl_id: ENSG00000205927
        fold_change: 3.5
        gene_symbol: OLIG2
        id: gene:057
        name: OLIG2
        p_value: 0.0002
      id: molsim:019
      methodology: Single-cell RNA sequencing with developmental trajectory analysis
      name: Neural Development Gene Expression
      similarity_score: 0.88
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.81
        confidence_interval_upper: 0.92
        p_value: 0.0001
        statistical_test: Wilcoxon rank-sum test
    reproducibility:
      batch_to_batch_variation: 0.18
      coefficient_of_variation: 0.16
      description: Inter-batch neural development and toxicity response consistency
      id: repro:019
      inter_laboratory_consistency: 0.79
      name: Brain Organoid Reproducibility
      quality_control_metrics:
      - metric_name: Neural network formation
        metric_value: 0.87
        pass_fail_status: true
        threshold: 0.75
      - metric_name: Electrical activity onset
        metric_value: 0.82
        pass_fail_status: true
        threshold: 0.7
      - metric_name: Cell type diversity
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      replicate_count: 24
      reproducibility_score: 0.84
name: Human Brain Organoid Neurotoxicity Model
organ_modeled:
  id: UBERON:0000955
  name: brain
references:
- authors:
  - Johnson KL
  - Smith RA
  - Brown TM
  - Davis JH
  id: doi:10.3389/fncel.2024.1480845
  journal: Frontiers in Cellular Neuroscience
  title: Organoid intelligence for developmental neurotoxicity testing
  url: https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2024.1480845/full
  year: 2024
- authors:
  - Lee SJ
  - Park MH
  - Kim YW
  - Choi HJ
  id: doi:10.3390/ijms25231252
  journal: International Journal of Molecular Sciences
  title: Human-Induced Pluripotent Stem Cell-Derived Neural Organoids as a Novel In
    Vitro Platform for Developmental Neurotoxicity Assessment
  url: https://www.mdpi.com/1422-0067/25/23/12523
  year: 2024
spatial_context: 3D brain tissue architecture with cortical layering and neural networks
type: Organoid

```
## TissueOnChip-example-003
### Input
```yaml
barrier_functions:
- Stratum corneum barrier integrity
- Transepidermal water loss control
- UV protection mechanisms
- Chemical penetration resistance
biological_organization_level: TISSUE
complexity_level: HIGH
description: A microfluidic skin-on-chip model that recreates the human skin barrier
  function  using primary human keratinocytes, fibroblasts, and melanocytes in a 3D
  configuration.  The model features an air-liquid interface, physiological skin architecture,
  and  real-time monitoring capabilities for cosmetics safety testing and dermatotoxicity  assessment
  without animal testing.
id: tissueonchip:003
mechanical_forces:
  description: Static mechanical tension to maintain skin architecture
  duration_minutes: 2880
  id: mechanical:005
  name: Physiological skin tension
  stimulation_type:
  - TENSION
microfluidic_design:
  architecture_type: MULTI_CHANNEL
  channel_configuration:
  - PARALLEL
  channel_dimensions:
  - channel_name: epidermal_chamber
    height: 500
    length: 15.0
    width: 8000
  - channel_name: dermal_chamber
    height: 1000
    length: 15.0
    width: 8000
  - channel_name: media_channel
    height: 200
    length: 15.0
    width: 500
  description: Multi-chamber device with air-liquid interface and perfusion channels
  flow_control_method:
  - SYRINGE_PUMP
  id: microfluidic:005
  interface_type:
  - AIR_LIQUID
  - CELL_CELL
  material:
  - PDMS
  membrane_pore_size: 0.4
  membrane_thickness: 25
  membrane_type: POROUS_POLYMER
  name: Skin-On-Chip Design
  number_of_channels: 4
  sensors_integrated:
  - TEER
  - OPTICAL
  surface_treatment:
  - COLLAGEN
  - FIBRONECTIN
models:
- biological_system_modeled: skin_barrier:001
  concordance:
    functional_parity: Physiological barrier function and permeability
    molecular_similarity: Expression of skin barrier proteins and differentiation
      markers
    reproducibility: Consistent barrier formation across chip batches
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.85
        cell_type:
          id: CL:0000312
          name: keratinocyte
        model_proportion: 0.8
        proportion_ratio: 0.94
      - biological_proportion: 0.12
        cell_type:
          id: CL:0000057
          name: fibroblast
        model_proportion: 0.15
        proportion_ratio: 1.25
      coverage_percentage: 82.0
      description: Analysis of skin cell diversity and organization
      id: cellcov:009
      missing_cell_types:
      - id: CL:0000451
        name: dendritic cell
      - id: CL:0000771
        name: eosinophil
      name: Skin Cell Type Representation
      represented_cell_types:
      - id: CL:0000312
        name: keratinocyte
      - id: CL:0000057
        name: fibroblast
      - id: CL:0000148
        name: melanocyte
      single_cell_method: Immunofluorescence with skin-specific markers
    functional_parity:
      conserved_functions:
      - Stratum corneum formation
      - Tight junction integrity
      - Chemical barrier function
      - Inflammatory response
      description: Evaluation of barrier integrity and chemical permeability
      dose_response_similarity:
        compound_tested: Sodium dodecyl sulfate irritation
        correlation_coefficient: 0.89
        ec50_ratio: 1.07
        max_response_ratio: 0.95
      functional_assays:
      - assay_result: 8.5
        assay_type: Barrier integrity
        id: assay:044
        methodology: Gravimetric water loss measurement
        name: Transepidermal water loss
        reference_value: 9.2
        units: "g/m\xB2/h"
      - assay_result: 1.2e-06
        assay_type: Chemical penetration
        id: assay:045
        methodology: Franz cell diffusion assay
        name: Caffeine permeability
        reference_value: 1.5e-06
        units: cm/s
      - assay_result: 2.8
        assay_type: Inflammatory biomarker
        id: assay:046
        methodology: ELISA-based cytokine quantification
        name: SDS irritation response
        reference_value: 3.1
        units: "fold increase IL-1\u03B1"
      functional_similarity_score: 0.93
      id: funcpar:018
      impaired_functions:
      - Sebaceous gland function
      - Hair follicle development
      name: Skin Barrier Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.345
        ensembl_id: ENSG00000186847
        fold_change: 1.2
        gene_symbol: KRT14
        id: gene:054
        name: KRT14
        p_value: 0.234
      correlation_coefficient: 0.87
      data_source: Human skin biopsy reference dataset from healthy volunteers
      description: Transcriptomic comparison with human skin biopsy samples
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000186395
        fold_change: 8.2
        gene_symbol: KRT10
        id: gene:051
        name: KRT10
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000143631
        fold_change: 12.5
        gene_symbol: FLG
        id: gene:052
        name: FLG
        p_value: 0.0001
      - adjusted_p_value: 0.002
        ensembl_id: ENSG00000103222
        fold_change: 3.8
        gene_symbol: ABCC1
        id: gene:053
        name: ABCC1
        p_value: 0.0002
      id: molsim:018
      methodology: Bulk RNA sequencing with skin differentiation marker analysis
      name: Skin Barrier Gene Expression Profile
      similarity_score: 0.91
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.84
        confidence_interval_upper: 0.95
        p_value: 0.0001
        statistical_test: Spearman correlation
    reproducibility:
      batch_to_batch_variation: 0.11
      coefficient_of_variation: 0.09
      description: Inter-chip barrier function and response consistency
      id: repro:018
      inter_laboratory_consistency: 0.87
      name: Skin Chip Reproducibility
      quality_control_metrics:
      - metric_name: Barrier formation time
        metric_value: 0.92
        pass_fail_status: true
        threshold: 0.85
      - metric_name: TEER stability
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Differentiation marker expression
        metric_value: 0.94
        pass_fail_status: true
        threshold: 0.85
      replicate_count: 32
      reproducibility_score: 0.91
name: Human Skin-On-Chip Dermatotoxicity Model
perfusion_system: "Continuous perfusion of basal medium at 5 \u03BCL/hr with air exposure\
  \ to apical surface"
references:
- authors:
  - Chen L
  - Wang H
  - Liu Y
  - Zhang M
  id: PMID:37938128
  journal: Lab on a Chip
  title: Towards skin-on-a-chip for screening the dermal absorption of cosmetics
  url: https://pubmed.ncbi.nlm.nih.gov/37938128/
  year: 2024
- authors:
  - Wang M
  - Zhang L
  - Hao H
  - Yan M
  - Zhu Z
  id: doi:10.1177/09636897241235464
  journal: Cell Transplantation
  title: Applications of Engineered Skin Tissue for Cosmetic Component and Toxicology
    Detection
  url: https://journals.sagepub.com/doi/10.1177/09636897241235464
  year: 2024
sensor_integration:
- TEER
- OPTICAL
- IMPEDANCE
spatial_context: 3D skin architecture with epidermis, dermis, and air-liquid interface
tissue_architecture: Multilayer structure with stratified epidermis and dermal fibroblast
  layer
tissue_modeled:
  id: UBERON:0002097
  name: skin of body
type: TissueOnChip

```
## Organoid-example-takahashi-2023
### Input
```yaml
biological_organization_level: ORGAN
cell_source: Human induced pluripotent stem cells differentiated using established
  protocol
cell_types:
- id: CL:0002563
  name: intestinal epithelial cell
- id: CL:0000036
  name: epithelial cell
- id: CL:0000584
  name: enterocyte
complexity_level: HIGH
culture_system: "Cost-reduced culture system using type I collagen gel instead of\
  \ Matrigel. Advanced DMEM/F12 medium supplemented with L-WRNH conditioned medium\
  \ to reduce growth factor costs. Organoids maintained at 37\xB0C in 5% CO2 incubator\
  \ with medium changes every 2-3 days and passaging every 6-7 days."
description: Human intestinal organoids derived from induced pluripotent stem cells
  using cost-reduction strategies for high-throughput drug cytotoxicity screening.
  Features collagen gel matrix and conditioned medium to reduce culture costs while
  maintaining physiological relevance for drug absorption and metabolism studies.
differentiation_method: Multi-step endoderm and intestinal lineage induction from
  human iPS cells. Initial endoderm differentiation followed by intestinal specification
  using growth factors in defined medium conditions. Cost-reduced protocol utilizing
  L-WRNH conditioned medium and collagen gel matrix instead of expensive Matrigel.
id: organoid:takahashi_2023
models:
- biological_system_modeled: intestinal_drug_toxicity:001
  concordance:
    functional_parity: Physiological drug absorption and metabolism responses comparable
      to in vivo
    molecular_similarity: Expression of intestinal epithelial markers and drug metabolism
      enzymes
    reproducibility: Consistent organoid formation and drug screening results across
      batches
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.75
        cell_type:
          id: CL:0000584
          name: enterocyte
        model_proportion: 0.7
        proportion_ratio: 0.93
      - biological_proportion: 0.12
        cell_type:
          id: CL:0000160
          name: goblet cell
        model_proportion: 0.15
        proportion_ratio: 1.25
      coverage_percentage: 75.0
      description: Analysis of cell type diversity in cost-reduced organoids
      id: cellcov:011
      missing_cell_types:
      - id: CL:0000451
        name: dendritic cell
      - id: CL:0000235
        name: macrophage
      name: Intestinal Cell Type Representation
      represented_cell_types:
      - id: CL:0002563
        name: intestinal epithelial cell
      - id: CL:0000584
        name: enterocyte
      - id: CL:0000160
        name: goblet cell
      single_cell_method: Immunofluorescence with intestinal lineage markers
    functional_parity:
      conserved_functions:
      - Drug absorption modeling
      - Cytotoxicity assessment
      - Metabolic enzyme activity
      - Barrier function
      description: Validation of organoid-based screening vs conventional Caco-2 assays
      dose_response_similarity:
        compound_tested: Representative cytotoxic compounds
        correlation_coefficient: 0.82
        ec50_ratio: 1.18
        max_response_ratio: 0.91
      functional_assays:
      - assay_result: 0.89
        assay_type: Cell viability
        id: assay:068
        methodology: Luminescence-based ATP quantification for screening validation
        name: CellTiter-Glo 3D viability
        reference_value: 0.85
        units: Z'-factor
      - assay_result: 3500
        assay_type: Drug screening
        id: assay:069
        methodology: "High-throughput screening at 2 \u03BCM with >40% inhibition\
          \ cutoff"
        name: Compound cytotoxicity screening
        reference_value: 3500
        units: compounds tested
      - assay_result: 0.78
        assay_type: Cross-validation
        id: assay:070
        methodology: Comparison of hit compounds between organoid and Caco-2 screening
        name: Caco-2 correlation
        reference_value: 0.75
        units: correlation coefficient
      functional_similarity_score: 0.85
      id: funcpar:takahashi_001
      impaired_functions:
      - Immune system interactions
      - Microbial interactions
      name: Drug Screening Performance Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.856
        ensembl_id: ENSG00000075624
        fold_change: 1.0
        gene_symbol: ACTB
        id: gene:086
        name: ACTB
        p_value: 0.789
      correlation_coefficient: 0.83
      data_source: Human intestinal biopsy reference dataset
      description: Comparison of organoid gene expression with native intestinal tissue
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000096384
        fold_change: 8.5
        gene_symbol: VIL1
        id: gene:083
        name: VILLIN1
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000165556
        fold_change: 6.2
        gene_symbol: CDX2
        id: gene:084
        name: CDX2
        p_value: 0.0001
      - adjusted_p_value: 0.002
        ensembl_id: ENSG00000145384
        fold_change: 4.8
        gene_symbol: FABP2
        id: gene:085
        name: FABP2
        p_value: 0.0002
      id: molsim:takahashi_001
      methodology: RNA sequencing with intestinal epithelial marker analysis
      name: Intestinal Epithelial Gene Expression Profile
      similarity_score: 0.87
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.8
        confidence_interval_upper: 0.91
        p_value: 0.0001
        statistical_test: DESeq2 differential expression analysis
    reproducibility:
      batch_to_batch_variation: 0.14
      coefficient_of_variation: 0.12
      description: Inter-batch consistency of cost-reduced culture system
      id: repro:takahashi_001
      inter_laboratory_consistency: 0.85
      name: Cost-Reduced Organoid Reproducibility
      quality_control_metrics:
      - metric_name: Organoid formation efficiency
        metric_value: 0.91
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Epithelial marker expression
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.75
      - metric_name: Drug screening Z'-factor
        metric_value: 0.87
        pass_fail_status: true
        threshold: 0.7
      replicate_count: 48
      reproducibility_score: 0.88
name: Cost-Reduced Human Intestinal Organoid Drug Screening Model
organ_modeled:
  id: UBERON:0000160
  name: intestine
references:
- authors:
  - Takahashi Y
  - Mizuno T
  - Morikawa Y
  - Fukuda K
  id: doi:10.1038/s41598-023-32438-2
  journal: Scientific Reports
  title: Drug cytotoxicity screening using human intestinal organoids propagated with
    extensive cost-reduction strategies
  url: https://www.nature.com/articles/s41598-023-32438-2
  year: 2023
spatial_context: 3D intestinal epithelial architecture with cost-reduced culture matrix
type: Organoid

```
## MLModel-example-001
### Input
```yaml
biological_organization_level: SUBCELLULAR
complexity_level: HIGH
cross_validation:
  cv_method: STRATIFIED_K_FOLD
  cv_score: 0.89
  n_folds: 5
description: A deep neural network model for predicting cardiotoxicity from chemical
  structure  and molecular descriptors. The model uses transfer learning from large
  chemical  databases and incorporates multiple endpoints including QT prolongation,  arrhythmia
  risk, and cardiomyocyte viability. Designed for early-stage  drug development and
  regulatory safety assessment.
feature_types:
- MOLECULAR
- PHENOTYPIC
- TRANSCRIPTOMIC
id: mlmodel:001
ml_algorithm: DEEP_LEARNING
model_interpretability: INTERPRETABLE
models:
- biological_system_modeled: cardiotoxicity_prediction:001
  concordance:
    functional_parity: Accurate prediction of multiple cardiotoxicity mechanisms
    molecular_similarity: High correlation with experimental cardiotoxicity endpoints
    reproducibility: Consistent performance across validation datasets
  is_computed: true
  structured_concordance:
    functional_parity:
      conserved_functions:
      - hERG channel binding prediction
      - QT prolongation risk assessment
      - Arrhythmia classification
      - Cardiomyocyte viability prediction
      description: Multi-endpoint cardiotoxicity prediction accuracy
      dose_response_similarity:
        compound_tested: Dofetilide hERG inhibition
        correlation_coefficient: 0.82
        ec50_ratio: 1.15
        max_response_ratio: 0.89
      functional_assays:
      - assay_result: 0.91
        assay_type: Binary classification
        id: assay:059
        methodology: ROC analysis against experimental hERG patch clamp data
        name: hERG inhibition prediction
        reference_value: 0.87
        units: AUC
      - assay_result: 0.84
        assay_type: Regression
        id: assay:060
        methodology: Linear correlation with clinical QTc measurements
        name: QT prolongation prediction
        reference_value: 0.81
        units: "R\xB2"
      - assay_result: 0.86
        assay_type: Binary classification
        id: assay:061
        methodology: Precision-recall analysis of cell viability data
        name: Cardiomyocyte cytotoxicity
        reference_value: 0.83
        units: F1-score
      functional_similarity_score: 0.88
      id: funcpar:023
      impaired_functions:
      - Long-term chronic effects
      - Individual variability modeling
      name: Cardiotoxicity Prediction Performance
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.856
        ensembl_id: ENSG00000075624
        fold_change: 1.0
        gene_symbol: ACTB
        id: gene:074
        name: ACTB
        p_value: 0.782
      correlation_coefficient: 0.89
      data_source: ChEMBL cardiotoxicity dataset and FDA Adverse Event Reporting System
      description: Chemical-target interaction predictions for cardiac toxicity
      differentially_expressed_genes:
      - adjusted_p_value: 0.01
        ensembl_id: ENSG00000055118
        fold_change: 3.8
        gene_symbol: KCNH2
        id: gene:071
        name: KCNH2
        p_value: 0.001
      - adjusted_p_value: 0.02
        ensembl_id: ENSG00000183873
        fold_change: 2.5
        gene_symbol: SCN5A
        id: gene:072
        name: SCN5A
        p_value: 0.002
      - adjusted_p_value: 0.01
        ensembl_id: ENSG00000151067
        fold_change: 2.8
        gene_symbol: CACNA1C
        id: gene:073
        name: CACNA1C
        p_value: 0.001
      id: molsim:023
      methodology: Molecular docking and target prediction with known cardiotoxic
        compounds
      name: Cardiotoxicity Molecular Targets
      similarity_score: 0.92
      statistical_significance:
        adjusted_p_value: 0.01
        confidence_interval_lower: 0.86
        confidence_interval_upper: 0.95
        p_value: 0.001
        statistical_test: Bootstrap confidence intervals
    reproducibility:
      batch_to_batch_variation: 0.04
      coefficient_of_variation: 0.07
      description: Cross-validation and external test set consistency
      id: repro:023
      inter_laboratory_consistency: 0.91
      name: Model Validation Reproducibility
      quality_control_metrics:
      - metric_name: Cross-validation stability
        metric_value: 0.94
        pass_fail_status: true
        threshold: 0.9
      - metric_name: External validation performance
        metric_value: 0.91
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Feature importance consistency
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      replicate_count: 100
      reproducibility_score: 0.93
name: Deep Learning Cardiotoxicity Prediction Model
references:
- authors:
  - Chen X
  - Liu Y
  - Wang Z
  - Zhang H
  id: doi:10.1016/j.compbiomed.2024.108445
  journal: Computers in Biology and Medicine
  title: 'Deep learning for cardiotoxicity prediction: integrating molecular descriptors
    and biological pathways'
  url: https://www.sciencedirect.com/science/article/pii/S001048252400123X
  year: 2024
- authors:
  - Rodriguez M
  - Kim J
  - Anderson L
  - Thompson R
  id: doi:10.1021/acs.jcim.4c00789
  journal: Journal of Chemical Information and Modeling
  title: Multi-task learning for comprehensive cardiotoxicity assessment using chemical
    structure information
  url: https://pubs.acs.org/doi/10.1021/acs.jcim.4c00789
  year: 2024
spatial_context: Chemical-biological interaction space with molecular target predictions
training_data_size: 125000
type: MLModel

```
## ThreeDCellCulture-example-001
### Input
```yaml
biological_organization_level: TISSUE
cell_source: Primary human hepatocytes, hepatic stellate cells, and Kupffer cells
  from healthy donors
cell_types:
- id: CL:0000182
  name: hepatocyte
- id: CL:0000091
  name: Kupffer cell
- id: CL:0002293
  name: epithelial cell of thymus
complexity_level: HIGH
description: A three-dimensional bioprinted liver tissue construct created using bioink
  containing  primary human hepatocytes, hepatic stellate cells, and Kupffer cells.
  The tissue is  printed with precise spatial organization to mimic liver lobule architecture
  and  includes perfusable vascular channels. Used for drug metabolism studies,  hepatotoxicity
  screening, and disease modeling.
id: threedcellculture:001
matrix_composition: Alginate-gelatin methacrylate bioink with collagen Type I, crosslinked
  with  calcium chloride and UV exposure. Includes sacrificial gelatin channels for  vascularization
  and perfusion network.
models:
- biological_system_modeled: liver_metabolism:002
  concordance:
    functional_parity: Physiological drug metabolism and albumin production
    molecular_similarity: High expression of hepatic metabolism enzymes and transporters
    reproducibility: Consistent printing quality and metabolic function
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.75
        cell_type:
          id: CL:0000182
          name: hepatocyte
        model_proportion: 0.8
        proportion_ratio: 1.07
      - biological_proportion: 0.2
        cell_type:
          id: CL:0000091
          name: Kupffer cell
        model_proportion: 0.15
        proportion_ratio: 0.75
      coverage_percentage: 85.0
      description: Analysis of hepatic cell diversity in bioprinted tissue
      id: cellcov:012
      missing_cell_types:
      - id: CL:0000071
        name: blood vessel endothelial cell
      - id: CL:0000738
        name: leukocyte
      name: Bioprinted Liver Cell Type Representation
      represented_cell_types:
      - id: CL:0000182
        name: hepatocyte
      - id: CL:0000091
        name: Kupffer cell
      - id: CL:0002293
        name: epithelial cell of thymus
      single_cell_method: Immunofluorescence with hepatic lineage markers
    functional_parity:
      conserved_functions:
      - Cytochrome P450 metabolism
      - Albumin synthesis
      - Bile acid production
      - Urea synthesis
      description: Evaluation of drug metabolism and liver-specific functions
      dose_response_similarity:
        compound_tested: Acetaminophen hepatotoxicity
        correlation_coefficient: 0.87
        ec50_ratio: 1.12
        max_response_ratio: 0.93
      functional_assays:
      - assay_result: 85.6
        assay_type: Enzyme activity
        id: assay:053
        methodology: "Testosterone 6\u03B2-hydroxylation assay"
        name: CYP3A4 activity
        reference_value: 92.3
        units: pmol/min/mg protein
      - assay_result: 12.8
        assay_type: Protein production
        id: assay:054
        methodology: ELISA-based albumin quantification in culture medium
        name: Albumin secretion
        reference_value: 14.2
        units: "\u03BCg/day/mg tissue"
      - assay_result: 0.42
        assay_type: Hepatotoxicity
        id: assay:055
        methodology: MTT viability assay after 24h APAP exposure
        name: Acetaminophen toxicity
        reference_value: 0.38
        units: viability fraction
      functional_similarity_score: 0.91
      id: funcpar:021
      impaired_functions:
      - Immune surveillance function
      - Regenerative capacity
      name: Bioprinted Hepatic Metabolism Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.934
        ensembl_id: ENSG00000111640
        fold_change: 1.0
        gene_symbol: GAPDH
        id: gene:066
        name: GAPDH
        p_value: 0.892
      correlation_coefficient: 0.86
      data_source: Human liver biopsy reference dataset from healthy donors
      description: RNA-seq comparison with human liver tissue samples
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000160868
        fold_change: 8.5
        gene_symbol: CYP3A4
        id: gene:063
        name: CYP3A4
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000163631
        fold_change: 15.2
        gene_symbol: ALB
        id: gene:064
        name: ALB
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000241635
        fold_change: 6.8
        gene_symbol: UGT1A1
        id: gene:065
        name: UGT1A1
        p_value: 0.0001
      id: molsim:021
      methodology: Bulk RNA sequencing with hepatic function panel analysis
      name: Bioprinted Hepatic Function Gene Expression
      similarity_score: 0.89
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.83
        confidence_interval_upper: 0.93
        p_value: 0.0001
        statistical_test: Pearson correlation
    reproducibility:
      batch_to_batch_variation: 0.14
      coefficient_of_variation: 0.12
      description: Print quality and functional consistency assessment
      id: repro:021
      inter_laboratory_consistency: 0.85
      name: Bioprinted Tissue Reproducibility
      quality_control_metrics:
      - metric_name: Print fidelity
        metric_value: 0.92
        pass_fail_status: true
        threshold: 0.85
      - metric_name: Cell viability post-printing
        metric_value: 0.89
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Metabolic function stability
        metric_value: 0.86
        pass_fail_status: true
        threshold: 0.75
      replicate_count: 18
      reproducibility_score: 0.88
name: 3D Bioprinted Liver Tissue Model
references:
- authors:
  - Zhang W
  - Liu H
  - Chen Y
  - Wang X
  id: doi:10.1080/17452759.2024.2384662
  journal: Virtual and Physical Prototyping
  title: Recent advances in 3D bioprinting of tissues and organs for transplantation
    and drug screening
  url: https://www.tandfonline.com/doi/full/10.1080/17452759.2024.2384662
  year: 2024
- authors:
  - Kim SH
  - Park JY
  - Lee MK
  - Cho DW
  id: doi:10.3389/fbioe.2025.1457872
  journal: Frontiers in Bioengineering and Biotechnology
  title: 3D bioprinting for the construction of drug testing models-development strategies
    and regulatory concerns
  url: https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2025.1457872/full
  year: 2025
size_range: 10 x 10 x 2 mm tissue constructs
spatial_context: 3D liver lobule architecture with hepatocyte cords and sinusoidal
  spaces
three_d_architecture: SCAFFOLD_BASED
type: ThreeDCellCulture

```
## Organoid-example-001
### Input
```yaml
cell_source: Human induced pluripotent stem cells (iPSCs) from healthy donors
cell_types:
- id: CL:0000540
  name: neuron
- id: CL:0000127
  name: astrocyte
- id: CL:0000128
  name: oligodendrocyte
- id: CL:0011020
  name: neural progenitor cell
- id: CL:0000125
  name: glial cell
culture_system: Matrigel dome culture with orbital shaking at 80 rpm. Organoids are  maintained
  in neural differentiation medium with regular feeding every  3-4 days for up to
  60 days.
description: A 3D brain organoid derived from human induced pluripotent stem cells
  (iPSCs)  that recapitulates key aspects of early human brain development. The organoid  contains
  neural progenitor cells, mature neurons, astrocytes, and oligodendrocytes  organized
  in cortical-like structures with defined layers. Used for modeling  neurodevelopmental
  disorders and drug screening.
differentiation_method: Dual SMAD inhibition protocol with LDN193189 and SB431542
  followed by  neural induction using N2B27 medium. Organoids are generated using  hanging
  drop method followed by embedding in Matrigel droplets.
id: organoid:001
models:
- biological_system_modeled: neurodevelopment:001
  concordance:
    cell_type_coverage: Contains major brain cell types found in developing cortex
    functional_parity: Exhibits spontaneous electrical activity and synaptic transmission
    molecular_similarity: 85% similarity in transcriptomic profiles
    pathway_concordance: Strong overlap in Wnt and Notch signaling pathways
    phenotype_overlap: High concordance with human fetal brain gene expression
    reproducibility: Batch-to-batch coefficient of variation <20%
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.52
        cell_type:
          id: CL:0000540
          name: neuron
        model_proportion: 0.45
        proportion_ratio: 0.87
      - biological_proportion: 0.28
        cell_type:
          id: CL:0011020
          name: neural progenitor cell
        model_proportion: 0.32
        proportion_ratio: 1.14
      coverage_percentage: 78.5
      description: Single-cell analysis of cell type diversity
      id: cellcov:001
      missing_cell_types:
      - id: CL:0000129
        name: microglial cell
      name: Brain Cell Type Representation
      represented_cell_types:
      - id: CL:0000540
        name: neuron
      - id: CL:0000127
        name: astrocyte
      - id: CL:0011020
        name: neural progenitor cell
      single_cell_method: scRNA-seq with cell type deconvolution
    functional_parity:
      conserved_functions:
      - Spontaneous electrical activity
      - Synaptic transmission
      - Action potential generation
      description: Electrophysiological and synaptic function evaluation
      functional_assays:
      - assay_result: 12.5
        assay_type: Electrophysiology
        id: assay:001
        methodology: 60-channel MEA recording for 30 minutes
        name: Multi-electrode array recording
        reference_value: 15.2
        units: spikes/min
      functional_similarity_score: 0.72
      id: funcpar:001
      impaired_functions:
      - Complex network oscillations
      - Long-term potentiation
      name: Neuronal Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.523
        ensembl_id: ENSG00000007372
        fold_change: 1.1
        gene_symbol: PAX6
        id: gene:003
        name: PAX6
        p_value: 0.456
      correlation_coefficient: 0.82
      data_source: scRNA-seq comparison with gestational week 12-16 human fetal brain
      description: RNA-seq based comparison with human fetal brain tissue
      differentially_expressed_genes:
      - adjusted_p_value: 0.01
        ensembl_id: ENSG00000181449
        fold_change: 2.3
        gene_symbol: SOX2
        id: gene:001
        name: SOX2
        p_value: 0.001
      - adjusted_p_value: 0.02
        ensembl_id: ENSG00000132688
        fold_change: 1.8
        gene_symbol: NES
        id: gene:002
        name: NESTIN
        p_value: 0.005
      id: molsim:001
      methodology: Single-cell RNA sequencing with 10X Genomics platform
      name: Brain Organoid Transcriptomic Similarity
      similarity_score: 0.85
      statistical_significance:
        adjusted_p_value: 0.005
        confidence_interval_lower: 0.78
        confidence_interval_upper: 0.88
        p_value: 0.001
        statistical_test: Spearman correlation
    pathway_concordance:
      active_pathways:
      - activity_score: 0.82
        enrichment_score: 2.1
        id: pathway:001
        name: Wnt signaling pathway
        pathway_database: KEGG
        pathway_id: hsa04310
      - activity_score: 0.78
        enrichment_score: 1.9
        id: pathway:002
        name: Notch signaling pathway
        pathway_database: KEGG
        pathway_id: hsa04330
      description: GSEA analysis of key brain development pathways
      enrichment_statistics:
      - enrichment_score: 2.1
        genes_in_dataset: 89
        genes_in_pathway: 143
        p_value: 0.001
        q_value: 0.01
      id: pathconcord:001
      name: Neurodevelopmental Pathway Analysis
      pathway_analysis_method: Gene Set Enrichment Analysis (GSEA)
      pathway_overlap_score: 0.75
    reproducibility:
      batch_to_batch_variation: 0.15
      coefficient_of_variation: 0.18
      description: Inter-batch and inter-laboratory consistency
      id: repro:001
      inter_laboratory_consistency: 0.75
      name: Organoid Reproducibility Assessment
      quality_control_metrics:
      - metric_name: Organoid diameter
        metric_value: 450.0
        pass_fail_status: true
        threshold: 400.0
      - metric_name: Cell viability
        metric_value: 0.92
        pass_fail_status: true
        threshold: 0.85
      replicate_count: 24
      reproducibility_score: 0.83
name: 3D Brain Organoid Model
organ_modeled:
  id: UBERON:0000955
  name: brain
type: Organoid

```
## MetabolicModel-example-001
### Input
```yaml
biological_organization_level: CELLULAR
complexity_level: HIGH
description: A genome-scale metabolic network model using flux balance analysis to
  identify  metabolic vulnerabilities in cancer cells. The model integrates transcriptomic  data
  from cancer patients with metabolic pathway databases to predict optimal  drug targets
  with minimal side effects. Used for systematic identification  of anti-cancer therapeutic
  targets and metabolic biomarkers.
id: metabolicmodel:001
models:
- biological_system_modeled: cancer_metabolism:001
  concordance:
    functional_parity: Accurate prediction of metabolic flux distributions
    molecular_similarity: High correlation with cancer cell metabolic profiles
    reproducibility: Consistent target identification across cancer types
  is_computed: true
  structured_concordance:
    functional_parity:
      conserved_functions:
      - Essential gene identification
      - Growth rate prediction
      - Metabolic flux distribution
      - Biomarker identification
      description: Drug target identification accuracy and side effect prediction
      dose_response_similarity:
        compound_tested: 2-Deoxyglucose glycolysis inhibition
        correlation_coefficient: 0.77
        ec50_ratio: 1.22
        max_response_ratio: 0.86
      functional_assays:
      - assay_result: 0.82
        assay_type: Gene knockout simulation
        id: assay:065
        methodology: ROC analysis against CRISPR essentiality screens
        name: Essential gene prediction
        reference_value: 0.78
        units: AUC
      - assay_result: 0.79
        assay_type: Metabolic inhibitor screening
        id: assay:066
        methodology: FBA predictions vs GDSC drug response data
        name: Drug sensitivity prediction
        reference_value: 0.75
        units: Spearman correlation
      - assay_result: 0.74
        assay_type: Normal tissue impact
        id: assay:067
        methodology: Normal cell line viability prediction
        name: Side effect prediction
        reference_value: 0.71
        units: specificity
      functional_similarity_score: 0.86
      id: funcpar:025
      impaired_functions:
      - Regulatory network integration
      - Temporal dynamics modeling
      name: Metabolic Target Prediction Performance
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.567
        ensembl_id: ENSG00000111640
        fold_change: 1.1
        gene_symbol: GAPDH
        id: gene:082
        name: GAPDH
        p_value: 0.456
      correlation_coefficient: 0.84
      data_source: Cancer Cell Line Encyclopedia metabolomics data
      description: FBA predictions compared with experimental flux measurements
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000134333
        fold_change: 4.5
        gene_symbol: LDHA
        id: gene:079
        name: LDHA
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000170525
        fold_change: 3.8
        gene_symbol: PFKFB3
        id: gene:080
        name: PFKFB3
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000117394
        fold_change: 6.2
        gene_symbol: SLC2A1
        id: gene:081
        name: GLUT1
        p_value: 0.0001
      id: molsim:025
      methodology: 13C metabolic flux analysis validation with cancer cell lines
      name: Metabolic Flux Correlation Analysis
      similarity_score: 0.88
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.81
        confidence_interval_upper: 0.92
        p_value: 0.0001
        statistical_test: FBA flux variability analysis
    reproducibility:
      batch_to_batch_variation: 0.12
      coefficient_of_variation: 0.15
      description: Cross-validation and multi-dataset consistency
      id: repro:025
      inter_laboratory_consistency: 0.82
      name: FBA Model Reproducibility
      quality_control_metrics:
      - metric_name: Flux solution uniqueness
        metric_value: 0.88
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Target ranking stability
        metric_value: 0.84
        pass_fail_status: true
        threshold: 0.75
      - metric_name: Cross-cancer type consistency
        metric_value: 0.81
        pass_fail_status: true
        threshold: 0.7
      replicate_count: 156
      reproducibility_score: 0.85
name: Flux Balance Analysis Cancer Metabolism Model
references:
- authors:
  - Liu L
  - Zhou X
  - Chen L
  - Wang Y
  id: doi:10.1186/1752-0509-5-S1-S11
  journal: BMC Systems Biology
  title: Two-stage flux balance analysis of metabolic networks for drug target identification
  url: https://bmcsystbiol.biomedcentral.com/articles/10.1186/1752-0509-5-S1-S11
  year: 2024
- authors:
  - Kaste JAV
  - Campos AD
  - Navid A
  id: doi:10.1002/btpr.3413
  journal: Biotechnology Progress
  title: Model validation and selection in metabolic flux analysis and flux balance
    analysis
  url: https://aiche.onlinelibrary.wiley.com/doi/10.1002/btpr.3413
  year: 2024
spatial_context: Cellular metabolic network with flux distributions and pathway interactions
type: MetabolicModel

```
## QSARModel-example-001
### Input
```yaml
activity_endpoint: Drug-induced liver injury (DILI) binary classification
biological_organization_level: ORGAN
complexity_level: MODERATE
computational_method: Random Forest with molecular fingerprints and physicochemical
  descriptors
description: A Random Forest-based QSAR model for predicting drug-induced liver injury
  (DILI)  based on molecular descriptors. The model was trained on a curated dataset
  of  compounds with known hepatotoxicity profiles and achieves high accuracy in  predicting
  liver toxicity risk.
id: qsar:001
model_performance:
  accuracy: 0.82
  auc: 0.87
  r_squared: 0.73
  rmse: 0.31
  sensitivity: 0.78
  specificity: 0.85
models:
- biological_system_modeled: liver_toxicity:001
  concordance:
    functional_parity: Predicts hepatotoxicity endpoints
    molecular_similarity: Based on chemical structure similarity
    reproducibility: "Cross-validation AUC 0.87 \xB1 0.03"
  is_computed: true
  structured_concordance:
    functional_parity:
      conserved_functions:
      - DILI risk classification
      - Severity prediction
      - Chemical space coverage
      description: Evaluation of model performance in predicting liver toxicity
      dose_response_similarity:
        compound_tested: Representative hepatotoxicants
        correlation_coefficient: 0.65
        ec50_ratio: 1.8
        max_response_ratio: 0.92
      functional_assays:
      - assay_result: 0.82
        assay_type: Binary classification
        id: assay:006
        methodology: Balanced accuracy on held-out test set
        name: DILI classification accuracy
        reference_value: 0.85
        units: accuracy score
      - assay_result: 0.78
        assay_type: Performance metric
        id: assay:007
        methodology: True positive rate for hepatotoxic compounds
        name: Sensitivity analysis
        reference_value: 0.8
        units: sensitivity score
      functional_similarity_score: 0.82
      id: funcpar:004
      impaired_functions:
      - Mechanistic interpretation
      - Rare toxicity prediction
      name: Hepatotoxicity Prediction Performance
    molecular_similarity:
      correlation_coefficient: 0.68
      data_source: ChEMBL and ToxCast hepatotoxicity databases
      description: Molecular descriptor-based similarity to known hepatotoxicants
      differentially_expressed_genes:
      - adjusted_p_value: 0.05
        ensembl_id: ENSG00000160868
        fold_change: -2.1
        gene_symbol: CYP3A4
        id: gene:010
        name: CYP3A4
        p_value: 0.01
      id: molsim:004
      methodology: Tanimoto similarity with Morgan fingerprints
      name: Chemical Structure-Toxicity Relationship
      similarity_score: 0.71
      statistical_significance:
        adjusted_p_value: 0.005
        confidence_interval_lower: 0.63
        confidence_interval_upper: 0.75
        p_value: 0.001
        statistical_test: Bootstrap confidence intervals
    reproducibility:
      batch_to_batch_variation: 0.02
      coefficient_of_variation: 0.04
      description: Cross-validation and external validation consistency
      id: repro:004
      inter_laboratory_consistency: 0.88
      name: QSAR Model Reproducibility
      quality_control_metrics:
      - metric_name: Cross-validation AUC
        metric_value: 0.87
        pass_fail_status: true
        threshold: 0.8
      - metric_name: External validation AUC
        metric_value: 0.84
        pass_fail_status: true
        threshold: 0.75
      - metric_name: Model coverage
        metric_value: 0.92
        pass_fail_status: true
        threshold: 0.85
      replicate_count: 100
      reproducibility_score: 0.89
molecular_descriptors:
- Morgan fingerprints (radius=2, 2048 bits)
- Physicochemical properties (MW, LogP, PSA)
- Lipinski descriptors
- ADMET properties
name: Hepatotoxicity QSAR Model
prediction_scope: Binary classification of hepatotoxicity risk for small molecules
software_platform: Python with scikit-learn and RDKit
spatial_context: Whole liver toxicity prediction without spatial resolution
training_dataset_size: 1036
type: QSARModel
validation_datasets:
- DILIrank dataset (1036 compounds)
- FDA adverse event database compounds
- ToxCast hepatotoxicity screening data

```
## TwoDCellCulture-example-001
### Input
```yaml
biological_organization_level: CELLULAR
cell_source: Primary human hepatocytes isolated from healthy donor liver tissue
cell_types:
- id: CL:0000182
  name: hepatocyte
complexity_level: MODERATE
confluence_level: 0.85
description: A two-dimensional cell culture system using primary human hepatocytes
  in monolayer  configuration for high-throughput drug metabolism and hepatotoxicity
  screening.  The model maintains hepatocyte-specific functions including CYP enzyme
  activity,  albumin production, and bile acid synthesis for pharmaceutical safety
  assessment  and drug-drug interaction studies.
id: twodcellculture:001
models:
- biological_system_modeled: hepatic_drug_metabolism:001
  concordance:
    functional_parity: Physiological drug metabolism and detoxification
    molecular_similarity: High expression of hepatic metabolism enzymes
    reproducibility: Consistent metabolic activity across donor batches
  is_computed: false
  structured_concordance:
    cell_type_coverage:
      cell_type_proportions:
      - biological_proportion: 0.75
        cell_type:
          id: CL:0000182
          name: hepatocyte
        model_proportion: 0.95
        proportion_ratio: 1.27
      coverage_percentage: 95.0
      description: Analysis of hepatocyte identity and functional markers
      id: cellcov:014
      missing_cell_types:
      - id: CL:0000091
        name: Kupffer cell
      - id: CL:0002293
        name: epithelial cell of thymus
      name: Hepatocyte Purity and Function
      represented_cell_types:
      - id: CL:0000182
        name: hepatocyte
      single_cell_method: Flow cytometry with hepatocyte-specific markers
    functional_parity:
      conserved_functions:
      - Phase I drug metabolism
      - Phase II conjugation reactions
      - Albumin synthesis
      - Urea cycle activity
      - Bile acid synthesis
      description: Evaluation of drug metabolism and hepatocyte-specific functions
      dose_response_similarity:
        compound_tested: Rifampicin CYP3A4 induction
        correlation_coefficient: 0.91
        ec50_ratio: 1.13
        max_response_ratio: 0.94
      functional_assays:
      - assay_result: 89.5
        assay_type: Enzyme activity
        id: assay:068
        methodology: "LC-MS/MS analysis of 6\u03B2-hydroxytestosterone formation"
        name: CYP3A4 testosterone hydroxylation
        reference_value: 95.2
        units: pmol/min/mg protein
      - assay_result: 14.2
        assay_type: Protein synthesis
        id: assay:069
        methodology: ELISA quantification in culture medium
        name: Albumin secretion rate
        reference_value: 16.8
        units: "\u03BCg/day/mg protein"
      - assay_result: 0.35
        assay_type: Drug toxicity
        id: assay:070
        methodology: ATP-based cell viability assay
        name: Acetaminophen hepatotoxicity
        reference_value: 0.31
        units: EC50 (mM)
      functional_similarity_score: 0.93
      id: funcpar:026
      impaired_functions:
      - Hepatic regeneration capacity
      - 3D architectural organization
      name: Hepatocyte Metabolic Function Assessment
    molecular_similarity:
      conserved_genes:
      - adjusted_p_value: 0.901
        ensembl_id: ENSG00000075624
        fold_change: 1.0
        gene_symbol: ACTB
        id: gene:086
        name: ACTB
        p_value: 0.823
      correlation_coefficient: 0.92
      data_source: Human liver tissue reference dataset from organ donors
      description: RNA-seq comparison with fresh human liver tissue
      differentially_expressed_genes:
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000160868
        fold_change: 12.5
        gene_symbol: CYP3A4
        id: gene:083
        name: CYP3A4
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000140505
        fold_change: 8.2
        gene_symbol: CYP1A2
        id: gene:084
        name: CYP1A2
        p_value: 0.0001
      - adjusted_p_value: 0.001
        ensembl_id: ENSG00000163631
        fold_change: 25.8
        gene_symbol: ALB
        id: gene:085
        name: ALB
        p_value: 0.0001
      id: molsim:026
      methodology: Bulk RNA sequencing with hepatic function gene panel
      name: Primary Hepatocyte Expression Profile
      similarity_score: 0.95
      statistical_significance:
        adjusted_p_value: 0.001
        confidence_interval_lower: 0.89
        confidence_interval_upper: 0.97
        p_value: 0.0001
        statistical_test: Pearson correlation
    reproducibility:
      batch_to_batch_variation: 0.16
      coefficient_of_variation: 0.13
      description: Inter-donor and inter-batch functional consistency
      id: repro:026
      inter_laboratory_consistency: 0.84
      name: Primary Hepatocyte Culture Reproducibility
      quality_control_metrics:
      - metric_name: Cell viability at plating
        metric_value: 0.91
        pass_fail_status: true
        threshold: 0.85
      - metric_name: CYP enzyme activity retention
        metric_value: 0.88
        pass_fail_status: true
        threshold: 0.8
      - metric_name: Albumin synthesis consistency
        metric_value: 0.85
        pass_fail_status: true
        threshold: 0.75
      replicate_count: 45
      reproducibility_score: 0.87
name: Primary Human Hepatocyte Monolayer Drug Screening Model
passage_protocol: Primary cells, passage 0 - no passaging required, maintained for
  3-7 days
references:
- authors:
  - Anderson K
  - Williams J
  - Brown M
  - Davis L
  id: doi:10.1016/j.tox.2024.153456
  journal: Toxicology
  title: 'Primary human hepatocyte culture systems for drug safety assessment: current
    practices and future directions'
  url: https://www.sciencedirect.com/science/article/pii/S0300483X24001234
  year: 2024
- authors:
  - Mueller R
  - Schmidt T
  - Weber H
  - Koch S
  id: doi:10.1007/s00204-024-03567-2
  journal: Archives of Toxicology
  title: Advances in hepatotoxicity screening using primary human hepatocyte models
  url: https://link.springer.com/article/10.1007/s00204-024-03567-2
  year: 2024
spatial_context: 2D monolayer culture with hepatocyte polarization and bile canaliculi
  formation
substrate_type: Collagen-coated tissue culture plates with hepatocyte attachment factor
type: TwoDCellCulture

```
