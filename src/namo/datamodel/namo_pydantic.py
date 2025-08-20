from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'namo',
     'default_range': 'string',
     'description': 'New Approach Methodology Ontology and Schema',
     'id': 'https://w3id.org/monarch-initiative/namo',
     'imports': ['linkml:types'],
     'license': 'BSD-3-Clause',
     'name': 'namo',
     'prefixes': {'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'EDAM': {'prefix_prefix': 'EDAM',
                           'prefix_reference': 'http://edamontology.org/'},
                  'EFO': {'prefix_prefix': 'EFO',
                          'prefix_reference': 'http://www.ebi.ac.uk/efo/EFO_'},
                  'MAMO': {'prefix_prefix': 'MAMO',
                           'prefix_reference': 'http://identifiers.org/mamo/MAMO_'},
                  'MESH': {'prefix_prefix': 'MESH',
                           'prefix_reference': 'http://id.nlm.nih.gov/mesh/'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'namo': {'prefix_prefix': 'namo',
                           'prefix_reference': 'https://w3id.org/monarch-initiative/namo/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://monarch-initiative.github.io/namo'],
     'source_file': 'src/namo/schema/namo.yaml',
     'title': 'namo'} )

class SpeciesEnum(str):
    pass


class OrganEnum(str):
    pass


class CellTypeEnum(str):
    pass


class StrainEnum(str):
    pass


class AgeEnum(str):
    pass


class RelativeTimeEnum(str, Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"


class CaseOrControlEnum(str, Enum):
    case_role_in_case_control_study = "CASE"
    control_role_in_case_control_study = "CONTROL"


class StudyDesignEnum(str):
    pass


class InvestigativeProtocolEnum(str):
    pass


class SampleProcessingEnum(str):
    pass


class PresenceEnum(str, Enum):
    PRESENT = "PRESENT"
    """
    The entity is present
    """
    ABSENT = "ABSENT"
    """
    The entity is absent
    """
    BELOW_DETECTION_LIMIT = "BELOW_DETECTION_LIMIT"
    """
    The entity is below the detection limit
    """
    ABOVE_DETECTION_LIMIT = "ABOVE_DETECTION_LIMIT"
    """
    The entity is above the detection limit
    """


class PredictionOutcomeEnum(str, Enum):
    TP = "TP"
    """
    True Positive
    """
    FP = "FP"
    """
    False Positive
    """
    TN = "TN"
    """
    True Negative
    """
    FN = "FN"
    """
    False Negative
    """


class MicrofluidicArchitectureEnum(str, Enum):
    SINGLE_CHANNEL = "SINGLE_CHANNEL"
    """
    Single channel design
    """
    TWO_CHANNEL = "TWO_CHANNEL"
    """
    Two-channel design with separated compartments
    """
    MULTI_CHANNEL = "MULTI_CHANNEL"
    """
    Multiple channels (>2) design
    """
    LAYERED = "LAYERED"
    """
    Layered/stacked channel architecture
    """
    RADIAL = "RADIAL"
    """
    Radial channel architecture
    """
    NETWORK = "NETWORK"
    """
    Network of interconnected channels
    """


class ChannelConfigurationEnum(str, Enum):
    PARALLEL = "PARALLEL"
    """
    Parallel channel configuration
    """
    SERIAL = "SERIAL"
    """
    Serial/sequential channel configuration
    """
    BRANCHING = "BRANCHING"
    """
    Branching channel configuration
    """
    CIRCULAR = "CIRCULAR"
    """
    Circular/loop channel configuration
    """
    SERPENTINE = "SERPENTINE"
    """
    Serpentine channel pattern
    """
    Y_SHAPED = "Y_SHAPED"
    """
    Y-shaped channel junction
    """
    T_SHAPED = "T_SHAPED"
    """
    T-shaped channel junction
    """


class MembraneTypeEnum(str, Enum):
    POROUS_POLYMER = "POROUS_POLYMER"
    """
    Porous polymer membrane (e.g., PET, PC)
    """
    PDMS = "PDMS"
    """
    Polydimethylsiloxane membrane
    """
    COLLAGEN = "COLLAGEN"
    """
    Collagen-based membrane
    """
    ECM_COATED = "ECM_COATED"
    """
    Extracellular matrix-coated membrane
    """
    TRACK_ETCHED = "TRACK_ETCHED"
    """
    Track-etched membrane
    """
    ELECTROSPUN = "ELECTROSPUN"
    """
    Electrospun fiber membrane
    """
    HYDROGEL = "HYDROGEL"
    """
    Hydrogel membrane
    """


class InterfaceTypeEnum(str, Enum):
    AIR_LIQUID = "AIR_LIQUID"
    """
    Air-liquid interface
    """
    LIQUID_LIQUID = "LIQUID_LIQUID"
    """
    Liquid-liquid interface
    """
    CELL_CELL = "CELL_CELL"
    """
    Direct cell-cell interface
    """
    TISSUE_TISSUE = "TISSUE_TISSUE"
    """
    Tissue-tissue interface
    """
    VASCULAR_EPITHELIAL = "VASCULAR_EPITHELIAL"
    """
    Vascular-epithelial interface
    """


class DeviceMaterialEnum(str, Enum):
    PDMS = "PDMS"
    """
    Polydimethylsiloxane
    """
    GLASS = "GLASS"
    """
    Glass
    """
    PLASTIC = "PLASTIC"
    """
    Plastic (general)
    """
    POLYSTYRENE = "POLYSTYRENE"
    """
    Polystyrene
    """
    POLYCARBONATE = "POLYCARBONATE"
    """
    Polycarbonate
    """
    PMMA = "PMMA"
    """
    Poly(methyl methacrylate)
    """
    COC = "COC"
    """
    Cyclic olefin copolymer
    """
    SILICON = "SILICON"
    """
    Silicon
    """
    HYDROGEL = "HYDROGEL"
    """
    Hydrogel materials
    """


class SurfaceCoatingEnum(str, Enum):
    FIBRONECTIN = "FIBRONECTIN"
    """
    Fibronectin coating
    """
    COLLAGEN = "COLLAGEN"
    """
    Collagen coating
    """
    LAMININ = "LAMININ"
    """
    Laminin coating
    """
    MATRIGEL = "MATRIGEL"
    """
    Matrigel coating
    """
    POLY_L_LYSINE = "POLY_L_LYSINE"
    """
    Poly-L-lysine coating
    """
    GELATIN = "GELATIN"
    """
    Gelatin coating
    """
    RGD_PEPTIDE = "RGD_PEPTIDE"
    """
    RGD peptide coating
    """
    ANTI_FOULING = "ANTI_FOULING"
    """
    Anti-fouling coating
    """
    OXYGEN_PLASMA = "OXYGEN_PLASMA"
    """
    Oxygen plasma treatment
    """


class FlowControlMethodEnum(str, Enum):
    SYRINGE_PUMP = "SYRINGE_PUMP"
    """
    Syringe pump-driven flow
    """
    PERISTALTIC_PUMP = "PERISTALTIC_PUMP"
    """
    Peristaltic pump-driven flow
    """
    GRAVITY_DRIVEN = "GRAVITY_DRIVEN"
    """
    Gravity-driven flow
    """
    PRESSURE_DRIVEN = "PRESSURE_DRIVEN"
    """
    Pressure-driven flow
    """
    ELECTROOSMOTIC = "ELECTROOSMOTIC"
    """
    Electroosmotic flow
    """
    CAPILLARY_ACTION = "CAPILLARY_ACTION"
    """
    Capillary action-driven flow
    """
    PNEUMATIC_VALVES = "PNEUMATIC_VALVES"
    """
    Pneumatic valve control
    """
    MICROVALVES = "MICROVALVES"
    """
    Integrated microvalves
    """


class IntegratedSensorEnum(str, Enum):
    TEER = "TEER"
    """
    Trans-epithelial electrical resistance sensor
    """
    OXYGEN = "OXYGEN"
    """
    Oxygen sensor
    """
    PH = "PH"
    """
    pH sensor
    """
    TEMPERATURE = "TEMPERATURE"
    """
    Temperature sensor
    """
    PRESSURE = "PRESSURE"
    """
    Pressure sensor
    """
    FLOW_RATE = "FLOW_RATE"
    """
    Flow rate sensor
    """
    ELECTROCHEMICAL = "ELECTROCHEMICAL"
    """
    Electrochemical sensors
    """
    OPTICAL = "OPTICAL"
    """
    Optical sensors
    """
    IMPEDANCE = "IMPEDANCE"
    """
    Impedance sensors
    """


class MechanicalStimulationTypeEnum(str, Enum):
    CYCLIC_STRETCH = "CYCLIC_STRETCH"
    """
    Cyclic stretching
    """
    SHEAR_STRESS = "SHEAR_STRESS"
    """
    Fluid shear stress
    """
    COMPRESSION = "COMPRESSION"
    """
    Compression forces
    """
    TENSION = "TENSION"
    """
    Tensile forces
    """
    HYDROSTATIC_PRESSURE = "HYDROSTATIC_PRESSURE"
    """
    Hydrostatic pressure
    """
    PULSATILE_FLOW = "PULSATILE_FLOW"
    """
    Pulsatile flow
    """
    BREATHING_MOTION = "BREATHING_MOTION"
    """
    Breathing-like cyclic motion
    """
    PERISTALTIC_MOTION = "PERISTALTIC_MOTION"
    """
    Peristaltic-like motion
    """


class BiologicalOrganizationLevelEnum(str, Enum):
    SUBCELLULAR = "SUBCELLULAR"
    """
    Within a cell - subcellular components and molecular interactions
    """
    CELLULAR = "CELLULAR"
    """
    Individual cell level - single cell behavior and properties
    """
    CELLULAR_NEIGHBORHOOD = "CELLULAR_NEIGHBORHOOD"
    """
    Cell-cell interactions and local microenvironments
    """
    TISSUE = "TISSUE"
    """
    Tissue-level organization and multicellular structures
    """
    ORGAN = "ORGAN"
    """
    Organ-level physiology and function
    """
    SYSTEM = "SYSTEM"
    """
    Organ system and whole-body physiological integration
    """


class ComplexityLevelEnum(str, Enum):
    LOW = "LOW"
    """
    Simple, well-defined system with limited variables
    """
    MODERATE = "MODERATE"
    """
    Intermediate complexity with multiple interacting components
    """
    HIGH = "HIGH"
    """
    Complex system with many variables and emergent properties
    """


class ThreeDArchitectureEnum(str, Enum):
    SPHEROID = "SPHEROID"
    """
    Spherical 3D cell aggregates
    """
    ORGANOID = "ORGANOID"
    """
    Self-organizing 3D structures with organ-like features
    """
    SCAFFOLD_BASED = "SCAFFOLD_BASED"
    """
    Cells grown on 3D scaffolds or matrices
    """
    HYDROGEL_EMBEDDED = "HYDROGEL_EMBEDDED"
    """
    Cells embedded in hydrogel matrices
    """
    BIOPRINTED = "BIOPRINTED"
    """
    3D bioprinted structures
    """
    HANGING_DROP = "HANGING_DROP"
    """
    Spheroids formed using hanging drop method
    """


class CocultureConfigurationEnum(str, Enum):
    DIRECT_CONTACT = "DIRECT_CONTACT"
    """
    Cells in direct physical contact
    """
    TRANSWELL = "TRANSWELL"
    """
    Cells separated by permeable membrane
    """
    CONDITIONED_MEDIA = "CONDITIONED_MEDIA"
    """
    Cells exposed to media conditioned by other cells
    """
    MICROPATTERN = "MICROPATTERN"
    """
    Cells patterned in defined spatial arrangements
    """
    GRADIENT = "GRADIENT"
    """
    Cells exposed to chemical or physical gradients
    """


class RatioTypeEnum(str, Enum):
    PERCENTAGE = "PERCENTAGE"
    """
    Percentage of total cells
    """
    ABSOLUTE = "ABSOLUTE"
    """
    Absolute cell numbers
    """
    FOLD = "FOLD"
    """
    Fold ratio relative to reference
    """


class PBPKCompartmentEnum(str, Enum):
    LIVER = "LIVER"
    """
    Hepatic compartment
    """
    KIDNEY = "KIDNEY"
    """
    Renal compartment
    """
    LUNG = "LUNG"
    """
    Pulmonary compartment
    """
    BRAIN = "BRAIN"
    """
    Central nervous system compartment
    """
    HEART = "HEART"
    """
    Cardiac compartment
    """
    MUSCLE = "MUSCLE"
    """
    Skeletal muscle compartment
    """
    FAT = "FAT"
    """
    Adipose tissue compartment
    """
    SKIN = "SKIN"
    """
    Dermal compartment
    """
    BONE = "BONE"
    """
    Bone tissue compartment
    """
    GI_TRACT = "GI_TRACT"
    """
    Gastrointestinal tract compartment
    """
    PLASMA = "PLASMA"
    """
    Plasma compartment
    """
    BLOOD = "BLOOD"
    """
    Blood compartment
    """


class DigitalTwinScopeEnum(str, Enum):
    ORGAN = "ORGAN"
    """
    Digital twin of a specific organ
    """
    PATIENT = "PATIENT"
    """
    Digital twin of an individual patient
    """
    POPULATION = "POPULATION"
    """
    Digital twin representing a population
    """
    PATHWAY = "PATHWAY"
    """
    Digital twin of biological pathways
    """
    DISEASE = "DISEASE"
    """
    Digital twin of disease progression
    """


class MLAlgorithmEnum(str, Enum):
    RANDOM_FOREST = "RANDOM_FOREST"
    """
    Random Forest algorithm
    """
    SUPPORT_VECTOR_MACHINE = "SUPPORT_VECTOR_MACHINE"
    """
    Support Vector Machine
    """
    NEURAL_NETWORK = "NEURAL_NETWORK"
    """
    Artificial Neural Networks
    """
    DEEP_LEARNING = "DEEP_LEARNING"
    """
    Deep learning models
    """
    GRADIENT_BOOSTING = "GRADIENT_BOOSTING"
    """
    Gradient boosting methods
    """
    LINEAR_REGRESSION = "LINEAR_REGRESSION"
    """
    Linear regression models
    """
    LOGISTIC_REGRESSION = "LOGISTIC_REGRESSION"
    """
    Logistic regression models
    """
    NAIVE_BAYES = "NAIVE_BAYES"
    """
    Naive Bayes classifier
    """
    K_MEANS = "K_MEANS"
    """
    K-means clustering
    """
    REINFORCEMENT_LEARNING = "REINFORCEMENT_LEARNING"
    """
    Reinforcement learning approaches
    """


class FeatureTypeEnum(str, Enum):
    MOLECULAR = "MOLECULAR"
    """
    Molecular descriptors and chemical features
    """
    PHENOTYPIC = "PHENOTYPIC"
    """
    Phenotypic and physiological features
    """
    GENOMIC = "GENOMIC"
    """
    Genomic and genetic features
    """
    TRANSCRIPTOMIC = "TRANSCRIPTOMIC"
    """
    Gene expression features
    """
    PROTEOMIC = "PROTEOMIC"
    """
    Protein abundance and modification features
    """
    METABOLOMIC = "METABOLOMIC"
    """
    Metabolite concentration features
    """
    IMAGING = "IMAGING"
    """
    Image-derived features
    """
    CLINICAL = "CLINICAL"
    """
    Clinical and demographic features
    """
    TEMPORAL = "TEMPORAL"
    """
    Time-series and temporal features
    """


class InterpretabilityLevelEnum(str, Enum):
    BLACK_BOX = "BLACK_BOX"
    """
    No interpretability - predictions only
    """
    INTERPRETABLE = "INTERPRETABLE"
    """
    Some level of feature importance available
    """
    EXPLAINABLE = "EXPLAINABLE"
    """
    Full mechanistic interpretation possible
    """
    CAUSAL = "CAUSAL"
    """
    Causal relationships can be inferred
    """


class CrossValidationMethodEnum(str, Enum):
    K_FOLD = "K_FOLD"
    """
    K-fold cross-validation
    """
    STRATIFIED_K_FOLD = "STRATIFIED_K_FOLD"
    """
    Stratified k-fold cross-validation
    """
    LEAVE_ONE_OUT = "LEAVE_ONE_OUT"
    """
    Leave-one-out cross-validation
    """
    TIME_SERIES_SPLIT = "TIME_SERIES_SPLIT"
    """
    Time series cross-validation
    """
    MONTE_CARLO = "MONTE_CARLO"
    """
    Monte Carlo cross-validation
    """



class Dataset(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    model_systems: Optional[list[Union[ModelSystem,AnimalModel,NAMModel,CellularSystem,MicrophysiologicalSystem,InSilicoModel,QSARModel,PBPKModel,DigitalTwin,MLModel,MetabolicModel,OrganOnChip,TissueOnChip,TwoDCellCulture,ThreeDCellCulture,CoCulture,Organoid,CellLineModel]]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'model_systems', 'domain_of': ['Dataset']} })
    studies: Optional[list[Study]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'studies', 'domain_of': ['Dataset']} })


class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["NamedThing"] = Field(default="NamedThing", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class Study(NamedThing):
    """
    A study is a structured investigation or analysis, often involving the collection and interpretation of data, to answer specific research questions or test hypotheses.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    context_of_use: Optional[str] = Field(default=None, description="""What decision will this inform? Care? Policy? Drug approval?""", json_schema_extra = { "linkml_meta": {'alias': 'context_of_use', 'domain_of': ['Study']} })
    biological_context: Optional[str] = Field(default=None, description="""tissue/region (anatomy), cell types, sex/age equivalents, mechanics (e.g., cyclic stretch), microenvironment""", json_schema_extra = { "linkml_meta": {'alias': 'biological_context', 'domain_of': ['Study']} })
    perturbations: Optional[str] = Field(default=None, description="""exposure/dose/time; diet/drugs/toxicants""", json_schema_extra = { "linkml_meta": {'alias': 'perturbations', 'domain_of': ['Study']} })
    endpoints: Optional[str] = Field(default=None, description="""phenotypes, function (TEER/leak, beating rate), and multi-omics""", json_schema_extra = { "linkml_meta": {'alias': 'endpoints', 'domain_of': ['Study']} })
    plan_comparators: Optional[str] = Field(default=None, description="""human data, gold-standard assays, or high-quality animal references""", json_schema_extra = { "linkml_meta": {'alias': 'plan_comparators', 'domain_of': ['Study']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["Study"] = Field(default="Study", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class ModelSystem(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["ModelSystem"] = Field(default="ModelSystem", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class AnimalModel(ModelSystem):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    species: str = Field(default=..., description="""The species of the animal used in the model system.""", json_schema_extra = { "linkml_meta": {'alias': 'species',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'SpeciesEnum'}],
         'domain_of': ['AnimalModel']} })
    strain: Optional[str] = Field(default=None, description="""The specific strain of the animal used in the model system.""", json_schema_extra = { "linkml_meta": {'alias': 'strain',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'StrainEnum'}],
         'domain_of': ['AnimalModel']} })
    age: Optional[str] = Field(default=None, description="""The age of the animal used in the model system.""", json_schema_extra = { "linkml_meta": {'alias': 'age',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'OrganismAgeEnum'}],
         'domain_of': ['AnimalModel']} })
    environment: Optional[str] = Field(default=None, description="""The environmental conditions under which the animal model is maintained.""", json_schema_extra = { "linkml_meta": {'alias': 'environment', 'domain_of': ['AnimalModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["AnimalModel"] = Field(default="AnimalModel", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class NAMModel(ModelSystem):
    """
    A New Approach Methodology (NAM) model, which is a type of model system that does not involve the use of animals.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["NAMModel"] = Field(default="NAMModel", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class CellularSystem(NAMModel):
    """
    Cell-based model systems that use living cells to model biological processes. Includes 2D cultures, 3D systems, and co-cultures.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    cell_types: Optional[list[Term]] = Field(default=None, description="""Cell types present in the cellular system""", json_schema_extra = { "linkml_meta": {'alias': 'cell_types',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeEnum'}],
         'domain_of': ['CellularSystem', 'OrganOnChip']} })
    cell_source: Optional[str] = Field(default=None, description="""Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)""", json_schema_extra = { "linkml_meta": {'alias': 'cell_source', 'domain_of': ['CellularSystem', 'OrganOnChip']} })
    culture_conditions: Optional[str] = Field(default=None, description="""Standard culture conditions and media used""", json_schema_extra = { "linkml_meta": {'alias': 'culture_conditions', 'domain_of': ['CellularSystem']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["CellularSystem"] = Field(default="CellularSystem", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class TwoDCellCulture(CellularSystem):
    """
    Conventional monolayer cell cultures grown on flat surfaces. Simple but limited in physiological relevance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., plastic, glass, coated surfaces)""", json_schema_extra = { "linkml_meta": {'alias': 'substrate_type', 'domain_of': ['TwoDCellCulture']} })
    confluence_level: Optional[float] = Field(default=None, description="""Typical confluence level maintained (0.0-1.0)""", json_schema_extra = { "linkml_meta": {'alias': 'confluence_level', 'domain_of': ['TwoDCellCulture']} })
    passage_protocol: Optional[str] = Field(default=None, description="""Standard passaging protocol and frequency""", json_schema_extra = { "linkml_meta": {'alias': 'passage_protocol', 'domain_of': ['TwoDCellCulture']} })
    cell_types: Optional[list[Term]] = Field(default=None, description="""Cell types present in the cellular system""", json_schema_extra = { "linkml_meta": {'alias': 'cell_types',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeEnum'}],
         'domain_of': ['CellularSystem', 'OrganOnChip']} })
    cell_source: Optional[str] = Field(default=None, description="""Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)""", json_schema_extra = { "linkml_meta": {'alias': 'cell_source', 'domain_of': ['CellularSystem', 'OrganOnChip']} })
    culture_conditions: Optional[str] = Field(default=None, description="""Standard culture conditions and media used""", json_schema_extra = { "linkml_meta": {'alias': 'culture_conditions', 'domain_of': ['CellularSystem']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["TwoDCellCulture"] = Field(default="TwoDCellCulture", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class ThreeDCellCulture(CellularSystem):
    """
    Three-dimensional cell culture systems including spheroids and organoids. More physiologically relevant with 3D architecture.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    three_d_architecture: Optional[ThreeDArchitectureEnum] = Field(default=None, description="""Type of 3D architecture (spheroid, organoid, scaffold-based, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'three_d_architecture', 'domain_of': ['ThreeDCellCulture']} })
    matrix_composition: Optional[str] = Field(default=None, description="""Composition of extracellular matrix or scaffold material""", json_schema_extra = { "linkml_meta": {'alias': 'matrix_composition', 'domain_of': ['ThreeDCellCulture']} })
    size_range: Optional[str] = Field(default=None, description="""Typical size range of 3D structures""", json_schema_extra = { "linkml_meta": {'alias': 'size_range', 'domain_of': ['ThreeDCellCulture']} })
    cell_types: Optional[list[Term]] = Field(default=None, description="""Cell types present in the cellular system""", json_schema_extra = { "linkml_meta": {'alias': 'cell_types',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeEnum'}],
         'domain_of': ['CellularSystem', 'OrganOnChip']} })
    cell_source: Optional[str] = Field(default=None, description="""Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)""", json_schema_extra = { "linkml_meta": {'alias': 'cell_source', 'domain_of': ['CellularSystem', 'OrganOnChip']} })
    culture_conditions: Optional[str] = Field(default=None, description="""Standard culture conditions and media used""", json_schema_extra = { "linkml_meta": {'alias': 'culture_conditions', 'domain_of': ['CellularSystem']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["ThreeDCellCulture"] = Field(default="ThreeDCellCulture", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class CoCulture(CellularSystem):
    """
    Co-culture systems combining multiple cell types to mimic  microenvironments and cell-cell interactions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    coculture_configuration: Optional[CocultureConfigurationEnum] = Field(default=None, description="""Configuration of co-culture (direct contact, transwell, conditioned media)""", json_schema_extra = { "linkml_meta": {'alias': 'coculture_configuration', 'domain_of': ['CoCulture']} })
    cell_ratios: Optional[list[CellRatio]] = Field(default=None, description="""Ratios of different cell types in the co-culture""", json_schema_extra = { "linkml_meta": {'alias': 'cell_ratios', 'domain_of': ['CoCulture']} })
    interaction_mechanisms: Optional[list[str]] = Field(default=None, description="""Mechanisms of cell-cell interaction (paracrine, direct contact, mechanical)""", json_schema_extra = { "linkml_meta": {'alias': 'interaction_mechanisms', 'domain_of': ['CoCulture']} })
    cell_types: Optional[list[Term]] = Field(default=None, description="""Cell types present in the cellular system""", json_schema_extra = { "linkml_meta": {'alias': 'cell_types',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeEnum'}],
         'domain_of': ['CellularSystem', 'OrganOnChip']} })
    cell_source: Optional[str] = Field(default=None, description="""Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)""", json_schema_extra = { "linkml_meta": {'alias': 'cell_source', 'domain_of': ['CellularSystem', 'OrganOnChip']} })
    culture_conditions: Optional[str] = Field(default=None, description="""Standard culture conditions and media used""", json_schema_extra = { "linkml_meta": {'alias': 'culture_conditions', 'domain_of': ['CellularSystem']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["CoCulture"] = Field(default="CoCulture", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class Organoid(ThreeDCellCulture):
    """
    A 3D cell culture system that self-organizes to recapitulate key structural and functional aspects of an organ or tissue
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    organ_modeled: Optional[Term] = Field(default=None, description="""The organ or tissue being modeled""", json_schema_extra = { "linkml_meta": {'alias': 'organ_modeled',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'OrganEnum'}],
         'domain_of': ['Organoid', 'OrganOnChip']} })
    differentiation_method: Optional[str] = Field(default=None, description="""Method used to differentiate cells into organoid (e.g., directed differentiation protocol)""", json_schema_extra = { "linkml_meta": {'alias': 'differentiation_method', 'domain_of': ['Organoid']} })
    culture_system: Optional[str] = Field(default=None, description="""Culture system used (e.g., Matrigel dome, suspension culture, air-liquid interface)""", json_schema_extra = { "linkml_meta": {'alias': 'culture_system', 'domain_of': ['Organoid']} })
    three_d_architecture: Optional[ThreeDArchitectureEnum] = Field(default=None, description="""Type of 3D architecture (spheroid, organoid, scaffold-based, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'three_d_architecture', 'domain_of': ['ThreeDCellCulture']} })
    matrix_composition: Optional[str] = Field(default=None, description="""Composition of extracellular matrix or scaffold material""", json_schema_extra = { "linkml_meta": {'alias': 'matrix_composition', 'domain_of': ['ThreeDCellCulture']} })
    size_range: Optional[str] = Field(default=None, description="""Typical size range of 3D structures""", json_schema_extra = { "linkml_meta": {'alias': 'size_range', 'domain_of': ['ThreeDCellCulture']} })
    cell_types: Optional[list[Term]] = Field(default=None, description="""Cell types present in the cellular system""", json_schema_extra = { "linkml_meta": {'alias': 'cell_types',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeEnum'}],
         'domain_of': ['CellularSystem', 'OrganOnChip']} })
    cell_source: Optional[str] = Field(default=None, description="""Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)""", json_schema_extra = { "linkml_meta": {'alias': 'cell_source', 'domain_of': ['CellularSystem', 'OrganOnChip']} })
    culture_conditions: Optional[str] = Field(default=None, description="""Standard culture conditions and media used""", json_schema_extra = { "linkml_meta": {'alias': 'culture_conditions', 'domain_of': ['CellularSystem']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["Organoid"] = Field(default="Organoid", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class CellLineModel(TwoDCellCulture):
    """
    A model system based on immortalized cell lines that can be maintained in culture indefinitely. Examples: HepG2, A549, Caco-2, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    passage_range: Optional[str] = Field(default=None, description="""Recommended passage number range for experimental use""", json_schema_extra = { "linkml_meta": {'alias': 'passage_range', 'domain_of': ['CellLineModel']} })
    authentication_method: Optional[str] = Field(default=None, description="""Method used for cell line authentication (e.g., STR profiling, mycoplasma testing)""", json_schema_extra = { "linkml_meta": {'alias': 'authentication_method', 'domain_of': ['CellLineModel']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., plastic, glass, coated surfaces)""", json_schema_extra = { "linkml_meta": {'alias': 'substrate_type', 'domain_of': ['TwoDCellCulture']} })
    confluence_level: Optional[float] = Field(default=None, description="""Typical confluence level maintained (0.0-1.0)""", json_schema_extra = { "linkml_meta": {'alias': 'confluence_level', 'domain_of': ['TwoDCellCulture']} })
    passage_protocol: Optional[str] = Field(default=None, description="""Standard passaging protocol and frequency""", json_schema_extra = { "linkml_meta": {'alias': 'passage_protocol', 'domain_of': ['TwoDCellCulture']} })
    cell_types: Optional[list[Term]] = Field(default=None, description="""Cell types present in the cellular system""", json_schema_extra = { "linkml_meta": {'alias': 'cell_types',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeEnum'}],
         'domain_of': ['CellularSystem', 'OrganOnChip']} })
    cell_source: Optional[str] = Field(default=None, description="""Source of cells (e.g., primary, iPSC-derived, immortalized cell lines)""", json_schema_extra = { "linkml_meta": {'alias': 'cell_source', 'domain_of': ['CellularSystem', 'OrganOnChip']} })
    culture_conditions: Optional[str] = Field(default=None, description="""Standard culture conditions and media used""", json_schema_extra = { "linkml_meta": {'alias': 'culture_conditions', 'domain_of': ['CellularSystem']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["CellLineModel"] = Field(default="CellLineModel", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class MicrophysiologicalSystem(NAMModel):
    """
    Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials,  and living cells to replicate tissue-level physiology and dynamics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    microfluidic_design: Optional[MicrofluidicDesign] = Field(default=None, description="""Detailed design specifications of the microfluidic device""", json_schema_extra = { "linkml_meta": {'alias': 'microfluidic_design', 'domain_of': ['MicrophysiologicalSystem']} })
    mechanical_forces: Optional[MechanicalStimulation] = Field(default=None, description="""Mechanical forces applied to the model system""", json_schema_extra = { "linkml_meta": {'alias': 'mechanical_forces', 'domain_of': ['MicrophysiologicalSystem']} })
    perfusion_system: Optional[str] = Field(default=None, description="""Description of perfusion and flow systems""", json_schema_extra = { "linkml_meta": {'alias': 'perfusion_system', 'domain_of': ['MicrophysiologicalSystem']} })
    sensor_integration: Optional[list[IntegratedSensorEnum]] = Field(default=None, description="""Sensors integrated for real-time monitoring""", json_schema_extra = { "linkml_meta": {'alias': 'sensor_integration', 'domain_of': ['MicrophysiologicalSystem']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["MicrophysiologicalSystem"] = Field(default="MicrophysiologicalSystem", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class OrganOnChip(MicrophysiologicalSystem):
    """
    A model system that simulates the physiological functions of an organ using a microfluidic device. Examples: Airway-on-chip, ...
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    organ_modeled: Optional[Term] = Field(default=None, description="""The organ or anatomical structure being modeled (e.g., lung, airway, alveolus)""", json_schema_extra = { "linkml_meta": {'alias': 'organ_modeled',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'OrganEnum'}],
         'domain_of': ['Organoid', 'OrganOnChip']} })
    cell_types: Optional[list[Term]] = Field(default=None, description="""Cell types present in the organ-on-chip model""", json_schema_extra = { "linkml_meta": {'alias': 'cell_types',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CellTypeEnum'}],
         'domain_of': ['CellularSystem', 'OrganOnChip']} })
    cell_source: Optional[str] = Field(default=None, description="""Source of cells (e.g., primary human cells, iPSC-derived, cell line, patient-derived)""", json_schema_extra = { "linkml_meta": {'alias': 'cell_source', 'domain_of': ['CellularSystem', 'OrganOnChip']} })
    microfluidic_design: Optional[MicrofluidicDesign] = Field(default=None, description="""Detailed design specifications of the microfluidic device""", json_schema_extra = { "linkml_meta": {'alias': 'microfluidic_design', 'domain_of': ['MicrophysiologicalSystem']} })
    mechanical_forces: Optional[MechanicalStimulation] = Field(default=None, description="""Mechanical forces applied to the model system""", json_schema_extra = { "linkml_meta": {'alias': 'mechanical_forces', 'domain_of': ['MicrophysiologicalSystem']} })
    perfusion_system: Optional[str] = Field(default=None, description="""Description of perfusion and flow systems""", json_schema_extra = { "linkml_meta": {'alias': 'perfusion_system', 'domain_of': ['MicrophysiologicalSystem']} })
    sensor_integration: Optional[list[IntegratedSensorEnum]] = Field(default=None, description="""Sensors integrated for real-time monitoring""", json_schema_extra = { "linkml_meta": {'alias': 'sensor_integration', 'domain_of': ['MicrophysiologicalSystem']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["OrganOnChip"] = Field(default="OrganOnChip", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class TissueOnChip(MicrophysiologicalSystem):
    """
    Tissue-level microphysiological systems that model specific tissue functions and multi-cellular interactions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    tissue_modeled: Optional[Term] = Field(default=None, description="""The specific tissue being modeled""", json_schema_extra = { "linkml_meta": {'alias': 'tissue_modeled', 'domain_of': ['TissueOnChip']} })
    tissue_architecture: Optional[str] = Field(default=None, description="""Description of tissue-level architecture and organization""", json_schema_extra = { "linkml_meta": {'alias': 'tissue_architecture', 'domain_of': ['TissueOnChip']} })
    barrier_functions: Optional[list[str]] = Field(default=None, description="""Tissue barrier functions modeled (epithelial, endothelial, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'barrier_functions', 'domain_of': ['TissueOnChip']} })
    microfluidic_design: Optional[MicrofluidicDesign] = Field(default=None, description="""Detailed design specifications of the microfluidic device""", json_schema_extra = { "linkml_meta": {'alias': 'microfluidic_design', 'domain_of': ['MicrophysiologicalSystem']} })
    mechanical_forces: Optional[MechanicalStimulation] = Field(default=None, description="""Mechanical forces applied to the model system""", json_schema_extra = { "linkml_meta": {'alias': 'mechanical_forces', 'domain_of': ['MicrophysiologicalSystem']} })
    perfusion_system: Optional[str] = Field(default=None, description="""Description of perfusion and flow systems""", json_schema_extra = { "linkml_meta": {'alias': 'perfusion_system', 'domain_of': ['MicrophysiologicalSystem']} })
    sensor_integration: Optional[list[IntegratedSensorEnum]] = Field(default=None, description="""Sensors integrated for real-time monitoring""", json_schema_extra = { "linkml_meta": {'alias': 'sensor_integration', 'domain_of': ['MicrophysiologicalSystem']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["TissueOnChip"] = Field(default="TissueOnChip", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class InSilicoModel(NAMModel):
    """
    Computational models that simulate biological processes without physical biological components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    computational_method: Optional[str] = Field(default=None, description="""Primary computational method or algorithm used""", json_schema_extra = { "linkml_meta": {'alias': 'computational_method', 'domain_of': ['InSilicoModel']} })
    software_platform: Optional[str] = Field(default=None, description="""Software platform or programming language used""", json_schema_extra = { "linkml_meta": {'alias': 'software_platform', 'domain_of': ['InSilicoModel']} })
    validation_datasets: Optional[list[str]] = Field(default=None, description="""Datasets used for model training and validation""", json_schema_extra = { "linkml_meta": {'alias': 'validation_datasets', 'domain_of': ['InSilicoModel']} })
    prediction_scope: Optional[str] = Field(default=None, description="""Scope and limitations of model predictions""", json_schema_extra = { "linkml_meta": {'alias': 'prediction_scope', 'domain_of': ['InSilicoModel']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["InSilicoModel"] = Field(default="InSilicoModel", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class QSARModel(InSilicoModel):
    """
    Quantitative Structure-Activity Relationship models that predict  chemical/biological activity from molecular structure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    molecular_descriptors: Optional[list[str]] = Field(default=None, description="""Types of molecular descriptors used (topological, electronic, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'molecular_descriptors', 'domain_of': ['QSARModel']} })
    activity_endpoint: Optional[str] = Field(default=None, description="""Biological activity or property being predicted""", json_schema_extra = { "linkml_meta": {'alias': 'activity_endpoint', 'domain_of': ['QSARModel']} })
    training_dataset_size: Optional[int] = Field(default=None, description="""Number of compounds in training dataset""", json_schema_extra = { "linkml_meta": {'alias': 'training_dataset_size', 'domain_of': ['QSARModel']} })
    model_performance: Optional[ModelPerformance] = Field(default=None, description="""Statistical performance metrics of the model""", json_schema_extra = { "linkml_meta": {'alias': 'model_performance', 'domain_of': ['QSARModel']} })
    computational_method: Optional[str] = Field(default=None, description="""Primary computational method or algorithm used""", json_schema_extra = { "linkml_meta": {'alias': 'computational_method', 'domain_of': ['InSilicoModel']} })
    software_platform: Optional[str] = Field(default=None, description="""Software platform or programming language used""", json_schema_extra = { "linkml_meta": {'alias': 'software_platform', 'domain_of': ['InSilicoModel']} })
    validation_datasets: Optional[list[str]] = Field(default=None, description="""Datasets used for model training and validation""", json_schema_extra = { "linkml_meta": {'alias': 'validation_datasets', 'domain_of': ['InSilicoModel']} })
    prediction_scope: Optional[str] = Field(default=None, description="""Scope and limitations of model predictions""", json_schema_extra = { "linkml_meta": {'alias': 'prediction_scope', 'domain_of': ['InSilicoModel']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["QSARModel"] = Field(default="QSARModel", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class PBPKModel(InSilicoModel):
    """
    Physiologically Based Pharmacokinetic models that simulate drug  absorption, distribution, metabolism, and excretion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    compartments: Optional[list[PBPKCompartment]] = Field(default=None, description="""Physiological compartments included in the model""", json_schema_extra = { "linkml_meta": {'alias': 'compartments', 'domain_of': ['PBPKModel']} })
    species_modeled: Optional[Term] = Field(default=None, description="""Species for which the model is designed""", json_schema_extra = { "linkml_meta": {'alias': 'species_modeled', 'domain_of': ['PBPKModel']} })
    drug_properties: Optional[DrugProperties] = Field(default=None, description="""Physicochemical and pharmacological properties modeled""", json_schema_extra = { "linkml_meta": {'alias': 'drug_properties', 'domain_of': ['PBPKModel']} })
    elimination_pathways: Optional[list[str]] = Field(default=None, description="""Drug elimination and metabolism pathways included""", json_schema_extra = { "linkml_meta": {'alias': 'elimination_pathways', 'domain_of': ['PBPKModel']} })
    computational_method: Optional[str] = Field(default=None, description="""Primary computational method or algorithm used""", json_schema_extra = { "linkml_meta": {'alias': 'computational_method', 'domain_of': ['InSilicoModel']} })
    software_platform: Optional[str] = Field(default=None, description="""Software platform or programming language used""", json_schema_extra = { "linkml_meta": {'alias': 'software_platform', 'domain_of': ['InSilicoModel']} })
    validation_datasets: Optional[list[str]] = Field(default=None, description="""Datasets used for model training and validation""", json_schema_extra = { "linkml_meta": {'alias': 'validation_datasets', 'domain_of': ['InSilicoModel']} })
    prediction_scope: Optional[str] = Field(default=None, description="""Scope and limitations of model predictions""", json_schema_extra = { "linkml_meta": {'alias': 'prediction_scope', 'domain_of': ['InSilicoModel']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["PBPKModel"] = Field(default="PBPKModel", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class DigitalTwin(InSilicoModel):
    """
    Computational replicas of biological systems for real-time prediction and personalized modeling.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    twin_scope: Optional[DigitalTwinScopeEnum] = Field(default=None, description="""Scope of digital twin (organ, patient, population)""", json_schema_extra = { "linkml_meta": {'alias': 'twin_scope', 'domain_of': ['DigitalTwin']} })
    real_time_data_sources: Optional[list[str]] = Field(default=None, description="""Sources of real-time data for model updating""", json_schema_extra = { "linkml_meta": {'alias': 'real_time_data_sources', 'domain_of': ['DigitalTwin']} })
    personalization_parameters: Optional[list[str]] = Field(default=None, description="""Parameters used for personalization (genetic, phenotypic, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'personalization_parameters', 'domain_of': ['DigitalTwin']} })
    update_frequency: Optional[str] = Field(default=None, description="""Frequency of model updates based on new data""", json_schema_extra = { "linkml_meta": {'alias': 'update_frequency', 'domain_of': ['DigitalTwin']} })
    computational_method: Optional[str] = Field(default=None, description="""Primary computational method or algorithm used""", json_schema_extra = { "linkml_meta": {'alias': 'computational_method', 'domain_of': ['InSilicoModel']} })
    software_platform: Optional[str] = Field(default=None, description="""Software platform or programming language used""", json_schema_extra = { "linkml_meta": {'alias': 'software_platform', 'domain_of': ['InSilicoModel']} })
    validation_datasets: Optional[list[str]] = Field(default=None, description="""Datasets used for model training and validation""", json_schema_extra = { "linkml_meta": {'alias': 'validation_datasets', 'domain_of': ['InSilicoModel']} })
    prediction_scope: Optional[str] = Field(default=None, description="""Scope and limitations of model predictions""", json_schema_extra = { "linkml_meta": {'alias': 'prediction_scope', 'domain_of': ['InSilicoModel']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["DigitalTwin"] = Field(default="DigitalTwin", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class MLModel(InSilicoModel):
    """
    Machine Learning and AI-based models for prediction, mechanism inference, and hypothesis generation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    ml_algorithm: Optional[MLAlgorithmEnum] = Field(default=None, description="""Type of machine learning algorithm used""", json_schema_extra = { "linkml_meta": {'alias': 'ml_algorithm', 'domain_of': ['MLModel']} })
    feature_types: Optional[list[FeatureTypeEnum]] = Field(default=None, description="""Types of features used (molecular, phenotypic, imaging, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'feature_types', 'domain_of': ['MLModel']} })
    training_data_size: Optional[int] = Field(default=None, description="""Size of training dataset""", json_schema_extra = { "linkml_meta": {'alias': 'training_data_size', 'domain_of': ['MLModel']} })
    model_interpretability: Optional[InterpretabilityLevelEnum] = Field(default=None, description="""Level of model interpretability (black box, interpretable, explainable)""", json_schema_extra = { "linkml_meta": {'alias': 'model_interpretability', 'domain_of': ['MLModel']} })
    cross_validation: Optional[CrossValidation] = Field(default=None, description="""Cross-validation strategy and results""", json_schema_extra = { "linkml_meta": {'alias': 'cross_validation', 'domain_of': ['MLModel']} })
    computational_method: Optional[str] = Field(default=None, description="""Primary computational method or algorithm used""", json_schema_extra = { "linkml_meta": {'alias': 'computational_method', 'domain_of': ['InSilicoModel']} })
    software_platform: Optional[str] = Field(default=None, description="""Software platform or programming language used""", json_schema_extra = { "linkml_meta": {'alias': 'software_platform', 'domain_of': ['InSilicoModel']} })
    validation_datasets: Optional[list[str]] = Field(default=None, description="""Datasets used for model training and validation""", json_schema_extra = { "linkml_meta": {'alias': 'validation_datasets', 'domain_of': ['InSilicoModel']} })
    prediction_scope: Optional[str] = Field(default=None, description="""Scope and limitations of model predictions""", json_schema_extra = { "linkml_meta": {'alias': 'prediction_scope', 'domain_of': ['InSilicoModel']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["MLModel"] = Field(default="MLModel", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class MetabolicModel(InSilicoModel):
    """
    A model that simulates the metabolic processes of an organism or system. Examples: Virtual Physiological Human, ...
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    computational_method: Optional[str] = Field(default=None, description="""Primary computational method or algorithm used""", json_schema_extra = { "linkml_meta": {'alias': 'computational_method', 'domain_of': ['InSilicoModel']} })
    software_platform: Optional[str] = Field(default=None, description="""Software platform or programming language used""", json_schema_extra = { "linkml_meta": {'alias': 'software_platform', 'domain_of': ['InSilicoModel']} })
    validation_datasets: Optional[list[str]] = Field(default=None, description="""Datasets used for model training and validation""", json_schema_extra = { "linkml_meta": {'alias': 'validation_datasets', 'domain_of': ['InSilicoModel']} })
    prediction_scope: Optional[str] = Field(default=None, description="""Scope and limitations of model predictions""", json_schema_extra = { "linkml_meta": {'alias': 'prediction_scope', 'domain_of': ['InSilicoModel']} })
    biological_organization_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization represented by the model""", json_schema_extra = { "linkml_meta": {'alias': 'biological_organization_level', 'domain_of': ['NAMModel']} })
    spatial_context: Optional[str] = Field(default=None, description="""Description of spatial organization and context captured by the model""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_context', 'domain_of': ['NAMModel']} })
    complexity_level: Optional[ComplexityLevelEnum] = Field(default=None, description="""Level of biological complexity represented (subcellular, cellular, tissue, organ, system)""", json_schema_extra = { "linkml_meta": {'alias': 'complexity_level', 'domain_of': ['NAMModel']} })
    references: Optional[list[Reference]] = Field(default=None, description="""Literature references that describe, validate, or support this model""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['NAMModel']} })
    models: Optional[list[ModelsRelationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'models', 'domain_of': ['ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["MetabolicModel"] = Field(default="MetabolicModel", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class CellRatio(ConfiguredBaseModel):
    """
    Ratio specification for different cell types in co-culture systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    cell_type: Optional[Term] = Field(default=None, description="""The cell type for which the ratio is specified""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type', 'domain_of': ['CellRatio', 'CellTypeProportion']} })
    ratio: Optional[float] = Field(default=None, description="""Proportion or ratio of this cell type (0.0-1.0 or absolute numbers)""", json_schema_extra = { "linkml_meta": {'alias': 'ratio', 'domain_of': ['CellRatio']} })
    ratio_type: Optional[RatioTypeEnum] = Field(default=None, description="""Type of ratio specification (percentage, absolute, fold)""", json_schema_extra = { "linkml_meta": {'alias': 'ratio_type', 'domain_of': ['CellRatio']} })


class ModelPerformance(ConfiguredBaseModel):
    """
    Statistical performance metrics for computational models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    accuracy: Optional[float] = Field(default=None, description="""Overall accuracy of the model (0.0-1.0)""", json_schema_extra = { "linkml_meta": {'alias': 'accuracy', 'domain_of': ['ModelPerformance']} })
    sensitivity: Optional[float] = Field(default=None, description="""Sensitivity/recall of the model (0.0-1.0)""", json_schema_extra = { "linkml_meta": {'alias': 'sensitivity', 'domain_of': ['ModelPerformance']} })
    specificity: Optional[float] = Field(default=None, description="""Specificity of the model (0.0-1.0)""", json_schema_extra = { "linkml_meta": {'alias': 'specificity', 'domain_of': ['ModelPerformance']} })
    r_squared: Optional[float] = Field(default=None, description="""R-squared value for regression models""", json_schema_extra = { "linkml_meta": {'alias': 'r_squared', 'domain_of': ['ModelPerformance']} })
    rmse: Optional[float] = Field(default=None, description="""Root mean square error""", json_schema_extra = { "linkml_meta": {'alias': 'rmse', 'domain_of': ['ModelPerformance']} })
    auc: Optional[float] = Field(default=None, description="""Area under the ROC curve""", json_schema_extra = { "linkml_meta": {'alias': 'auc', 'domain_of': ['ModelPerformance']} })


class PBPKCompartment(NamedThing):
    """
    A physiological compartment in a PBPK model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    compartment_type: Optional[PBPKCompartmentEnum] = Field(default=None, description="""Type of physiological compartment""", json_schema_extra = { "linkml_meta": {'alias': 'compartment_type', 'domain_of': ['PBPKCompartment']} })
    volume: Optional[float] = Field(default=None, description="""Volume of the compartment (L)""", json_schema_extra = { "linkml_meta": {'alias': 'volume', 'domain_of': ['PBPKCompartment']} })
    blood_flow: Optional[float] = Field(default=None, description="""Blood flow to the compartment (L/h)""", json_schema_extra = { "linkml_meta": {'alias': 'blood_flow', 'domain_of': ['PBPKCompartment']} })
    partition_coefficient: Optional[float] = Field(default=None, description="""Tissue-to-plasma partition coefficient""", json_schema_extra = { "linkml_meta": {'alias': 'partition_coefficient', 'domain_of': ['PBPKCompartment']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["PBPKCompartment"] = Field(default="PBPKCompartment", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class DrugProperties(ConfiguredBaseModel):
    """
    Physicochemical and pharmacological properties of a drug in PBPK models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    molecular_weight: Optional[float] = Field(default=None, description="""Molecular weight (g/mol)""", json_schema_extra = { "linkml_meta": {'alias': 'molecular_weight', 'domain_of': ['DrugProperties']} })
    logp: Optional[float] = Field(default=None, description="""Lipophilicity (log P)""", json_schema_extra = { "linkml_meta": {'alias': 'logp', 'domain_of': ['DrugProperties']} })
    pka: Optional[float] = Field(default=None, description="""Acid dissociation constant""", json_schema_extra = { "linkml_meta": {'alias': 'pka', 'domain_of': ['DrugProperties']} })
    protein_binding: Optional[float] = Field(default=None, description="""Fraction bound to plasma proteins (0.0-1.0)""", json_schema_extra = { "linkml_meta": {'alias': 'protein_binding', 'domain_of': ['DrugProperties']} })
    clearance: Optional[float] = Field(default=None, description="""Total body clearance (L/h)""", json_schema_extra = { "linkml_meta": {'alias': 'clearance', 'domain_of': ['DrugProperties']} })


class CrossValidation(ConfiguredBaseModel):
    """
    Cross-validation strategy and results for ML models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    cv_method: Optional[CrossValidationMethodEnum] = Field(default=None, description="""Type of cross-validation used""", json_schema_extra = { "linkml_meta": {'alias': 'cv_method', 'domain_of': ['CrossValidation']} })
    n_folds: Optional[int] = Field(default=None, description="""Number of folds in cross-validation""", json_schema_extra = { "linkml_meta": {'alias': 'n_folds', 'domain_of': ['CrossValidation']} })
    cv_score: Optional[float] = Field(default=None, description="""Average cross-validation score""", json_schema_extra = { "linkml_meta": {'alias': 'cv_score', 'domain_of': ['CrossValidation']} })
    cv_std: Optional[float] = Field(default=None, description="""Standard deviation of cross-validation scores""", json_schema_extra = { "linkml_meta": {'alias': 'cv_std', 'domain_of': ['CrossValidation']} })


class MicrofluidicDesign(NamedThing):
    """
    Detailed specification of a microfluidic device design including its architecture, materials, dimensions, and functional features.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    architecture_type: Optional[MicrofluidicArchitectureEnum] = Field(default=None, description="""The overall architecture type of the microfluidic device""", json_schema_extra = { "linkml_meta": {'alias': 'architecture_type', 'domain_of': ['MicrofluidicDesign']} })
    number_of_channels: Optional[int] = Field(default=None, description="""Total number of channels in the device""", json_schema_extra = { "linkml_meta": {'alias': 'number_of_channels', 'domain_of': ['MicrofluidicDesign']} })
    channel_configuration: Optional[list[ChannelConfigurationEnum]] = Field(default=None, description="""Configuration of channels (e.g., parallel, serial, branching)""", json_schema_extra = { "linkml_meta": {'alias': 'channel_configuration', 'domain_of': ['MicrofluidicDesign']} })
    membrane_type: Optional[MembraneTypeEnum] = Field(default=None, description="""Type of membrane used in the device if applicable""", json_schema_extra = { "linkml_meta": {'alias': 'membrane_type', 'domain_of': ['MicrofluidicDesign']} })
    membrane_pore_size: Optional[float] = Field(default=None, description="""Pore size of the membrane in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'membrane_pore_size', 'domain_of': ['MicrofluidicDesign']} })
    membrane_thickness: Optional[float] = Field(default=None, description="""Thickness of the membrane in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'membrane_thickness', 'domain_of': ['MicrofluidicDesign']} })
    interface_type: Optional[list[InterfaceTypeEnum]] = Field(default=None, description="""Type of interface(s) present in the device""", json_schema_extra = { "linkml_meta": {'alias': 'interface_type', 'domain_of': ['MicrofluidicDesign']} })
    channel_dimensions: Optional[list[ChannelDimensions]] = Field(default=None, description="""Dimensions of the channels in the device""", json_schema_extra = { "linkml_meta": {'alias': 'channel_dimensions', 'domain_of': ['MicrofluidicDesign']} })
    material: Optional[list[DeviceMaterialEnum]] = Field(default=None, description="""Materials used to construct the device""", json_schema_extra = { "linkml_meta": {'alias': 'material', 'domain_of': ['MicrofluidicDesign']} })
    surface_treatment: Optional[list[SurfaceCoatingEnum]] = Field(default=None, description="""Surface treatments or coatings applied to the device""", json_schema_extra = { "linkml_meta": {'alias': 'surface_treatment', 'domain_of': ['MicrofluidicDesign']} })
    flow_control_method: Optional[list[FlowControlMethodEnum]] = Field(default=None, description="""Methods used to control fluid flow in the device""", json_schema_extra = { "linkml_meta": {'alias': 'flow_control_method', 'domain_of': ['MicrofluidicDesign']} })
    sensors_integrated: Optional[list[IntegratedSensorEnum]] = Field(default=None, description="""Sensors integrated into the device for monitoring""", json_schema_extra = { "linkml_meta": {'alias': 'sensors_integrated', 'domain_of': ['MicrofluidicDesign']} })
    special_features: Optional[list[str]] = Field(default=None, description="""Additional special features of the device (e.g., valves, mixers, gradient generators)""", json_schema_extra = { "linkml_meta": {'alias': 'special_features', 'domain_of': ['MicrofluidicDesign']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["MicrofluidicDesign"] = Field(default="MicrofluidicDesign", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class ChannelDimensions(ConfiguredBaseModel):
    """
    Dimensions of a microfluidic channel
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    channel_name: Optional[str] = Field(default=None, description="""Name or identifier of the channel (e.g., apical, basolateral, vascular)""", json_schema_extra = { "linkml_meta": {'alias': 'channel_name', 'domain_of': ['ChannelDimensions']} })
    width: Optional[float] = Field(default=None, description="""Width of the channel in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'width', 'domain_of': ['ChannelDimensions']} })
    height: Optional[float] = Field(default=None, description="""Height of the channel in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'height', 'domain_of': ['ChannelDimensions']} })
    length: Optional[float] = Field(default=None, description="""Length of the channel in millimeters""", json_schema_extra = { "linkml_meta": {'alias': 'length', 'domain_of': ['ChannelDimensions']} })


class MechanicalStimulation(NamedThing):
    """
    Specification of mechanical forces applied to the model system
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    stimulation_type: Optional[list[MechanicalStimulationTypeEnum]] = Field(default=None, description="""Type of mechanical stimulation applied""", json_schema_extra = { "linkml_meta": {'alias': 'stimulation_type', 'domain_of': ['MechanicalStimulation']} })
    cyclic_stretch_percent: Optional[float] = Field(default=None, description="""Percentage of cyclic stretch applied (if applicable)""", json_schema_extra = { "linkml_meta": {'alias': 'cyclic_stretch_percent', 'domain_of': ['MechanicalStimulation']} })
    frequency_hz: Optional[float] = Field(default=None, description="""Frequency of mechanical stimulation in Hertz""", json_schema_extra = { "linkml_meta": {'alias': 'frequency_hz', 'domain_of': ['MechanicalStimulation']} })
    shear_stress: Optional[float] = Field(default=None, description="""Shear stress applied in dyn/cm²""", json_schema_extra = { "linkml_meta": {'alias': 'shear_stress', 'domain_of': ['MechanicalStimulation']} })
    pressure_pascal: Optional[float] = Field(default=None, description="""Pressure applied in Pascals""", json_schema_extra = { "linkml_meta": {'alias': 'pressure_pascal', 'domain_of': ['MechanicalStimulation']} })
    duration_minutes: Optional[float] = Field(default=None, description="""Duration of mechanical stimulation in minutes""", json_schema_extra = { "linkml_meta": {'alias': 'duration_minutes', 'domain_of': ['MechanicalStimulation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["MechanicalStimulation"] = Field(default="MechanicalStimulation", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class BiologicalSystem(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["BiologicalSystem"] = Field(default="BiologicalSystem", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class ModelsRelationship(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    biological_system_modeled: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'biological_system_modeled', 'domain_of': ['ModelsRelationship']} })
    is_computed: Optional[bool] = Field(default=None, description="""Indicates whether the model is computed or derived from experimental data.""", json_schema_extra = { "linkml_meta": {'alias': 'is_computed', 'domain_of': ['ModelsRelationship']} })
    concordance: Optional[ConcordanceResult] = Field(default=None, description="""Metrics used to assess the concordance between the model system and the biological system, such as sensitivity, specificity, and accuracy.""", json_schema_extra = { "linkml_meta": {'alias': 'concordance', 'domain_of': ['ModelsRelationship']} })
    structured_concordance: Optional[StructuredConcordanceResult] = Field(default=None, description="""Detailed structured assessment of concordance between the model system and the biological system, with rich metadata and supporting evidence.""", json_schema_extra = { "linkml_meta": {'alias': 'structured_concordance', 'domain_of': ['ModelsRelationship']} })


class ConcordanceResult(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    phenotype_overlap: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'phenotype_overlap',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    molecular_similarity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'molecular_similarity',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    pathway_concordance: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pathway_concordance',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    cell_type_coverage: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cell_type_coverage',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    functional_parity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'functional_parity',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    reproducibility: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'reproducibility',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })


class StructuredConcordanceResult(ConfiguredBaseModel):
    """
    Detailed structured assessment of concordance between model and biological systems with rich metadata, evidence, and quantitative measures.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    molecular_similarity: Optional[MolecularSimilarity] = Field(default=None, description="""Detailed assessment of molecular-level similarity including gene expression, protein levels, and metabolic profiles.""", json_schema_extra = { "linkml_meta": {'alias': 'molecular_similarity',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    pathway_concordance: Optional[PathwayConcordance] = Field(default=None, description="""Assessment of biological pathway conservation and activity levels.""", json_schema_extra = { "linkml_meta": {'alias': 'pathway_concordance',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    phenotype_overlap: Optional[PhenotypeOverlap] = Field(default=None, description="""Comparison of phenotypic manifestations between model and biological system.""", json_schema_extra = { "linkml_meta": {'alias': 'phenotype_overlap',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    cell_type_coverage: Optional[CellTypeCoverage] = Field(default=None, description="""Assessment of cell type representation and cellular diversity.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type_coverage',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    functional_parity: Optional[FunctionalParity] = Field(default=None, description="""Evaluation of functional capabilities and physiological responses.""", json_schema_extra = { "linkml_meta": {'alias': 'functional_parity',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })
    reproducibility: Optional[Reproducibility] = Field(default=None, description="""Assessment of experimental reproducibility and consistency.""", json_schema_extra = { "linkml_meta": {'alias': 'reproducibility',
         'domain_of': ['ConcordanceResult', 'StructuredConcordanceResult']} })


class MolecularSimilarity(NamedThing):
    """
    Detailed assessment of molecular-level concordance between model and biological systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    similarity_score: Optional[float] = Field(default=None, description="""Quantitative similarity score (0.0-1.0) based on molecular profiles.""", json_schema_extra = { "linkml_meta": {'alias': 'similarity_score', 'domain_of': ['MolecularSimilarity']} })
    correlation_coefficient: Optional[float] = Field(default=None, description="""Pearson correlation coefficient for expression profiles.""", json_schema_extra = { "linkml_meta": {'alias': 'correlation_coefficient',
         'domain_of': ['MolecularSimilarity', 'DoseResponseSimilarity']} })
    differentially_expressed_genes: Optional[list[Gene]] = Field(default=None, description="""List of genes that are differentially expressed in the model system.""", json_schema_extra = { "linkml_meta": {'alias': 'differentially_expressed_genes',
         'domain_of': ['MolecularSimilarity']} })
    conserved_genes: Optional[list[Gene]] = Field(default=None, description="""List of genes with conserved expression patterns between model and target.""", json_schema_extra = { "linkml_meta": {'alias': 'conserved_genes', 'domain_of': ['MolecularSimilarity']} })
    methodology: Optional[str] = Field(default=None, description="""Description of experimental methods used for molecular comparison.""", json_schema_extra = { "linkml_meta": {'alias': 'methodology',
         'domain_of': ['MolecularSimilarity', 'FunctionalAssay']} })
    data_source: Optional[str] = Field(default=None, description="""Source of molecular data (e.g., RNA-seq, proteomics, metabolomics).""", json_schema_extra = { "linkml_meta": {'alias': 'data_source', 'domain_of': ['MolecularSimilarity']} })
    statistical_significance: Optional[StatisticalSignificance] = Field(default=None, description="""Statistical measures of significance for the molecular similarity.""", json_schema_extra = { "linkml_meta": {'alias': 'statistical_significance', 'domain_of': ['MolecularSimilarity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["MolecularSimilarity"] = Field(default="MolecularSimilarity", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class PathwayConcordance(NamedThing):
    """
    Assessment of biological pathway conservation and activity between model and biological systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    pathway_overlap_score: Optional[float] = Field(default=None, description="""Quantitative score (0.0-1.0) representing pathway overlap.""", json_schema_extra = { "linkml_meta": {'alias': 'pathway_overlap_score', 'domain_of': ['PathwayConcordance']} })
    active_pathways: Optional[list[Pathway]] = Field(default=None, description="""List of biological pathways that are active in both systems.""", json_schema_extra = { "linkml_meta": {'alias': 'active_pathways', 'domain_of': ['PathwayConcordance']} })
    divergent_pathways: Optional[list[Pathway]] = Field(default=None, description="""List of pathways that show different activity patterns.""", json_schema_extra = { "linkml_meta": {'alias': 'divergent_pathways', 'domain_of': ['PathwayConcordance']} })
    pathway_analysis_method: Optional[str] = Field(default=None, description="""Method used for pathway analysis (e.g., GSEA, Over-representation analysis).""", json_schema_extra = { "linkml_meta": {'alias': 'pathway_analysis_method', 'domain_of': ['PathwayConcordance']} })
    enrichment_statistics: Optional[list[EnrichmentStatistics]] = Field(default=None, description="""Statistical measures of pathway enrichment.""", json_schema_extra = { "linkml_meta": {'alias': 'enrichment_statistics', 'domain_of': ['PathwayConcordance']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["PathwayConcordance"] = Field(default="PathwayConcordance", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class PhenotypeOverlap(NamedThing):
    """
    Comparison of phenotypic manifestations between model and biological systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    phenotype_similarity_score: Optional[float] = Field(default=None, description="""Quantitative score (0.0-1.0) representing phenotypic similarity.""", json_schema_extra = { "linkml_meta": {'alias': 'phenotype_similarity_score', 'domain_of': ['PhenotypeOverlap']} })
    shared_phenotypes: Optional[list[Term]] = Field(default=None, description="""List of phenotypes present in both model and biological system.""", json_schema_extra = { "linkml_meta": {'alias': 'shared_phenotypes', 'domain_of': ['PhenotypeOverlap']} })
    model_specific_phenotypes: Optional[list[Term]] = Field(default=None, description="""List of phenotypes present only in the model system.""", json_schema_extra = { "linkml_meta": {'alias': 'model_specific_phenotypes', 'domain_of': ['PhenotypeOverlap']} })
    biological_specific_phenotypes: Optional[list[Term]] = Field(default=None, description="""List of phenotypes present only in the biological system.""", json_schema_extra = { "linkml_meta": {'alias': 'biological_specific_phenotypes', 'domain_of': ['PhenotypeOverlap']} })
    phenotype_ontology: Optional[str] = Field(default=None, description="""Ontology used for phenotype classification (e.g., HPO, MP).""", json_schema_extra = { "linkml_meta": {'alias': 'phenotype_ontology', 'domain_of': ['PhenotypeOverlap']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["PhenotypeOverlap"] = Field(default="PhenotypeOverlap", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class CellTypeCoverage(NamedThing):
    """
    Assessment of cell type representation and cellular diversity between systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    coverage_percentage: Optional[float] = Field(default=None, description="""Percentage of target cell types represented in the model system.""", json_schema_extra = { "linkml_meta": {'alias': 'coverage_percentage', 'domain_of': ['CellTypeCoverage']} })
    represented_cell_types: Optional[list[Term]] = Field(default=None, description="""List of cell types present in both model and biological system.""", json_schema_extra = { "linkml_meta": {'alias': 'represented_cell_types', 'domain_of': ['CellTypeCoverage']} })
    missing_cell_types: Optional[list[Term]] = Field(default=None, description="""List of cell types present in biological system but missing in model.""", json_schema_extra = { "linkml_meta": {'alias': 'missing_cell_types', 'domain_of': ['CellTypeCoverage']} })
    cell_type_proportions: Optional[list[CellTypeProportion]] = Field(default=None, description="""Quantitative comparison of cell type proportions.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type_proportions', 'domain_of': ['CellTypeCoverage']} })
    single_cell_method: Optional[str] = Field(default=None, description="""Method used for single-cell analysis (e.g., scRNA-seq, flow cytometry).""", json_schema_extra = { "linkml_meta": {'alias': 'single_cell_method', 'domain_of': ['CellTypeCoverage']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["CellTypeCoverage"] = Field(default="CellTypeCoverage", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class FunctionalParity(NamedThing):
    """
    Evaluation of functional capabilities and physiological responses between systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    functional_similarity_score: Optional[float] = Field(default=None, description="""Quantitative score (0.0-1.0) representing functional similarity.""", json_schema_extra = { "linkml_meta": {'alias': 'functional_similarity_score', 'domain_of': ['FunctionalParity']} })
    conserved_functions: Optional[list[str]] = Field(default=None, description="""List of biological functions conserved between model and biological system.""", json_schema_extra = { "linkml_meta": {'alias': 'conserved_functions', 'domain_of': ['FunctionalParity']} })
    impaired_functions: Optional[list[str]] = Field(default=None, description="""List of functions that are impaired or absent in the model system.""", json_schema_extra = { "linkml_meta": {'alias': 'impaired_functions', 'domain_of': ['FunctionalParity']} })
    functional_assays: Optional[list[FunctionalAssay]] = Field(default=None, description="""List of functional assays used to assess parity.""", json_schema_extra = { "linkml_meta": {'alias': 'functional_assays', 'domain_of': ['FunctionalParity']} })
    dose_response_similarity: Optional[DoseResponseSimilarity] = Field(default=None, description="""Comparison of dose-response relationships for therapeutic compounds.""", json_schema_extra = { "linkml_meta": {'alias': 'dose_response_similarity', 'domain_of': ['FunctionalParity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["FunctionalParity"] = Field(default="FunctionalParity", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class Reproducibility(NamedThing):
    """
    Assessment of experimental reproducibility and consistency of the model system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    reproducibility_score: Optional[float] = Field(default=None, description="""Quantitative score (0.0-1.0) representing reproducibility.""", json_schema_extra = { "linkml_meta": {'alias': 'reproducibility_score', 'domain_of': ['Reproducibility']} })
    coefficient_of_variation: Optional[float] = Field(default=None, description="""Coefficient of variation across experimental replicates.""", json_schema_extra = { "linkml_meta": {'alias': 'coefficient_of_variation', 'domain_of': ['Reproducibility']} })
    batch_to_batch_variation: Optional[float] = Field(default=None, description="""Measure of variation between different experimental batches.""", json_schema_extra = { "linkml_meta": {'alias': 'batch_to_batch_variation', 'domain_of': ['Reproducibility']} })
    inter_laboratory_consistency: Optional[float] = Field(default=None, description="""Measure of consistency across different laboratories.""", json_schema_extra = { "linkml_meta": {'alias': 'inter_laboratory_consistency', 'domain_of': ['Reproducibility']} })
    replicate_count: Optional[int] = Field(default=None, description="""Number of experimental replicates used in assessment.""", json_schema_extra = { "linkml_meta": {'alias': 'replicate_count', 'domain_of': ['Reproducibility']} })
    quality_control_metrics: Optional[list[QualityControlMetric]] = Field(default=None, description="""List of quality control measures and their values.""", json_schema_extra = { "linkml_meta": {'alias': 'quality_control_metrics', 'domain_of': ['Reproducibility']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["Reproducibility"] = Field(default="Reproducibility", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class Gene(NamedThing):
    """
    A gene entity with identifiers and expression information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    gene_symbol: Optional[str] = Field(default=None, description="""Standard gene symbol (e.g., HGNC symbol for human genes).""", json_schema_extra = { "linkml_meta": {'alias': 'gene_symbol', 'domain_of': ['Gene']} })
    ensembl_id: Optional[str] = Field(default=None, description="""Ensembl gene identifier.""", json_schema_extra = { "linkml_meta": {'alias': 'ensembl_id', 'domain_of': ['Gene']} })
    entrez_id: Optional[int] = Field(default=None, description="""NCBI Entrez gene identifier.""", json_schema_extra = { "linkml_meta": {'alias': 'entrez_id', 'domain_of': ['Gene']} })
    fold_change: Optional[float] = Field(default=None, description="""Fold change in expression compared to control or reference.""", json_schema_extra = { "linkml_meta": {'alias': 'fold_change', 'domain_of': ['Gene']} })
    p_value: Optional[float] = Field(default=None, description="""Statistical p-value for differential expression.""", json_schema_extra = { "linkml_meta": {'alias': 'p_value',
         'domain_of': ['Gene', 'StatisticalSignificance', 'EnrichmentStatistics']} })
    adjusted_p_value: Optional[float] = Field(default=None, description="""Multiple testing corrected p-value.""", json_schema_extra = { "linkml_meta": {'alias': 'adjusted_p_value', 'domain_of': ['Gene', 'StatisticalSignificance']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["Gene"] = Field(default="Gene", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class Pathway(NamedThing):
    """
    A biological pathway with activity and enrichment information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    pathway_database: Optional[str] = Field(default=None, description="""Source database (e.g., KEGG, Reactome, GO).""", json_schema_extra = { "linkml_meta": {'alias': 'pathway_database', 'domain_of': ['Pathway']} })
    pathway_id: Optional[str] = Field(default=None, description="""Database-specific pathway identifier.""", json_schema_extra = { "linkml_meta": {'alias': 'pathway_id', 'domain_of': ['Pathway']} })
    activity_score: Optional[float] = Field(default=None, description="""Quantitative measure of pathway activity.""", json_schema_extra = { "linkml_meta": {'alias': 'activity_score', 'domain_of': ['Pathway']} })
    enrichment_score: Optional[float] = Field(default=None, description="""Statistical enrichment score for the pathway.""", json_schema_extra = { "linkml_meta": {'alias': 'enrichment_score', 'domain_of': ['Pathway', 'EnrichmentStatistics']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["Pathway"] = Field(default="Pathway", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class StatisticalSignificance(ConfiguredBaseModel):
    """
    Statistical measures of significance for molecular comparisons.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    p_value: Optional[float] = Field(default=None, description="""Statistical p-value.""", json_schema_extra = { "linkml_meta": {'alias': 'p_value',
         'domain_of': ['Gene', 'StatisticalSignificance', 'EnrichmentStatistics']} })
    adjusted_p_value: Optional[float] = Field(default=None, description="""Multiple testing corrected p-value.""", json_schema_extra = { "linkml_meta": {'alias': 'adjusted_p_value', 'domain_of': ['Gene', 'StatisticalSignificance']} })
    confidence_interval_lower: Optional[float] = Field(default=None, description="""Lower bound of confidence interval.""", json_schema_extra = { "linkml_meta": {'alias': 'confidence_interval_lower', 'domain_of': ['StatisticalSignificance']} })
    confidence_interval_upper: Optional[float] = Field(default=None, description="""Upper bound of confidence interval.""", json_schema_extra = { "linkml_meta": {'alias': 'confidence_interval_upper', 'domain_of': ['StatisticalSignificance']} })
    statistical_test: Optional[str] = Field(default=None, description="""Name of statistical test used.""", json_schema_extra = { "linkml_meta": {'alias': 'statistical_test', 'domain_of': ['StatisticalSignificance']} })


class EnrichmentStatistics(ConfiguredBaseModel):
    """
    Statistical measures for pathway enrichment analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    enrichment_score: Optional[float] = Field(default=None, description="""Quantitative enrichment score.""", json_schema_extra = { "linkml_meta": {'alias': 'enrichment_score', 'domain_of': ['Pathway', 'EnrichmentStatistics']} })
    p_value: Optional[float] = Field(default=None, description="""Statistical p-value for enrichment.""", json_schema_extra = { "linkml_meta": {'alias': 'p_value',
         'domain_of': ['Gene', 'StatisticalSignificance', 'EnrichmentStatistics']} })
    q_value: Optional[float] = Field(default=None, description="""False discovery rate corrected p-value.""", json_schema_extra = { "linkml_meta": {'alias': 'q_value', 'domain_of': ['EnrichmentStatistics']} })
    genes_in_pathway: Optional[int] = Field(default=None, description="""Number of genes in the pathway.""", json_schema_extra = { "linkml_meta": {'alias': 'genes_in_pathway', 'domain_of': ['EnrichmentStatistics']} })
    genes_in_dataset: Optional[int] = Field(default=None, description="""Number of genes from dataset found in pathway.""", json_schema_extra = { "linkml_meta": {'alias': 'genes_in_dataset', 'domain_of': ['EnrichmentStatistics']} })


class CellTypeProportion(ConfiguredBaseModel):
    """
    Quantitative comparison of cell type proportions between systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    cell_type: Optional[Term] = Field(default=None, description="""The cell type being compared.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type', 'domain_of': ['CellRatio', 'CellTypeProportion']} })
    model_proportion: Optional[float] = Field(default=None, description="""Proportion of this cell type in the model system.""", json_schema_extra = { "linkml_meta": {'alias': 'model_proportion', 'domain_of': ['CellTypeProportion']} })
    biological_proportion: Optional[float] = Field(default=None, description="""Proportion of this cell type in the biological system.""", json_schema_extra = { "linkml_meta": {'alias': 'biological_proportion', 'domain_of': ['CellTypeProportion']} })
    proportion_ratio: Optional[float] = Field(default=None, description="""Ratio of model to biological proportions.""", json_schema_extra = { "linkml_meta": {'alias': 'proportion_ratio', 'domain_of': ['CellTypeProportion']} })


class FunctionalAssay(NamedThing):
    """
    A functional assay used to assess biological capabilities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    assay_type: Optional[str] = Field(default=None, description="""Type of functional assay (e.g., TEER, permeability, metabolic activity).""", json_schema_extra = { "linkml_meta": {'alias': 'assay_type', 'domain_of': ['FunctionalAssay']} })
    assay_result: Optional[float] = Field(default=None, description="""Quantitative result of the assay.""", json_schema_extra = { "linkml_meta": {'alias': 'assay_result', 'domain_of': ['FunctionalAssay']} })
    reference_value: Optional[float] = Field(default=None, description="""Reference or control value for comparison.""", json_schema_extra = { "linkml_meta": {'alias': 'reference_value', 'domain_of': ['FunctionalAssay']} })
    units: Optional[str] = Field(default=None, description="""Units of measurement for the assay result.""", json_schema_extra = { "linkml_meta": {'alias': 'units', 'domain_of': ['FunctionalAssay']} })
    methodology: Optional[str] = Field(default=None, description="""Detailed methodology for the assay.""", json_schema_extra = { "linkml_meta": {'alias': 'methodology',
         'domain_of': ['MolecularSimilarity', 'FunctionalAssay']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["FunctionalAssay"] = Field(default="FunctionalAssay", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


class DoseResponseSimilarity(ConfiguredBaseModel):
    """
    Comparison of dose-response relationships between model and biological systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    correlation_coefficient: Optional[float] = Field(default=None, description="""Correlation coefficient between dose-response curves.""", json_schema_extra = { "linkml_meta": {'alias': 'correlation_coefficient',
         'domain_of': ['MolecularSimilarity', 'DoseResponseSimilarity']} })
    ec50_ratio: Optional[float] = Field(default=None, description="""Ratio of EC50 values between model and biological system.""", json_schema_extra = { "linkml_meta": {'alias': 'ec50_ratio', 'domain_of': ['DoseResponseSimilarity']} })
    max_response_ratio: Optional[float] = Field(default=None, description="""Ratio of maximum responses between systems.""", json_schema_extra = { "linkml_meta": {'alias': 'max_response_ratio', 'domain_of': ['DoseResponseSimilarity']} })
    compound_tested: Optional[str] = Field(default=None, description="""Name of compound used in dose-response testing.""", json_schema_extra = { "linkml_meta": {'alias': 'compound_tested', 'domain_of': ['DoseResponseSimilarity']} })


class QualityControlMetric(ConfiguredBaseModel):
    """
    A quality control measure and its associated value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    metric_name: Optional[str] = Field(default=None, description="""Name of the quality control metric.""", json_schema_extra = { "linkml_meta": {'alias': 'metric_name', 'domain_of': ['QualityControlMetric']} })
    metric_value: Optional[float] = Field(default=None, description="""Value of the quality control metric.""", json_schema_extra = { "linkml_meta": {'alias': 'metric_value', 'domain_of': ['QualityControlMetric']} })
    threshold: Optional[float] = Field(default=None, description="""Acceptable threshold for this metric.""", json_schema_extra = { "linkml_meta": {'alias': 'threshold', 'domain_of': ['QualityControlMetric']} })
    pass_fail_status: Optional[bool] = Field(default=None, description="""Whether this metric passes quality control criteria.""", json_schema_extra = { "linkml_meta": {'alias': 'pass_fail_status', 'domain_of': ['QualityControlMetric']} })


class Reference(ConfiguredBaseModel):
    """
    A literature reference with identifier and title for citing published work.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    id: str = Field(default=..., description="""Persistent identifier for the reference (DOI, PMID, PMCID, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing', 'Reference']} })
    title: str = Field(default=..., description="""Title of the referenced publication or dataset""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Reference']} })
    authors: Optional[list[str]] = Field(default=None, description="""Authors of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'authors', 'domain_of': ['Reference']} })
    journal: Optional[str] = Field(default=None, description="""Journal or publication venue""", json_schema_extra = { "linkml_meta": {'alias': 'journal', 'domain_of': ['Reference']} })
    year: Optional[int] = Field(default=None, description="""Publication year""", json_schema_extra = { "linkml_meta": {'alias': 'year', 'domain_of': ['Reference']} })
    url: Optional[str] = Field(default=None, description="""URL to access the publication""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Reference']} })


class Term(NamedThing):
    """
    A term is a concept or entity that can be defined and used in a specific context, often within a controlled vocabulary or ontology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/monarch-initiative/namo'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Reference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    type: Literal["Term"] = Field(default="Term", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['NamedThing']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Dataset.model_rebuild()
NamedThing.model_rebuild()
Study.model_rebuild()
ModelSystem.model_rebuild()
AnimalModel.model_rebuild()
NAMModel.model_rebuild()
CellularSystem.model_rebuild()
TwoDCellCulture.model_rebuild()
ThreeDCellCulture.model_rebuild()
CoCulture.model_rebuild()
Organoid.model_rebuild()
CellLineModel.model_rebuild()
MicrophysiologicalSystem.model_rebuild()
OrganOnChip.model_rebuild()
TissueOnChip.model_rebuild()
InSilicoModel.model_rebuild()
QSARModel.model_rebuild()
PBPKModel.model_rebuild()
DigitalTwin.model_rebuild()
MLModel.model_rebuild()
MetabolicModel.model_rebuild()
CellRatio.model_rebuild()
ModelPerformance.model_rebuild()
PBPKCompartment.model_rebuild()
DrugProperties.model_rebuild()
CrossValidation.model_rebuild()
MicrofluidicDesign.model_rebuild()
ChannelDimensions.model_rebuild()
MechanicalStimulation.model_rebuild()
BiologicalSystem.model_rebuild()
ModelsRelationship.model_rebuild()
ConcordanceResult.model_rebuild()
StructuredConcordanceResult.model_rebuild()
MolecularSimilarity.model_rebuild()
PathwayConcordance.model_rebuild()
PhenotypeOverlap.model_rebuild()
CellTypeCoverage.model_rebuild()
FunctionalParity.model_rebuild()
Reproducibility.model_rebuild()
Gene.model_rebuild()
Pathway.model_rebuild()
StatisticalSignificance.model_rebuild()
EnrichmentStatistics.model_rebuild()
CellTypeProportion.model_rebuild()
FunctionalAssay.model_rebuild()
DoseResponseSimilarity.model_rebuild()
QualityControlMetric.model_rebuild()
Reference.model_rebuild()
Term.model_rebuild()

