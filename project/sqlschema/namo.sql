-- # Class: Dataset
--     * Slot: id
-- # Class: NamedThing Description: A generic grouping for any identifiable entity
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: Study Description: A study is a structured investigation or analysis, often involving the collection and interpretation of data, to answer specific research questions or test hypotheses.
--     * Slot: context_of_use Description: What decision will this inform? Care? Policy? Drug approval?
--     * Slot: biological_context Description: tissue/region (anatomy), cell types, sex/age equivalents, mechanics (e.g., cyclic stretch), microenvironment
--     * Slot: perturbations Description: exposure/dose/time; diet/drugs/toxicants
--     * Slot: endpoints Description: phenotypes, function (TEER/leak, beating rate), and multi-omics
--     * Slot: plan_comparators Description: human data, gold-standard assays, or high-quality animal references
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Abstract Class: ModelSystem
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: AnimalModel
--     * Slot: species Description: The species of the animal used in the model system.
--     * Slot: strain Description: The specific strain of the animal used in the model system.
--     * Slot: age Description: The age of the animal used in the model system.
--     * Slot: environment Description: The environmental conditions under which the animal model is maintained.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Abstract Class: NAMModel Description: A New Approach Methodology (NAM) model, which is a type of model system that does not involve the use of animals.
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Abstract Class: CellularSystem Description: Cell-based model systems that use living cells to model biological processes. Includes 2D cultures, 3D systems, and co-cultures.
--     * Slot: cell_source Description: Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)
--     * Slot: culture_conditions Description: Standard culture conditions and media used
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: TwoDCellCulture Description: Conventional monolayer cell cultures grown on flat surfaces. Simple but limited in physiological relevance.
--     * Slot: substrate_type Description: Type of culture substrate (e.g., plastic, glass, coated surfaces)
--     * Slot: confluence_level Description: Typical confluence level maintained (0.0-1.0)
--     * Slot: passage_protocol Description: Standard passaging protocol and frequency
--     * Slot: cell_source Description: Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)
--     * Slot: culture_conditions Description: Standard culture conditions and media used
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: ThreeDCellCulture Description: Three-dimensional cell culture systems including spheroids and organoids. More physiologically relevant with 3D architecture.
--     * Slot: three_d_architecture Description: Type of 3D architecture (spheroid, organoid, scaffold-based, etc.)
--     * Slot: matrix_composition Description: Composition of extracellular matrix or scaffold material
--     * Slot: size_range Description: Typical size range of 3D structures
--     * Slot: cell_source Description: Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)
--     * Slot: culture_conditions Description: Standard culture conditions and media used
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: CoCulture Description: Co-culture systems combining multiple cell types to mimic  microenvironments and cell-cell interactions.
--     * Slot: coculture_configuration Description: Configuration of co-culture (direct contact, transwell, conditioned media)
--     * Slot: cell_source Description: Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)
--     * Slot: culture_conditions Description: Standard culture conditions and media used
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: Organoid Description: A 3D cell culture system that self-organizes to recapitulate key structural and functional aspects of an organ or tissue
--     * Slot: differentiation_method Description: Method used to differentiate cells into organoid (e.g., directed differentiation protocol)
--     * Slot: culture_system Description: Culture system used (e.g., Matrigel dome, suspension culture, air-liquid interface)
--     * Slot: three_d_architecture Description: Type of 3D architecture (spheroid, organoid, scaffold-based, etc.)
--     * Slot: matrix_composition Description: Composition of extracellular matrix or scaffold material
--     * Slot: size_range Description: Typical size range of 3D structures
--     * Slot: cell_source Description: Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)
--     * Slot: culture_conditions Description: Standard culture conditions and media used
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: organ_modeled_id Description: The organ or tissue being modeled
-- # Class: CellLineModel Description: A model system based on immortalized cell lines that can be maintained in culture indefinitely. Examples: HepG2, A549, Caco-2, etc.
--     * Slot: passage_range Description: Recommended passage number range for experimental use
--     * Slot: authentication_method Description: Method used for cell line authentication (e.g., STR profiling, mycoplasma testing)
--     * Slot: substrate_type Description: Type of culture substrate (e.g., plastic, glass, coated surfaces)
--     * Slot: confluence_level Description: Typical confluence level maintained (0.0-1.0)
--     * Slot: passage_protocol Description: Standard passaging protocol and frequency
--     * Slot: cell_source Description: Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)
--     * Slot: culture_conditions Description: Standard culture conditions and media used
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Abstract Class: MicrophysiologicalSystem Description: Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials,  and living cells to replicate tissue-level physiology and dynamics.
--     * Slot: perfusion_system Description: Description of perfusion and flow systems
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: microfluidic_design_id Description: Detailed design specifications of the microfluidic device
--     * Slot: mechanical_forces_id Description: Mechanical forces applied to the model system
-- # Class: OrganOnChip Description: A model system that simulates the physiological functions of an organ using a microfluidic device. Examples: Airway-on-chip, ...
--     * Slot: cell_source Description: Source of cells (e.g., primary human cells, iPSC-derived, cell line, patient-derived)
--     * Slot: perfusion_system Description: Description of perfusion and flow systems
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: organ_modeled_id Description: The organ or anatomical structure being modeled (e.g., lung, airway, alveolus)
--     * Slot: microfluidic_design_id Description: Detailed design specifications of the microfluidic device
--     * Slot: mechanical_forces_id Description: Mechanical forces applied to the model system
-- # Class: TissueOnChip Description: Tissue-level microphysiological systems that model specific tissue functions and multi-cellular interactions.
--     * Slot: tissue_architecture Description: Description of tissue-level architecture and organization
--     * Slot: perfusion_system Description: Description of perfusion and flow systems
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: tissue_modeled_id Description: The specific tissue being modeled
--     * Slot: microfluidic_design_id Description: Detailed design specifications of the microfluidic device
--     * Slot: mechanical_forces_id Description: Mechanical forces applied to the model system
-- # Abstract Class: InSilicoModel Description: Computational models that simulate biological processes without physical biological components.
--     * Slot: computational_method Description: Primary computational method or algorithm used
--     * Slot: software_platform Description: Software platform or programming language used
--     * Slot: prediction_scope Description: Scope and limitations of model predictions
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: QSARModel Description: Quantitative Structure-Activity Relationship models that predict  chemical/biological activity from molecular structure.
--     * Slot: activity_endpoint Description: Biological activity or property being predicted
--     * Slot: training_dataset_size Description: Number of compounds in training dataset
--     * Slot: computational_method Description: Primary computational method or algorithm used
--     * Slot: software_platform Description: Software platform or programming language used
--     * Slot: prediction_scope Description: Scope and limitations of model predictions
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: model_performance_id Description: Statistical performance metrics of the model
-- # Class: PBPKModel Description: Physiologically Based Pharmacokinetic models that simulate drug  absorption, distribution, metabolism, and excretion.
--     * Slot: computational_method Description: Primary computational method or algorithm used
--     * Slot: software_platform Description: Software platform or programming language used
--     * Slot: prediction_scope Description: Scope and limitations of model predictions
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: species_modeled_id Description: Species for which the model is designed
--     * Slot: drug_properties_id Description: Physicochemical and pharmacological properties modeled
-- # Class: DigitalTwin Description: Computational replicas of biological systems for real-time prediction and personalized modeling.
--     * Slot: twin_scope Description: Scope of digital twin (organ, patient, population)
--     * Slot: update_frequency Description: Frequency of model updates based on new data
--     * Slot: computational_method Description: Primary computational method or algorithm used
--     * Slot: software_platform Description: Software platform or programming language used
--     * Slot: prediction_scope Description: Scope and limitations of model predictions
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: MLModel Description: Machine Learning and AI-based models for prediction, mechanism inference, and hypothesis generation.
--     * Slot: ml_algorithm Description: Type of machine learning algorithm used
--     * Slot: training_data_size Description: Size of training dataset
--     * Slot: model_interpretability Description: Level of model interpretability (black box, interpretable, explainable)
--     * Slot: computational_method Description: Primary computational method or algorithm used
--     * Slot: software_platform Description: Software platform or programming language used
--     * Slot: prediction_scope Description: Scope and limitations of model predictions
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: cross_validation_id Description: Cross-validation strategy and results
-- # Class: MetabolicModel Description: A model that simulates the metabolic processes of an organism or system. Examples: Virtual Physiological Human, ...
--     * Slot: computational_method Description: Primary computational method or algorithm used
--     * Slot: software_platform Description: Software platform or programming language used
--     * Slot: prediction_scope Description: Scope and limitations of model predictions
--     * Slot: biological_organization_level Description: The level of biological organization represented by the model
--     * Slot: spatial_context Description: Description of spatial organization and context captured by the model
--     * Slot: complexity_level Description: Level of biological complexity represented (subcellular, cellular, tissue, organ, system)
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: CellRatio Description: Ratio specification for different cell types in co-culture systems.
--     * Slot: id
--     * Slot: ratio Description: Proportion or ratio of this cell type (0.0-1.0 or absolute numbers)
--     * Slot: ratio_type Description: Type of ratio specification (percentage, absolute, fold)
--     * Slot: CoCulture_id Description: Autocreated FK slot
--     * Slot: cell_type_id Description: The cell type for which the ratio is specified
-- # Class: ModelPerformance Description: Statistical performance metrics for computational models.
--     * Slot: id
--     * Slot: accuracy Description: Overall accuracy of the model (0.0-1.0)
--     * Slot: sensitivity Description: Sensitivity/recall of the model (0.0-1.0)
--     * Slot: specificity Description: Specificity of the model (0.0-1.0)
--     * Slot: r_squared Description: R-squared value for regression models
--     * Slot: rmse Description: Root mean square error
--     * Slot: auc Description: Area under the ROC curve
-- # Class: PBPKCompartment Description: A physiological compartment in a PBPK model.
--     * Slot: compartment_type Description: Type of physiological compartment
--     * Slot: volume Description: Volume of the compartment (L)
--     * Slot: blood_flow Description: Blood flow to the compartment (L/h)
--     * Slot: partition_coefficient Description: Tissue-to-plasma partition coefficient
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: PBPKModel_id Description: Autocreated FK slot
-- # Class: DrugProperties Description: Physicochemical and pharmacological properties of a drug in PBPK models.
--     * Slot: id
--     * Slot: molecular_weight Description: Molecular weight (g/mol)
--     * Slot: logp Description: Lipophilicity (log P)
--     * Slot: pka Description: Acid dissociation constant
--     * Slot: protein_binding Description: Fraction bound to plasma proteins (0.0-1.0)
--     * Slot: clearance Description: Total body clearance (L/h)
-- # Class: CrossValidation Description: Cross-validation strategy and results for ML models.
--     * Slot: id
--     * Slot: cv_method Description: Type of cross-validation used
--     * Slot: n_folds Description: Number of folds in cross-validation
--     * Slot: cv_score Description: Average cross-validation score
--     * Slot: cv_std Description: Standard deviation of cross-validation scores
-- # Class: MicrofluidicDesign Description: Detailed specification of a microfluidic device design including its architecture, materials, dimensions, and functional features.
--     * Slot: architecture_type Description: The overall architecture type of the microfluidic device
--     * Slot: number_of_channels Description: Total number of channels in the device
--     * Slot: membrane_type Description: Type of membrane used in the device if applicable
--     * Slot: membrane_pore_size Description: Pore size of the membrane in micrometers
--     * Slot: membrane_thickness Description: Thickness of the membrane in micrometers
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: ChannelDimensions Description: Dimensions of a microfluidic channel
--     * Slot: id
--     * Slot: channel_name Description: Name or identifier of the channel (e.g., apical, basolateral, vascular)
--     * Slot: width Description: Width of the channel in micrometers
--     * Slot: height Description: Height of the channel in micrometers
--     * Slot: length Description: Length of the channel in millimeters
-- # Class: MechanicalStimulation Description: Specification of mechanical forces applied to the model system
--     * Slot: cyclic_stretch_percent Description: Percentage of cyclic stretch applied (if applicable)
--     * Slot: frequency_hz Description: Frequency of mechanical stimulation in Hertz
--     * Slot: shear_stress Description: Shear stress applied in dyn/cm²
--     * Slot: pressure_pascal Description: Pressure applied in Pascals
--     * Slot: duration_minutes Description: Duration of mechanical stimulation in minutes
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: BiologicalSystem
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: ModelsRelationship
--     * Slot: id
--     * Slot: biological_system_modeled
--     * Slot: is_computed Description: Indicates whether the model is computed or derived from experimental data.
--     * Slot: concordance_id Description: Metrics used to assess the concordance between the model system and the biological system, such as sensitivity, specificity, and accuracy.
--     * Slot: structured_concordance_id Description: Detailed structured assessment of concordance between the model system and the biological system, with rich metadata and supporting evidence.
-- # Class: ConcordanceResult
--     * Slot: id
--     * Slot: phenotype_overlap
--     * Slot: molecular_similarity
--     * Slot: pathway_concordance
--     * Slot: cell_type_coverage
--     * Slot: functional_parity
--     * Slot: reproducibility
-- # Class: StructuredConcordanceResult Description: Detailed structured assessment of concordance between model and biological systems with rich metadata, evidence, and quantitative measures.
--     * Slot: id
--     * Slot: molecular_similarity_id Description: Detailed assessment of molecular-level similarity including gene expression, protein levels, and metabolic profiles.
--     * Slot: pathway_concordance_id Description: Assessment of biological pathway conservation and activity levels.
--     * Slot: phenotype_overlap_id Description: Comparison of phenotypic manifestations between model and biological system.
--     * Slot: cell_type_coverage_id Description: Assessment of cell type representation and cellular diversity.
--     * Slot: functional_parity_id Description: Evaluation of functional capabilities and physiological responses.
--     * Slot: reproducibility_id Description: Assessment of experimental reproducibility and consistency.
-- # Class: MolecularSimilarity Description: Detailed assessment of molecular-level concordance between model and biological systems.
--     * Slot: similarity_score Description: Quantitative similarity score (0.0-1.0) based on molecular profiles.
--     * Slot: correlation_coefficient Description: Pearson correlation coefficient for expression profiles.
--     * Slot: methodology Description: Description of experimental methods used for molecular comparison.
--     * Slot: data_source Description: Source of molecular data (e.g., RNA-seq, proteomics, metabolomics).
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: statistical_significance_id Description: Statistical measures of significance for the molecular similarity.
-- # Class: PathwayConcordance Description: Assessment of biological pathway conservation and activity between model and biological systems.
--     * Slot: pathway_overlap_score Description: Quantitative score (0.0-1.0) representing pathway overlap.
--     * Slot: pathway_analysis_method Description: Method used for pathway analysis (e.g., GSEA, Over-representation analysis).
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: PhenotypeOverlap Description: Comparison of phenotypic manifestations between model and biological systems.
--     * Slot: phenotype_similarity_score Description: Quantitative score (0.0-1.0) representing phenotypic similarity.
--     * Slot: phenotype_ontology Description: Ontology used for phenotype classification (e.g., HPO, MP).
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: CellTypeCoverage Description: Assessment of cell type representation and cellular diversity between systems.
--     * Slot: coverage_percentage Description: Percentage of target cell types represented in the model system.
--     * Slot: single_cell_method Description: Method used for single-cell analysis (e.g., scRNA-seq, flow cytometry).
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: FunctionalParity Description: Evaluation of functional capabilities and physiological responses between systems.
--     * Slot: functional_similarity_score Description: Quantitative score (0.0-1.0) representing functional similarity.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: dose_response_similarity_id Description: Comparison of dose-response relationships for therapeutic compounds.
-- # Class: Reproducibility Description: Assessment of experimental reproducibility and consistency of the model system.
--     * Slot: reproducibility_score Description: Quantitative score (0.0-1.0) representing reproducibility.
--     * Slot: coefficient_of_variation Description: Coefficient of variation across experimental replicates.
--     * Slot: batch_to_batch_variation Description: Measure of variation between different experimental batches.
--     * Slot: inter_laboratory_consistency Description: Measure of consistency across different laboratories.
--     * Slot: replicate_count Description: Number of experimental replicates used in assessment.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
-- # Class: Gene Description: A gene entity with identifiers and expression information.
--     * Slot: gene_symbol Description: Standard gene symbol (e.g., HGNC symbol for human genes).
--     * Slot: ensembl_id Description: Ensembl gene identifier.
--     * Slot: entrez_id Description: NCBI Entrez gene identifier.
--     * Slot: fold_change Description: Fold change in expression compared to control or reference.
--     * Slot: p_value Description: Statistical p-value for differential expression.
--     * Slot: adjusted_p_value Description: Multiple testing corrected p-value.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: MolecularSimilarity_id Description: Autocreated FK slot
-- # Class: Pathway Description: A biological pathway with activity and enrichment information.
--     * Slot: pathway_database Description: Source database (e.g., KEGG, Reactome, GO).
--     * Slot: pathway_id Description: Database-specific pathway identifier.
--     * Slot: activity_score Description: Quantitative measure of pathway activity.
--     * Slot: enrichment_score Description: Statistical enrichment score for the pathway.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: PathwayConcordance_id Description: Autocreated FK slot
-- # Class: StatisticalSignificance Description: Statistical measures of significance for molecular comparisons.
--     * Slot: id
--     * Slot: p_value Description: Statistical p-value.
--     * Slot: adjusted_p_value Description: Multiple testing corrected p-value.
--     * Slot: confidence_interval_lower Description: Lower bound of confidence interval.
--     * Slot: confidence_interval_upper Description: Upper bound of confidence interval.
--     * Slot: statistical_test Description: Name of statistical test used.
-- # Class: EnrichmentStatistics Description: Statistical measures for pathway enrichment analysis.
--     * Slot: id
--     * Slot: enrichment_score Description: Quantitative enrichment score.
--     * Slot: p_value Description: Statistical p-value for enrichment.
--     * Slot: q_value Description: False discovery rate corrected p-value.
--     * Slot: genes_in_pathway Description: Number of genes in the pathway.
--     * Slot: genes_in_dataset Description: Number of genes from dataset found in pathway.
--     * Slot: PathwayConcordance_id Description: Autocreated FK slot
-- # Class: CellTypeProportion Description: Quantitative comparison of cell type proportions between systems.
--     * Slot: id
--     * Slot: model_proportion Description: Proportion of this cell type in the model system.
--     * Slot: biological_proportion Description: Proportion of this cell type in the biological system.
--     * Slot: proportion_ratio Description: Ratio of model to biological proportions.
--     * Slot: CellTypeCoverage_id Description: Autocreated FK slot
--     * Slot: cell_type_id Description: The cell type being compared.
-- # Class: FunctionalAssay Description: A functional assay used to assess biological capabilities.
--     * Slot: assay_type Description: Type of functional assay (e.g., TEER, permeability, metabolic activity).
--     * Slot: assay_result Description: Quantitative result of the assay.
--     * Slot: reference_value Description: Reference or control value for comparison.
--     * Slot: units Description: Units of measurement for the assay result.
--     * Slot: methodology Description: Detailed methodology for the assay.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: FunctionalParity_id Description: Autocreated FK slot
-- # Class: DoseResponseSimilarity Description: Comparison of dose-response relationships between model and biological systems.
--     * Slot: id
--     * Slot: correlation_coefficient Description: Correlation coefficient between dose-response curves.
--     * Slot: ec50_ratio Description: Ratio of EC50 values between model and biological system.
--     * Slot: max_response_ratio Description: Ratio of maximum responses between systems.
--     * Slot: compound_tested Description: Name of compound used in dose-response testing.
-- # Class: QualityControlMetric Description: A quality control measure and its associated value.
--     * Slot: id
--     * Slot: metric_name Description: Name of the quality control metric.
--     * Slot: metric_value Description: Value of the quality control metric.
--     * Slot: threshold Description: Acceptable threshold for this metric.
--     * Slot: pass_fail_status Description: Whether this metric passes quality control criteria.
--     * Slot: Reproducibility_id Description: Autocreated FK slot
-- # Class: Reference Description: A literature reference with identifier and title for citing published work.
--     * Slot: id Description: Persistent identifier for the reference (DOI, PMID, PMCID, etc.)
--     * Slot: title Description: Title of the referenced publication or dataset
--     * Slot: journal Description: Journal or publication venue
--     * Slot: year Description: Publication year
--     * Slot: url Description: URL to access the publication
--     * Slot: NAMModel_id Description: Autocreated FK slot
--     * Slot: CellularSystem_id Description: Autocreated FK slot
--     * Slot: TwoDCellCulture_id Description: Autocreated FK slot
--     * Slot: ThreeDCellCulture_id Description: Autocreated FK slot
--     * Slot: CoCulture_id Description: Autocreated FK slot
--     * Slot: Organoid_id Description: Autocreated FK slot
--     * Slot: CellLineModel_id Description: Autocreated FK slot
--     * Slot: MicrophysiologicalSystem_id Description: Autocreated FK slot
--     * Slot: OrganOnChip_id Description: Autocreated FK slot
--     * Slot: TissueOnChip_id Description: Autocreated FK slot
--     * Slot: InSilicoModel_id Description: Autocreated FK slot
--     * Slot: QSARModel_id Description: Autocreated FK slot
--     * Slot: PBPKModel_id Description: Autocreated FK slot
--     * Slot: DigitalTwin_id Description: Autocreated FK slot
--     * Slot: MLModel_id Description: Autocreated FK slot
--     * Slot: MetabolicModel_id Description: Autocreated FK slot
-- # Class: Term Description: A term is a concept or entity that can be defined and used in a specific context, often within a controlled vocabulary or ontology.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type
--     * Slot: CellularSystem_id Description: Autocreated FK slot
--     * Slot: TwoDCellCulture_id Description: Autocreated FK slot
--     * Slot: ThreeDCellCulture_id Description: Autocreated FK slot
--     * Slot: CoCulture_id Description: Autocreated FK slot
--     * Slot: Organoid_id Description: Autocreated FK slot
--     * Slot: CellLineModel_id Description: Autocreated FK slot
--     * Slot: OrganOnChip_id Description: Autocreated FK slot
--     * Slot: PhenotypeOverlap_id Description: Autocreated FK slot
--     * Slot: CellTypeCoverage_id Description: Autocreated FK slot
-- # Class: ModelSystem_models
--     * Slot: ModelSystem_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: AnimalModel_models
--     * Slot: AnimalModel_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: NAMModel_models
--     * Slot: NAMModel_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: CellularSystem_models
--     * Slot: CellularSystem_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: TwoDCellCulture_models
--     * Slot: TwoDCellCulture_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: ThreeDCellCulture_models
--     * Slot: ThreeDCellCulture_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: CoCulture_interaction_mechanisms
--     * Slot: CoCulture_id Description: Autocreated FK slot
--     * Slot: interaction_mechanisms Description: Mechanisms of cell-cell interaction (paracrine, direct contact, mechanical)
-- # Class: CoCulture_models
--     * Slot: CoCulture_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: Organoid_models
--     * Slot: Organoid_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: CellLineModel_models
--     * Slot: CellLineModel_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: MicrophysiologicalSystem_sensor_integration
--     * Slot: MicrophysiologicalSystem_id Description: Autocreated FK slot
--     * Slot: sensor_integration Description: Sensors integrated for real-time monitoring
-- # Class: MicrophysiologicalSystem_models
--     * Slot: MicrophysiologicalSystem_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: OrganOnChip_sensor_integration
--     * Slot: OrganOnChip_id Description: Autocreated FK slot
--     * Slot: sensor_integration Description: Sensors integrated for real-time monitoring
-- # Class: OrganOnChip_models
--     * Slot: OrganOnChip_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: TissueOnChip_barrier_functions
--     * Slot: TissueOnChip_id Description: Autocreated FK slot
--     * Slot: barrier_functions Description: Tissue barrier functions modeled (epithelial, endothelial, etc.)
-- # Class: TissueOnChip_sensor_integration
--     * Slot: TissueOnChip_id Description: Autocreated FK slot
--     * Slot: sensor_integration Description: Sensors integrated for real-time monitoring
-- # Class: TissueOnChip_models
--     * Slot: TissueOnChip_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: InSilicoModel_validation_datasets
--     * Slot: InSilicoModel_id Description: Autocreated FK slot
--     * Slot: validation_datasets Description: Datasets used for model training and validation
-- # Class: InSilicoModel_models
--     * Slot: InSilicoModel_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: QSARModel_molecular_descriptors
--     * Slot: QSARModel_id Description: Autocreated FK slot
--     * Slot: molecular_descriptors Description: Types of molecular descriptors used (topological, electronic, etc.)
-- # Class: QSARModel_validation_datasets
--     * Slot: QSARModel_id Description: Autocreated FK slot
--     * Slot: validation_datasets Description: Datasets used for model training and validation
-- # Class: QSARModel_models
--     * Slot: QSARModel_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: PBPKModel_elimination_pathways
--     * Slot: PBPKModel_id Description: Autocreated FK slot
--     * Slot: elimination_pathways Description: Drug elimination and metabolism pathways included
-- # Class: PBPKModel_validation_datasets
--     * Slot: PBPKModel_id Description: Autocreated FK slot
--     * Slot: validation_datasets Description: Datasets used for model training and validation
-- # Class: PBPKModel_models
--     * Slot: PBPKModel_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: DigitalTwin_real_time_data_sources
--     * Slot: DigitalTwin_id Description: Autocreated FK slot
--     * Slot: real_time_data_sources Description: Sources of real-time data for model updating
-- # Class: DigitalTwin_personalization_parameters
--     * Slot: DigitalTwin_id Description: Autocreated FK slot
--     * Slot: personalization_parameters Description: Parameters used for personalization (genetic, phenotypic, etc.)
-- # Class: DigitalTwin_validation_datasets
--     * Slot: DigitalTwin_id Description: Autocreated FK slot
--     * Slot: validation_datasets Description: Datasets used for model training and validation
-- # Class: DigitalTwin_models
--     * Slot: DigitalTwin_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: MLModel_feature_types
--     * Slot: MLModel_id Description: Autocreated FK slot
--     * Slot: feature_types Description: Types of features used (molecular, phenotypic, imaging, etc.)
-- # Class: MLModel_validation_datasets
--     * Slot: MLModel_id Description: Autocreated FK slot
--     * Slot: validation_datasets Description: Datasets used for model training and validation
-- # Class: MLModel_models
--     * Slot: MLModel_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: MetabolicModel_validation_datasets
--     * Slot: MetabolicModel_id Description: Autocreated FK slot
--     * Slot: validation_datasets Description: Datasets used for model training and validation
-- # Class: MetabolicModel_models
--     * Slot: MetabolicModel_id Description: Autocreated FK slot
--     * Slot: models_id
-- # Class: MicrofluidicDesign_channel_configuration
--     * Slot: MicrofluidicDesign_id Description: Autocreated FK slot
--     * Slot: channel_configuration Description: Configuration of channels (e.g., parallel, serial, branching)
-- # Class: MicrofluidicDesign_interface_type
--     * Slot: MicrofluidicDesign_id Description: Autocreated FK slot
--     * Slot: interface_type Description: Type of interface(s) present in the device
-- # Class: MicrofluidicDesign_channel_dimensions
--     * Slot: MicrofluidicDesign_id Description: Autocreated FK slot
--     * Slot: channel_dimensions_id Description: Dimensions of the channels in the device
-- # Class: MicrofluidicDesign_material
--     * Slot: MicrofluidicDesign_id Description: Autocreated FK slot
--     * Slot: material Description: Materials used to construct the device
-- # Class: MicrofluidicDesign_surface_treatment
--     * Slot: MicrofluidicDesign_id Description: Autocreated FK slot
--     * Slot: surface_treatment Description: Surface treatments or coatings applied to the device
-- # Class: MicrofluidicDesign_flow_control_method
--     * Slot: MicrofluidicDesign_id Description: Autocreated FK slot
--     * Slot: flow_control_method Description: Methods used to control fluid flow in the device
-- # Class: MicrofluidicDesign_sensors_integrated
--     * Slot: MicrofluidicDesign_id Description: Autocreated FK slot
--     * Slot: sensors_integrated Description: Sensors integrated into the device for monitoring
-- # Class: MicrofluidicDesign_special_features
--     * Slot: MicrofluidicDesign_id Description: Autocreated FK slot
--     * Slot: special_features Description: Additional special features of the device (e.g., valves, mixers, gradient generators)
-- # Class: MechanicalStimulation_stimulation_type
--     * Slot: MechanicalStimulation_id Description: Autocreated FK slot
--     * Slot: stimulation_type Description: Type of mechanical stimulation applied
-- # Class: FunctionalParity_conserved_functions
--     * Slot: FunctionalParity_id Description: Autocreated FK slot
--     * Slot: conserved_functions Description: List of biological functions conserved between model and biological system.
-- # Class: FunctionalParity_impaired_functions
--     * Slot: FunctionalParity_id Description: Autocreated FK slot
--     * Slot: impaired_functions Description: List of functions that are impaired or absent in the model system.
-- # Class: Reference_authors
--     * Slot: Reference_id Description: Autocreated FK slot
--     * Slot: authors Description: Authors of the publication

CREATE TABLE "Dataset" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Dataset_id" ON "Dataset" (id);
CREATE TABLE "NamedThing" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NamedThing_id" ON "NamedThing" (id);
CREATE TABLE "NAMModel" (
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NAMModel_id" ON "NAMModel" (id);
CREATE TABLE "CellularSystem" (
	cell_source TEXT,
	culture_conditions TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CellularSystem_id" ON "CellularSystem" (id);
CREATE TABLE "TwoDCellCulture" (
	substrate_type TEXT,
	confluence_level FLOAT,
	passage_protocol TEXT,
	cell_source TEXT,
	culture_conditions TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TwoDCellCulture_id" ON "TwoDCellCulture" (id);
CREATE TABLE "ThreeDCellCulture" (
	three_d_architecture VARCHAR(17),
	matrix_composition TEXT,
	size_range TEXT,
	cell_source TEXT,
	culture_conditions TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ThreeDCellCulture_id" ON "ThreeDCellCulture" (id);
CREATE TABLE "CoCulture" (
	coculture_configuration VARCHAR(17),
	cell_source TEXT,
	culture_conditions TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CoCulture_id" ON "CoCulture" (id);
CREATE TABLE "Organoid" (
	differentiation_method TEXT,
	culture_system TEXT,
	three_d_architecture VARCHAR(17),
	matrix_composition TEXT,
	size_range TEXT,
	cell_source TEXT,
	culture_conditions TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	organ_modeled_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(organ_modeled_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_Organoid_id" ON "Organoid" (id);
CREATE TABLE "CellLineModel" (
	passage_range TEXT,
	authentication_method TEXT,
	substrate_type TEXT,
	confluence_level FLOAT,
	passage_protocol TEXT,
	cell_source TEXT,
	culture_conditions TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CellLineModel_id" ON "CellLineModel" (id);
CREATE TABLE "OrganOnChip" (
	cell_source TEXT,
	perfusion_system TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	organ_modeled_id TEXT,
	microfluidic_design_id TEXT,
	mechanical_forces_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(organ_modeled_id) REFERENCES "Term" (id),
	FOREIGN KEY(microfluidic_design_id) REFERENCES "MicrofluidicDesign" (id),
	FOREIGN KEY(mechanical_forces_id) REFERENCES "MechanicalStimulation" (id)
);CREATE INDEX "ix_OrganOnChip_id" ON "OrganOnChip" (id);
CREATE TABLE "InSilicoModel" (
	computational_method TEXT,
	software_platform TEXT,
	prediction_scope TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_InSilicoModel_id" ON "InSilicoModel" (id);
CREATE TABLE "DigitalTwin" (
	twin_scope VARCHAR(10),
	update_frequency TEXT,
	computational_method TEXT,
	software_platform TEXT,
	prediction_scope TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_DigitalTwin_id" ON "DigitalTwin" (id);
CREATE TABLE "MetabolicModel" (
	computational_method TEXT,
	software_platform TEXT,
	prediction_scope TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MetabolicModel_id" ON "MetabolicModel" (id);
CREATE TABLE "ModelPerformance" (
	id INTEGER NOT NULL,
	accuracy FLOAT,
	sensitivity FLOAT,
	specificity FLOAT,
	r_squared FLOAT,
	rmse FLOAT,
	auc FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ModelPerformance_id" ON "ModelPerformance" (id);
CREATE TABLE "DrugProperties" (
	id INTEGER NOT NULL,
	molecular_weight FLOAT,
	logp FLOAT,
	pka FLOAT,
	protein_binding FLOAT,
	clearance FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_DrugProperties_id" ON "DrugProperties" (id);
CREATE TABLE "CrossValidation" (
	id INTEGER NOT NULL,
	cv_method VARCHAR(17),
	n_folds INTEGER,
	cv_score FLOAT,
	cv_std FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CrossValidation_id" ON "CrossValidation" (id);
CREATE TABLE "MicrofluidicDesign" (
	architecture_type VARCHAR(14),
	number_of_channels INTEGER,
	membrane_type VARCHAR(14),
	membrane_pore_size FLOAT,
	membrane_thickness FLOAT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MicrofluidicDesign_id" ON "MicrofluidicDesign" (id);
CREATE TABLE "ChannelDimensions" (
	id INTEGER NOT NULL,
	channel_name TEXT,
	width FLOAT,
	height FLOAT,
	length FLOAT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ChannelDimensions_id" ON "ChannelDimensions" (id);
CREATE TABLE "MechanicalStimulation" (
	cyclic_stretch_percent FLOAT,
	frequency_hz FLOAT,
	shear_stress FLOAT,
	pressure_pascal FLOAT,
	duration_minutes FLOAT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MechanicalStimulation_id" ON "MechanicalStimulation" (id);
CREATE TABLE "BiologicalSystem" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_BiologicalSystem_id" ON "BiologicalSystem" (id);
CREATE TABLE "ConcordanceResult" (
	id INTEGER NOT NULL,
	phenotype_overlap TEXT,
	molecular_similarity TEXT,
	pathway_concordance TEXT,
	cell_type_coverage TEXT,
	functional_parity TEXT,
	reproducibility TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ConcordanceResult_id" ON "ConcordanceResult" (id);
CREATE TABLE "PathwayConcordance" (
	pathway_overlap_score FLOAT,
	pathway_analysis_method TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_PathwayConcordance_id" ON "PathwayConcordance" (id);
CREATE TABLE "PhenotypeOverlap" (
	phenotype_similarity_score FLOAT,
	phenotype_ontology TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_PhenotypeOverlap_id" ON "PhenotypeOverlap" (id);
CREATE TABLE "CellTypeCoverage" (
	coverage_percentage FLOAT,
	single_cell_method TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CellTypeCoverage_id" ON "CellTypeCoverage" (id);
CREATE TABLE "Reproducibility" (
	reproducibility_score FLOAT,
	coefficient_of_variation FLOAT,
	batch_to_batch_variation FLOAT,
	inter_laboratory_consistency FLOAT,
	replicate_count INTEGER,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Reproducibility_id" ON "Reproducibility" (id);
CREATE TABLE "StatisticalSignificance" (
	id INTEGER NOT NULL,
	p_value FLOAT,
	adjusted_p_value FLOAT,
	confidence_interval_lower FLOAT,
	confidence_interval_upper FLOAT,
	statistical_test TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_StatisticalSignificance_id" ON "StatisticalSignificance" (id);
CREATE TABLE "DoseResponseSimilarity" (
	id INTEGER NOT NULL,
	correlation_coefficient FLOAT,
	ec50_ratio FLOAT,
	max_response_ratio FLOAT,
	compound_tested TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_DoseResponseSimilarity_id" ON "DoseResponseSimilarity" (id);
CREATE TABLE "Term" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	"CellularSystem_id" TEXT,
	"TwoDCellCulture_id" TEXT,
	"ThreeDCellCulture_id" TEXT,
	"CoCulture_id" TEXT,
	"Organoid_id" TEXT,
	"CellLineModel_id" TEXT,
	"OrganOnChip_id" TEXT,
	"PhenotypeOverlap_id" TEXT,
	"CellTypeCoverage_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CellularSystem_id") REFERENCES "CellularSystem" (id),
	FOREIGN KEY("TwoDCellCulture_id") REFERENCES "TwoDCellCulture" (id),
	FOREIGN KEY("ThreeDCellCulture_id") REFERENCES "ThreeDCellCulture" (id),
	FOREIGN KEY("CoCulture_id") REFERENCES "CoCulture" (id),
	FOREIGN KEY("Organoid_id") REFERENCES "Organoid" (id),
	FOREIGN KEY("CellLineModel_id") REFERENCES "CellLineModel" (id),
	FOREIGN KEY("OrganOnChip_id") REFERENCES "OrganOnChip" (id),
	FOREIGN KEY("PhenotypeOverlap_id") REFERENCES "PhenotypeOverlap" (id),
	FOREIGN KEY("CellTypeCoverage_id") REFERENCES "CellTypeCoverage" (id)
);CREATE INDEX "ix_Term_id" ON "Term" (id);
CREATE TABLE "Study" (
	context_of_use TEXT,
	biological_context TEXT,
	perturbations TEXT,
	endpoints TEXT,
	plan_comparators TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	"Dataset_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Study_id" ON "Study" (id);
CREATE TABLE "ModelSystem" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	"Dataset_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_ModelSystem_id" ON "ModelSystem" (id);
CREATE TABLE "AnimalModel" (
	species TEXT NOT NULL,
	strain TEXT,
	age TEXT,
	environment TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(species) REFERENCES "Term" (id),
	FOREIGN KEY(strain) REFERENCES "Term" (id),
	FOREIGN KEY(age) REFERENCES "Term" (id),
	FOREIGN KEY(environment) REFERENCES "Term" (id)
);CREATE INDEX "ix_AnimalModel_id" ON "AnimalModel" (id);
CREATE TABLE "MicrophysiologicalSystem" (
	perfusion_system TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	microfluidic_design_id TEXT,
	mechanical_forces_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(microfluidic_design_id) REFERENCES "MicrofluidicDesign" (id),
	FOREIGN KEY(mechanical_forces_id) REFERENCES "MechanicalStimulation" (id)
);CREATE INDEX "ix_MicrophysiologicalSystem_id" ON "MicrophysiologicalSystem" (id);
CREATE TABLE "TissueOnChip" (
	tissue_architecture TEXT,
	perfusion_system TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	tissue_modeled_id TEXT,
	microfluidic_design_id TEXT,
	mechanical_forces_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(tissue_modeled_id) REFERENCES "Term" (id),
	FOREIGN KEY(microfluidic_design_id) REFERENCES "MicrofluidicDesign" (id),
	FOREIGN KEY(mechanical_forces_id) REFERENCES "MechanicalStimulation" (id)
);CREATE INDEX "ix_TissueOnChip_id" ON "TissueOnChip" (id);
CREATE TABLE "QSARModel" (
	activity_endpoint TEXT,
	training_dataset_size INTEGER,
	computational_method TEXT,
	software_platform TEXT,
	prediction_scope TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	model_performance_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(model_performance_id) REFERENCES "ModelPerformance" (id)
);CREATE INDEX "ix_QSARModel_id" ON "QSARModel" (id);
CREATE TABLE "PBPKModel" (
	computational_method TEXT,
	software_platform TEXT,
	prediction_scope TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	species_modeled_id TEXT,
	drug_properties_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(species_modeled_id) REFERENCES "Term" (id),
	FOREIGN KEY(drug_properties_id) REFERENCES "DrugProperties" (id)
);CREATE INDEX "ix_PBPKModel_id" ON "PBPKModel" (id);
CREATE TABLE "MLModel" (
	ml_algorithm VARCHAR(22),
	training_data_size INTEGER,
	model_interpretability VARCHAR(13),
	computational_method TEXT,
	software_platform TEXT,
	prediction_scope TEXT,
	biological_organization_level VARCHAR(21),
	spatial_context TEXT,
	complexity_level VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	cross_validation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(cross_validation_id) REFERENCES "CrossValidation" (id)
);CREATE INDEX "ix_MLModel_id" ON "MLModel" (id);
CREATE TABLE "CellRatio" (
	id INTEGER NOT NULL,
	ratio FLOAT,
	ratio_type VARCHAR(10),
	"CoCulture_id" TEXT,
	cell_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CoCulture_id") REFERENCES "CoCulture" (id),
	FOREIGN KEY(cell_type_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_CellRatio_id" ON "CellRatio" (id);
CREATE TABLE "MolecularSimilarity" (
	similarity_score FLOAT,
	correlation_coefficient FLOAT,
	methodology TEXT,
	data_source TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	statistical_significance_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(statistical_significance_id) REFERENCES "StatisticalSignificance" (id)
);CREATE INDEX "ix_MolecularSimilarity_id" ON "MolecularSimilarity" (id);
CREATE TABLE "FunctionalParity" (
	functional_similarity_score FLOAT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	dose_response_similarity_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(dose_response_similarity_id) REFERENCES "DoseResponseSimilarity" (id)
);CREATE INDEX "ix_FunctionalParity_id" ON "FunctionalParity" (id);
CREATE TABLE "Pathway" (
	pathway_database TEXT,
	pathway_id TEXT,
	activity_score FLOAT,
	enrichment_score FLOAT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	"PathwayConcordance_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PathwayConcordance_id") REFERENCES "PathwayConcordance" (id)
);CREATE INDEX "ix_Pathway_id" ON "Pathway" (id);
CREATE TABLE "EnrichmentStatistics" (
	id INTEGER NOT NULL,
	enrichment_score FLOAT,
	p_value FLOAT,
	q_value FLOAT,
	genes_in_pathway INTEGER,
	genes_in_dataset INTEGER,
	"PathwayConcordance_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PathwayConcordance_id") REFERENCES "PathwayConcordance" (id)
);CREATE INDEX "ix_EnrichmentStatistics_id" ON "EnrichmentStatistics" (id);
CREATE TABLE "CellTypeProportion" (
	id INTEGER NOT NULL,
	model_proportion FLOAT,
	biological_proportion FLOAT,
	proportion_ratio FLOAT,
	"CellTypeCoverage_id" TEXT,
	cell_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CellTypeCoverage_id") REFERENCES "CellTypeCoverage" (id),
	FOREIGN KEY(cell_type_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_CellTypeProportion_id" ON "CellTypeProportion" (id);
CREATE TABLE "QualityControlMetric" (
	id INTEGER NOT NULL,
	metric_name TEXT,
	metric_value FLOAT,
	threshold FLOAT,
	pass_fail_status BOOLEAN,
	"Reproducibility_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Reproducibility_id") REFERENCES "Reproducibility" (id)
);CREATE INDEX "ix_QualityControlMetric_id" ON "QualityControlMetric" (id);
CREATE TABLE "CoCulture_interaction_mechanisms" (
	"CoCulture_id" TEXT,
	interaction_mechanisms TEXT,
	PRIMARY KEY ("CoCulture_id", interaction_mechanisms),
	FOREIGN KEY("CoCulture_id") REFERENCES "CoCulture" (id)
);CREATE INDEX "ix_CoCulture_interaction_mechanisms_CoCulture_id" ON "CoCulture_interaction_mechanisms" ("CoCulture_id");CREATE INDEX "ix_CoCulture_interaction_mechanisms_interaction_mechanisms" ON "CoCulture_interaction_mechanisms" (interaction_mechanisms);
CREATE TABLE "OrganOnChip_sensor_integration" (
	"OrganOnChip_id" TEXT,
	sensor_integration VARCHAR(15),
	PRIMARY KEY ("OrganOnChip_id", sensor_integration),
	FOREIGN KEY("OrganOnChip_id") REFERENCES "OrganOnChip" (id)
);CREATE INDEX "ix_OrganOnChip_sensor_integration_sensor_integration" ON "OrganOnChip_sensor_integration" (sensor_integration);CREATE INDEX "ix_OrganOnChip_sensor_integration_OrganOnChip_id" ON "OrganOnChip_sensor_integration" ("OrganOnChip_id");
CREATE TABLE "InSilicoModel_validation_datasets" (
	"InSilicoModel_id" TEXT,
	validation_datasets TEXT,
	PRIMARY KEY ("InSilicoModel_id", validation_datasets),
	FOREIGN KEY("InSilicoModel_id") REFERENCES "InSilicoModel" (id)
);CREATE INDEX "ix_InSilicoModel_validation_datasets_InSilicoModel_id" ON "InSilicoModel_validation_datasets" ("InSilicoModel_id");CREATE INDEX "ix_InSilicoModel_validation_datasets_validation_datasets" ON "InSilicoModel_validation_datasets" (validation_datasets);
CREATE TABLE "DigitalTwin_real_time_data_sources" (
	"DigitalTwin_id" TEXT,
	real_time_data_sources TEXT,
	PRIMARY KEY ("DigitalTwin_id", real_time_data_sources),
	FOREIGN KEY("DigitalTwin_id") REFERENCES "DigitalTwin" (id)
);CREATE INDEX "ix_DigitalTwin_real_time_data_sources_DigitalTwin_id" ON "DigitalTwin_real_time_data_sources" ("DigitalTwin_id");CREATE INDEX "ix_DigitalTwin_real_time_data_sources_real_time_data_sources" ON "DigitalTwin_real_time_data_sources" (real_time_data_sources);
CREATE TABLE "DigitalTwin_personalization_parameters" (
	"DigitalTwin_id" TEXT,
	personalization_parameters TEXT,
	PRIMARY KEY ("DigitalTwin_id", personalization_parameters),
	FOREIGN KEY("DigitalTwin_id") REFERENCES "DigitalTwin" (id)
);CREATE INDEX "ix_DigitalTwin_personalization_parameters_DigitalTwin_id" ON "DigitalTwin_personalization_parameters" ("DigitalTwin_id");CREATE INDEX "ix_DigitalTwin_personalization_parameters_personalization_parameters" ON "DigitalTwin_personalization_parameters" (personalization_parameters);
CREATE TABLE "DigitalTwin_validation_datasets" (
	"DigitalTwin_id" TEXT,
	validation_datasets TEXT,
	PRIMARY KEY ("DigitalTwin_id", validation_datasets),
	FOREIGN KEY("DigitalTwin_id") REFERENCES "DigitalTwin" (id)
);CREATE INDEX "ix_DigitalTwin_validation_datasets_validation_datasets" ON "DigitalTwin_validation_datasets" (validation_datasets);CREATE INDEX "ix_DigitalTwin_validation_datasets_DigitalTwin_id" ON "DigitalTwin_validation_datasets" ("DigitalTwin_id");
CREATE TABLE "MetabolicModel_validation_datasets" (
	"MetabolicModel_id" TEXT,
	validation_datasets TEXT,
	PRIMARY KEY ("MetabolicModel_id", validation_datasets),
	FOREIGN KEY("MetabolicModel_id") REFERENCES "MetabolicModel" (id)
);CREATE INDEX "ix_MetabolicModel_validation_datasets_MetabolicModel_id" ON "MetabolicModel_validation_datasets" ("MetabolicModel_id");CREATE INDEX "ix_MetabolicModel_validation_datasets_validation_datasets" ON "MetabolicModel_validation_datasets" (validation_datasets);
CREATE TABLE "MicrofluidicDesign_channel_configuration" (
	"MicrofluidicDesign_id" TEXT,
	channel_configuration VARCHAR(10),
	PRIMARY KEY ("MicrofluidicDesign_id", channel_configuration),
	FOREIGN KEY("MicrofluidicDesign_id") REFERENCES "MicrofluidicDesign" (id)
);CREATE INDEX "ix_MicrofluidicDesign_channel_configuration_channel_configuration" ON "MicrofluidicDesign_channel_configuration" (channel_configuration);CREATE INDEX "ix_MicrofluidicDesign_channel_configuration_MicrofluidicDesign_id" ON "MicrofluidicDesign_channel_configuration" ("MicrofluidicDesign_id");
CREATE TABLE "MicrofluidicDesign_interface_type" (
	"MicrofluidicDesign_id" TEXT,
	interface_type VARCHAR(19),
	PRIMARY KEY ("MicrofluidicDesign_id", interface_type),
	FOREIGN KEY("MicrofluidicDesign_id") REFERENCES "MicrofluidicDesign" (id)
);CREATE INDEX "ix_MicrofluidicDesign_interface_type_interface_type" ON "MicrofluidicDesign_interface_type" (interface_type);CREATE INDEX "ix_MicrofluidicDesign_interface_type_MicrofluidicDesign_id" ON "MicrofluidicDesign_interface_type" ("MicrofluidicDesign_id");
CREATE TABLE "MicrofluidicDesign_channel_dimensions" (
	"MicrofluidicDesign_id" TEXT,
	channel_dimensions_id INTEGER,
	PRIMARY KEY ("MicrofluidicDesign_id", channel_dimensions_id),
	FOREIGN KEY("MicrofluidicDesign_id") REFERENCES "MicrofluidicDesign" (id),
	FOREIGN KEY(channel_dimensions_id) REFERENCES "ChannelDimensions" (id)
);CREATE INDEX "ix_MicrofluidicDesign_channel_dimensions_MicrofluidicDesign_id" ON "MicrofluidicDesign_channel_dimensions" ("MicrofluidicDesign_id");CREATE INDEX "ix_MicrofluidicDesign_channel_dimensions_channel_dimensions_id" ON "MicrofluidicDesign_channel_dimensions" (channel_dimensions_id);
CREATE TABLE "MicrofluidicDesign_material" (
	"MicrofluidicDesign_id" TEXT,
	material VARCHAR(13),
	PRIMARY KEY ("MicrofluidicDesign_id", material),
	FOREIGN KEY("MicrofluidicDesign_id") REFERENCES "MicrofluidicDesign" (id)
);CREATE INDEX "ix_MicrofluidicDesign_material_MicrofluidicDesign_id" ON "MicrofluidicDesign_material" ("MicrofluidicDesign_id");CREATE INDEX "ix_MicrofluidicDesign_material_material" ON "MicrofluidicDesign_material" (material);
CREATE TABLE "MicrofluidicDesign_surface_treatment" (
	"MicrofluidicDesign_id" TEXT,
	surface_treatment VARCHAR(13),
	PRIMARY KEY ("MicrofluidicDesign_id", surface_treatment),
	FOREIGN KEY("MicrofluidicDesign_id") REFERENCES "MicrofluidicDesign" (id)
);CREATE INDEX "ix_MicrofluidicDesign_surface_treatment_MicrofluidicDesign_id" ON "MicrofluidicDesign_surface_treatment" ("MicrofluidicDesign_id");CREATE INDEX "ix_MicrofluidicDesign_surface_treatment_surface_treatment" ON "MicrofluidicDesign_surface_treatment" (surface_treatment);
CREATE TABLE "MicrofluidicDesign_flow_control_method" (
	"MicrofluidicDesign_id" TEXT,
	flow_control_method VARCHAR(16),
	PRIMARY KEY ("MicrofluidicDesign_id", flow_control_method),
	FOREIGN KEY("MicrofluidicDesign_id") REFERENCES "MicrofluidicDesign" (id)
);CREATE INDEX "ix_MicrofluidicDesign_flow_control_method_MicrofluidicDesign_id" ON "MicrofluidicDesign_flow_control_method" ("MicrofluidicDesign_id");CREATE INDEX "ix_MicrofluidicDesign_flow_control_method_flow_control_method" ON "MicrofluidicDesign_flow_control_method" (flow_control_method);
CREATE TABLE "MicrofluidicDesign_sensors_integrated" (
	"MicrofluidicDesign_id" TEXT,
	sensors_integrated VARCHAR(15),
	PRIMARY KEY ("MicrofluidicDesign_id", sensors_integrated),
	FOREIGN KEY("MicrofluidicDesign_id") REFERENCES "MicrofluidicDesign" (id)
);CREATE INDEX "ix_MicrofluidicDesign_sensors_integrated_MicrofluidicDesign_id" ON "MicrofluidicDesign_sensors_integrated" ("MicrofluidicDesign_id");CREATE INDEX "ix_MicrofluidicDesign_sensors_integrated_sensors_integrated" ON "MicrofluidicDesign_sensors_integrated" (sensors_integrated);
CREATE TABLE "MicrofluidicDesign_special_features" (
	"MicrofluidicDesign_id" TEXT,
	special_features TEXT,
	PRIMARY KEY ("MicrofluidicDesign_id", special_features),
	FOREIGN KEY("MicrofluidicDesign_id") REFERENCES "MicrofluidicDesign" (id)
);CREATE INDEX "ix_MicrofluidicDesign_special_features_special_features" ON "MicrofluidicDesign_special_features" (special_features);CREATE INDEX "ix_MicrofluidicDesign_special_features_MicrofluidicDesign_id" ON "MicrofluidicDesign_special_features" ("MicrofluidicDesign_id");
CREATE TABLE "MechanicalStimulation_stimulation_type" (
	"MechanicalStimulation_id" TEXT,
	stimulation_type VARCHAR(20),
	PRIMARY KEY ("MechanicalStimulation_id", stimulation_type),
	FOREIGN KEY("MechanicalStimulation_id") REFERENCES "MechanicalStimulation" (id)
);CREATE INDEX "ix_MechanicalStimulation_stimulation_type_MechanicalStimulation_id" ON "MechanicalStimulation_stimulation_type" ("MechanicalStimulation_id");CREATE INDEX "ix_MechanicalStimulation_stimulation_type_stimulation_type" ON "MechanicalStimulation_stimulation_type" (stimulation_type);
CREATE TABLE "PBPKCompartment" (
	compartment_type VARCHAR(8),
	volume FLOAT,
	blood_flow FLOAT,
	partition_coefficient FLOAT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	"PBPKModel_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PBPKModel_id") REFERENCES "PBPKModel" (id)
);CREATE INDEX "ix_PBPKCompartment_id" ON "PBPKCompartment" (id);
CREATE TABLE "StructuredConcordanceResult" (
	id INTEGER NOT NULL,
	molecular_similarity_id TEXT,
	pathway_concordance_id TEXT,
	phenotype_overlap_id TEXT,
	cell_type_coverage_id TEXT,
	functional_parity_id TEXT,
	reproducibility_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(molecular_similarity_id) REFERENCES "MolecularSimilarity" (id),
	FOREIGN KEY(pathway_concordance_id) REFERENCES "PathwayConcordance" (id),
	FOREIGN KEY(phenotype_overlap_id) REFERENCES "PhenotypeOverlap" (id),
	FOREIGN KEY(cell_type_coverage_id) REFERENCES "CellTypeCoverage" (id),
	FOREIGN KEY(functional_parity_id) REFERENCES "FunctionalParity" (id),
	FOREIGN KEY(reproducibility_id) REFERENCES "Reproducibility" (id)
);CREATE INDEX "ix_StructuredConcordanceResult_id" ON "StructuredConcordanceResult" (id);
CREATE TABLE "Gene" (
	gene_symbol TEXT,
	ensembl_id TEXT,
	entrez_id INTEGER,
	fold_change FLOAT,
	p_value FLOAT,
	adjusted_p_value FLOAT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	"MolecularSimilarity_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("MolecularSimilarity_id") REFERENCES "MolecularSimilarity" (id)
);CREATE INDEX "ix_Gene_id" ON "Gene" (id);
CREATE TABLE "FunctionalAssay" (
	assay_type TEXT,
	assay_result FLOAT,
	reference_value FLOAT,
	units TEXT,
	methodology TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	"FunctionalParity_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("FunctionalParity_id") REFERENCES "FunctionalParity" (id)
);CREATE INDEX "ix_FunctionalAssay_id" ON "FunctionalAssay" (id);
CREATE TABLE "Reference" (
	id TEXT NOT NULL,
	title TEXT NOT NULL,
	journal TEXT,
	year INTEGER,
	url TEXT,
	"NAMModel_id" TEXT,
	"CellularSystem_id" TEXT,
	"TwoDCellCulture_id" TEXT,
	"ThreeDCellCulture_id" TEXT,
	"CoCulture_id" TEXT,
	"Organoid_id" TEXT,
	"CellLineModel_id" TEXT,
	"MicrophysiologicalSystem_id" TEXT,
	"OrganOnChip_id" TEXT,
	"TissueOnChip_id" TEXT,
	"InSilicoModel_id" TEXT,
	"QSARModel_id" TEXT,
	"PBPKModel_id" TEXT,
	"DigitalTwin_id" TEXT,
	"MLModel_id" TEXT,
	"MetabolicModel_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NAMModel_id") REFERENCES "NAMModel" (id),
	FOREIGN KEY("CellularSystem_id") REFERENCES "CellularSystem" (id),
	FOREIGN KEY("TwoDCellCulture_id") REFERENCES "TwoDCellCulture" (id),
	FOREIGN KEY("ThreeDCellCulture_id") REFERENCES "ThreeDCellCulture" (id),
	FOREIGN KEY("CoCulture_id") REFERENCES "CoCulture" (id),
	FOREIGN KEY("Organoid_id") REFERENCES "Organoid" (id),
	FOREIGN KEY("CellLineModel_id") REFERENCES "CellLineModel" (id),
	FOREIGN KEY("MicrophysiologicalSystem_id") REFERENCES "MicrophysiologicalSystem" (id),
	FOREIGN KEY("OrganOnChip_id") REFERENCES "OrganOnChip" (id),
	FOREIGN KEY("TissueOnChip_id") REFERENCES "TissueOnChip" (id),
	FOREIGN KEY("InSilicoModel_id") REFERENCES "InSilicoModel" (id),
	FOREIGN KEY("QSARModel_id") REFERENCES "QSARModel" (id),
	FOREIGN KEY("PBPKModel_id") REFERENCES "PBPKModel" (id),
	FOREIGN KEY("DigitalTwin_id") REFERENCES "DigitalTwin" (id),
	FOREIGN KEY("MLModel_id") REFERENCES "MLModel" (id),
	FOREIGN KEY("MetabolicModel_id") REFERENCES "MetabolicModel" (id)
);CREATE INDEX "ix_Reference_id" ON "Reference" (id);
CREATE TABLE "MicrophysiologicalSystem_sensor_integration" (
	"MicrophysiologicalSystem_id" TEXT,
	sensor_integration VARCHAR(15),
	PRIMARY KEY ("MicrophysiologicalSystem_id", sensor_integration),
	FOREIGN KEY("MicrophysiologicalSystem_id") REFERENCES "MicrophysiologicalSystem" (id)
);CREATE INDEX "ix_MicrophysiologicalSystem_sensor_integration_sensor_integration" ON "MicrophysiologicalSystem_sensor_integration" (sensor_integration);CREATE INDEX "ix_MicrophysiologicalSystem_sensor_integration_MicrophysiologicalSystem_id" ON "MicrophysiologicalSystem_sensor_integration" ("MicrophysiologicalSystem_id");
CREATE TABLE "TissueOnChip_barrier_functions" (
	"TissueOnChip_id" TEXT,
	barrier_functions TEXT,
	PRIMARY KEY ("TissueOnChip_id", barrier_functions),
	FOREIGN KEY("TissueOnChip_id") REFERENCES "TissueOnChip" (id)
);CREATE INDEX "ix_TissueOnChip_barrier_functions_barrier_functions" ON "TissueOnChip_barrier_functions" (barrier_functions);CREATE INDEX "ix_TissueOnChip_barrier_functions_TissueOnChip_id" ON "TissueOnChip_barrier_functions" ("TissueOnChip_id");
CREATE TABLE "TissueOnChip_sensor_integration" (
	"TissueOnChip_id" TEXT,
	sensor_integration VARCHAR(15),
	PRIMARY KEY ("TissueOnChip_id", sensor_integration),
	FOREIGN KEY("TissueOnChip_id") REFERENCES "TissueOnChip" (id)
);CREATE INDEX "ix_TissueOnChip_sensor_integration_TissueOnChip_id" ON "TissueOnChip_sensor_integration" ("TissueOnChip_id");CREATE INDEX "ix_TissueOnChip_sensor_integration_sensor_integration" ON "TissueOnChip_sensor_integration" (sensor_integration);
CREATE TABLE "QSARModel_molecular_descriptors" (
	"QSARModel_id" TEXT,
	molecular_descriptors TEXT,
	PRIMARY KEY ("QSARModel_id", molecular_descriptors),
	FOREIGN KEY("QSARModel_id") REFERENCES "QSARModel" (id)
);CREATE INDEX "ix_QSARModel_molecular_descriptors_molecular_descriptors" ON "QSARModel_molecular_descriptors" (molecular_descriptors);CREATE INDEX "ix_QSARModel_molecular_descriptors_QSARModel_id" ON "QSARModel_molecular_descriptors" ("QSARModel_id");
CREATE TABLE "QSARModel_validation_datasets" (
	"QSARModel_id" TEXT,
	validation_datasets TEXT,
	PRIMARY KEY ("QSARModel_id", validation_datasets),
	FOREIGN KEY("QSARModel_id") REFERENCES "QSARModel" (id)
);CREATE INDEX "ix_QSARModel_validation_datasets_QSARModel_id" ON "QSARModel_validation_datasets" ("QSARModel_id");CREATE INDEX "ix_QSARModel_validation_datasets_validation_datasets" ON "QSARModel_validation_datasets" (validation_datasets);
CREATE TABLE "PBPKModel_elimination_pathways" (
	"PBPKModel_id" TEXT,
	elimination_pathways TEXT,
	PRIMARY KEY ("PBPKModel_id", elimination_pathways),
	FOREIGN KEY("PBPKModel_id") REFERENCES "PBPKModel" (id)
);CREATE INDEX "ix_PBPKModel_elimination_pathways_PBPKModel_id" ON "PBPKModel_elimination_pathways" ("PBPKModel_id");CREATE INDEX "ix_PBPKModel_elimination_pathways_elimination_pathways" ON "PBPKModel_elimination_pathways" (elimination_pathways);
CREATE TABLE "PBPKModel_validation_datasets" (
	"PBPKModel_id" TEXT,
	validation_datasets TEXT,
	PRIMARY KEY ("PBPKModel_id", validation_datasets),
	FOREIGN KEY("PBPKModel_id") REFERENCES "PBPKModel" (id)
);CREATE INDEX "ix_PBPKModel_validation_datasets_validation_datasets" ON "PBPKModel_validation_datasets" (validation_datasets);CREATE INDEX "ix_PBPKModel_validation_datasets_PBPKModel_id" ON "PBPKModel_validation_datasets" ("PBPKModel_id");
CREATE TABLE "MLModel_feature_types" (
	"MLModel_id" TEXT,
	feature_types VARCHAR(14),
	PRIMARY KEY ("MLModel_id", feature_types),
	FOREIGN KEY("MLModel_id") REFERENCES "MLModel" (id)
);CREATE INDEX "ix_MLModel_feature_types_MLModel_id" ON "MLModel_feature_types" ("MLModel_id");CREATE INDEX "ix_MLModel_feature_types_feature_types" ON "MLModel_feature_types" (feature_types);
CREATE TABLE "MLModel_validation_datasets" (
	"MLModel_id" TEXT,
	validation_datasets TEXT,
	PRIMARY KEY ("MLModel_id", validation_datasets),
	FOREIGN KEY("MLModel_id") REFERENCES "MLModel" (id)
);CREATE INDEX "ix_MLModel_validation_datasets_MLModel_id" ON "MLModel_validation_datasets" ("MLModel_id");CREATE INDEX "ix_MLModel_validation_datasets_validation_datasets" ON "MLModel_validation_datasets" (validation_datasets);
CREATE TABLE "FunctionalParity_conserved_functions" (
	"FunctionalParity_id" TEXT,
	conserved_functions TEXT,
	PRIMARY KEY ("FunctionalParity_id", conserved_functions),
	FOREIGN KEY("FunctionalParity_id") REFERENCES "FunctionalParity" (id)
);CREATE INDEX "ix_FunctionalParity_conserved_functions_conserved_functions" ON "FunctionalParity_conserved_functions" (conserved_functions);CREATE INDEX "ix_FunctionalParity_conserved_functions_FunctionalParity_id" ON "FunctionalParity_conserved_functions" ("FunctionalParity_id");
CREATE TABLE "FunctionalParity_impaired_functions" (
	"FunctionalParity_id" TEXT,
	impaired_functions TEXT,
	PRIMARY KEY ("FunctionalParity_id", impaired_functions),
	FOREIGN KEY("FunctionalParity_id") REFERENCES "FunctionalParity" (id)
);CREATE INDEX "ix_FunctionalParity_impaired_functions_impaired_functions" ON "FunctionalParity_impaired_functions" (impaired_functions);CREATE INDEX "ix_FunctionalParity_impaired_functions_FunctionalParity_id" ON "FunctionalParity_impaired_functions" ("FunctionalParity_id");
CREATE TABLE "ModelsRelationship" (
	id INTEGER NOT NULL,
	biological_system_modeled TEXT,
	is_computed BOOLEAN,
	concordance_id INTEGER,
	structured_concordance_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(biological_system_modeled) REFERENCES "BiologicalSystem" (id),
	FOREIGN KEY(concordance_id) REFERENCES "ConcordanceResult" (id),
	FOREIGN KEY(structured_concordance_id) REFERENCES "StructuredConcordanceResult" (id)
);CREATE INDEX "ix_ModelsRelationship_id" ON "ModelsRelationship" (id);
CREATE TABLE "Reference_authors" (
	"Reference_id" TEXT,
	authors TEXT,
	PRIMARY KEY ("Reference_id", authors),
	FOREIGN KEY("Reference_id") REFERENCES "Reference" (id)
);CREATE INDEX "ix_Reference_authors_authors" ON "Reference_authors" (authors);CREATE INDEX "ix_Reference_authors_Reference_id" ON "Reference_authors" ("Reference_id");
CREATE TABLE "ModelSystem_models" (
	"ModelSystem_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("ModelSystem_id", models_id),
	FOREIGN KEY("ModelSystem_id") REFERENCES "ModelSystem" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_ModelSystem_models_ModelSystem_id" ON "ModelSystem_models" ("ModelSystem_id");CREATE INDEX "ix_ModelSystem_models_models_id" ON "ModelSystem_models" (models_id);
CREATE TABLE "AnimalModel_models" (
	"AnimalModel_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("AnimalModel_id", models_id),
	FOREIGN KEY("AnimalModel_id") REFERENCES "AnimalModel" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_AnimalModel_models_models_id" ON "AnimalModel_models" (models_id);CREATE INDEX "ix_AnimalModel_models_AnimalModel_id" ON "AnimalModel_models" ("AnimalModel_id");
CREATE TABLE "NAMModel_models" (
	"NAMModel_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("NAMModel_id", models_id),
	FOREIGN KEY("NAMModel_id") REFERENCES "NAMModel" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_NAMModel_models_models_id" ON "NAMModel_models" (models_id);CREATE INDEX "ix_NAMModel_models_NAMModel_id" ON "NAMModel_models" ("NAMModel_id");
CREATE TABLE "CellularSystem_models" (
	"CellularSystem_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("CellularSystem_id", models_id),
	FOREIGN KEY("CellularSystem_id") REFERENCES "CellularSystem" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_CellularSystem_models_models_id" ON "CellularSystem_models" (models_id);CREATE INDEX "ix_CellularSystem_models_CellularSystem_id" ON "CellularSystem_models" ("CellularSystem_id");
CREATE TABLE "TwoDCellCulture_models" (
	"TwoDCellCulture_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("TwoDCellCulture_id", models_id),
	FOREIGN KEY("TwoDCellCulture_id") REFERENCES "TwoDCellCulture" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_TwoDCellCulture_models_TwoDCellCulture_id" ON "TwoDCellCulture_models" ("TwoDCellCulture_id");CREATE INDEX "ix_TwoDCellCulture_models_models_id" ON "TwoDCellCulture_models" (models_id);
CREATE TABLE "ThreeDCellCulture_models" (
	"ThreeDCellCulture_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("ThreeDCellCulture_id", models_id),
	FOREIGN KEY("ThreeDCellCulture_id") REFERENCES "ThreeDCellCulture" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_ThreeDCellCulture_models_models_id" ON "ThreeDCellCulture_models" (models_id);CREATE INDEX "ix_ThreeDCellCulture_models_ThreeDCellCulture_id" ON "ThreeDCellCulture_models" ("ThreeDCellCulture_id");
CREATE TABLE "CoCulture_models" (
	"CoCulture_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("CoCulture_id", models_id),
	FOREIGN KEY("CoCulture_id") REFERENCES "CoCulture" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_CoCulture_models_CoCulture_id" ON "CoCulture_models" ("CoCulture_id");CREATE INDEX "ix_CoCulture_models_models_id" ON "CoCulture_models" (models_id);
CREATE TABLE "Organoid_models" (
	"Organoid_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("Organoid_id", models_id),
	FOREIGN KEY("Organoid_id") REFERENCES "Organoid" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_Organoid_models_Organoid_id" ON "Organoid_models" ("Organoid_id");CREATE INDEX "ix_Organoid_models_models_id" ON "Organoid_models" (models_id);
CREATE TABLE "CellLineModel_models" (
	"CellLineModel_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("CellLineModel_id", models_id),
	FOREIGN KEY("CellLineModel_id") REFERENCES "CellLineModel" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_CellLineModel_models_CellLineModel_id" ON "CellLineModel_models" ("CellLineModel_id");CREATE INDEX "ix_CellLineModel_models_models_id" ON "CellLineModel_models" (models_id);
CREATE TABLE "MicrophysiologicalSystem_models" (
	"MicrophysiologicalSystem_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("MicrophysiologicalSystem_id", models_id),
	FOREIGN KEY("MicrophysiologicalSystem_id") REFERENCES "MicrophysiologicalSystem" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_MicrophysiologicalSystem_models_models_id" ON "MicrophysiologicalSystem_models" (models_id);CREATE INDEX "ix_MicrophysiologicalSystem_models_MicrophysiologicalSystem_id" ON "MicrophysiologicalSystem_models" ("MicrophysiologicalSystem_id");
CREATE TABLE "OrganOnChip_models" (
	"OrganOnChip_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("OrganOnChip_id", models_id),
	FOREIGN KEY("OrganOnChip_id") REFERENCES "OrganOnChip" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_OrganOnChip_models_models_id" ON "OrganOnChip_models" (models_id);CREATE INDEX "ix_OrganOnChip_models_OrganOnChip_id" ON "OrganOnChip_models" ("OrganOnChip_id");
CREATE TABLE "TissueOnChip_models" (
	"TissueOnChip_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("TissueOnChip_id", models_id),
	FOREIGN KEY("TissueOnChip_id") REFERENCES "TissueOnChip" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_TissueOnChip_models_models_id" ON "TissueOnChip_models" (models_id);CREATE INDEX "ix_TissueOnChip_models_TissueOnChip_id" ON "TissueOnChip_models" ("TissueOnChip_id");
CREATE TABLE "InSilicoModel_models" (
	"InSilicoModel_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("InSilicoModel_id", models_id),
	FOREIGN KEY("InSilicoModel_id") REFERENCES "InSilicoModel" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_InSilicoModel_models_InSilicoModel_id" ON "InSilicoModel_models" ("InSilicoModel_id");CREATE INDEX "ix_InSilicoModel_models_models_id" ON "InSilicoModel_models" (models_id);
CREATE TABLE "QSARModel_models" (
	"QSARModel_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("QSARModel_id", models_id),
	FOREIGN KEY("QSARModel_id") REFERENCES "QSARModel" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_QSARModel_models_QSARModel_id" ON "QSARModel_models" ("QSARModel_id");CREATE INDEX "ix_QSARModel_models_models_id" ON "QSARModel_models" (models_id);
CREATE TABLE "PBPKModel_models" (
	"PBPKModel_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("PBPKModel_id", models_id),
	FOREIGN KEY("PBPKModel_id") REFERENCES "PBPKModel" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_PBPKModel_models_PBPKModel_id" ON "PBPKModel_models" ("PBPKModel_id");CREATE INDEX "ix_PBPKModel_models_models_id" ON "PBPKModel_models" (models_id);
CREATE TABLE "DigitalTwin_models" (
	"DigitalTwin_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("DigitalTwin_id", models_id),
	FOREIGN KEY("DigitalTwin_id") REFERENCES "DigitalTwin" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_DigitalTwin_models_DigitalTwin_id" ON "DigitalTwin_models" ("DigitalTwin_id");CREATE INDEX "ix_DigitalTwin_models_models_id" ON "DigitalTwin_models" (models_id);
CREATE TABLE "MLModel_models" (
	"MLModel_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("MLModel_id", models_id),
	FOREIGN KEY("MLModel_id") REFERENCES "MLModel" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_MLModel_models_models_id" ON "MLModel_models" (models_id);CREATE INDEX "ix_MLModel_models_MLModel_id" ON "MLModel_models" ("MLModel_id");
CREATE TABLE "MetabolicModel_models" (
	"MetabolicModel_id" TEXT,
	models_id INTEGER,
	PRIMARY KEY ("MetabolicModel_id", models_id),
	FOREIGN KEY("MetabolicModel_id") REFERENCES "MetabolicModel" (id),
	FOREIGN KEY(models_id) REFERENCES "ModelsRelationship" (id)
);CREATE INDEX "ix_MetabolicModel_models_MetabolicModel_id" ON "MetabolicModel_models" ("MetabolicModel_id");CREATE INDEX "ix_MetabolicModel_models_models_id" ON "MetabolicModel_models" (models_id);
