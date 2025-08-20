# NAMO Ontology Mapping Strategy

## Overview

This document outlines the strategic approach for integrating ontology terms into the NAMO schema enums. Based on analysis of the current schema and research into LinkML best practices, we propose a systematic migration from static permissible values to dynamic ontology-backed enumerations.

## Strategic Approach

### Big Picture Goals

1. **Maximize FAIR principles**: Make data more Findable, Accessible, Interoperable, and Reusable
2. **Leverage existing standards**: Use established ontologies where appropriate rather than creating custom vocabularies
3. **Maintain schema usability**: Ensure changes don't break existing functionality or user workflows
4. **Enable semantic reasoning**: Allow for ontology-driven validation and inference
5. **Phased implementation**: Roll out changes incrementally to minimize disruption

### Implementation Philosophy

**Single Ontology Sources** (Preferred): Where a well-established ontology covers the entire concept space
- Examples: Cell types (CL), Anatomy/Organs (UBERON), Species (NCBITaxon)
- Strategy: Use `reachable_from` with appropriate source nodes

**Multiple Ontology Sources** (When necessary): Where no single ontology covers the full domain
- Examples: Machine learning algorithms, microfluidic components
- Strategy: Combine ontologies using boolean expressions or create curated value sets

**Custom Controlled Vocabularies** (Last resort): Where no suitable ontologies exist
- Examples: Highly domain-specific technical specifications
- Strategy: Keep as static enums but enhance with ontology mappings where possible

## Detailed Mapping Plan

### Category 1: Strong Ontology Candidates (High Priority)

These enums have clear, well-established ontology mappings and should be converted first:

#### SpeciesEnum → NCBITaxon
- **Current status**: Already configured with `reachable_from`
- **Source**: NCBITaxon:1 (root)
- **Action**: ✓ Already implemented correctly

#### CellTypeEnum → Cell Ontology (CL)
- **Current status**: Already configured with `reachable_from`
- **Source**: CL:0000000 (cell)
- **Action**: ✓ Already implemented correctly

#### OrganEnum → UBERON
- **Current status**: Already configured with `reachable_from`
- **Source**: UBERON:0001062 (anatomical entity)
- **Action**: ✓ Already implemented correctly

#### StudyDesignEnum → OBI
- **Current status**: Already configured with `reachable_from`
- **Source**: OBI:0500000 (study design)
- **Action**: ✓ Already implemented correctly

#### InvestigativeProtocolEnum → OBI
- **Current status**: Already configured with `reachable_from`
- **Source**: OBI:0000272 (protocol)
- **Action**: ✓ Already implemented correctly

#### SampleProcessingEnum → OBI
- **Current status**: Already configured with `reachable_from`
- **Source**: OBI:0000094 (material processing)
- **Action**: ✓ Already implemented correctly

### Category 2: Moderate Ontology Candidates (Medium Priority)

These enums have some ontological support but may require more complex mappings:

#### MLAlgorithmEnum → Multiple Sources
- **Primary source**: OBI (machine learning processes)
- **Secondary**: EDAM, NCIT for specific algorithms
- **Mapping strategy**: Use OBI:0002587 (machine learning) as base, expand with specific algorithm terms
- **Recommended terms**:
  - Random Forest → OBI:0002846 (random forest algorithm) [if exists]
  - Neural Network → NCIT:C176231 subset
  - Support Vector Machine → Use EDAM or create mapping

#### CrossValidationMethodEnum → OBI
- **Source**: OBI statistical analysis methods
- **Base term**: Found OBI:0200033 (leave one out cross validation method)
- **Strategy**: Expand to include k-fold, stratified methods
- **Action needed**: Research more OBI terms for cross-validation methods

#### FeatureTypeEnum → Multiple Sources
- **Sources**: EDAM (bioinformatics data types), OBI (data types)
- **Strategy**: Map to appropriate data type ontologies
- **Examples**:
  - GENOMIC → EDAM:topic_0622 (genomics)
  - TRANSCRIPTOMIC → EDAM:topic_3308 (transcriptomics)
  - PROTEOMIC → EDAM:topic_0121 (proteomics)

#### PBPKCompartmentEnum → Multiple Sources
- **Primary**: UBERON for anatomical compartments
- **Secondary**: CHEBI for chemical compartments (plasma, blood)
- **Strategy**: Create composite enum with anatomy + chemistry terms
- **Examples**:
  - LIVER → UBERON:0002107
  - KIDNEY → UBERON:0002113
  - PLASMA → CHEBI:60425

### Category 3: Technical/Domain-Specific Enums (Lower Priority)

These enums represent technical specifications with limited ontology coverage:

#### Microfluidics-Related Enums
- **Coverage**: Limited ontology support found
- **Strategy**: Keep as controlled vocabularies, add ontology mappings where available
- **Enums affected**:
  - MicrofluidicArchitectureEnum
  - ChannelConfigurationEnum
  - MembraneTypeEnum
  - DeviceMaterialEnum
  - FlowControlMethodEnum

#### BiologicalOrganizationLevelEnum
- **Potential source**: Some GO terms for organization levels
- **Strategy**: Map to appropriate GO cellular component organization terms
- **Base**: GO:0016043 (cellular component organization)

#### ComplexityLevelEnum
- **Status**: Likely custom vocabulary
- **Strategy**: Keep as-is, potentially add PATO mappings for complexity qualities

### Category 4: Well-Defined Static Enums (Maintain As-Is)

These enums have clear, stable value sets that don't benefit from ontology integration:

#### CaseOrControlEnum
- **Current mapping**: Already mapped to OBI terms
- **Action**: ✓ Keep current implementation

#### RelativeTimeEnum
- **Nature**: Temporal relationships
- **Action**: Keep as static enum (BEFORE, AFTER, AT_SAME_TIME_AS)

#### PresenceEnum
- **Nature**: Measurement qualifiers
- **Action**: Keep as static enum, potentially add PATO mappings

#### PredictionOutcomeEnum
- **Nature**: Classification outcomes (TP, FP, TN, FN)
- **Action**: Keep as static enum

### Category 5: Undefined/Empty Enums (Needs Research)

These enums are declared but not populated:

#### StrainEnum
- **Current status**: Empty
- **Strategy**: Research strain ontologies (potentially EFO, JAX strains)
- **Action needed**: Define scope and populate with appropriate terms

#### AgeEnum  
- **Current status**: Empty
- **Strategy**: Could use PATO age qualities or developmental stage ontologies
- **Action needed**: Define whether this is chronological age or developmental stage

#### OrganismAgeEnum
- **Current status**: Referenced in bindings but not defined
- **Strategy**: Link to developmental stage ontologies (UBERON, developmental stages)
- **Action needed**: Create enum with appropriate age/stage terms

## Implementation Roadmap

### Phase 1: Validation and Documentation (Weeks 1-2)
1. Validate current `reachable_from` implementations work correctly
2. Test schema generation and validation with existing ontology-backed enums
3. Document current tooling support for dynamic enums

### Phase 2: High-Value Ontology Integration (Weeks 3-4)
1. Implement MLAlgorithmEnum with OBI mappings
2. Add CrossValidationMethodEnum ontology backing
3. Enhance FeatureTypeEnum with EDAM mappings
4. Create PBPKCompartmentEnum with UBERON/CHEBI sources

### Phase 3: Technical Vocabulary Enhancement (Weeks 5-6)
1. Add ontology mappings to microfluidics enums where available
2. Implement BiologicalOrganizationLevelEnum with GO terms
3. Research and populate StrainEnum and AgeEnum

### Phase 4: Validation and Refinement (Weeks 7-8)
1. Test all implementations with example data
2. Validate schema generation across all targets (Python, OWL, JSON Schema)
3. Update documentation and examples
4. Create migration guide for existing data

## LinkML Best Practices Applied

### Dynamic Enum Configuration
```yaml
enums:
  MLAlgorithmEnum:
    reachable_from:
      source_ontology: obo:obi
      source_nodes:
        - OBI:0002587  # machine learning
      include_self: false
      relationship_types:
        - rdfs:subClassOf
```

### Complex Value Set Composition
```yaml
enums:
  PBPKCompartmentEnum:
    description: Physiological compartments in PBPK models
    include:
      - reachable_from:
          source_ontology: obo:uberon
          source_nodes:
            - UBERON:0000062  # organ
      - reachable_from:
          source_ontology: obo:chebi
          source_nodes:
            - CHEBI:60425  # blood plasma
            - CHEBI:3435   # blood
```

### Backward Compatibility
- Keep existing permissible values as comments for reference
- Provide mapping tables from old values to new ontology terms
- Use gradual migration with validation warnings before errors

## Quality Assurance

### Validation Criteria
1. All ontology terms must be resolvable via OLS
2. Schema generation must succeed for all target formats
3. Example data must validate against new constraints
4. Performance impact must be acceptable

### Testing Strategy
1. Unit tests for each modified enum
2. Integration tests with real example data
3. Schema generation tests across all formats
4. Performance benchmarks for validation

## Maintenance Strategy

### Ontology Updates
- Monitor source ontology releases for new relevant terms
- Establish process for reviewing and incorporating ontology updates
- Document version dependencies

### Community Feedback
- Collect feedback from NAMO users on ontology term availability
- Establish process for requesting new terms from upstream ontologies
- Document alternative term suggestions

## Success Metrics

1. **Coverage**: Percentage of enums successfully mapped to ontologies
2. **Usability**: User feedback on term discoverability and appropriateness
3. **Interoperability**: Successful cross-validation with other schemas using same ontologies
4. **Maintenance**: Reduced effort required for vocabulary maintenance

## Conclusion

This strategic approach balances the benefits of ontology integration with practical implementation concerns. By prioritizing high-value, well-supported mappings first, we can achieve significant improvements in semantic interoperability while maintaining schema stability and usability.

The phased approach allows for learning and adjustment while building confidence in the ontology integration approach. Success in the early phases will inform decisions about more complex mappings in later phases.