# Auto generated from namo.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-20T11:54:58
# Schema: namo
#
# id: https://w3id.org/monarch-initiative/namo
# description: NAMO (New Approach Methodology Ontology) is a comprehensive schema for representing diverse
#   in vitro and in silico model systems used as alternatives to traditional animal testing.
#   It supports organoids, organ-on-chip systems, 3D cell cultures, computational models, and
#   other New Approach Methodologies (NAMs) used in toxicology, drug discovery, and biomedical research.
#
#   ## Schema Organization
#
#   The schema follows a hierarchical structure that mirrors how NAM research is organized and conducted:
#
#   The top-level entity is a [Dataset](Dataset.md), which serves as a container for related research
#   activities. A dataset might represent all NAM models from a specific laboratory, regulatory study,
#   or collaborative research program.
#
#   Each dataset contains one or more [Studies](Study.md), which are focused investigations using
#   specific NAM approaches. For example, a study might investigate "Hepatotoxicity screening using
#   liver organoids" or "Multi-organ drug ADMET assessment using microphysiological systems."
#
#   Within each study, you'll find:
#
#   ### Model Systems
#   The core of NAMO is the representation of different [NAM model types](NAMModel.md):
#
#   - **[Organoids](Organoid.md)**: Self-organizing 3D tissue models derived from stem cells that
#     recapitulate organ-specific architecture and function. Examples include brain organoids for
#     neurotoxicity testing, intestinal organoids for drug absorption studies, and liver organoids
#     for metabolism research.
#
#   - **[Organ-on-Chip Systems](OrganOnChip.md)**: Microfluidic devices that simulate organ-level
#     physiology with precise control over cellular microenvironment. These include lung-on-chip
#     for inhalation toxicology, heart-on-chip for cardiotoxicity assessment, and multi-organ
#     chips for systemic drug effects.
#
#   - **[Tissue-on-Chip Systems](TissueOnChip.md)**: Microfluidic models focused on specific tissue
#     functions such as blood-brain barrier chips, skin models for dermatological testing, and
#     kidney proximal tubule chips for nephrotoxicity screening.
#
#   - **[3D Cell Cultures](ThreeDCellCulture.md)**: Three-dimensional cell culture systems including
#     spheroids, scaffold-based cultures, and bioengineered tissues that provide more physiologically
#     relevant environments than traditional 2D cultures.
#
#   - **[2D Cell Cultures](TwoDCellCulture.md)**: Monolayer cell culture systems with specialized
#     configurations, substrates, and culture conditions optimized for specific applications.
#
#   - **[Co-Culture Systems](CoCulture.md)**: Multi-cell-type culture systems that model cellular
#     interactions, tissue interfaces, and organ-level communication pathways.
#
#   ### Computational Models
#   NAMO supports various in silico approaches:
#
#   - **[Machine Learning Models](MLModel.md)**: AI/ML systems for toxicity prediction, including
#     deep learning models for chemical structure-activity relationships, neural networks for
#     dose-response modeling, and ensemble methods for multi-endpoint prediction.
#
#   - **[QSAR Models](QSARModel.md)**: Quantitative Structure-Activity Relationship models that
#     predict biological activity from molecular structure, including traditional statistical
#     approaches and modern machine learning implementations.
#
#   - **[PBPK Models](PBPKModel.md)**: Physiologically-based pharmacokinetic models that simulate
#     drug absorption, distribution, metabolism, and excretion using mathematical representations
#     of biological processes.
#
#   - **[Digital Twins](DigitalTwin.md)**: Integrated computational models that combine multiple
#     data sources and modeling approaches to create personalized, real-time simulations of
#     biological systems.
#
#   - **[Metabolic Models](MetabolicModel.md)**: Systems biology models of cellular metabolism,
#     including flux balance analysis, kinetic modeling, and constraint-based approaches for
#     understanding metabolic perturbations.
#
#   ### Technical Specifications
#
#   #### Microfluidic Design
#   For chip-based systems, detailed [microfluidic design](MicrofluidicDesign.md) specifications
#   capture device architecture, including channel configurations, flow control methods, sensor
#   integration, and material properties essential for reproducibility and standardization.
#
#   #### Validation and Concordance
#   NAMO emphasizes validation through [structured concordance analysis](StructuredConcordanceResult.md):
#
#   - **[Molecular Similarity](MolecularSimilarity.md)**: Gene expression profiles, protein markers,
#     and metabolomic signatures compared to reference biological systems
#   - **[Functional Parity](FunctionalParity.md)**: Physiological responses, barrier functions,
#     and cellular behaviors that match in vivo counterparts
#   - **[Reproducibility](Reproducibility.md)**: Inter-laboratory consistency, batch-to-batch
#     variation, and quality control metrics
#
#   #### Performance Metrics
#   Quantitative assessment through standardized [functional assays](FunctionalAssay.md) that
#   measure model performance, sensitivity, specificity, and predictive accuracy against known
#   outcomes and regulatory endpoints.
#
#   ## Use Cases
#
#   NAMO supports diverse applications across multiple domains:
#
#   ### Regulatory Toxicology
#   - **Chemical Safety Assessment**: Systematic evaluation of chemical toxicity using integrated
#     NAM approaches, supporting regulatory submissions to EPA, FDA, and ECHA
#   - **Cosmetics Testing**: Non-animal approaches for skin sensitization, eye irritation, and
#     systemic toxicity assessment as required by regulations worldwide
#   - **Pesticide Evaluation**: Environmental and human health risk assessment using NAMs for
#     neurotoxicity, endocrine disruption, and developmental toxicity endpoints
#
#   ### Pharmaceutical Development
#   - **Drug Discovery**: Early-stage compound screening using organ-specific models to identify
#     promising candidates and eliminate toxic compounds
#   - **ADMET Profiling**: Absorption, Distribution, Metabolism, Excretion, and Toxicity assessment
#     using integrated organ-on-chip platforms and computational models
#   - **Precision Medicine**: Patient-derived organoids and digital twins for personalized drug
#     selection and dosing strategies
#
#   ### Academic Research
#   - **Disease Modeling**: Patient-specific organoids for studying rare diseases, cancer biology,
#     and genetic disorders in controlled laboratory environments
#   - **Mechanistic Studies**: Investigation of toxicity pathways, cellular responses, and
#     molecular mechanisms using well-characterized NAM systems
#   - **Method Development**: Innovation in NAM technologies, validation approaches, and
#     standardization protocols
#
#   ## Key Features
#
#   - **Multi-Modal Integration**: Support for combining multiple NAM approaches in integrated
#     testing strategies (ITS) and adverse outcome pathways (AOPs)
#   - **Standardization Focus**: Emphasis on reproducibility, quality control, and inter-laboratory
#     harmonization essential for regulatory acceptance
#   - **Literature Integration**: Comprehensive [reference](Reference.md) system linking models
#     to peer-reviewed publications, regulatory guidance, and validation studies
#   - **Ontology Alignment**: Integration with established ontologies including UBERON (anatomy),
#     CL (cell types), CHEBI (chemicals), and OBI (biomedical investigations)
#
#   For detailed curation guidelines, see:
#   - [How to Curate Organoid Papers](https://monarch-initiative.github.io/namo/how-to/curate-organoid-paper/)
#   - [How to Curate Organ-on-Chip Papers](https://monarch-initiative.github.io/namo/how-to/curate-organ-on-chip-paper/)
#
#   ## Community and Standards
#
#   NAMO is developed in collaboration with the NAM research community, regulatory agencies, and
#   standards organizations including OECD, ICCVAM, and ESTIV. It supports the 3Rs principles
#   (Replacement, Reduction, Refinement) and contributes to the transition toward animal-free
#   testing methodologies in safety assessment and biomedical research.
#
# license: BSD-3-Clause

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/EFO_')
MAMO = CurieNamespace('MAMO', 'http://identifiers.org/mamo/MAMO_')
MESH = CurieNamespace('MESH', 'http://id.nlm.nih.gov/mesh/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NAMO = CurieNamespace('namo', 'https://w3id.org/monarch-initiative/namo/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = NAMO


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class StudyId(NamedThingId):
    pass


class ModelSystemId(NamedThingId):
    pass


class AnimalModelId(ModelSystemId):
    pass


class NAMModelId(ModelSystemId):
    pass


class CellularSystemId(NAMModelId):
    pass


class TwoDCellCultureId(CellularSystemId):
    pass


class ThreeDCellCultureId(CellularSystemId):
    pass


class CoCultureId(CellularSystemId):
    pass


class OrganoidId(ThreeDCellCultureId):
    pass


class CellLineModelId(TwoDCellCultureId):
    pass


class MicrophysiologicalSystemId(NAMModelId):
    pass


class OrganOnChipId(MicrophysiologicalSystemId):
    pass


class TissueOnChipId(MicrophysiologicalSystemId):
    pass


class InSilicoModelId(NAMModelId):
    pass


class QSARModelId(InSilicoModelId):
    pass


class PBPKModelId(InSilicoModelId):
    pass


class DigitalTwinId(InSilicoModelId):
    pass


class MLModelId(InSilicoModelId):
    pass


class MetabolicModelId(InSilicoModelId):
    pass


class PBPKCompartmentId(NamedThingId):
    pass


class MicrofluidicDesignId(NamedThingId):
    pass


class MechanicalStimulationId(NamedThingId):
    pass


class BiologicalSystemId(NamedThingId):
    pass


class MolecularSimilarityId(NamedThingId):
    pass


class PathwayConcordanceId(NamedThingId):
    pass


class PhenotypeOverlapId(NamedThingId):
    pass


class CellTypeCoverageId(NamedThingId):
    pass


class FunctionalParityId(NamedThingId):
    pass


class ReproducibilityId(NamedThingId):
    pass


class GeneId(NamedThingId):
    pass


class PathwayId(NamedThingId):
    pass


class FunctionalAssayId(NamedThingId):
    pass


class ReferenceId(URIorCURIE):
    pass


class TermId(NamedThingId):
    pass


@dataclass(repr=False)
class Dataset(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["Dataset"]
    class_class_curie: ClassVar[str] = "namo:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = NAMO.Dataset

    model_systems: Optional[Union[dict[Union[str, ModelSystemId], Union[dict, "ModelSystem"]], list[Union[dict, "ModelSystem"]]]] = empty_dict()
    studies: Optional[Union[dict[Union[str, StudyId], Union[dict, "Study"]], list[Union[dict, "Study"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="model_systems", slot_type=ModelSystem, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = NAMO.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class Study(NamedThing):
    """
    A study is a structured investigation or analysis, often involving the collection and interpretation of data, to
    answer specific research questions or test hypotheses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["Study"]
    class_class_curie: ClassVar[str] = "namo:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = NAMO.Study

    id: Union[str, StudyId] = None
    context_of_use: Optional[str] = None
    biological_context: Optional[str] = None
    perturbations: Optional[str] = None
    endpoints: Optional[str] = None
    plan_comparators: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self.context_of_use is not None and not isinstance(self.context_of_use, str):
            self.context_of_use = str(self.context_of_use)

        if self.biological_context is not None and not isinstance(self.biological_context, str):
            self.biological_context = str(self.biological_context)

        if self.perturbations is not None and not isinstance(self.perturbations, str):
            self.perturbations = str(self.perturbations)

        if self.endpoints is not None and not isinstance(self.endpoints, str):
            self.endpoints = str(self.endpoints)

        if self.plan_comparators is not None and not isinstance(self.plan_comparators, str):
            self.plan_comparators = str(self.plan_comparators)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class ModelSystem(NamedThing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["ModelSystem"]
    class_class_curie: ClassVar[str] = "namo:ModelSystem"
    class_name: ClassVar[str] = "ModelSystem"
    class_model_uri: ClassVar[URIRef] = NAMO.ModelSystem

    id: Union[str, ModelSystemId] = None
    models: Optional[Union[Union[dict, "ModelsRelationship"], list[Union[dict, "ModelsRelationship"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.models, list):
            self.models = [self.models] if self.models is not None else []
        self.models = [v if isinstance(v, ModelsRelationship) else ModelsRelationship(**as_dict(v)) for v in self.models]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class AnimalModel(ModelSystem):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["AnimalModel"]
    class_class_curie: ClassVar[str] = "namo:AnimalModel"
    class_name: ClassVar[str] = "AnimalModel"
    class_model_uri: ClassVar[URIRef] = NAMO.AnimalModel

    id: Union[str, AnimalModelId] = None
    species: Union[str, TermId] = None
    strain: Optional[Union[str, TermId]] = None
    age: Optional[Union[str, TermId]] = None
    environment: Optional[Union[str, TermId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnimalModelId):
            self.id = AnimalModelId(self.id)

        if self._is_empty(self.species):
            self.MissingRequiredField("species")
        if not isinstance(self.species, TermId):
            self.species = TermId(self.species)

        if self.strain is not None and not isinstance(self.strain, TermId):
            self.strain = TermId(self.strain)

        if self.age is not None and not isinstance(self.age, TermId):
            self.age = TermId(self.age)

        if self.environment is not None and not isinstance(self.environment, TermId):
            self.environment = TermId(self.environment)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class NAMModel(ModelSystem):
    """
    A New Approach Methodology (NAM) model, which is a type of model system that does not involve the use of animals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["NAMModel"]
    class_class_curie: ClassVar[str] = "namo:NAMModel"
    class_name: ClassVar[str] = "NAMModel"
    class_model_uri: ClassVar[URIRef] = NAMO.NAMModel

    id: Union[str, NAMModelId] = None
    biological_organization_level: Optional[Union[str, "BiologicalOrganizationLevelEnum"]] = None
    spatial_context: Optional[str] = None
    complexity_level: Optional[Union[str, "ComplexityLevelEnum"]] = None
    references: Optional[Union[dict[Union[str, ReferenceId], Union[dict, "Reference"]], list[Union[dict, "Reference"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.biological_organization_level is not None and not isinstance(self.biological_organization_level, BiologicalOrganizationLevelEnum):
            self.biological_organization_level = BiologicalOrganizationLevelEnum(self.biological_organization_level)

        if self.spatial_context is not None and not isinstance(self.spatial_context, str):
            self.spatial_context = str(self.spatial_context)

        if self.complexity_level is not None and not isinstance(self.complexity_level, ComplexityLevelEnum):
            self.complexity_level = ComplexityLevelEnum(self.complexity_level)

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="id", keyed=True)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CellularSystem(NAMModel):
    """
    Cell-based model systems that use living cells to model biological processes. Includes 2D cultures, 3D systems,
    and co-cultures.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["CellularSystem"]
    class_class_curie: ClassVar[str] = "namo:CellularSystem"
    class_name: ClassVar[str] = "CellularSystem"
    class_model_uri: ClassVar[URIRef] = NAMO.CellularSystem

    id: Union[str, CellularSystemId] = None
    cell_types: Optional[Union[dict[Union[str, TermId], Union[dict, "Term"]], list[Union[dict, "Term"]]]] = empty_dict()
    cell_source: Optional[str] = None
    culture_conditions: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="cell_types", slot_type=Term, key_name="id", keyed=True)

        if self.cell_source is not None and not isinstance(self.cell_source, str):
            self.cell_source = str(self.cell_source)

        if self.culture_conditions is not None and not isinstance(self.culture_conditions, str):
            self.culture_conditions = str(self.culture_conditions)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class TwoDCellCulture(CellularSystem):
    """
    Conventional monolayer cell cultures grown on flat surfaces. Simple but limited in physiological relevance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["TwoDCellCulture"]
    class_class_curie: ClassVar[str] = "namo:TwoDCellCulture"
    class_name: ClassVar[str] = "TwoDCellCulture"
    class_model_uri: ClassVar[URIRef] = NAMO.TwoDCellCulture

    id: Union[str, TwoDCellCultureId] = None
    substrate_type: Optional[str] = None
    confluence_level: Optional[float] = None
    passage_protocol: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TwoDCellCultureId):
            self.id = TwoDCellCultureId(self.id)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.confluence_level is not None and not isinstance(self.confluence_level, float):
            self.confluence_level = float(self.confluence_level)

        if self.passage_protocol is not None and not isinstance(self.passage_protocol, str):
            self.passage_protocol = str(self.passage_protocol)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class ThreeDCellCulture(CellularSystem):
    """
    Three-dimensional cell culture systems including spheroids and organoids. More physiologically relevant with 3D
    architecture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["ThreeDCellCulture"]
    class_class_curie: ClassVar[str] = "namo:ThreeDCellCulture"
    class_name: ClassVar[str] = "ThreeDCellCulture"
    class_model_uri: ClassVar[URIRef] = NAMO.ThreeDCellCulture

    id: Union[str, ThreeDCellCultureId] = None
    three_d_architecture: Optional[Union[str, "ThreeDArchitectureEnum"]] = None
    matrix_composition: Optional[str] = None
    size_range: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThreeDCellCultureId):
            self.id = ThreeDCellCultureId(self.id)

        if self.three_d_architecture is not None and not isinstance(self.three_d_architecture, ThreeDArchitectureEnum):
            self.three_d_architecture = ThreeDArchitectureEnum(self.three_d_architecture)

        if self.matrix_composition is not None and not isinstance(self.matrix_composition, str):
            self.matrix_composition = str(self.matrix_composition)

        if self.size_range is not None and not isinstance(self.size_range, str):
            self.size_range = str(self.size_range)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CoCulture(CellularSystem):
    """
    Co-culture systems combining multiple cell types to mimic  microenvironments and cell-cell interactions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["CoCulture"]
    class_class_curie: ClassVar[str] = "namo:CoCulture"
    class_name: ClassVar[str] = "CoCulture"
    class_model_uri: ClassVar[URIRef] = NAMO.CoCulture

    id: Union[str, CoCultureId] = None
    coculture_configuration: Optional[Union[str, "CocultureConfigurationEnum"]] = None
    cell_ratios: Optional[Union[Union[dict, "CellRatio"], list[Union[dict, "CellRatio"]]]] = empty_list()
    interaction_mechanisms: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CoCultureId):
            self.id = CoCultureId(self.id)

        if self.coculture_configuration is not None and not isinstance(self.coculture_configuration, CocultureConfigurationEnum):
            self.coculture_configuration = CocultureConfigurationEnum(self.coculture_configuration)

        if not isinstance(self.cell_ratios, list):
            self.cell_ratios = [self.cell_ratios] if self.cell_ratios is not None else []
        self.cell_ratios = [v if isinstance(v, CellRatio) else CellRatio(**as_dict(v)) for v in self.cell_ratios]

        if not isinstance(self.interaction_mechanisms, list):
            self.interaction_mechanisms = [self.interaction_mechanisms] if self.interaction_mechanisms is not None else []
        self.interaction_mechanisms = [v if isinstance(v, str) else str(v) for v in self.interaction_mechanisms]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Organoid(ThreeDCellCulture):
    """
    A 3D cell culture system that self-organizes to recapitulate key structural and functional aspects of an organ or
    tissue
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["Organoid"]
    class_class_curie: ClassVar[str] = "namo:Organoid"
    class_name: ClassVar[str] = "Organoid"
    class_model_uri: ClassVar[URIRef] = NAMO.Organoid

    id: Union[str, OrganoidId] = None
    organ_modeled: Optional[Union[dict, "Term"]] = None
    differentiation_method: Optional[str] = None
    culture_system: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganoidId):
            self.id = OrganoidId(self.id)

        if self.organ_modeled is not None and not isinstance(self.organ_modeled, Term):
            self.organ_modeled = Term(**as_dict(self.organ_modeled))

        if self.differentiation_method is not None and not isinstance(self.differentiation_method, str):
            self.differentiation_method = str(self.differentiation_method)

        if self.culture_system is not None and not isinstance(self.culture_system, str):
            self.culture_system = str(self.culture_system)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CellLineModel(TwoDCellCulture):
    """
    A model system based on immortalized cell lines that can be maintained in culture indefinitely. Examples: HepG2,
    A549, Caco-2, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["CellLineModel"]
    class_class_curie: ClassVar[str] = "namo:CellLineModel"
    class_name: ClassVar[str] = "CellLineModel"
    class_model_uri: ClassVar[URIRef] = NAMO.CellLineModel

    id: Union[str, CellLineModelId] = None
    passage_range: Optional[str] = None
    authentication_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellLineModelId):
            self.id = CellLineModelId(self.id)

        if self.passage_range is not None and not isinstance(self.passage_range, str):
            self.passage_range = str(self.passage_range)

        if self.authentication_method is not None and not isinstance(self.authentication_method, str):
            self.authentication_method = str(self.authentication_method)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class MicrophysiologicalSystem(NAMModel):
    """
    Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials, and living cells to replicate
    tissue-level physiology and dynamics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["MicrophysiologicalSystem"]
    class_class_curie: ClassVar[str] = "namo:MicrophysiologicalSystem"
    class_name: ClassVar[str] = "MicrophysiologicalSystem"
    class_model_uri: ClassVar[URIRef] = NAMO.MicrophysiologicalSystem

    id: Union[str, MicrophysiologicalSystemId] = None
    microfluidic_design: Optional[Union[dict, "MicrofluidicDesign"]] = None
    mechanical_forces: Optional[Union[dict, "MechanicalStimulation"]] = None
    perfusion_system: Optional[str] = None
    sensor_integration: Optional[Union[Union[str, "IntegratedSensorEnum"], list[Union[str, "IntegratedSensorEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.microfluidic_design is not None and not isinstance(self.microfluidic_design, MicrofluidicDesign):
            self.microfluidic_design = MicrofluidicDesign(**as_dict(self.microfluidic_design))

        if self.mechanical_forces is not None and not isinstance(self.mechanical_forces, MechanicalStimulation):
            self.mechanical_forces = MechanicalStimulation(**as_dict(self.mechanical_forces))

        if self.perfusion_system is not None and not isinstance(self.perfusion_system, str):
            self.perfusion_system = str(self.perfusion_system)

        if not isinstance(self.sensor_integration, list):
            self.sensor_integration = [self.sensor_integration] if self.sensor_integration is not None else []
        self.sensor_integration = [v if isinstance(v, IntegratedSensorEnum) else IntegratedSensorEnum(v) for v in self.sensor_integration]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class OrganOnChip(MicrophysiologicalSystem):
    """
    A model system that simulates the physiological functions of an organ using a microfluidic device. Examples:
    Airway-on-chip, ...
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["OrganOnChip"]
    class_class_curie: ClassVar[str] = "namo:OrganOnChip"
    class_name: ClassVar[str] = "OrganOnChip"
    class_model_uri: ClassVar[URIRef] = NAMO.OrganOnChip

    id: Union[str, OrganOnChipId] = None
    organ_modeled: Optional[Union[dict, "Term"]] = None
    cell_types: Optional[Union[dict[Union[str, TermId], Union[dict, "Term"]], list[Union[dict, "Term"]]]] = empty_dict()
    cell_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganOnChipId):
            self.id = OrganOnChipId(self.id)

        if self.organ_modeled is not None and not isinstance(self.organ_modeled, Term):
            self.organ_modeled = Term(**as_dict(self.organ_modeled))

        self._normalize_inlined_as_list(slot_name="cell_types", slot_type=Term, key_name="id", keyed=True)

        if self.cell_source is not None and not isinstance(self.cell_source, str):
            self.cell_source = str(self.cell_source)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class TissueOnChip(MicrophysiologicalSystem):
    """
    Tissue-level microphysiological systems that model specific tissue functions and multi-cellular interactions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["TissueOnChip"]
    class_class_curie: ClassVar[str] = "namo:TissueOnChip"
    class_name: ClassVar[str] = "TissueOnChip"
    class_model_uri: ClassVar[URIRef] = NAMO.TissueOnChip

    id: Union[str, TissueOnChipId] = None
    tissue_modeled: Optional[Union[dict, "Term"]] = None
    tissue_architecture: Optional[str] = None
    barrier_functions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TissueOnChipId):
            self.id = TissueOnChipId(self.id)

        if self.tissue_modeled is not None and not isinstance(self.tissue_modeled, Term):
            self.tissue_modeled = Term(**as_dict(self.tissue_modeled))

        if self.tissue_architecture is not None and not isinstance(self.tissue_architecture, str):
            self.tissue_architecture = str(self.tissue_architecture)

        if not isinstance(self.barrier_functions, list):
            self.barrier_functions = [self.barrier_functions] if self.barrier_functions is not None else []
        self.barrier_functions = [v if isinstance(v, str) else str(v) for v in self.barrier_functions]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class InSilicoModel(NAMModel):
    """
    Computational models that simulate biological processes without physical biological components.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["InSilicoModel"]
    class_class_curie: ClassVar[str] = "namo:InSilicoModel"
    class_name: ClassVar[str] = "InSilicoModel"
    class_model_uri: ClassVar[URIRef] = NAMO.InSilicoModel

    id: Union[str, InSilicoModelId] = None
    computational_method: Optional[str] = None
    software_platform: Optional[str] = None
    validation_datasets: Optional[Union[str, list[str]]] = empty_list()
    prediction_scope: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.computational_method is not None and not isinstance(self.computational_method, str):
            self.computational_method = str(self.computational_method)

        if self.software_platform is not None and not isinstance(self.software_platform, str):
            self.software_platform = str(self.software_platform)

        if not isinstance(self.validation_datasets, list):
            self.validation_datasets = [self.validation_datasets] if self.validation_datasets is not None else []
        self.validation_datasets = [v if isinstance(v, str) else str(v) for v in self.validation_datasets]

        if self.prediction_scope is not None and not isinstance(self.prediction_scope, str):
            self.prediction_scope = str(self.prediction_scope)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class QSARModel(InSilicoModel):
    """
    Quantitative Structure-Activity Relationship models that predict chemical/biological activity from molecular
    structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["QSARModel"]
    class_class_curie: ClassVar[str] = "namo:QSARModel"
    class_name: ClassVar[str] = "QSARModel"
    class_model_uri: ClassVar[URIRef] = NAMO.QSARModel

    id: Union[str, QSARModelId] = None
    molecular_descriptors: Optional[Union[str, list[str]]] = empty_list()
    activity_endpoint: Optional[str] = None
    training_dataset_size: Optional[int] = None
    model_performance: Optional[Union[dict, "ModelPerformance"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QSARModelId):
            self.id = QSARModelId(self.id)

        if not isinstance(self.molecular_descriptors, list):
            self.molecular_descriptors = [self.molecular_descriptors] if self.molecular_descriptors is not None else []
        self.molecular_descriptors = [v if isinstance(v, str) else str(v) for v in self.molecular_descriptors]

        if self.activity_endpoint is not None and not isinstance(self.activity_endpoint, str):
            self.activity_endpoint = str(self.activity_endpoint)

        if self.training_dataset_size is not None and not isinstance(self.training_dataset_size, int):
            self.training_dataset_size = int(self.training_dataset_size)

        if self.model_performance is not None and not isinstance(self.model_performance, ModelPerformance):
            self.model_performance = ModelPerformance(**as_dict(self.model_performance))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class PBPKModel(InSilicoModel):
    """
    Physiologically Based Pharmacokinetic models that simulate drug absorption, distribution, metabolism, and
    excretion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["PBPKModel"]
    class_class_curie: ClassVar[str] = "namo:PBPKModel"
    class_name: ClassVar[str] = "PBPKModel"
    class_model_uri: ClassVar[URIRef] = NAMO.PBPKModel

    id: Union[str, PBPKModelId] = None
    compartments: Optional[Union[dict[Union[str, PBPKCompartmentId], Union[dict, "PBPKCompartment"]], list[Union[dict, "PBPKCompartment"]]]] = empty_dict()
    species_modeled: Optional[Union[dict, "Term"]] = None
    drug_properties: Optional[Union[dict, "DrugProperties"]] = None
    elimination_pathways: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PBPKModelId):
            self.id = PBPKModelId(self.id)

        self._normalize_inlined_as_list(slot_name="compartments", slot_type=PBPKCompartment, key_name="id", keyed=True)

        if self.species_modeled is not None and not isinstance(self.species_modeled, Term):
            self.species_modeled = Term(**as_dict(self.species_modeled))

        if self.drug_properties is not None and not isinstance(self.drug_properties, DrugProperties):
            self.drug_properties = DrugProperties(**as_dict(self.drug_properties))

        if not isinstance(self.elimination_pathways, list):
            self.elimination_pathways = [self.elimination_pathways] if self.elimination_pathways is not None else []
        self.elimination_pathways = [v if isinstance(v, str) else str(v) for v in self.elimination_pathways]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class DigitalTwin(InSilicoModel):
    """
    Computational replicas of biological systems for real-time prediction and personalized modeling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["DigitalTwin"]
    class_class_curie: ClassVar[str] = "namo:DigitalTwin"
    class_name: ClassVar[str] = "DigitalTwin"
    class_model_uri: ClassVar[URIRef] = NAMO.DigitalTwin

    id: Union[str, DigitalTwinId] = None
    twin_scope: Optional[Union[str, "DigitalTwinScopeEnum"]] = None
    real_time_data_sources: Optional[Union[str, list[str]]] = empty_list()
    personalization_parameters: Optional[Union[str, list[str]]] = empty_list()
    update_frequency: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalTwinId):
            self.id = DigitalTwinId(self.id)

        if self.twin_scope is not None and not isinstance(self.twin_scope, DigitalTwinScopeEnum):
            self.twin_scope = DigitalTwinScopeEnum(self.twin_scope)

        if not isinstance(self.real_time_data_sources, list):
            self.real_time_data_sources = [self.real_time_data_sources] if self.real_time_data_sources is not None else []
        self.real_time_data_sources = [v if isinstance(v, str) else str(v) for v in self.real_time_data_sources]

        if not isinstance(self.personalization_parameters, list):
            self.personalization_parameters = [self.personalization_parameters] if self.personalization_parameters is not None else []
        self.personalization_parameters = [v if isinstance(v, str) else str(v) for v in self.personalization_parameters]

        if self.update_frequency is not None and not isinstance(self.update_frequency, str):
            self.update_frequency = str(self.update_frequency)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class MLModel(InSilicoModel):
    """
    Machine Learning and AI-based models for prediction, mechanism inference, and hypothesis generation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["MLModel"]
    class_class_curie: ClassVar[str] = "namo:MLModel"
    class_name: ClassVar[str] = "MLModel"
    class_model_uri: ClassVar[URIRef] = NAMO.MLModel

    id: Union[str, MLModelId] = None
    ml_algorithm: Optional[Union[str, "MLAlgorithmEnum"]] = None
    feature_types: Optional[Union[Union[str, "FeatureTypeEnum"], list[Union[str, "FeatureTypeEnum"]]]] = empty_list()
    training_data_size: Optional[int] = None
    model_interpretability: Optional[Union[str, "InterpretabilityLevelEnum"]] = None
    cross_validation: Optional[Union[dict, "CrossValidation"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MLModelId):
            self.id = MLModelId(self.id)

        if self.ml_algorithm is not None and not isinstance(self.ml_algorithm, MLAlgorithmEnum):
            self.ml_algorithm = MLAlgorithmEnum(self.ml_algorithm)

        if not isinstance(self.feature_types, list):
            self.feature_types = [self.feature_types] if self.feature_types is not None else []
        self.feature_types = [v if isinstance(v, FeatureTypeEnum) else FeatureTypeEnum(v) for v in self.feature_types]

        if self.training_data_size is not None and not isinstance(self.training_data_size, int):
            self.training_data_size = int(self.training_data_size)

        if self.model_interpretability is not None and not isinstance(self.model_interpretability, InterpretabilityLevelEnum):
            self.model_interpretability = InterpretabilityLevelEnum(self.model_interpretability)

        if self.cross_validation is not None and not isinstance(self.cross_validation, CrossValidation):
            self.cross_validation = CrossValidation(**as_dict(self.cross_validation))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class MetabolicModel(InSilicoModel):
    """
    A model that simulates the metabolic processes of an organism or system. Examples: Virtual Physiological Human, ...
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["MetabolicModel"]
    class_class_curie: ClassVar[str] = "namo:MetabolicModel"
    class_name: ClassVar[str] = "MetabolicModel"
    class_model_uri: ClassVar[URIRef] = NAMO.MetabolicModel

    id: Union[str, MetabolicModelId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetabolicModelId):
            self.id = MetabolicModelId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CellRatio(YAMLRoot):
    """
    Ratio specification for different cell types in co-culture systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["CellRatio"]
    class_class_curie: ClassVar[str] = "namo:CellRatio"
    class_name: ClassVar[str] = "CellRatio"
    class_model_uri: ClassVar[URIRef] = NAMO.CellRatio

    cell_type: Optional[Union[dict, "Term"]] = None
    ratio: Optional[float] = None
    ratio_type: Optional[Union[str, "RatioTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cell_type is not None and not isinstance(self.cell_type, Term):
            self.cell_type = Term(**as_dict(self.cell_type))

        if self.ratio is not None and not isinstance(self.ratio, float):
            self.ratio = float(self.ratio)

        if self.ratio_type is not None and not isinstance(self.ratio_type, RatioTypeEnum):
            self.ratio_type = RatioTypeEnum(self.ratio_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelPerformance(YAMLRoot):
    """
    Statistical performance metrics for computational models.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["ModelPerformance"]
    class_class_curie: ClassVar[str] = "namo:ModelPerformance"
    class_name: ClassVar[str] = "ModelPerformance"
    class_model_uri: ClassVar[URIRef] = NAMO.ModelPerformance

    accuracy: Optional[float] = None
    sensitivity: Optional[float] = None
    specificity: Optional[float] = None
    r_squared: Optional[float] = None
    rmse: Optional[float] = None
    auc: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.accuracy is not None and not isinstance(self.accuracy, float):
            self.accuracy = float(self.accuracy)

        if self.sensitivity is not None and not isinstance(self.sensitivity, float):
            self.sensitivity = float(self.sensitivity)

        if self.specificity is not None and not isinstance(self.specificity, float):
            self.specificity = float(self.specificity)

        if self.r_squared is not None and not isinstance(self.r_squared, float):
            self.r_squared = float(self.r_squared)

        if self.rmse is not None and not isinstance(self.rmse, float):
            self.rmse = float(self.rmse)

        if self.auc is not None and not isinstance(self.auc, float):
            self.auc = float(self.auc)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PBPKCompartment(NamedThing):
    """
    A physiological compartment in a PBPK model.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["PBPKCompartment"]
    class_class_curie: ClassVar[str] = "namo:PBPKCompartment"
    class_name: ClassVar[str] = "PBPKCompartment"
    class_model_uri: ClassVar[URIRef] = NAMO.PBPKCompartment

    id: Union[str, PBPKCompartmentId] = None
    compartment_type: Optional[Union[str, "PBPKCompartmentEnum"]] = None
    volume: Optional[float] = None
    blood_flow: Optional[float] = None
    partition_coefficient: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PBPKCompartmentId):
            self.id = PBPKCompartmentId(self.id)

        if self.compartment_type is not None and not isinstance(self.compartment_type, PBPKCompartmentEnum):
            self.compartment_type = PBPKCompartmentEnum(self.compartment_type)

        if self.volume is not None and not isinstance(self.volume, float):
            self.volume = float(self.volume)

        if self.blood_flow is not None and not isinstance(self.blood_flow, float):
            self.blood_flow = float(self.blood_flow)

        if self.partition_coefficient is not None and not isinstance(self.partition_coefficient, float):
            self.partition_coefficient = float(self.partition_coefficient)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class DrugProperties(YAMLRoot):
    """
    Physicochemical and pharmacological properties of a drug in PBPK models.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["DrugProperties"]
    class_class_curie: ClassVar[str] = "namo:DrugProperties"
    class_name: ClassVar[str] = "DrugProperties"
    class_model_uri: ClassVar[URIRef] = NAMO.DrugProperties

    molecular_weight: Optional[float] = None
    logp: Optional[float] = None
    pka: Optional[float] = None
    protein_binding: Optional[float] = None
    clearance: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.molecular_weight is not None and not isinstance(self.molecular_weight, float):
            self.molecular_weight = float(self.molecular_weight)

        if self.logp is not None and not isinstance(self.logp, float):
            self.logp = float(self.logp)

        if self.pka is not None and not isinstance(self.pka, float):
            self.pka = float(self.pka)

        if self.protein_binding is not None and not isinstance(self.protein_binding, float):
            self.protein_binding = float(self.protein_binding)

        if self.clearance is not None and not isinstance(self.clearance, float):
            self.clearance = float(self.clearance)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CrossValidation(YAMLRoot):
    """
    Cross-validation strategy and results for ML models.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["CrossValidation"]
    class_class_curie: ClassVar[str] = "namo:CrossValidation"
    class_name: ClassVar[str] = "CrossValidation"
    class_model_uri: ClassVar[URIRef] = NAMO.CrossValidation

    cv_method: Optional[Union[str, "CrossValidationMethodEnum"]] = None
    n_folds: Optional[int] = None
    cv_score: Optional[float] = None
    cv_std: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cv_method is not None and not isinstance(self.cv_method, CrossValidationMethodEnum):
            self.cv_method = CrossValidationMethodEnum(self.cv_method)

        if self.n_folds is not None and not isinstance(self.n_folds, int):
            self.n_folds = int(self.n_folds)

        if self.cv_score is not None and not isinstance(self.cv_score, float):
            self.cv_score = float(self.cv_score)

        if self.cv_std is not None and not isinstance(self.cv_std, float):
            self.cv_std = float(self.cv_std)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MicrofluidicDesign(NamedThing):
    """
    Detailed specification of a microfluidic device design including its architecture, materials, dimensions, and
    functional features.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["MicrofluidicDesign"]
    class_class_curie: ClassVar[str] = "namo:MicrofluidicDesign"
    class_name: ClassVar[str] = "MicrofluidicDesign"
    class_model_uri: ClassVar[URIRef] = NAMO.MicrofluidicDesign

    id: Union[str, MicrofluidicDesignId] = None
    architecture_type: Optional[Union[str, "MicrofluidicArchitectureEnum"]] = None
    number_of_channels: Optional[int] = None
    channel_configuration: Optional[Union[Union[str, "ChannelConfigurationEnum"], list[Union[str, "ChannelConfigurationEnum"]]]] = empty_list()
    membrane_type: Optional[Union[str, "MembraneTypeEnum"]] = None
    membrane_pore_size: Optional[float] = None
    membrane_thickness: Optional[float] = None
    interface_type: Optional[Union[Union[str, "InterfaceTypeEnum"], list[Union[str, "InterfaceTypeEnum"]]]] = empty_list()
    channel_dimensions: Optional[Union[Union[dict, "ChannelDimensions"], list[Union[dict, "ChannelDimensions"]]]] = empty_list()
    material: Optional[Union[Union[str, "DeviceMaterialEnum"], list[Union[str, "DeviceMaterialEnum"]]]] = empty_list()
    surface_treatment: Optional[Union[Union[str, "SurfaceCoatingEnum"], list[Union[str, "SurfaceCoatingEnum"]]]] = empty_list()
    flow_control_method: Optional[Union[Union[str, "FlowControlMethodEnum"], list[Union[str, "FlowControlMethodEnum"]]]] = empty_list()
    sensors_integrated: Optional[Union[Union[str, "IntegratedSensorEnum"], list[Union[str, "IntegratedSensorEnum"]]]] = empty_list()
    special_features: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicrofluidicDesignId):
            self.id = MicrofluidicDesignId(self.id)

        if self.architecture_type is not None and not isinstance(self.architecture_type, MicrofluidicArchitectureEnum):
            self.architecture_type = MicrofluidicArchitectureEnum(self.architecture_type)

        if self.number_of_channels is not None and not isinstance(self.number_of_channels, int):
            self.number_of_channels = int(self.number_of_channels)

        if not isinstance(self.channel_configuration, list):
            self.channel_configuration = [self.channel_configuration] if self.channel_configuration is not None else []
        self.channel_configuration = [v if isinstance(v, ChannelConfigurationEnum) else ChannelConfigurationEnum(v) for v in self.channel_configuration]

        if self.membrane_type is not None and not isinstance(self.membrane_type, MembraneTypeEnum):
            self.membrane_type = MembraneTypeEnum(self.membrane_type)

        if self.membrane_pore_size is not None and not isinstance(self.membrane_pore_size, float):
            self.membrane_pore_size = float(self.membrane_pore_size)

        if self.membrane_thickness is not None and not isinstance(self.membrane_thickness, float):
            self.membrane_thickness = float(self.membrane_thickness)

        if not isinstance(self.interface_type, list):
            self.interface_type = [self.interface_type] if self.interface_type is not None else []
        self.interface_type = [v if isinstance(v, InterfaceTypeEnum) else InterfaceTypeEnum(v) for v in self.interface_type]

        if not isinstance(self.channel_dimensions, list):
            self.channel_dimensions = [self.channel_dimensions] if self.channel_dimensions is not None else []
        self.channel_dimensions = [v if isinstance(v, ChannelDimensions) else ChannelDimensions(**as_dict(v)) for v in self.channel_dimensions]

        if not isinstance(self.material, list):
            self.material = [self.material] if self.material is not None else []
        self.material = [v if isinstance(v, DeviceMaterialEnum) else DeviceMaterialEnum(v) for v in self.material]

        if not isinstance(self.surface_treatment, list):
            self.surface_treatment = [self.surface_treatment] if self.surface_treatment is not None else []
        self.surface_treatment = [v if isinstance(v, SurfaceCoatingEnum) else SurfaceCoatingEnum(v) for v in self.surface_treatment]

        if not isinstance(self.flow_control_method, list):
            self.flow_control_method = [self.flow_control_method] if self.flow_control_method is not None else []
        self.flow_control_method = [v if isinstance(v, FlowControlMethodEnum) else FlowControlMethodEnum(v) for v in self.flow_control_method]

        if not isinstance(self.sensors_integrated, list):
            self.sensors_integrated = [self.sensors_integrated] if self.sensors_integrated is not None else []
        self.sensors_integrated = [v if isinstance(v, IntegratedSensorEnum) else IntegratedSensorEnum(v) for v in self.sensors_integrated]

        if not isinstance(self.special_features, list):
            self.special_features = [self.special_features] if self.special_features is not None else []
        self.special_features = [v if isinstance(v, str) else str(v) for v in self.special_features]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class ChannelDimensions(YAMLRoot):
    """
    Dimensions of a microfluidic channel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["ChannelDimensions"]
    class_class_curie: ClassVar[str] = "namo:ChannelDimensions"
    class_name: ClassVar[str] = "ChannelDimensions"
    class_model_uri: ClassVar[URIRef] = NAMO.ChannelDimensions

    channel_name: Optional[str] = None
    width: Optional[float] = None
    height: Optional[float] = None
    length: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.channel_name is not None and not isinstance(self.channel_name, str):
            self.channel_name = str(self.channel_name)

        if self.width is not None and not isinstance(self.width, float):
            self.width = float(self.width)

        if self.height is not None and not isinstance(self.height, float):
            self.height = float(self.height)

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MechanicalStimulation(NamedThing):
    """
    Specification of mechanical forces applied to the model system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["MechanicalStimulation"]
    class_class_curie: ClassVar[str] = "namo:MechanicalStimulation"
    class_name: ClassVar[str] = "MechanicalStimulation"
    class_model_uri: ClassVar[URIRef] = NAMO.MechanicalStimulation

    id: Union[str, MechanicalStimulationId] = None
    stimulation_type: Optional[Union[Union[str, "MechanicalStimulationTypeEnum"], list[Union[str, "MechanicalStimulationTypeEnum"]]]] = empty_list()
    cyclic_stretch_percent: Optional[float] = None
    frequency_hz: Optional[float] = None
    shear_stress: Optional[float] = None
    pressure_pascal: Optional[float] = None
    duration_minutes: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MechanicalStimulationId):
            self.id = MechanicalStimulationId(self.id)

        if not isinstance(self.stimulation_type, list):
            self.stimulation_type = [self.stimulation_type] if self.stimulation_type is not None else []
        self.stimulation_type = [v if isinstance(v, MechanicalStimulationTypeEnum) else MechanicalStimulationTypeEnum(v) for v in self.stimulation_type]

        if self.cyclic_stretch_percent is not None and not isinstance(self.cyclic_stretch_percent, float):
            self.cyclic_stretch_percent = float(self.cyclic_stretch_percent)

        if self.frequency_hz is not None and not isinstance(self.frequency_hz, float):
            self.frequency_hz = float(self.frequency_hz)

        if self.shear_stress is not None and not isinstance(self.shear_stress, float):
            self.shear_stress = float(self.shear_stress)

        if self.pressure_pascal is not None and not isinstance(self.pressure_pascal, float):
            self.pressure_pascal = float(self.pressure_pascal)

        if self.duration_minutes is not None and not isinstance(self.duration_minutes, float):
            self.duration_minutes = float(self.duration_minutes)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class BiologicalSystem(NamedThing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["BiologicalSystem"]
    class_class_curie: ClassVar[str] = "namo:BiologicalSystem"
    class_name: ClassVar[str] = "BiologicalSystem"
    class_model_uri: ClassVar[URIRef] = NAMO.BiologicalSystem

    id: Union[str, BiologicalSystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalSystemId):
            self.id = BiologicalSystemId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class ModelsRelationship(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["ModelsRelationship"]
    class_class_curie: ClassVar[str] = "namo:ModelsRelationship"
    class_name: ClassVar[str] = "ModelsRelationship"
    class_model_uri: ClassVar[URIRef] = NAMO.ModelsRelationship

    biological_system_modeled: Optional[Union[str, BiologicalSystemId]] = None
    is_computed: Optional[Union[bool, Bool]] = None
    concordance: Optional[Union[dict, "ConcordanceResult"]] = None
    structured_concordance: Optional[Union[dict, "StructuredConcordanceResult"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.biological_system_modeled is not None and not isinstance(self.biological_system_modeled, BiologicalSystemId):
            self.biological_system_modeled = BiologicalSystemId(self.biological_system_modeled)

        if self.is_computed is not None and not isinstance(self.is_computed, Bool):
            self.is_computed = Bool(self.is_computed)

        if self.concordance is not None and not isinstance(self.concordance, ConcordanceResult):
            self.concordance = ConcordanceResult(**as_dict(self.concordance))

        if self.structured_concordance is not None and not isinstance(self.structured_concordance, StructuredConcordanceResult):
            self.structured_concordance = StructuredConcordanceResult(**as_dict(self.structured_concordance))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConcordanceResult(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["ConcordanceResult"]
    class_class_curie: ClassVar[str] = "namo:ConcordanceResult"
    class_name: ClassVar[str] = "ConcordanceResult"
    class_model_uri: ClassVar[URIRef] = NAMO.ConcordanceResult

    phenotype_overlap: Optional[str] = None
    molecular_similarity: Optional[str] = None
    pathway_concordance: Optional[str] = None
    cell_type_coverage: Optional[str] = None
    functional_parity: Optional[str] = None
    reproducibility: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.phenotype_overlap is not None and not isinstance(self.phenotype_overlap, str):
            self.phenotype_overlap = str(self.phenotype_overlap)

        if self.molecular_similarity is not None and not isinstance(self.molecular_similarity, str):
            self.molecular_similarity = str(self.molecular_similarity)

        if self.pathway_concordance is not None and not isinstance(self.pathway_concordance, str):
            self.pathway_concordance = str(self.pathway_concordance)

        if self.cell_type_coverage is not None and not isinstance(self.cell_type_coverage, str):
            self.cell_type_coverage = str(self.cell_type_coverage)

        if self.functional_parity is not None and not isinstance(self.functional_parity, str):
            self.functional_parity = str(self.functional_parity)

        if self.reproducibility is not None and not isinstance(self.reproducibility, str):
            self.reproducibility = str(self.reproducibility)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StructuredConcordanceResult(YAMLRoot):
    """
    Detailed structured assessment of concordance between model and biological systems with rich metadata, evidence,
    and quantitative measures.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["StructuredConcordanceResult"]
    class_class_curie: ClassVar[str] = "namo:StructuredConcordanceResult"
    class_name: ClassVar[str] = "StructuredConcordanceResult"
    class_model_uri: ClassVar[URIRef] = NAMO.StructuredConcordanceResult

    molecular_similarity: Optional[Union[dict, "MolecularSimilarity"]] = None
    pathway_concordance: Optional[Union[dict, "PathwayConcordance"]] = None
    phenotype_overlap: Optional[Union[dict, "PhenotypeOverlap"]] = None
    cell_type_coverage: Optional[Union[dict, "CellTypeCoverage"]] = None
    functional_parity: Optional[Union[dict, "FunctionalParity"]] = None
    reproducibility: Optional[Union[dict, "Reproducibility"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.molecular_similarity is not None and not isinstance(self.molecular_similarity, MolecularSimilarity):
            self.molecular_similarity = MolecularSimilarity(**as_dict(self.molecular_similarity))

        if self.pathway_concordance is not None and not isinstance(self.pathway_concordance, PathwayConcordance):
            self.pathway_concordance = PathwayConcordance(**as_dict(self.pathway_concordance))

        if self.phenotype_overlap is not None and not isinstance(self.phenotype_overlap, PhenotypeOverlap):
            self.phenotype_overlap = PhenotypeOverlap(**as_dict(self.phenotype_overlap))

        if self.cell_type_coverage is not None and not isinstance(self.cell_type_coverage, CellTypeCoverage):
            self.cell_type_coverage = CellTypeCoverage(**as_dict(self.cell_type_coverage))

        if self.functional_parity is not None and not isinstance(self.functional_parity, FunctionalParity):
            self.functional_parity = FunctionalParity(**as_dict(self.functional_parity))

        if self.reproducibility is not None and not isinstance(self.reproducibility, Reproducibility):
            self.reproducibility = Reproducibility(**as_dict(self.reproducibility))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularSimilarity(NamedThing):
    """
    Detailed assessment of molecular-level concordance between model and biological systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["MolecularSimilarity"]
    class_class_curie: ClassVar[str] = "namo:MolecularSimilarity"
    class_name: ClassVar[str] = "MolecularSimilarity"
    class_model_uri: ClassVar[URIRef] = NAMO.MolecularSimilarity

    id: Union[str, MolecularSimilarityId] = None
    similarity_score: Optional[float] = None
    correlation_coefficient: Optional[float] = None
    differentially_expressed_genes: Optional[Union[dict[Union[str, GeneId], Union[dict, "Gene"]], list[Union[dict, "Gene"]]]] = empty_dict()
    conserved_genes: Optional[Union[dict[Union[str, GeneId], Union[dict, "Gene"]], list[Union[dict, "Gene"]]]] = empty_dict()
    methodology: Optional[str] = None
    data_source: Optional[str] = None
    statistical_significance: Optional[Union[dict, "StatisticalSignificance"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularSimilarityId):
            self.id = MolecularSimilarityId(self.id)

        if self.similarity_score is not None and not isinstance(self.similarity_score, float):
            self.similarity_score = float(self.similarity_score)

        if self.correlation_coefficient is not None and not isinstance(self.correlation_coefficient, float):
            self.correlation_coefficient = float(self.correlation_coefficient)

        self._normalize_inlined_as_list(slot_name="differentially_expressed_genes", slot_type=Gene, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="conserved_genes", slot_type=Gene, key_name="id", keyed=True)

        if self.methodology is not None and not isinstance(self.methodology, str):
            self.methodology = str(self.methodology)

        if self.data_source is not None and not isinstance(self.data_source, str):
            self.data_source = str(self.data_source)

        if self.statistical_significance is not None and not isinstance(self.statistical_significance, StatisticalSignificance):
            self.statistical_significance = StatisticalSignificance(**as_dict(self.statistical_significance))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class PathwayConcordance(NamedThing):
    """
    Assessment of biological pathway conservation and activity between model and biological systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["PathwayConcordance"]
    class_class_curie: ClassVar[str] = "namo:PathwayConcordance"
    class_name: ClassVar[str] = "PathwayConcordance"
    class_model_uri: ClassVar[URIRef] = NAMO.PathwayConcordance

    id: Union[str, PathwayConcordanceId] = None
    pathway_overlap_score: Optional[float] = None
    active_pathways: Optional[Union[dict[Union[str, PathwayId], Union[dict, "Pathway"]], list[Union[dict, "Pathway"]]]] = empty_dict()
    divergent_pathways: Optional[Union[dict[Union[str, PathwayId], Union[dict, "Pathway"]], list[Union[dict, "Pathway"]]]] = empty_dict()
    pathway_analysis_method: Optional[str] = None
    enrichment_statistics: Optional[Union[Union[dict, "EnrichmentStatistics"], list[Union[dict, "EnrichmentStatistics"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathwayConcordanceId):
            self.id = PathwayConcordanceId(self.id)

        if self.pathway_overlap_score is not None and not isinstance(self.pathway_overlap_score, float):
            self.pathway_overlap_score = float(self.pathway_overlap_score)

        self._normalize_inlined_as_list(slot_name="active_pathways", slot_type=Pathway, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="divergent_pathways", slot_type=Pathway, key_name="id", keyed=True)

        if self.pathway_analysis_method is not None and not isinstance(self.pathway_analysis_method, str):
            self.pathway_analysis_method = str(self.pathway_analysis_method)

        if not isinstance(self.enrichment_statistics, list):
            self.enrichment_statistics = [self.enrichment_statistics] if self.enrichment_statistics is not None else []
        self.enrichment_statistics = [v if isinstance(v, EnrichmentStatistics) else EnrichmentStatistics(**as_dict(v)) for v in self.enrichment_statistics]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class PhenotypeOverlap(NamedThing):
    """
    Comparison of phenotypic manifestations between model and biological systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["PhenotypeOverlap"]
    class_class_curie: ClassVar[str] = "namo:PhenotypeOverlap"
    class_name: ClassVar[str] = "PhenotypeOverlap"
    class_model_uri: ClassVar[URIRef] = NAMO.PhenotypeOverlap

    id: Union[str, PhenotypeOverlapId] = None
    phenotype_similarity_score: Optional[float] = None
    shared_phenotypes: Optional[Union[dict[Union[str, TermId], Union[dict, "Term"]], list[Union[dict, "Term"]]]] = empty_dict()
    model_specific_phenotypes: Optional[Union[dict[Union[str, TermId], Union[dict, "Term"]], list[Union[dict, "Term"]]]] = empty_dict()
    biological_specific_phenotypes: Optional[Union[dict[Union[str, TermId], Union[dict, "Term"]], list[Union[dict, "Term"]]]] = empty_dict()
    phenotype_ontology: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeOverlapId):
            self.id = PhenotypeOverlapId(self.id)

        if self.phenotype_similarity_score is not None and not isinstance(self.phenotype_similarity_score, float):
            self.phenotype_similarity_score = float(self.phenotype_similarity_score)

        self._normalize_inlined_as_list(slot_name="shared_phenotypes", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="model_specific_phenotypes", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="biological_specific_phenotypes", slot_type=Term, key_name="id", keyed=True)

        if self.phenotype_ontology is not None and not isinstance(self.phenotype_ontology, str):
            self.phenotype_ontology = str(self.phenotype_ontology)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CellTypeCoverage(NamedThing):
    """
    Assessment of cell type representation and cellular diversity between systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["CellTypeCoverage"]
    class_class_curie: ClassVar[str] = "namo:CellTypeCoverage"
    class_name: ClassVar[str] = "CellTypeCoverage"
    class_model_uri: ClassVar[URIRef] = NAMO.CellTypeCoverage

    id: Union[str, CellTypeCoverageId] = None
    coverage_percentage: Optional[float] = None
    represented_cell_types: Optional[Union[dict[Union[str, TermId], Union[dict, "Term"]], list[Union[dict, "Term"]]]] = empty_dict()
    missing_cell_types: Optional[Union[dict[Union[str, TermId], Union[dict, "Term"]], list[Union[dict, "Term"]]]] = empty_dict()
    cell_type_proportions: Optional[Union[Union[dict, "CellTypeProportion"], list[Union[dict, "CellTypeProportion"]]]] = empty_list()
    single_cell_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellTypeCoverageId):
            self.id = CellTypeCoverageId(self.id)

        if self.coverage_percentage is not None and not isinstance(self.coverage_percentage, float):
            self.coverage_percentage = float(self.coverage_percentage)

        self._normalize_inlined_as_list(slot_name="represented_cell_types", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="missing_cell_types", slot_type=Term, key_name="id", keyed=True)

        if not isinstance(self.cell_type_proportions, list):
            self.cell_type_proportions = [self.cell_type_proportions] if self.cell_type_proportions is not None else []
        self.cell_type_proportions = [v if isinstance(v, CellTypeProportion) else CellTypeProportion(**as_dict(v)) for v in self.cell_type_proportions]

        if self.single_cell_method is not None and not isinstance(self.single_cell_method, str):
            self.single_cell_method = str(self.single_cell_method)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class FunctionalParity(NamedThing):
    """
    Evaluation of functional capabilities and physiological responses between systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["FunctionalParity"]
    class_class_curie: ClassVar[str] = "namo:FunctionalParity"
    class_name: ClassVar[str] = "FunctionalParity"
    class_model_uri: ClassVar[URIRef] = NAMO.FunctionalParity

    id: Union[str, FunctionalParityId] = None
    functional_similarity_score: Optional[float] = None
    conserved_functions: Optional[Union[str, list[str]]] = empty_list()
    impaired_functions: Optional[Union[str, list[str]]] = empty_list()
    functional_assays: Optional[Union[dict[Union[str, FunctionalAssayId], Union[dict, "FunctionalAssay"]], list[Union[dict, "FunctionalAssay"]]]] = empty_dict()
    dose_response_similarity: Optional[Union[dict, "DoseResponseSimilarity"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalParityId):
            self.id = FunctionalParityId(self.id)

        if self.functional_similarity_score is not None and not isinstance(self.functional_similarity_score, float):
            self.functional_similarity_score = float(self.functional_similarity_score)

        if not isinstance(self.conserved_functions, list):
            self.conserved_functions = [self.conserved_functions] if self.conserved_functions is not None else []
        self.conserved_functions = [v if isinstance(v, str) else str(v) for v in self.conserved_functions]

        if not isinstance(self.impaired_functions, list):
            self.impaired_functions = [self.impaired_functions] if self.impaired_functions is not None else []
        self.impaired_functions = [v if isinstance(v, str) else str(v) for v in self.impaired_functions]

        self._normalize_inlined_as_list(slot_name="functional_assays", slot_type=FunctionalAssay, key_name="id", keyed=True)

        if self.dose_response_similarity is not None and not isinstance(self.dose_response_similarity, DoseResponseSimilarity):
            self.dose_response_similarity = DoseResponseSimilarity(**as_dict(self.dose_response_similarity))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Reproducibility(NamedThing):
    """
    Assessment of experimental reproducibility and consistency of the model system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["Reproducibility"]
    class_class_curie: ClassVar[str] = "namo:Reproducibility"
    class_name: ClassVar[str] = "Reproducibility"
    class_model_uri: ClassVar[URIRef] = NAMO.Reproducibility

    id: Union[str, ReproducibilityId] = None
    reproducibility_score: Optional[float] = None
    coefficient_of_variation: Optional[float] = None
    batch_to_batch_variation: Optional[float] = None
    inter_laboratory_consistency: Optional[float] = None
    replicate_count: Optional[int] = None
    quality_control_metrics: Optional[Union[Union[dict, "QualityControlMetric"], list[Union[dict, "QualityControlMetric"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReproducibilityId):
            self.id = ReproducibilityId(self.id)

        if self.reproducibility_score is not None and not isinstance(self.reproducibility_score, float):
            self.reproducibility_score = float(self.reproducibility_score)

        if self.coefficient_of_variation is not None and not isinstance(self.coefficient_of_variation, float):
            self.coefficient_of_variation = float(self.coefficient_of_variation)

        if self.batch_to_batch_variation is not None and not isinstance(self.batch_to_batch_variation, float):
            self.batch_to_batch_variation = float(self.batch_to_batch_variation)

        if self.inter_laboratory_consistency is not None and not isinstance(self.inter_laboratory_consistency, float):
            self.inter_laboratory_consistency = float(self.inter_laboratory_consistency)

        if self.replicate_count is not None and not isinstance(self.replicate_count, int):
            self.replicate_count = int(self.replicate_count)

        if not isinstance(self.quality_control_metrics, list):
            self.quality_control_metrics = [self.quality_control_metrics] if self.quality_control_metrics is not None else []
        self.quality_control_metrics = [v if isinstance(v, QualityControlMetric) else QualityControlMetric(**as_dict(v)) for v in self.quality_control_metrics]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Gene(NamedThing):
    """
    A gene entity with identifiers and expression information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["Gene"]
    class_class_curie: ClassVar[str] = "namo:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = NAMO.Gene

    id: Union[str, GeneId] = None
    gene_symbol: Optional[str] = None
    ensembl_id: Optional[str] = None
    entrez_id: Optional[int] = None
    fold_change: Optional[float] = None
    p_value: Optional[float] = None
    adjusted_p_value: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        if self.gene_symbol is not None and not isinstance(self.gene_symbol, str):
            self.gene_symbol = str(self.gene_symbol)

        if self.ensembl_id is not None and not isinstance(self.ensembl_id, str):
            self.ensembl_id = str(self.ensembl_id)

        if self.entrez_id is not None and not isinstance(self.entrez_id, int):
            self.entrez_id = int(self.entrez_id)

        if self.fold_change is not None and not isinstance(self.fold_change, float):
            self.fold_change = float(self.fold_change)

        if self.p_value is not None and not isinstance(self.p_value, float):
            self.p_value = float(self.p_value)

        if self.adjusted_p_value is not None and not isinstance(self.adjusted_p_value, float):
            self.adjusted_p_value = float(self.adjusted_p_value)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Pathway(NamedThing):
    """
    A biological pathway with activity and enrichment information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["Pathway"]
    class_class_curie: ClassVar[str] = "namo:Pathway"
    class_name: ClassVar[str] = "Pathway"
    class_model_uri: ClassVar[URIRef] = NAMO.Pathway

    id: Union[str, PathwayId] = None
    pathway_database: Optional[str] = None
    pathway_id: Optional[str] = None
    activity_score: Optional[float] = None
    enrichment_score: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        if self.pathway_database is not None and not isinstance(self.pathway_database, str):
            self.pathway_database = str(self.pathway_database)

        if self.pathway_id is not None and not isinstance(self.pathway_id, str):
            self.pathway_id = str(self.pathway_id)

        if self.activity_score is not None and not isinstance(self.activity_score, float):
            self.activity_score = float(self.activity_score)

        if self.enrichment_score is not None and not isinstance(self.enrichment_score, float):
            self.enrichment_score = float(self.enrichment_score)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class StatisticalSignificance(YAMLRoot):
    """
    Statistical measures of significance for molecular comparisons.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["StatisticalSignificance"]
    class_class_curie: ClassVar[str] = "namo:StatisticalSignificance"
    class_name: ClassVar[str] = "StatisticalSignificance"
    class_model_uri: ClassVar[URIRef] = NAMO.StatisticalSignificance

    p_value: Optional[float] = None
    adjusted_p_value: Optional[float] = None
    confidence_interval_lower: Optional[float] = None
    confidence_interval_upper: Optional[float] = None
    statistical_test: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.p_value is not None and not isinstance(self.p_value, float):
            self.p_value = float(self.p_value)

        if self.adjusted_p_value is not None and not isinstance(self.adjusted_p_value, float):
            self.adjusted_p_value = float(self.adjusted_p_value)

        if self.confidence_interval_lower is not None and not isinstance(self.confidence_interval_lower, float):
            self.confidence_interval_lower = float(self.confidence_interval_lower)

        if self.confidence_interval_upper is not None and not isinstance(self.confidence_interval_upper, float):
            self.confidence_interval_upper = float(self.confidence_interval_upper)

        if self.statistical_test is not None and not isinstance(self.statistical_test, str):
            self.statistical_test = str(self.statistical_test)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnrichmentStatistics(YAMLRoot):
    """
    Statistical measures for pathway enrichment analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["EnrichmentStatistics"]
    class_class_curie: ClassVar[str] = "namo:EnrichmentStatistics"
    class_name: ClassVar[str] = "EnrichmentStatistics"
    class_model_uri: ClassVar[URIRef] = NAMO.EnrichmentStatistics

    enrichment_score: Optional[float] = None
    p_value: Optional[float] = None
    q_value: Optional[float] = None
    genes_in_pathway: Optional[int] = None
    genes_in_dataset: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.enrichment_score is not None and not isinstance(self.enrichment_score, float):
            self.enrichment_score = float(self.enrichment_score)

        if self.p_value is not None and not isinstance(self.p_value, float):
            self.p_value = float(self.p_value)

        if self.q_value is not None and not isinstance(self.q_value, float):
            self.q_value = float(self.q_value)

        if self.genes_in_pathway is not None and not isinstance(self.genes_in_pathway, int):
            self.genes_in_pathway = int(self.genes_in_pathway)

        if self.genes_in_dataset is not None and not isinstance(self.genes_in_dataset, int):
            self.genes_in_dataset = int(self.genes_in_dataset)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellTypeProportion(YAMLRoot):
    """
    Quantitative comparison of cell type proportions between systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["CellTypeProportion"]
    class_class_curie: ClassVar[str] = "namo:CellTypeProportion"
    class_name: ClassVar[str] = "CellTypeProportion"
    class_model_uri: ClassVar[URIRef] = NAMO.CellTypeProportion

    cell_type: Optional[Union[dict, "Term"]] = None
    model_proportion: Optional[float] = None
    biological_proportion: Optional[float] = None
    proportion_ratio: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cell_type is not None and not isinstance(self.cell_type, Term):
            self.cell_type = Term(**as_dict(self.cell_type))

        if self.model_proportion is not None and not isinstance(self.model_proportion, float):
            self.model_proportion = float(self.model_proportion)

        if self.biological_proportion is not None and not isinstance(self.biological_proportion, float):
            self.biological_proportion = float(self.biological_proportion)

        if self.proportion_ratio is not None and not isinstance(self.proportion_ratio, float):
            self.proportion_ratio = float(self.proportion_ratio)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalAssay(NamedThing):
    """
    A functional assay used to assess biological capabilities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["FunctionalAssay"]
    class_class_curie: ClassVar[str] = "namo:FunctionalAssay"
    class_name: ClassVar[str] = "FunctionalAssay"
    class_model_uri: ClassVar[URIRef] = NAMO.FunctionalAssay

    id: Union[str, FunctionalAssayId] = None
    assay_type: Optional[str] = None
    assay_result: Optional[float] = None
    reference_value: Optional[float] = None
    units: Optional[str] = None
    methodology: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalAssayId):
            self.id = FunctionalAssayId(self.id)

        if self.assay_type is not None and not isinstance(self.assay_type, str):
            self.assay_type = str(self.assay_type)

        if self.assay_result is not None and not isinstance(self.assay_result, float):
            self.assay_result = float(self.assay_result)

        if self.reference_value is not None and not isinstance(self.reference_value, float):
            self.reference_value = float(self.reference_value)

        if self.units is not None and not isinstance(self.units, str):
            self.units = str(self.units)

        if self.methodology is not None and not isinstance(self.methodology, str):
            self.methodology = str(self.methodology)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class DoseResponseSimilarity(YAMLRoot):
    """
    Comparison of dose-response relationships between model and biological systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["DoseResponseSimilarity"]
    class_class_curie: ClassVar[str] = "namo:DoseResponseSimilarity"
    class_name: ClassVar[str] = "DoseResponseSimilarity"
    class_model_uri: ClassVar[URIRef] = NAMO.DoseResponseSimilarity

    correlation_coefficient: Optional[float] = None
    ec50_ratio: Optional[float] = None
    max_response_ratio: Optional[float] = None
    compound_tested: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.correlation_coefficient is not None and not isinstance(self.correlation_coefficient, float):
            self.correlation_coefficient = float(self.correlation_coefficient)

        if self.ec50_ratio is not None and not isinstance(self.ec50_ratio, float):
            self.ec50_ratio = float(self.ec50_ratio)

        if self.max_response_ratio is not None and not isinstance(self.max_response_ratio, float):
            self.max_response_ratio = float(self.max_response_ratio)

        if self.compound_tested is not None and not isinstance(self.compound_tested, str):
            self.compound_tested = str(self.compound_tested)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QualityControlMetric(YAMLRoot):
    """
    A quality control measure and its associated value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["QualityControlMetric"]
    class_class_curie: ClassVar[str] = "namo:QualityControlMetric"
    class_name: ClassVar[str] = "QualityControlMetric"
    class_model_uri: ClassVar[URIRef] = NAMO.QualityControlMetric

    metric_name: Optional[str] = None
    metric_value: Optional[float] = None
    threshold: Optional[float] = None
    pass_fail_status: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.metric_name is not None and not isinstance(self.metric_name, str):
            self.metric_name = str(self.metric_name)

        if self.metric_value is not None and not isinstance(self.metric_value, float):
            self.metric_value = float(self.metric_value)

        if self.threshold is not None and not isinstance(self.threshold, float):
            self.threshold = float(self.threshold)

        if self.pass_fail_status is not None and not isinstance(self.pass_fail_status, Bool):
            self.pass_fail_status = Bool(self.pass_fail_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reference(YAMLRoot):
    """
    A literature reference with identifier and title for citing published work.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["Reference"]
    class_class_curie: ClassVar[str] = "namo:Reference"
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = NAMO.Reference

    id: Union[str, ReferenceId] = None
    title: str = None
    authors: Optional[Union[str, list[str]]] = empty_list()
    journal: Optional[str] = None
    year: Optional[int] = None
    url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferenceId):
            self.id = ReferenceId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self.journal is not None and not isinstance(self.journal, str):
            self.journal = str(self.journal)

        if self.year is not None and not isinstance(self.year, int):
            self.year = int(self.year)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Term(NamedThing):
    """
    A term is a concept or entity that can be defined and used in a specific context, often within a controlled
    vocabulary or ontology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["Term"]
    class_class_curie: ClassVar[str] = "namo:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = NAMO.Term

    id: Union[str, TermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TermId):
            self.id = TermId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


# Enumerations
class SpeciesEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SpeciesEnum",
    )

class OrganEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="OrganEnum",
    )

class CellTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellTypeEnum",
    )

class StrainEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StrainEnum",
    )

class AgeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AgeEnum",
    )

class RelativeTimeEnum(EnumDefinitionImpl):

    BEFORE = PermissibleValue(text="BEFORE")
    AFTER = PermissibleValue(text="AFTER")
    AT_SAME_TIME_AS = PermissibleValue(text="AT_SAME_TIME_AS")

    _defn = EnumDefinition(
        name="RelativeTimeEnum",
    )

class CaseOrControlEnum(EnumDefinitionImpl):

    CASE = PermissibleValue(
        text="CASE",
        title="case role in case-control study",
        meaning=OBI["0002492"])
    CONTROL = PermissibleValue(
        text="CONTROL",
        title="control role in case-control study",
        meaning=OBI["0002493"])

    _defn = EnumDefinition(
        name="CaseOrControlEnum",
    )

class StudyDesignEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StudyDesignEnum",
    )

class InvestigativeProtocolEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InvestigativeProtocolEnum",
    )

class SampleProcessingEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SampleProcessingEnum",
    )

class PresenceEnum(EnumDefinitionImpl):

    PRESENT = PermissibleValue(
        text="PRESENT",
        description="The entity is present")
    ABSENT = PermissibleValue(
        text="ABSENT",
        description="The entity is absent")
    BELOW_DETECTION_LIMIT = PermissibleValue(
        text="BELOW_DETECTION_LIMIT",
        description="The entity is below the detection limit")
    ABOVE_DETECTION_LIMIT = PermissibleValue(
        text="ABOVE_DETECTION_LIMIT",
        description="The entity is above the detection limit")

    _defn = EnumDefinition(
        name="PresenceEnum",
    )

class PredictionOutcomeEnum(EnumDefinitionImpl):

    TP = PermissibleValue(
        text="TP",
        description="True Positive")
    FP = PermissibleValue(
        text="FP",
        description="False Positive")
    TN = PermissibleValue(
        text="TN",
        description="True Negative")
    FN = PermissibleValue(
        text="FN",
        description="False Negative")

    _defn = EnumDefinition(
        name="PredictionOutcomeEnum",
    )

class MicrofluidicArchitectureEnum(EnumDefinitionImpl):

    SINGLE_CHANNEL = PermissibleValue(
        text="SINGLE_CHANNEL",
        description="Single channel design")
    TWO_CHANNEL = PermissibleValue(
        text="TWO_CHANNEL",
        description="Two-channel design with separated compartments")
    MULTI_CHANNEL = PermissibleValue(
        text="MULTI_CHANNEL",
        description="Multiple channels (>2) design")
    LAYERED = PermissibleValue(
        text="LAYERED",
        description="Layered/stacked channel architecture")
    RADIAL = PermissibleValue(
        text="RADIAL",
        description="Radial channel architecture")
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="Network of interconnected channels")

    _defn = EnumDefinition(
        name="MicrofluidicArchitectureEnum",
    )

class ChannelConfigurationEnum(EnumDefinitionImpl):

    PARALLEL = PermissibleValue(
        text="PARALLEL",
        description="Parallel channel configuration")
    SERIAL = PermissibleValue(
        text="SERIAL",
        description="Serial/sequential channel configuration")
    BRANCHING = PermissibleValue(
        text="BRANCHING",
        description="Branching channel configuration")
    CIRCULAR = PermissibleValue(
        text="CIRCULAR",
        description="Circular/loop channel configuration")
    SERPENTINE = PermissibleValue(
        text="SERPENTINE",
        description="Serpentine channel pattern")
    Y_SHAPED = PermissibleValue(
        text="Y_SHAPED",
        description="Y-shaped channel junction")
    T_SHAPED = PermissibleValue(
        text="T_SHAPED",
        description="T-shaped channel junction")

    _defn = EnumDefinition(
        name="ChannelConfigurationEnum",
    )

class MembraneTypeEnum(EnumDefinitionImpl):

    POROUS_POLYMER = PermissibleValue(
        text="POROUS_POLYMER",
        description="Porous polymer membrane (e.g., PET, PC)")
    PDMS = PermissibleValue(
        text="PDMS",
        description="Polydimethylsiloxane membrane")
    COLLAGEN = PermissibleValue(
        text="COLLAGEN",
        description="Collagen-based membrane")
    ECM_COATED = PermissibleValue(
        text="ECM_COATED",
        description="Extracellular matrix-coated membrane")
    TRACK_ETCHED = PermissibleValue(
        text="TRACK_ETCHED",
        description="Track-etched membrane")
    ELECTROSPUN = PermissibleValue(
        text="ELECTROSPUN",
        description="Electrospun fiber membrane")
    HYDROGEL = PermissibleValue(
        text="HYDROGEL",
        description="Hydrogel membrane")

    _defn = EnumDefinition(
        name="MembraneTypeEnum",
    )

class InterfaceTypeEnum(EnumDefinitionImpl):

    AIR_LIQUID = PermissibleValue(
        text="AIR_LIQUID",
        description="Air-liquid interface")
    LIQUID_LIQUID = PermissibleValue(
        text="LIQUID_LIQUID",
        description="Liquid-liquid interface")
    CELL_CELL = PermissibleValue(
        text="CELL_CELL",
        description="Direct cell-cell interface")
    TISSUE_TISSUE = PermissibleValue(
        text="TISSUE_TISSUE",
        description="Tissue-tissue interface")
    VASCULAR_EPITHELIAL = PermissibleValue(
        text="VASCULAR_EPITHELIAL",
        description="Vascular-epithelial interface")

    _defn = EnumDefinition(
        name="InterfaceTypeEnum",
    )

class DeviceMaterialEnum(EnumDefinitionImpl):

    PDMS = PermissibleValue(
        text="PDMS",
        description="Polydimethylsiloxane")
    GLASS = PermissibleValue(
        text="GLASS",
        description="Glass")
    PLASTIC = PermissibleValue(
        text="PLASTIC",
        description="Plastic (general)")
    POLYSTYRENE = PermissibleValue(
        text="POLYSTYRENE",
        description="Polystyrene")
    POLYCARBONATE = PermissibleValue(
        text="POLYCARBONATE",
        description="Polycarbonate")
    PMMA = PermissibleValue(
        text="PMMA",
        description="Poly(methyl methacrylate)")
    COC = PermissibleValue(
        text="COC",
        description="Cyclic olefin copolymer")
    SILICON = PermissibleValue(
        text="SILICON",
        description="Silicon")
    HYDROGEL = PermissibleValue(
        text="HYDROGEL",
        description="Hydrogel materials")

    _defn = EnumDefinition(
        name="DeviceMaterialEnum",
    )

class SurfaceCoatingEnum(EnumDefinitionImpl):

    FIBRONECTIN = PermissibleValue(
        text="FIBRONECTIN",
        description="Fibronectin coating",
        meaning=CHEBI["5058"])
    COLLAGEN = PermissibleValue(
        text="COLLAGEN",
        description="Collagen coating",
        meaning=CHEBI["3815"])
    LAMININ = PermissibleValue(
        text="LAMININ",
        description="Laminin coating",
        meaning=MESH["D007797"])
    MATRIGEL = PermissibleValue(
        text="MATRIGEL",
        description="Matrigel coating")
    POLY_L_LYSINE = PermissibleValue(
        text="POLY_L_LYSINE",
        description="Poly-L-lysine coating",
        meaning=CHEBI["53412"])
    GELATIN = PermissibleValue(
        text="GELATIN",
        description="Gelatin coating",
        meaning=CHEBI["5291"])
    RGD_PEPTIDE = PermissibleValue(
        text="RGD_PEPTIDE",
        description="RGD peptide coating",
        meaning=NCIT["C13288"])
    ANTI_FOULING = PermissibleValue(
        text="ANTI_FOULING",
        description="Anti-fouling coating")
    OXYGEN_PLASMA = PermissibleValue(
        text="OXYGEN_PLASMA",
        description="Oxygen plasma treatment")

    _defn = EnumDefinition(
        name="SurfaceCoatingEnum",
    )

class FlowControlMethodEnum(EnumDefinitionImpl):

    SYRINGE_PUMP = PermissibleValue(
        text="SYRINGE_PUMP",
        description="Syringe pump-driven flow")
    PERISTALTIC_PUMP = PermissibleValue(
        text="PERISTALTIC_PUMP",
        description="Peristaltic pump-driven flow")
    GRAVITY_DRIVEN = PermissibleValue(
        text="GRAVITY_DRIVEN",
        description="Gravity-driven flow")
    PRESSURE_DRIVEN = PermissibleValue(
        text="PRESSURE_DRIVEN",
        description="Pressure-driven flow")
    ELECTROOSMOTIC = PermissibleValue(
        text="ELECTROOSMOTIC",
        description="Electroosmotic flow")
    CAPILLARY_ACTION = PermissibleValue(
        text="CAPILLARY_ACTION",
        description="Capillary action-driven flow")
    PNEUMATIC_VALVES = PermissibleValue(
        text="PNEUMATIC_VALVES",
        description="Pneumatic valve control")
    MICROVALVES = PermissibleValue(
        text="MICROVALVES",
        description="Integrated microvalves")

    _defn = EnumDefinition(
        name="FlowControlMethodEnum",
    )

class IntegratedSensorEnum(EnumDefinitionImpl):

    TEER = PermissibleValue(
        text="TEER",
        description="Trans-epithelial electrical resistance sensor")
    OXYGEN = PermissibleValue(
        text="OXYGEN",
        description="Oxygen sensor")
    PH = PermissibleValue(
        text="PH",
        description="pH sensor")
    TEMPERATURE = PermissibleValue(
        text="TEMPERATURE",
        description="Temperature sensor")
    PRESSURE = PermissibleValue(
        text="PRESSURE",
        description="Pressure sensor")
    FLOW_RATE = PermissibleValue(
        text="FLOW_RATE",
        description="Flow rate sensor")
    ELECTROCHEMICAL = PermissibleValue(
        text="ELECTROCHEMICAL",
        description="Electrochemical sensors")
    OPTICAL = PermissibleValue(
        text="OPTICAL",
        description="Optical sensors")
    IMPEDANCE = PermissibleValue(
        text="IMPEDANCE",
        description="Impedance sensors")

    _defn = EnumDefinition(
        name="IntegratedSensorEnum",
    )

class MechanicalStimulationTypeEnum(EnumDefinitionImpl):

    CYCLIC_STRETCH = PermissibleValue(
        text="CYCLIC_STRETCH",
        description="Cyclic stretching")
    SHEAR_STRESS = PermissibleValue(
        text="SHEAR_STRESS",
        description="Fluid shear stress",
        meaning=EFO["0022075"])
    COMPRESSION = PermissibleValue(
        text="COMPRESSION",
        description="Compression forces")
    TENSION = PermissibleValue(
        text="TENSION",
        description="Tensile forces")
    HYDROSTATIC_PRESSURE = PermissibleValue(
        text="HYDROSTATIC_PRESSURE",
        description="Hydrostatic pressure",
        meaning=EFO["0000534"])
    PULSATILE_FLOW = PermissibleValue(
        text="PULSATILE_FLOW",
        description="Pulsatile flow")
    BREATHING_MOTION = PermissibleValue(
        text="BREATHING_MOTION",
        description="Breathing-like cyclic motion")
    PERISTALTIC_MOTION = PermissibleValue(
        text="PERISTALTIC_MOTION",
        description="Peristaltic-like motion")

    _defn = EnumDefinition(
        name="MechanicalStimulationTypeEnum",
    )

class BiologicalOrganizationLevelEnum(EnumDefinitionImpl):

    SUBCELLULAR = PermissibleValue(
        text="SUBCELLULAR",
        description="Within a cell - subcellular components and molecular interactions")
    CELLULAR = PermissibleValue(
        text="CELLULAR",
        description="Individual cell level - single cell behavior and properties")
    CELLULAR_NEIGHBORHOOD = PermissibleValue(
        text="CELLULAR_NEIGHBORHOOD",
        description="Cell-cell interactions and local microenvironments")
    TISSUE = PermissibleValue(
        text="TISSUE",
        description="Tissue-level organization and multicellular structures")
    ORGAN = PermissibleValue(
        text="ORGAN",
        description="Organ-level physiology and function")
    SYSTEM = PermissibleValue(
        text="SYSTEM",
        description="Organ system and whole-body physiological integration")

    _defn = EnumDefinition(
        name="BiologicalOrganizationLevelEnum",
    )

class ComplexityLevelEnum(EnumDefinitionImpl):

    LOW = PermissibleValue(
        text="LOW",
        description="Simple, well-defined system with limited variables")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Intermediate complexity with multiple interacting components")
    HIGH = PermissibleValue(
        text="HIGH",
        description="Complex system with many variables and emergent properties")

    _defn = EnumDefinition(
        name="ComplexityLevelEnum",
    )

class ThreeDArchitectureEnum(EnumDefinitionImpl):

    SPHEROID = PermissibleValue(
        text="SPHEROID",
        description="Spherical 3D cell aggregates")
    ORGANOID = PermissibleValue(
        text="ORGANOID",
        description="Self-organizing 3D structures with organ-like features")
    SCAFFOLD_BASED = PermissibleValue(
        text="SCAFFOLD_BASED",
        description="Cells grown on 3D scaffolds or matrices")
    HYDROGEL_EMBEDDED = PermissibleValue(
        text="HYDROGEL_EMBEDDED",
        description="Cells embedded in hydrogel matrices")
    BIOPRINTED = PermissibleValue(
        text="BIOPRINTED",
        description="3D bioprinted structures")
    HANGING_DROP = PermissibleValue(
        text="HANGING_DROP",
        description="Spheroids formed using hanging drop method")

    _defn = EnumDefinition(
        name="ThreeDArchitectureEnum",
    )

class CocultureConfigurationEnum(EnumDefinitionImpl):

    DIRECT_CONTACT = PermissibleValue(
        text="DIRECT_CONTACT",
        description="Cells in direct physical contact")
    TRANSWELL = PermissibleValue(
        text="TRANSWELL",
        description="Cells separated by permeable membrane")
    CONDITIONED_MEDIA = PermissibleValue(
        text="CONDITIONED_MEDIA",
        description="Cells exposed to media conditioned by other cells")
    MICROPATTERN = PermissibleValue(
        text="MICROPATTERN",
        description="Cells patterned in defined spatial arrangements")
    GRADIENT = PermissibleValue(
        text="GRADIENT",
        description="Cells exposed to chemical or physical gradients")

    _defn = EnumDefinition(
        name="CocultureConfigurationEnum",
    )

class RatioTypeEnum(EnumDefinitionImpl):

    PERCENTAGE = PermissibleValue(
        text="PERCENTAGE",
        description="Percentage of total cells")
    ABSOLUTE = PermissibleValue(
        text="ABSOLUTE",
        description="Absolute cell numbers")
    FOLD = PermissibleValue(
        text="FOLD",
        description="Fold ratio relative to reference")

    _defn = EnumDefinition(
        name="RatioTypeEnum",
    )

class PBPKCompartmentEnum(EnumDefinitionImpl):

    LIVER = PermissibleValue(
        text="LIVER",
        description="Hepatic compartment",
        meaning=UBERON["0002107"])
    KIDNEY = PermissibleValue(
        text="KIDNEY",
        description="Renal compartment",
        meaning=UBERON["0002113"])
    LUNG = PermissibleValue(
        text="LUNG",
        description="Pulmonary compartment",
        meaning=UBERON["0002048"])
    BRAIN = PermissibleValue(
        text="BRAIN",
        description="Central nervous system compartment",
        meaning=UBERON["0000955"])
    HEART = PermissibleValue(
        text="HEART",
        description="Cardiac compartment",
        meaning=UBERON["0000948"])
    MUSCLE = PermissibleValue(
        text="MUSCLE",
        description="Skeletal muscle compartment",
        meaning=UBERON["0001134"])
    FAT = PermissibleValue(
        text="FAT",
        description="Adipose tissue compartment")
    SKIN = PermissibleValue(
        text="SKIN",
        description="Dermal compartment")
    BONE = PermissibleValue(
        text="BONE",
        description="Bone tissue compartment")
    GI_TRACT = PermissibleValue(
        text="GI_TRACT",
        description="Gastrointestinal tract compartment")
    PLASMA = PermissibleValue(
        text="PLASMA",
        description="Plasma compartment",
        meaning=UBERON["0001969"])
    BLOOD = PermissibleValue(
        text="BLOOD",
        description="Blood compartment")

    _defn = EnumDefinition(
        name="PBPKCompartmentEnum",
    )

class DigitalTwinScopeEnum(EnumDefinitionImpl):

    ORGAN = PermissibleValue(
        text="ORGAN",
        description="Digital twin of a specific organ")
    PATIENT = PermissibleValue(
        text="PATIENT",
        description="Digital twin of an individual patient")
    POPULATION = PermissibleValue(
        text="POPULATION",
        description="Digital twin representing a population",
        meaning=MAMO["0000028"])
    PATHWAY = PermissibleValue(
        text="PATHWAY",
        description="Digital twin of biological pathways")
    DISEASE = PermissibleValue(
        text="DISEASE",
        description="Digital twin of disease progression")

    _defn = EnumDefinition(
        name="DigitalTwinScopeEnum",
    )

class MLAlgorithmEnum(EnumDefinitionImpl):

    RANDOM_FOREST = PermissibleValue(
        text="RANDOM_FOREST",
        description="Random Forest algorithm")
    SUPPORT_VECTOR_MACHINE = PermissibleValue(
        text="SUPPORT_VECTOR_MACHINE",
        description="Support Vector Machine",
        meaning=OBI["0000700"])
    NEURAL_NETWORK = PermissibleValue(
        text="NEURAL_NETWORK",
        description="Artificial Neural Networks")
    DEEP_LEARNING = PermissibleValue(
        text="DEEP_LEARNING",
        description="Deep learning models")
    GRADIENT_BOOSTING = PermissibleValue(
        text="GRADIENT_BOOSTING",
        description="Gradient boosting methods",
        meaning=MESH["D000098404"])
    LINEAR_REGRESSION = PermissibleValue(
        text="LINEAR_REGRESSION",
        description="Linear regression models",
        meaning=OBI["0200103"])
    LOGISTIC_REGRESSION = PermissibleValue(
        text="LOGISTIC_REGRESSION",
        description="Logistic regression models",
        meaning=OBI["0200002"])
    NAIVE_BAYES = PermissibleValue(
        text="NAIVE_BAYES",
        description="Naive Bayes classifier")
    K_MEANS = PermissibleValue(
        text="K_MEANS",
        description="K-means clustering",
        meaning=OBI["0200041"])
    REINFORCEMENT_LEARNING = PermissibleValue(
        text="REINFORCEMENT_LEARNING",
        description="Reinforcement learning approaches")

    _defn = EnumDefinition(
        name="MLAlgorithmEnum",
    )

class FeatureTypeEnum(EnumDefinitionImpl):

    MOLECULAR = PermissibleValue(
        text="MOLECULAR",
        description="Molecular descriptors and chemical features")
    PHENOTYPIC = PermissibleValue(
        text="PHENOTYPIC",
        description="Phenotypic and physiological features")
    GENOMIC = PermissibleValue(
        text="GENOMIC",
        description="Genomic and genetic features")
    TRANSCRIPTOMIC = PermissibleValue(
        text="TRANSCRIPTOMIC",
        description="Gene expression features",
        meaning=EDAM["3308"])
    PROTEOMIC = PermissibleValue(
        text="PROTEOMIC",
        description="Protein abundance and modification features",
        meaning=EDAM["0121"])
    METABOLOMIC = PermissibleValue(
        text="METABOLOMIC",
        description="Metabolite concentration features",
        meaning=EDAM["3172"])
    IMAGING = PermissibleValue(
        text="IMAGING",
        description="Image-derived features",
        meaning=EDAM["3382"])
    CLINICAL = PermissibleValue(
        text="CLINICAL",
        description="Clinical and demographic features")
    TEMPORAL = PermissibleValue(
        text="TEMPORAL",
        description="Time-series and temporal features")

    _defn = EnumDefinition(
        name="FeatureTypeEnum",
    )

class InterpretabilityLevelEnum(EnumDefinitionImpl):

    BLACK_BOX = PermissibleValue(
        text="BLACK_BOX",
        description="No interpretability - predictions only")
    INTERPRETABLE = PermissibleValue(
        text="INTERPRETABLE",
        description="Some level of feature importance available")
    EXPLAINABLE = PermissibleValue(
        text="EXPLAINABLE",
        description="Full mechanistic interpretation possible")
    CAUSAL = PermissibleValue(
        text="CAUSAL",
        description="Causal relationships can be inferred")

    _defn = EnumDefinition(
        name="InterpretabilityLevelEnum",
    )

class CrossValidationMethodEnum(EnumDefinitionImpl):

    K_FOLD = PermissibleValue(
        text="K_FOLD",
        description="K-fold cross-validation",
        meaning=OBI["0200032"])
    STRATIFIED_K_FOLD = PermissibleValue(
        text="STRATIFIED_K_FOLD",
        description="Stratified k-fold cross-validation")
    LEAVE_ONE_OUT = PermissibleValue(
        text="LEAVE_ONE_OUT",
        description="Leave-one-out cross-validation",
        meaning=OBI["0200033"])
    TIME_SERIES_SPLIT = PermissibleValue(
        text="TIME_SERIES_SPLIT",
        description="Time series cross-validation")
    MONTE_CARLO = PermissibleValue(
        text="MONTE_CARLO",
        description="Monte Carlo cross-validation")

    _defn = EnumDefinition(
        name="CrossValidationMethodEnum",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=NAMO.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=NAMO.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NAMO.description, domain=None, range=Optional[str])

slots.type = Slot(uri=NAMO.type, name="type", curie=NAMO.curie('type'),
                   model_uri=NAMO.type, domain=None, range=Optional[str])

slots.dataset__model_systems = Slot(uri=NAMO.model_systems, name="dataset__model_systems", curie=NAMO.curie('model_systems'),
                   model_uri=NAMO.dataset__model_systems, domain=None, range=Optional[Union[dict[Union[str, ModelSystemId], Union[dict, ModelSystem]], list[Union[dict, ModelSystem]]]])

slots.dataset__studies = Slot(uri=NAMO.studies, name="dataset__studies", curie=NAMO.curie('studies'),
                   model_uri=NAMO.dataset__studies, domain=None, range=Optional[Union[dict[Union[str, StudyId], Union[dict, Study]], list[Union[dict, Study]]]])

slots.study__context_of_use = Slot(uri=NAMO.context_of_use, name="study__context_of_use", curie=NAMO.curie('context_of_use'),
                   model_uri=NAMO.study__context_of_use, domain=None, range=Optional[str])

slots.study__biological_context = Slot(uri=NAMO.biological_context, name="study__biological_context", curie=NAMO.curie('biological_context'),
                   model_uri=NAMO.study__biological_context, domain=None, range=Optional[str])

slots.study__perturbations = Slot(uri=NAMO.perturbations, name="study__perturbations", curie=NAMO.curie('perturbations'),
                   model_uri=NAMO.study__perturbations, domain=None, range=Optional[str])

slots.study__endpoints = Slot(uri=NAMO.endpoints, name="study__endpoints", curie=NAMO.curie('endpoints'),
                   model_uri=NAMO.study__endpoints, domain=None, range=Optional[str])

slots.study__plan_comparators = Slot(uri=NAMO.plan_comparators, name="study__plan_comparators", curie=NAMO.curie('plan_comparators'),
                   model_uri=NAMO.study__plan_comparators, domain=None, range=Optional[str])

slots.modelSystem__models = Slot(uri=NAMO.models, name="modelSystem__models", curie=NAMO.curie('models'),
                   model_uri=NAMO.modelSystem__models, domain=None, range=Optional[Union[Union[dict, ModelsRelationship], list[Union[dict, ModelsRelationship]]]])

slots.animalModel__species = Slot(uri=NAMO.species, name="animalModel__species", curie=NAMO.curie('species'),
                   model_uri=NAMO.animalModel__species, domain=None, range=Union[str, TermId])

slots.animalModel__strain = Slot(uri=NAMO.strain, name="animalModel__strain", curie=NAMO.curie('strain'),
                   model_uri=NAMO.animalModel__strain, domain=None, range=Optional[Union[str, TermId]])

slots.animalModel__age = Slot(uri=NAMO.age, name="animalModel__age", curie=NAMO.curie('age'),
                   model_uri=NAMO.animalModel__age, domain=None, range=Optional[Union[str, TermId]])

slots.animalModel__environment = Slot(uri=NAMO.environment, name="animalModel__environment", curie=NAMO.curie('environment'),
                   model_uri=NAMO.animalModel__environment, domain=None, range=Optional[Union[str, TermId]])

slots.nAMModel__biological_organization_level = Slot(uri=NAMO.biological_organization_level, name="nAMModel__biological_organization_level", curie=NAMO.curie('biological_organization_level'),
                   model_uri=NAMO.nAMModel__biological_organization_level, domain=None, range=Optional[Union[str, "BiologicalOrganizationLevelEnum"]])

slots.nAMModel__spatial_context = Slot(uri=NAMO.spatial_context, name="nAMModel__spatial_context", curie=NAMO.curie('spatial_context'),
                   model_uri=NAMO.nAMModel__spatial_context, domain=None, range=Optional[str])

slots.nAMModel__complexity_level = Slot(uri=NAMO.complexity_level, name="nAMModel__complexity_level", curie=NAMO.curie('complexity_level'),
                   model_uri=NAMO.nAMModel__complexity_level, domain=None, range=Optional[Union[str, "ComplexityLevelEnum"]])

slots.nAMModel__references = Slot(uri=NAMO.references, name="nAMModel__references", curie=NAMO.curie('references'),
                   model_uri=NAMO.nAMModel__references, domain=None, range=Optional[Union[dict[Union[str, ReferenceId], Union[dict, Reference]], list[Union[dict, Reference]]]])

slots.cellularSystem__cell_types = Slot(uri=NAMO.cell_types, name="cellularSystem__cell_types", curie=NAMO.curie('cell_types'),
                   model_uri=NAMO.cellularSystem__cell_types, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.cellularSystem__cell_source = Slot(uri=NAMO.cell_source, name="cellularSystem__cell_source", curie=NAMO.curie('cell_source'),
                   model_uri=NAMO.cellularSystem__cell_source, domain=None, range=Optional[str])

slots.cellularSystem__culture_conditions = Slot(uri=NAMO.culture_conditions, name="cellularSystem__culture_conditions", curie=NAMO.curie('culture_conditions'),
                   model_uri=NAMO.cellularSystem__culture_conditions, domain=None, range=Optional[str])

slots.twoDCellCulture__substrate_type = Slot(uri=NAMO.substrate_type, name="twoDCellCulture__substrate_type", curie=NAMO.curie('substrate_type'),
                   model_uri=NAMO.twoDCellCulture__substrate_type, domain=None, range=Optional[str])

slots.twoDCellCulture__confluence_level = Slot(uri=NAMO.confluence_level, name="twoDCellCulture__confluence_level", curie=NAMO.curie('confluence_level'),
                   model_uri=NAMO.twoDCellCulture__confluence_level, domain=None, range=Optional[float])

slots.twoDCellCulture__passage_protocol = Slot(uri=NAMO.passage_protocol, name="twoDCellCulture__passage_protocol", curie=NAMO.curie('passage_protocol'),
                   model_uri=NAMO.twoDCellCulture__passage_protocol, domain=None, range=Optional[str])

slots.threeDCellCulture__three_d_architecture = Slot(uri=NAMO.three_d_architecture, name="threeDCellCulture__three_d_architecture", curie=NAMO.curie('three_d_architecture'),
                   model_uri=NAMO.threeDCellCulture__three_d_architecture, domain=None, range=Optional[Union[str, "ThreeDArchitectureEnum"]])

slots.threeDCellCulture__matrix_composition = Slot(uri=NAMO.matrix_composition, name="threeDCellCulture__matrix_composition", curie=NAMO.curie('matrix_composition'),
                   model_uri=NAMO.threeDCellCulture__matrix_composition, domain=None, range=Optional[str])

slots.threeDCellCulture__size_range = Slot(uri=NAMO.size_range, name="threeDCellCulture__size_range", curie=NAMO.curie('size_range'),
                   model_uri=NAMO.threeDCellCulture__size_range, domain=None, range=Optional[str])

slots.coCulture__coculture_configuration = Slot(uri=NAMO.coculture_configuration, name="coCulture__coculture_configuration", curie=NAMO.curie('coculture_configuration'),
                   model_uri=NAMO.coCulture__coculture_configuration, domain=None, range=Optional[Union[str, "CocultureConfigurationEnum"]])

slots.coCulture__cell_ratios = Slot(uri=NAMO.cell_ratios, name="coCulture__cell_ratios", curie=NAMO.curie('cell_ratios'),
                   model_uri=NAMO.coCulture__cell_ratios, domain=None, range=Optional[Union[Union[dict, CellRatio], list[Union[dict, CellRatio]]]])

slots.coCulture__interaction_mechanisms = Slot(uri=NAMO.interaction_mechanisms, name="coCulture__interaction_mechanisms", curie=NAMO.curie('interaction_mechanisms'),
                   model_uri=NAMO.coCulture__interaction_mechanisms, domain=None, range=Optional[Union[str, list[str]]])

slots.organoid__organ_modeled = Slot(uri=NAMO.organ_modeled, name="organoid__organ_modeled", curie=NAMO.curie('organ_modeled'),
                   model_uri=NAMO.organoid__organ_modeled, domain=None, range=Optional[Union[dict, Term]])

slots.organoid__differentiation_method = Slot(uri=NAMO.differentiation_method, name="organoid__differentiation_method", curie=NAMO.curie('differentiation_method'),
                   model_uri=NAMO.organoid__differentiation_method, domain=None, range=Optional[str])

slots.organoid__culture_system = Slot(uri=NAMO.culture_system, name="organoid__culture_system", curie=NAMO.curie('culture_system'),
                   model_uri=NAMO.organoid__culture_system, domain=None, range=Optional[str])

slots.cellLineModel__passage_range = Slot(uri=NAMO.passage_range, name="cellLineModel__passage_range", curie=NAMO.curie('passage_range'),
                   model_uri=NAMO.cellLineModel__passage_range, domain=None, range=Optional[str])

slots.cellLineModel__authentication_method = Slot(uri=NAMO.authentication_method, name="cellLineModel__authentication_method", curie=NAMO.curie('authentication_method'),
                   model_uri=NAMO.cellLineModel__authentication_method, domain=None, range=Optional[str])

slots.microphysiologicalSystem__microfluidic_design = Slot(uri=NAMO.microfluidic_design, name="microphysiologicalSystem__microfluidic_design", curie=NAMO.curie('microfluidic_design'),
                   model_uri=NAMO.microphysiologicalSystem__microfluidic_design, domain=None, range=Optional[Union[dict, MicrofluidicDesign]])

slots.microphysiologicalSystem__mechanical_forces = Slot(uri=NAMO.mechanical_forces, name="microphysiologicalSystem__mechanical_forces", curie=NAMO.curie('mechanical_forces'),
                   model_uri=NAMO.microphysiologicalSystem__mechanical_forces, domain=None, range=Optional[Union[dict, MechanicalStimulation]])

slots.microphysiologicalSystem__perfusion_system = Slot(uri=NAMO.perfusion_system, name="microphysiologicalSystem__perfusion_system", curie=NAMO.curie('perfusion_system'),
                   model_uri=NAMO.microphysiologicalSystem__perfusion_system, domain=None, range=Optional[str])

slots.microphysiologicalSystem__sensor_integration = Slot(uri=NAMO.sensor_integration, name="microphysiologicalSystem__sensor_integration", curie=NAMO.curie('sensor_integration'),
                   model_uri=NAMO.microphysiologicalSystem__sensor_integration, domain=None, range=Optional[Union[Union[str, "IntegratedSensorEnum"], list[Union[str, "IntegratedSensorEnum"]]]])

slots.organOnChip__organ_modeled = Slot(uri=NAMO.organ_modeled, name="organOnChip__organ_modeled", curie=NAMO.curie('organ_modeled'),
                   model_uri=NAMO.organOnChip__organ_modeled, domain=None, range=Optional[Union[dict, Term]])

slots.organOnChip__cell_types = Slot(uri=NAMO.cell_types, name="organOnChip__cell_types", curie=NAMO.curie('cell_types'),
                   model_uri=NAMO.organOnChip__cell_types, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.organOnChip__cell_source = Slot(uri=NAMO.cell_source, name="organOnChip__cell_source", curie=NAMO.curie('cell_source'),
                   model_uri=NAMO.organOnChip__cell_source, domain=None, range=Optional[str])

slots.tissueOnChip__tissue_modeled = Slot(uri=NAMO.tissue_modeled, name="tissueOnChip__tissue_modeled", curie=NAMO.curie('tissue_modeled'),
                   model_uri=NAMO.tissueOnChip__tissue_modeled, domain=None, range=Optional[Union[dict, Term]])

slots.tissueOnChip__tissue_architecture = Slot(uri=NAMO.tissue_architecture, name="tissueOnChip__tissue_architecture", curie=NAMO.curie('tissue_architecture'),
                   model_uri=NAMO.tissueOnChip__tissue_architecture, domain=None, range=Optional[str])

slots.tissueOnChip__barrier_functions = Slot(uri=NAMO.barrier_functions, name="tissueOnChip__barrier_functions", curie=NAMO.curie('barrier_functions'),
                   model_uri=NAMO.tissueOnChip__barrier_functions, domain=None, range=Optional[Union[str, list[str]]])

slots.inSilicoModel__computational_method = Slot(uri=NAMO.computational_method, name="inSilicoModel__computational_method", curie=NAMO.curie('computational_method'),
                   model_uri=NAMO.inSilicoModel__computational_method, domain=None, range=Optional[str])

slots.inSilicoModel__software_platform = Slot(uri=NAMO.software_platform, name="inSilicoModel__software_platform", curie=NAMO.curie('software_platform'),
                   model_uri=NAMO.inSilicoModel__software_platform, domain=None, range=Optional[str])

slots.inSilicoModel__validation_datasets = Slot(uri=NAMO.validation_datasets, name="inSilicoModel__validation_datasets", curie=NAMO.curie('validation_datasets'),
                   model_uri=NAMO.inSilicoModel__validation_datasets, domain=None, range=Optional[Union[str, list[str]]])

slots.inSilicoModel__prediction_scope = Slot(uri=NAMO.prediction_scope, name="inSilicoModel__prediction_scope", curie=NAMO.curie('prediction_scope'),
                   model_uri=NAMO.inSilicoModel__prediction_scope, domain=None, range=Optional[str])

slots.qSARModel__molecular_descriptors = Slot(uri=NAMO.molecular_descriptors, name="qSARModel__molecular_descriptors", curie=NAMO.curie('molecular_descriptors'),
                   model_uri=NAMO.qSARModel__molecular_descriptors, domain=None, range=Optional[Union[str, list[str]]])

slots.qSARModel__activity_endpoint = Slot(uri=NAMO.activity_endpoint, name="qSARModel__activity_endpoint", curie=NAMO.curie('activity_endpoint'),
                   model_uri=NAMO.qSARModel__activity_endpoint, domain=None, range=Optional[str])

slots.qSARModel__training_dataset_size = Slot(uri=NAMO.training_dataset_size, name="qSARModel__training_dataset_size", curie=NAMO.curie('training_dataset_size'),
                   model_uri=NAMO.qSARModel__training_dataset_size, domain=None, range=Optional[int])

slots.qSARModel__model_performance = Slot(uri=NAMO.model_performance, name="qSARModel__model_performance", curie=NAMO.curie('model_performance'),
                   model_uri=NAMO.qSARModel__model_performance, domain=None, range=Optional[Union[dict, ModelPerformance]])

slots.pBPKModel__compartments = Slot(uri=NAMO.compartments, name="pBPKModel__compartments", curie=NAMO.curie('compartments'),
                   model_uri=NAMO.pBPKModel__compartments, domain=None, range=Optional[Union[dict[Union[str, PBPKCompartmentId], Union[dict, PBPKCompartment]], list[Union[dict, PBPKCompartment]]]])

slots.pBPKModel__species_modeled = Slot(uri=NAMO.species_modeled, name="pBPKModel__species_modeled", curie=NAMO.curie('species_modeled'),
                   model_uri=NAMO.pBPKModel__species_modeled, domain=None, range=Optional[Union[dict, Term]])

slots.pBPKModel__drug_properties = Slot(uri=NAMO.drug_properties, name="pBPKModel__drug_properties", curie=NAMO.curie('drug_properties'),
                   model_uri=NAMO.pBPKModel__drug_properties, domain=None, range=Optional[Union[dict, DrugProperties]])

slots.pBPKModel__elimination_pathways = Slot(uri=NAMO.elimination_pathways, name="pBPKModel__elimination_pathways", curie=NAMO.curie('elimination_pathways'),
                   model_uri=NAMO.pBPKModel__elimination_pathways, domain=None, range=Optional[Union[str, list[str]]])

slots.digitalTwin__twin_scope = Slot(uri=NAMO.twin_scope, name="digitalTwin__twin_scope", curie=NAMO.curie('twin_scope'),
                   model_uri=NAMO.digitalTwin__twin_scope, domain=None, range=Optional[Union[str, "DigitalTwinScopeEnum"]])

slots.digitalTwin__real_time_data_sources = Slot(uri=NAMO.real_time_data_sources, name="digitalTwin__real_time_data_sources", curie=NAMO.curie('real_time_data_sources'),
                   model_uri=NAMO.digitalTwin__real_time_data_sources, domain=None, range=Optional[Union[str, list[str]]])

slots.digitalTwin__personalization_parameters = Slot(uri=NAMO.personalization_parameters, name="digitalTwin__personalization_parameters", curie=NAMO.curie('personalization_parameters'),
                   model_uri=NAMO.digitalTwin__personalization_parameters, domain=None, range=Optional[Union[str, list[str]]])

slots.digitalTwin__update_frequency = Slot(uri=NAMO.update_frequency, name="digitalTwin__update_frequency", curie=NAMO.curie('update_frequency'),
                   model_uri=NAMO.digitalTwin__update_frequency, domain=None, range=Optional[str])

slots.mLModel__ml_algorithm = Slot(uri=NAMO.ml_algorithm, name="mLModel__ml_algorithm", curie=NAMO.curie('ml_algorithm'),
                   model_uri=NAMO.mLModel__ml_algorithm, domain=None, range=Optional[Union[str, "MLAlgorithmEnum"]])

slots.mLModel__feature_types = Slot(uri=NAMO.feature_types, name="mLModel__feature_types", curie=NAMO.curie('feature_types'),
                   model_uri=NAMO.mLModel__feature_types, domain=None, range=Optional[Union[Union[str, "FeatureTypeEnum"], list[Union[str, "FeatureTypeEnum"]]]])

slots.mLModel__training_data_size = Slot(uri=NAMO.training_data_size, name="mLModel__training_data_size", curie=NAMO.curie('training_data_size'),
                   model_uri=NAMO.mLModel__training_data_size, domain=None, range=Optional[int])

slots.mLModel__model_interpretability = Slot(uri=NAMO.model_interpretability, name="mLModel__model_interpretability", curie=NAMO.curie('model_interpretability'),
                   model_uri=NAMO.mLModel__model_interpretability, domain=None, range=Optional[Union[str, "InterpretabilityLevelEnum"]])

slots.mLModel__cross_validation = Slot(uri=NAMO.cross_validation, name="mLModel__cross_validation", curie=NAMO.curie('cross_validation'),
                   model_uri=NAMO.mLModel__cross_validation, domain=None, range=Optional[Union[dict, CrossValidation]])

slots.cellRatio__cell_type = Slot(uri=NAMO.cell_type, name="cellRatio__cell_type", curie=NAMO.curie('cell_type'),
                   model_uri=NAMO.cellRatio__cell_type, domain=None, range=Optional[Union[dict, Term]])

slots.cellRatio__ratio = Slot(uri=NAMO.ratio, name="cellRatio__ratio", curie=NAMO.curie('ratio'),
                   model_uri=NAMO.cellRatio__ratio, domain=None, range=Optional[float])

slots.cellRatio__ratio_type = Slot(uri=NAMO.ratio_type, name="cellRatio__ratio_type", curie=NAMO.curie('ratio_type'),
                   model_uri=NAMO.cellRatio__ratio_type, domain=None, range=Optional[Union[str, "RatioTypeEnum"]])

slots.modelPerformance__accuracy = Slot(uri=NAMO.accuracy, name="modelPerformance__accuracy", curie=NAMO.curie('accuracy'),
                   model_uri=NAMO.modelPerformance__accuracy, domain=None, range=Optional[float])

slots.modelPerformance__sensitivity = Slot(uri=NAMO.sensitivity, name="modelPerformance__sensitivity", curie=NAMO.curie('sensitivity'),
                   model_uri=NAMO.modelPerformance__sensitivity, domain=None, range=Optional[float])

slots.modelPerformance__specificity = Slot(uri=NAMO.specificity, name="modelPerformance__specificity", curie=NAMO.curie('specificity'),
                   model_uri=NAMO.modelPerformance__specificity, domain=None, range=Optional[float])

slots.modelPerformance__r_squared = Slot(uri=NAMO.r_squared, name="modelPerformance__r_squared", curie=NAMO.curie('r_squared'),
                   model_uri=NAMO.modelPerformance__r_squared, domain=None, range=Optional[float])

slots.modelPerformance__rmse = Slot(uri=NAMO.rmse, name="modelPerformance__rmse", curie=NAMO.curie('rmse'),
                   model_uri=NAMO.modelPerformance__rmse, domain=None, range=Optional[float])

slots.modelPerformance__auc = Slot(uri=NAMO.auc, name="modelPerformance__auc", curie=NAMO.curie('auc'),
                   model_uri=NAMO.modelPerformance__auc, domain=None, range=Optional[float])

slots.pBPKCompartment__compartment_type = Slot(uri=NAMO.compartment_type, name="pBPKCompartment__compartment_type", curie=NAMO.curie('compartment_type'),
                   model_uri=NAMO.pBPKCompartment__compartment_type, domain=None, range=Optional[Union[str, "PBPKCompartmentEnum"]])

slots.pBPKCompartment__volume = Slot(uri=NAMO.volume, name="pBPKCompartment__volume", curie=NAMO.curie('volume'),
                   model_uri=NAMO.pBPKCompartment__volume, domain=None, range=Optional[float])

slots.pBPKCompartment__blood_flow = Slot(uri=NAMO.blood_flow, name="pBPKCompartment__blood_flow", curie=NAMO.curie('blood_flow'),
                   model_uri=NAMO.pBPKCompartment__blood_flow, domain=None, range=Optional[float])

slots.pBPKCompartment__partition_coefficient = Slot(uri=NAMO.partition_coefficient, name="pBPKCompartment__partition_coefficient", curie=NAMO.curie('partition_coefficient'),
                   model_uri=NAMO.pBPKCompartment__partition_coefficient, domain=None, range=Optional[float])

slots.drugProperties__molecular_weight = Slot(uri=NAMO.molecular_weight, name="drugProperties__molecular_weight", curie=NAMO.curie('molecular_weight'),
                   model_uri=NAMO.drugProperties__molecular_weight, domain=None, range=Optional[float])

slots.drugProperties__logp = Slot(uri=NAMO.logp, name="drugProperties__logp", curie=NAMO.curie('logp'),
                   model_uri=NAMO.drugProperties__logp, domain=None, range=Optional[float])

slots.drugProperties__pka = Slot(uri=NAMO.pka, name="drugProperties__pka", curie=NAMO.curie('pka'),
                   model_uri=NAMO.drugProperties__pka, domain=None, range=Optional[float])

slots.drugProperties__protein_binding = Slot(uri=NAMO.protein_binding, name="drugProperties__protein_binding", curie=NAMO.curie('protein_binding'),
                   model_uri=NAMO.drugProperties__protein_binding, domain=None, range=Optional[float])

slots.drugProperties__clearance = Slot(uri=NAMO.clearance, name="drugProperties__clearance", curie=NAMO.curie('clearance'),
                   model_uri=NAMO.drugProperties__clearance, domain=None, range=Optional[float])

slots.crossValidation__cv_method = Slot(uri=NAMO.cv_method, name="crossValidation__cv_method", curie=NAMO.curie('cv_method'),
                   model_uri=NAMO.crossValidation__cv_method, domain=None, range=Optional[Union[str, "CrossValidationMethodEnum"]])

slots.crossValidation__n_folds = Slot(uri=NAMO.n_folds, name="crossValidation__n_folds", curie=NAMO.curie('n_folds'),
                   model_uri=NAMO.crossValidation__n_folds, domain=None, range=Optional[int])

slots.crossValidation__cv_score = Slot(uri=NAMO.cv_score, name="crossValidation__cv_score", curie=NAMO.curie('cv_score'),
                   model_uri=NAMO.crossValidation__cv_score, domain=None, range=Optional[float])

slots.crossValidation__cv_std = Slot(uri=NAMO.cv_std, name="crossValidation__cv_std", curie=NAMO.curie('cv_std'),
                   model_uri=NAMO.crossValidation__cv_std, domain=None, range=Optional[float])

slots.microfluidicDesign__architecture_type = Slot(uri=NAMO.architecture_type, name="microfluidicDesign__architecture_type", curie=NAMO.curie('architecture_type'),
                   model_uri=NAMO.microfluidicDesign__architecture_type, domain=None, range=Optional[Union[str, "MicrofluidicArchitectureEnum"]])

slots.microfluidicDesign__number_of_channels = Slot(uri=NAMO.number_of_channels, name="microfluidicDesign__number_of_channels", curie=NAMO.curie('number_of_channels'),
                   model_uri=NAMO.microfluidicDesign__number_of_channels, domain=None, range=Optional[int])

slots.microfluidicDesign__channel_configuration = Slot(uri=NAMO.channel_configuration, name="microfluidicDesign__channel_configuration", curie=NAMO.curie('channel_configuration'),
                   model_uri=NAMO.microfluidicDesign__channel_configuration, domain=None, range=Optional[Union[Union[str, "ChannelConfigurationEnum"], list[Union[str, "ChannelConfigurationEnum"]]]])

slots.microfluidicDesign__membrane_type = Slot(uri=NAMO.membrane_type, name="microfluidicDesign__membrane_type", curie=NAMO.curie('membrane_type'),
                   model_uri=NAMO.microfluidicDesign__membrane_type, domain=None, range=Optional[Union[str, "MembraneTypeEnum"]])

slots.microfluidicDesign__membrane_pore_size = Slot(uri=NAMO.membrane_pore_size, name="microfluidicDesign__membrane_pore_size", curie=NAMO.curie('membrane_pore_size'),
                   model_uri=NAMO.microfluidicDesign__membrane_pore_size, domain=None, range=Optional[float])

slots.microfluidicDesign__membrane_thickness = Slot(uri=NAMO.membrane_thickness, name="microfluidicDesign__membrane_thickness", curie=NAMO.curie('membrane_thickness'),
                   model_uri=NAMO.microfluidicDesign__membrane_thickness, domain=None, range=Optional[float])

slots.microfluidicDesign__interface_type = Slot(uri=NAMO.interface_type, name="microfluidicDesign__interface_type", curie=NAMO.curie('interface_type'),
                   model_uri=NAMO.microfluidicDesign__interface_type, domain=None, range=Optional[Union[Union[str, "InterfaceTypeEnum"], list[Union[str, "InterfaceTypeEnum"]]]])

slots.microfluidicDesign__channel_dimensions = Slot(uri=NAMO.channel_dimensions, name="microfluidicDesign__channel_dimensions", curie=NAMO.curie('channel_dimensions'),
                   model_uri=NAMO.microfluidicDesign__channel_dimensions, domain=None, range=Optional[Union[Union[dict, ChannelDimensions], list[Union[dict, ChannelDimensions]]]])

slots.microfluidicDesign__material = Slot(uri=NAMO.material, name="microfluidicDesign__material", curie=NAMO.curie('material'),
                   model_uri=NAMO.microfluidicDesign__material, domain=None, range=Optional[Union[Union[str, "DeviceMaterialEnum"], list[Union[str, "DeviceMaterialEnum"]]]])

slots.microfluidicDesign__surface_treatment = Slot(uri=NAMO.surface_treatment, name="microfluidicDesign__surface_treatment", curie=NAMO.curie('surface_treatment'),
                   model_uri=NAMO.microfluidicDesign__surface_treatment, domain=None, range=Optional[Union[Union[str, "SurfaceCoatingEnum"], list[Union[str, "SurfaceCoatingEnum"]]]])

slots.microfluidicDesign__flow_control_method = Slot(uri=NAMO.flow_control_method, name="microfluidicDesign__flow_control_method", curie=NAMO.curie('flow_control_method'),
                   model_uri=NAMO.microfluidicDesign__flow_control_method, domain=None, range=Optional[Union[Union[str, "FlowControlMethodEnum"], list[Union[str, "FlowControlMethodEnum"]]]])

slots.microfluidicDesign__sensors_integrated = Slot(uri=NAMO.sensors_integrated, name="microfluidicDesign__sensors_integrated", curie=NAMO.curie('sensors_integrated'),
                   model_uri=NAMO.microfluidicDesign__sensors_integrated, domain=None, range=Optional[Union[Union[str, "IntegratedSensorEnum"], list[Union[str, "IntegratedSensorEnum"]]]])

slots.microfluidicDesign__special_features = Slot(uri=NAMO.special_features, name="microfluidicDesign__special_features", curie=NAMO.curie('special_features'),
                   model_uri=NAMO.microfluidicDesign__special_features, domain=None, range=Optional[Union[str, list[str]]])

slots.channelDimensions__channel_name = Slot(uri=NAMO.channel_name, name="channelDimensions__channel_name", curie=NAMO.curie('channel_name'),
                   model_uri=NAMO.channelDimensions__channel_name, domain=None, range=Optional[str])

slots.channelDimensions__width = Slot(uri=NAMO.width, name="channelDimensions__width", curie=NAMO.curie('width'),
                   model_uri=NAMO.channelDimensions__width, domain=None, range=Optional[float])

slots.channelDimensions__height = Slot(uri=NAMO.height, name="channelDimensions__height", curie=NAMO.curie('height'),
                   model_uri=NAMO.channelDimensions__height, domain=None, range=Optional[float])

slots.channelDimensions__length = Slot(uri=NAMO.length, name="channelDimensions__length", curie=NAMO.curie('length'),
                   model_uri=NAMO.channelDimensions__length, domain=None, range=Optional[float])

slots.mechanicalStimulation__stimulation_type = Slot(uri=NAMO.stimulation_type, name="mechanicalStimulation__stimulation_type", curie=NAMO.curie('stimulation_type'),
                   model_uri=NAMO.mechanicalStimulation__stimulation_type, domain=None, range=Optional[Union[Union[str, "MechanicalStimulationTypeEnum"], list[Union[str, "MechanicalStimulationTypeEnum"]]]])

slots.mechanicalStimulation__cyclic_stretch_percent = Slot(uri=NAMO.cyclic_stretch_percent, name="mechanicalStimulation__cyclic_stretch_percent", curie=NAMO.curie('cyclic_stretch_percent'),
                   model_uri=NAMO.mechanicalStimulation__cyclic_stretch_percent, domain=None, range=Optional[float])

slots.mechanicalStimulation__frequency_hz = Slot(uri=NAMO.frequency_hz, name="mechanicalStimulation__frequency_hz", curie=NAMO.curie('frequency_hz'),
                   model_uri=NAMO.mechanicalStimulation__frequency_hz, domain=None, range=Optional[float])

slots.mechanicalStimulation__shear_stress = Slot(uri=NAMO.shear_stress, name="mechanicalStimulation__shear_stress", curie=NAMO.curie('shear_stress'),
                   model_uri=NAMO.mechanicalStimulation__shear_stress, domain=None, range=Optional[float])

slots.mechanicalStimulation__pressure_pascal = Slot(uri=NAMO.pressure_pascal, name="mechanicalStimulation__pressure_pascal", curie=NAMO.curie('pressure_pascal'),
                   model_uri=NAMO.mechanicalStimulation__pressure_pascal, domain=None, range=Optional[float])

slots.mechanicalStimulation__duration_minutes = Slot(uri=NAMO.duration_minutes, name="mechanicalStimulation__duration_minutes", curie=NAMO.curie('duration_minutes'),
                   model_uri=NAMO.mechanicalStimulation__duration_minutes, domain=None, range=Optional[float])

slots.modelsRelationship__biological_system_modeled = Slot(uri=NAMO.biological_system_modeled, name="modelsRelationship__biological_system_modeled", curie=NAMO.curie('biological_system_modeled'),
                   model_uri=NAMO.modelsRelationship__biological_system_modeled, domain=None, range=Optional[Union[str, BiologicalSystemId]])

slots.modelsRelationship__is_computed = Slot(uri=NAMO.is_computed, name="modelsRelationship__is_computed", curie=NAMO.curie('is_computed'),
                   model_uri=NAMO.modelsRelationship__is_computed, domain=None, range=Optional[Union[bool, Bool]])

slots.modelsRelationship__concordance = Slot(uri=NAMO.concordance, name="modelsRelationship__concordance", curie=NAMO.curie('concordance'),
                   model_uri=NAMO.modelsRelationship__concordance, domain=None, range=Optional[Union[dict, ConcordanceResult]])

slots.modelsRelationship__structured_concordance = Slot(uri=NAMO.structured_concordance, name="modelsRelationship__structured_concordance", curie=NAMO.curie('structured_concordance'),
                   model_uri=NAMO.modelsRelationship__structured_concordance, domain=None, range=Optional[Union[dict, StructuredConcordanceResult]])

slots.concordanceResult__phenotype_overlap = Slot(uri=NAMO.phenotype_overlap, name="concordanceResult__phenotype_overlap", curie=NAMO.curie('phenotype_overlap'),
                   model_uri=NAMO.concordanceResult__phenotype_overlap, domain=None, range=Optional[str])

slots.concordanceResult__molecular_similarity = Slot(uri=NAMO.molecular_similarity, name="concordanceResult__molecular_similarity", curie=NAMO.curie('molecular_similarity'),
                   model_uri=NAMO.concordanceResult__molecular_similarity, domain=None, range=Optional[str])

slots.concordanceResult__pathway_concordance = Slot(uri=NAMO.pathway_concordance, name="concordanceResult__pathway_concordance", curie=NAMO.curie('pathway_concordance'),
                   model_uri=NAMO.concordanceResult__pathway_concordance, domain=None, range=Optional[str])

slots.concordanceResult__cell_type_coverage = Slot(uri=NAMO.cell_type_coverage, name="concordanceResult__cell_type_coverage", curie=NAMO.curie('cell_type_coverage'),
                   model_uri=NAMO.concordanceResult__cell_type_coverage, domain=None, range=Optional[str])

slots.concordanceResult__functional_parity = Slot(uri=NAMO.functional_parity, name="concordanceResult__functional_parity", curie=NAMO.curie('functional_parity'),
                   model_uri=NAMO.concordanceResult__functional_parity, domain=None, range=Optional[str])

slots.concordanceResult__reproducibility = Slot(uri=NAMO.reproducibility, name="concordanceResult__reproducibility", curie=NAMO.curie('reproducibility'),
                   model_uri=NAMO.concordanceResult__reproducibility, domain=None, range=Optional[str])

slots.structuredConcordanceResult__molecular_similarity = Slot(uri=NAMO.molecular_similarity, name="structuredConcordanceResult__molecular_similarity", curie=NAMO.curie('molecular_similarity'),
                   model_uri=NAMO.structuredConcordanceResult__molecular_similarity, domain=None, range=Optional[Union[dict, MolecularSimilarity]])

slots.structuredConcordanceResult__pathway_concordance = Slot(uri=NAMO.pathway_concordance, name="structuredConcordanceResult__pathway_concordance", curie=NAMO.curie('pathway_concordance'),
                   model_uri=NAMO.structuredConcordanceResult__pathway_concordance, domain=None, range=Optional[Union[dict, PathwayConcordance]])

slots.structuredConcordanceResult__phenotype_overlap = Slot(uri=NAMO.phenotype_overlap, name="structuredConcordanceResult__phenotype_overlap", curie=NAMO.curie('phenotype_overlap'),
                   model_uri=NAMO.structuredConcordanceResult__phenotype_overlap, domain=None, range=Optional[Union[dict, PhenotypeOverlap]])

slots.structuredConcordanceResult__cell_type_coverage = Slot(uri=NAMO.cell_type_coverage, name="structuredConcordanceResult__cell_type_coverage", curie=NAMO.curie('cell_type_coverage'),
                   model_uri=NAMO.structuredConcordanceResult__cell_type_coverage, domain=None, range=Optional[Union[dict, CellTypeCoverage]])

slots.structuredConcordanceResult__functional_parity = Slot(uri=NAMO.functional_parity, name="structuredConcordanceResult__functional_parity", curie=NAMO.curie('functional_parity'),
                   model_uri=NAMO.structuredConcordanceResult__functional_parity, domain=None, range=Optional[Union[dict, FunctionalParity]])

slots.structuredConcordanceResult__reproducibility = Slot(uri=NAMO.reproducibility, name="structuredConcordanceResult__reproducibility", curie=NAMO.curie('reproducibility'),
                   model_uri=NAMO.structuredConcordanceResult__reproducibility, domain=None, range=Optional[Union[dict, Reproducibility]])

slots.molecularSimilarity__similarity_score = Slot(uri=NAMO.similarity_score, name="molecularSimilarity__similarity_score", curie=NAMO.curie('similarity_score'),
                   model_uri=NAMO.molecularSimilarity__similarity_score, domain=None, range=Optional[float])

slots.molecularSimilarity__correlation_coefficient = Slot(uri=NAMO.correlation_coefficient, name="molecularSimilarity__correlation_coefficient", curie=NAMO.curie('correlation_coefficient'),
                   model_uri=NAMO.molecularSimilarity__correlation_coefficient, domain=None, range=Optional[float])

slots.molecularSimilarity__differentially_expressed_genes = Slot(uri=NAMO.differentially_expressed_genes, name="molecularSimilarity__differentially_expressed_genes", curie=NAMO.curie('differentially_expressed_genes'),
                   model_uri=NAMO.molecularSimilarity__differentially_expressed_genes, domain=None, range=Optional[Union[dict[Union[str, GeneId], Union[dict, Gene]], list[Union[dict, Gene]]]])

slots.molecularSimilarity__conserved_genes = Slot(uri=NAMO.conserved_genes, name="molecularSimilarity__conserved_genes", curie=NAMO.curie('conserved_genes'),
                   model_uri=NAMO.molecularSimilarity__conserved_genes, domain=None, range=Optional[Union[dict[Union[str, GeneId], Union[dict, Gene]], list[Union[dict, Gene]]]])

slots.molecularSimilarity__methodology = Slot(uri=NAMO.methodology, name="molecularSimilarity__methodology", curie=NAMO.curie('methodology'),
                   model_uri=NAMO.molecularSimilarity__methodology, domain=None, range=Optional[str])

slots.molecularSimilarity__data_source = Slot(uri=NAMO.data_source, name="molecularSimilarity__data_source", curie=NAMO.curie('data_source'),
                   model_uri=NAMO.molecularSimilarity__data_source, domain=None, range=Optional[str])

slots.molecularSimilarity__statistical_significance = Slot(uri=NAMO.statistical_significance, name="molecularSimilarity__statistical_significance", curie=NAMO.curie('statistical_significance'),
                   model_uri=NAMO.molecularSimilarity__statistical_significance, domain=None, range=Optional[Union[dict, StatisticalSignificance]])

slots.pathwayConcordance__pathway_overlap_score = Slot(uri=NAMO.pathway_overlap_score, name="pathwayConcordance__pathway_overlap_score", curie=NAMO.curie('pathway_overlap_score'),
                   model_uri=NAMO.pathwayConcordance__pathway_overlap_score, domain=None, range=Optional[float])

slots.pathwayConcordance__active_pathways = Slot(uri=NAMO.active_pathways, name="pathwayConcordance__active_pathways", curie=NAMO.curie('active_pathways'),
                   model_uri=NAMO.pathwayConcordance__active_pathways, domain=None, range=Optional[Union[dict[Union[str, PathwayId], Union[dict, Pathway]], list[Union[dict, Pathway]]]])

slots.pathwayConcordance__divergent_pathways = Slot(uri=NAMO.divergent_pathways, name="pathwayConcordance__divergent_pathways", curie=NAMO.curie('divergent_pathways'),
                   model_uri=NAMO.pathwayConcordance__divergent_pathways, domain=None, range=Optional[Union[dict[Union[str, PathwayId], Union[dict, Pathway]], list[Union[dict, Pathway]]]])

slots.pathwayConcordance__pathway_analysis_method = Slot(uri=NAMO.pathway_analysis_method, name="pathwayConcordance__pathway_analysis_method", curie=NAMO.curie('pathway_analysis_method'),
                   model_uri=NAMO.pathwayConcordance__pathway_analysis_method, domain=None, range=Optional[str])

slots.pathwayConcordance__enrichment_statistics = Slot(uri=NAMO.enrichment_statistics, name="pathwayConcordance__enrichment_statistics", curie=NAMO.curie('enrichment_statistics'),
                   model_uri=NAMO.pathwayConcordance__enrichment_statistics, domain=None, range=Optional[Union[Union[dict, EnrichmentStatistics], list[Union[dict, EnrichmentStatistics]]]])

slots.phenotypeOverlap__phenotype_similarity_score = Slot(uri=NAMO.phenotype_similarity_score, name="phenotypeOverlap__phenotype_similarity_score", curie=NAMO.curie('phenotype_similarity_score'),
                   model_uri=NAMO.phenotypeOverlap__phenotype_similarity_score, domain=None, range=Optional[float])

slots.phenotypeOverlap__shared_phenotypes = Slot(uri=NAMO.shared_phenotypes, name="phenotypeOverlap__shared_phenotypes", curie=NAMO.curie('shared_phenotypes'),
                   model_uri=NAMO.phenotypeOverlap__shared_phenotypes, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.phenotypeOverlap__model_specific_phenotypes = Slot(uri=NAMO.model_specific_phenotypes, name="phenotypeOverlap__model_specific_phenotypes", curie=NAMO.curie('model_specific_phenotypes'),
                   model_uri=NAMO.phenotypeOverlap__model_specific_phenotypes, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.phenotypeOverlap__biological_specific_phenotypes = Slot(uri=NAMO.biological_specific_phenotypes, name="phenotypeOverlap__biological_specific_phenotypes", curie=NAMO.curie('biological_specific_phenotypes'),
                   model_uri=NAMO.phenotypeOverlap__biological_specific_phenotypes, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.phenotypeOverlap__phenotype_ontology = Slot(uri=NAMO.phenotype_ontology, name="phenotypeOverlap__phenotype_ontology", curie=NAMO.curie('phenotype_ontology'),
                   model_uri=NAMO.phenotypeOverlap__phenotype_ontology, domain=None, range=Optional[str])

slots.cellTypeCoverage__coverage_percentage = Slot(uri=NAMO.coverage_percentage, name="cellTypeCoverage__coverage_percentage", curie=NAMO.curie('coverage_percentage'),
                   model_uri=NAMO.cellTypeCoverage__coverage_percentage, domain=None, range=Optional[float])

slots.cellTypeCoverage__represented_cell_types = Slot(uri=NAMO.represented_cell_types, name="cellTypeCoverage__represented_cell_types", curie=NAMO.curie('represented_cell_types'),
                   model_uri=NAMO.cellTypeCoverage__represented_cell_types, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.cellTypeCoverage__missing_cell_types = Slot(uri=NAMO.missing_cell_types, name="cellTypeCoverage__missing_cell_types", curie=NAMO.curie('missing_cell_types'),
                   model_uri=NAMO.cellTypeCoverage__missing_cell_types, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.cellTypeCoverage__cell_type_proportions = Slot(uri=NAMO.cell_type_proportions, name="cellTypeCoverage__cell_type_proportions", curie=NAMO.curie('cell_type_proportions'),
                   model_uri=NAMO.cellTypeCoverage__cell_type_proportions, domain=None, range=Optional[Union[Union[dict, CellTypeProportion], list[Union[dict, CellTypeProportion]]]])

slots.cellTypeCoverage__single_cell_method = Slot(uri=NAMO.single_cell_method, name="cellTypeCoverage__single_cell_method", curie=NAMO.curie('single_cell_method'),
                   model_uri=NAMO.cellTypeCoverage__single_cell_method, domain=None, range=Optional[str])

slots.functionalParity__functional_similarity_score = Slot(uri=NAMO.functional_similarity_score, name="functionalParity__functional_similarity_score", curie=NAMO.curie('functional_similarity_score'),
                   model_uri=NAMO.functionalParity__functional_similarity_score, domain=None, range=Optional[float])

slots.functionalParity__conserved_functions = Slot(uri=NAMO.conserved_functions, name="functionalParity__conserved_functions", curie=NAMO.curie('conserved_functions'),
                   model_uri=NAMO.functionalParity__conserved_functions, domain=None, range=Optional[Union[str, list[str]]])

slots.functionalParity__impaired_functions = Slot(uri=NAMO.impaired_functions, name="functionalParity__impaired_functions", curie=NAMO.curie('impaired_functions'),
                   model_uri=NAMO.functionalParity__impaired_functions, domain=None, range=Optional[Union[str, list[str]]])

slots.functionalParity__functional_assays = Slot(uri=NAMO.functional_assays, name="functionalParity__functional_assays", curie=NAMO.curie('functional_assays'),
                   model_uri=NAMO.functionalParity__functional_assays, domain=None, range=Optional[Union[dict[Union[str, FunctionalAssayId], Union[dict, FunctionalAssay]], list[Union[dict, FunctionalAssay]]]])

slots.functionalParity__dose_response_similarity = Slot(uri=NAMO.dose_response_similarity, name="functionalParity__dose_response_similarity", curie=NAMO.curie('dose_response_similarity'),
                   model_uri=NAMO.functionalParity__dose_response_similarity, domain=None, range=Optional[Union[dict, DoseResponseSimilarity]])

slots.reproducibility__reproducibility_score = Slot(uri=NAMO.reproducibility_score, name="reproducibility__reproducibility_score", curie=NAMO.curie('reproducibility_score'),
                   model_uri=NAMO.reproducibility__reproducibility_score, domain=None, range=Optional[float])

slots.reproducibility__coefficient_of_variation = Slot(uri=NAMO.coefficient_of_variation, name="reproducibility__coefficient_of_variation", curie=NAMO.curie('coefficient_of_variation'),
                   model_uri=NAMO.reproducibility__coefficient_of_variation, domain=None, range=Optional[float])

slots.reproducibility__batch_to_batch_variation = Slot(uri=NAMO.batch_to_batch_variation, name="reproducibility__batch_to_batch_variation", curie=NAMO.curie('batch_to_batch_variation'),
                   model_uri=NAMO.reproducibility__batch_to_batch_variation, domain=None, range=Optional[float])

slots.reproducibility__inter_laboratory_consistency = Slot(uri=NAMO.inter_laboratory_consistency, name="reproducibility__inter_laboratory_consistency", curie=NAMO.curie('inter_laboratory_consistency'),
                   model_uri=NAMO.reproducibility__inter_laboratory_consistency, domain=None, range=Optional[float])

slots.reproducibility__replicate_count = Slot(uri=NAMO.replicate_count, name="reproducibility__replicate_count", curie=NAMO.curie('replicate_count'),
                   model_uri=NAMO.reproducibility__replicate_count, domain=None, range=Optional[int])

slots.reproducibility__quality_control_metrics = Slot(uri=NAMO.quality_control_metrics, name="reproducibility__quality_control_metrics", curie=NAMO.curie('quality_control_metrics'),
                   model_uri=NAMO.reproducibility__quality_control_metrics, domain=None, range=Optional[Union[Union[dict, QualityControlMetric], list[Union[dict, QualityControlMetric]]]])

slots.gene__gene_symbol = Slot(uri=NAMO.gene_symbol, name="gene__gene_symbol", curie=NAMO.curie('gene_symbol'),
                   model_uri=NAMO.gene__gene_symbol, domain=None, range=Optional[str])

slots.gene__ensembl_id = Slot(uri=NAMO.ensembl_id, name="gene__ensembl_id", curie=NAMO.curie('ensembl_id'),
                   model_uri=NAMO.gene__ensembl_id, domain=None, range=Optional[str])

slots.gene__entrez_id = Slot(uri=NAMO.entrez_id, name="gene__entrez_id", curie=NAMO.curie('entrez_id'),
                   model_uri=NAMO.gene__entrez_id, domain=None, range=Optional[int])

slots.gene__fold_change = Slot(uri=NAMO.fold_change, name="gene__fold_change", curie=NAMO.curie('fold_change'),
                   model_uri=NAMO.gene__fold_change, domain=None, range=Optional[float])

slots.gene__p_value = Slot(uri=NAMO.p_value, name="gene__p_value", curie=NAMO.curie('p_value'),
                   model_uri=NAMO.gene__p_value, domain=None, range=Optional[float])

slots.gene__adjusted_p_value = Slot(uri=NAMO.adjusted_p_value, name="gene__adjusted_p_value", curie=NAMO.curie('adjusted_p_value'),
                   model_uri=NAMO.gene__adjusted_p_value, domain=None, range=Optional[float])

slots.pathway__pathway_database = Slot(uri=NAMO.pathway_database, name="pathway__pathway_database", curie=NAMO.curie('pathway_database'),
                   model_uri=NAMO.pathway__pathway_database, domain=None, range=Optional[str])

slots.pathway__pathway_id = Slot(uri=NAMO.pathway_id, name="pathway__pathway_id", curie=NAMO.curie('pathway_id'),
                   model_uri=NAMO.pathway__pathway_id, domain=None, range=Optional[str])

slots.pathway__activity_score = Slot(uri=NAMO.activity_score, name="pathway__activity_score", curie=NAMO.curie('activity_score'),
                   model_uri=NAMO.pathway__activity_score, domain=None, range=Optional[float])

slots.pathway__enrichment_score = Slot(uri=NAMO.enrichment_score, name="pathway__enrichment_score", curie=NAMO.curie('enrichment_score'),
                   model_uri=NAMO.pathway__enrichment_score, domain=None, range=Optional[float])

slots.statisticalSignificance__p_value = Slot(uri=NAMO.p_value, name="statisticalSignificance__p_value", curie=NAMO.curie('p_value'),
                   model_uri=NAMO.statisticalSignificance__p_value, domain=None, range=Optional[float])

slots.statisticalSignificance__adjusted_p_value = Slot(uri=NAMO.adjusted_p_value, name="statisticalSignificance__adjusted_p_value", curie=NAMO.curie('adjusted_p_value'),
                   model_uri=NAMO.statisticalSignificance__adjusted_p_value, domain=None, range=Optional[float])

slots.statisticalSignificance__confidence_interval_lower = Slot(uri=NAMO.confidence_interval_lower, name="statisticalSignificance__confidence_interval_lower", curie=NAMO.curie('confidence_interval_lower'),
                   model_uri=NAMO.statisticalSignificance__confidence_interval_lower, domain=None, range=Optional[float])

slots.statisticalSignificance__confidence_interval_upper = Slot(uri=NAMO.confidence_interval_upper, name="statisticalSignificance__confidence_interval_upper", curie=NAMO.curie('confidence_interval_upper'),
                   model_uri=NAMO.statisticalSignificance__confidence_interval_upper, domain=None, range=Optional[float])

slots.statisticalSignificance__statistical_test = Slot(uri=NAMO.statistical_test, name="statisticalSignificance__statistical_test", curie=NAMO.curie('statistical_test'),
                   model_uri=NAMO.statisticalSignificance__statistical_test, domain=None, range=Optional[str])

slots.enrichmentStatistics__enrichment_score = Slot(uri=NAMO.enrichment_score, name="enrichmentStatistics__enrichment_score", curie=NAMO.curie('enrichment_score'),
                   model_uri=NAMO.enrichmentStatistics__enrichment_score, domain=None, range=Optional[float])

slots.enrichmentStatistics__p_value = Slot(uri=NAMO.p_value, name="enrichmentStatistics__p_value", curie=NAMO.curie('p_value'),
                   model_uri=NAMO.enrichmentStatistics__p_value, domain=None, range=Optional[float])

slots.enrichmentStatistics__q_value = Slot(uri=NAMO.q_value, name="enrichmentStatistics__q_value", curie=NAMO.curie('q_value'),
                   model_uri=NAMO.enrichmentStatistics__q_value, domain=None, range=Optional[float])

slots.enrichmentStatistics__genes_in_pathway = Slot(uri=NAMO.genes_in_pathway, name="enrichmentStatistics__genes_in_pathway", curie=NAMO.curie('genes_in_pathway'),
                   model_uri=NAMO.enrichmentStatistics__genes_in_pathway, domain=None, range=Optional[int])

slots.enrichmentStatistics__genes_in_dataset = Slot(uri=NAMO.genes_in_dataset, name="enrichmentStatistics__genes_in_dataset", curie=NAMO.curie('genes_in_dataset'),
                   model_uri=NAMO.enrichmentStatistics__genes_in_dataset, domain=None, range=Optional[int])

slots.cellTypeProportion__cell_type = Slot(uri=NAMO.cell_type, name="cellTypeProportion__cell_type", curie=NAMO.curie('cell_type'),
                   model_uri=NAMO.cellTypeProportion__cell_type, domain=None, range=Optional[Union[dict, Term]])

slots.cellTypeProportion__model_proportion = Slot(uri=NAMO.model_proportion, name="cellTypeProportion__model_proportion", curie=NAMO.curie('model_proportion'),
                   model_uri=NAMO.cellTypeProportion__model_proportion, domain=None, range=Optional[float])

slots.cellTypeProportion__biological_proportion = Slot(uri=NAMO.biological_proportion, name="cellTypeProportion__biological_proportion", curie=NAMO.curie('biological_proportion'),
                   model_uri=NAMO.cellTypeProportion__biological_proportion, domain=None, range=Optional[float])

slots.cellTypeProportion__proportion_ratio = Slot(uri=NAMO.proportion_ratio, name="cellTypeProportion__proportion_ratio", curie=NAMO.curie('proportion_ratio'),
                   model_uri=NAMO.cellTypeProportion__proportion_ratio, domain=None, range=Optional[float])

slots.functionalAssay__assay_type = Slot(uri=NAMO.assay_type, name="functionalAssay__assay_type", curie=NAMO.curie('assay_type'),
                   model_uri=NAMO.functionalAssay__assay_type, domain=None, range=Optional[str])

slots.functionalAssay__assay_result = Slot(uri=NAMO.assay_result, name="functionalAssay__assay_result", curie=NAMO.curie('assay_result'),
                   model_uri=NAMO.functionalAssay__assay_result, domain=None, range=Optional[float])

slots.functionalAssay__reference_value = Slot(uri=NAMO.reference_value, name="functionalAssay__reference_value", curie=NAMO.curie('reference_value'),
                   model_uri=NAMO.functionalAssay__reference_value, domain=None, range=Optional[float])

slots.functionalAssay__units = Slot(uri=NAMO.units, name="functionalAssay__units", curie=NAMO.curie('units'),
                   model_uri=NAMO.functionalAssay__units, domain=None, range=Optional[str])

slots.functionalAssay__methodology = Slot(uri=NAMO.methodology, name="functionalAssay__methodology", curie=NAMO.curie('methodology'),
                   model_uri=NAMO.functionalAssay__methodology, domain=None, range=Optional[str])

slots.doseResponseSimilarity__correlation_coefficient = Slot(uri=NAMO.correlation_coefficient, name="doseResponseSimilarity__correlation_coefficient", curie=NAMO.curie('correlation_coefficient'),
                   model_uri=NAMO.doseResponseSimilarity__correlation_coefficient, domain=None, range=Optional[float])

slots.doseResponseSimilarity__ec50_ratio = Slot(uri=NAMO.ec50_ratio, name="doseResponseSimilarity__ec50_ratio", curie=NAMO.curie('ec50_ratio'),
                   model_uri=NAMO.doseResponseSimilarity__ec50_ratio, domain=None, range=Optional[float])

slots.doseResponseSimilarity__max_response_ratio = Slot(uri=NAMO.max_response_ratio, name="doseResponseSimilarity__max_response_ratio", curie=NAMO.curie('max_response_ratio'),
                   model_uri=NAMO.doseResponseSimilarity__max_response_ratio, domain=None, range=Optional[float])

slots.doseResponseSimilarity__compound_tested = Slot(uri=NAMO.compound_tested, name="doseResponseSimilarity__compound_tested", curie=NAMO.curie('compound_tested'),
                   model_uri=NAMO.doseResponseSimilarity__compound_tested, domain=None, range=Optional[str])

slots.qualityControlMetric__metric_name = Slot(uri=NAMO.metric_name, name="qualityControlMetric__metric_name", curie=NAMO.curie('metric_name'),
                   model_uri=NAMO.qualityControlMetric__metric_name, domain=None, range=Optional[str])

slots.qualityControlMetric__metric_value = Slot(uri=NAMO.metric_value, name="qualityControlMetric__metric_value", curie=NAMO.curie('metric_value'),
                   model_uri=NAMO.qualityControlMetric__metric_value, domain=None, range=Optional[float])

slots.qualityControlMetric__threshold = Slot(uri=NAMO.threshold, name="qualityControlMetric__threshold", curie=NAMO.curie('threshold'),
                   model_uri=NAMO.qualityControlMetric__threshold, domain=None, range=Optional[float])

slots.qualityControlMetric__pass_fail_status = Slot(uri=NAMO.pass_fail_status, name="qualityControlMetric__pass_fail_status", curie=NAMO.curie('pass_fail_status'),
                   model_uri=NAMO.qualityControlMetric__pass_fail_status, domain=None, range=Optional[Union[bool, Bool]])

slots.reference__id = Slot(uri=NAMO.id, name="reference__id", curie=NAMO.curie('id'),
                   model_uri=NAMO.reference__id, domain=None, range=URIRef)

slots.reference__title = Slot(uri=NAMO.title, name="reference__title", curie=NAMO.curie('title'),
                   model_uri=NAMO.reference__title, domain=None, range=str)

slots.reference__authors = Slot(uri=NAMO.authors, name="reference__authors", curie=NAMO.curie('authors'),
                   model_uri=NAMO.reference__authors, domain=None, range=Optional[Union[str, list[str]]])

slots.reference__journal = Slot(uri=NAMO.journal, name="reference__journal", curie=NAMO.curie('journal'),
                   model_uri=NAMO.reference__journal, domain=None, range=Optional[str])

slots.reference__year = Slot(uri=NAMO.year, name="reference__year", curie=NAMO.curie('year'),
                   model_uri=NAMO.reference__year, domain=None, range=Optional[int])

slots.reference__url = Slot(uri=NAMO.url, name="reference__url", curie=NAMO.curie('url'),
                   model_uri=NAMO.reference__url, domain=None, range=Optional[Union[str, URI]])
