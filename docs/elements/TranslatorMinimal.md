---
search:
  boost: 1.0
---


# Subset: TranslatorMinimal 


_Minimum subset of translator work_



<div data-search-exclude markdown="1">

URI: [TranslatorMinimal](TranslatorMinimal.md)








## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo



































































        














        





















        














        







































        


















        






























        

























































        

        










        























































































        








































        

        














        

        

        












        



        


        




















        








        



        




        



        

        

        

        




























        






















        



        


        





        








        

        











        



        

        


        


















        


        

        

        

        










        


        





        















        

        










        












        

        










        

        


        







        

        


        




        

        

        



        









        



















        

        




        


        


        

        


        









        

        

        

        


        

        

































        

        


        

        

        


        

        

        

        




        









        



        

        



        


        


        






        
























        

        







        









        















        












        

        




        






        


        

        




        

        

        


        




        

        

        

        


        

        






        

        




        

        

        

        












        







        





        

        

        




        


        



        


        

        











        






























        

        




        





        

        


        


        

        






        

        




        













        



        



        










        


        

        




        

        

        


        





        

        

        




        

        

















        



        




















        



        

        
















        

        





























































        


        

        

        





## Classes in subset

| Class | Description |
| --- | --- |
| [ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemi... |
| [ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular ent... |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more mol... |
| [Disease](Disease.md) | A disease is a disposition to undergo pathological processes that exists in a... |
| [EpigenomicEntity](EpigenomicEntity.md) | A mixin for entities that represent epigenomic modifications or features asso... |
| [Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |
| [GenomicEntity](GenomicEntity.md) | A generically dependent continuant that carries biological sequence that is p... |
| [MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently ... |
| [MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular e... |
| [NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |
| [SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability i... |


### Slots from [ChemicalEntity](ChemicalEntity.md) also in _translator_minimal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized  |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity  |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity **identifier** |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity  |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity  |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing  |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity  |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge...  |

### Slots from [ChemicalMixture](ChemicalMixture.md) also in _translator_minimal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized  |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity  |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity **identifier** |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity  |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity  |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing  |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity  |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge...  |

### Slots from [ComplexMolecularMixture](ComplexMolecularMixture.md) also in _translator_minimal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized  |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity  |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity **identifier** |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity  |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity  |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing  |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity  |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge...  |

### Slots from [Disease](Disease.md) also in _translator_minimal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized  |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity  |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity **identifier** |
| [in_taxon](in_taxon.md) | * <br/> [OrganismTaxon](OrganismTaxon.md) | connects an entity to its taxonomic classification  |
| [in_taxon_label](in_taxon_label.md) | 0..1 <br/> [LabelType](LabelType.md) | The human readable scientific name for the taxon of the entity  |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity  |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity  |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing  |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity  |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge...  |


### Slots from [Gene](Gene.md) also in _translator_minimal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized  |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity  |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity **identifier** |
| [in_taxon](in_taxon.md) | * <br/> [OrganismTaxon](OrganismTaxon.md) | connects an entity to its taxonomic classification  |
| [in_taxon_label](in_taxon_label.md) | 0..1 <br/> [LabelType](LabelType.md) | The human readable scientific name for the taxon of the entity  |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity  |
| [name](name.md) | 0..1 <br/> [SymbolType](SymbolType.md) | genes are typically designated by a short symbol and a full name  |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing  |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity  |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge...  |


### Slots from [MolecularEntity](MolecularEntity.md) also in _translator_minimal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized  |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity  |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity **identifier** |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity  |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity  |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing  |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity  |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge...  |

### Slots from [MolecularMixture](MolecularMixture.md) also in _translator_minimal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized  |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity  |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity **identifier** |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity  |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity  |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing  |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity  |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge...  |

### Slots from [NucleicAcidEntity](NucleicAcidEntity.md) also in _translator_minimal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized  |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity  |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity **identifier** |
| [in_taxon](in_taxon.md) | * <br/> [OrganismTaxon](OrganismTaxon.md) | connects an entity to its taxonomic classification  |
| [in_taxon_label](in_taxon_label.md) | 0..1 <br/> [LabelType](LabelType.md) | The human readable scientific name for the taxon of the entity  |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity  |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity  |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing  |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity  |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge...  |

### Slots from [SmallMolecule](SmallMolecule.md) also in _translator_minimal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [Uriorcurie](Uriorcurie.md) | Name of the high level ontology class in which this entity is categorized  |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity  |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for an entity **identifier** |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity  |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity  |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing  |
| [taxon](taxon.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A property that indicates the taxonomic classification of an entity  |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge...  |




## Slots in subset

| Slot | Description |
| --- | --- |
| [actively_involved_in](actively_involved_in.md) | holds between a continuant and a process or function, where the continuant ac... |
| [actively_involves](actively_involves.md) |  |
| [affects](affects.md) | Describes an entity that has an effect on the state or quality of another exi... |
| [affects_likelihood_of](affects_likelihood_of.md) | Holds between two entities where the presence or application of one alters th... |
| [affects_sensitivity_to](affects_sensitivity_to.md) | holds between two chemical entities or genes or gene products where the actio... |
| [anatomical_context_qualifier](anatomical_context_qualifier.md) | A statement qualifier representing an anatomical location where an relationsh... |
| [applied_to_treat](applied_to_treat.md) | Holds between an  substance, procedure, or activity and a medical condition, ... |
| [aspect_qualifier](aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [beneficial_in_models_for](beneficial_in_models_for.md) | Holds between an  substance, procedure, or activity and a medical condition, ... |
| [biomarker_for](biomarker_for.md) | holds between a measurable chemical entity and a disease or phenotypic featur... |
| [broad_match](broad_match.md) | a list of terms from different schemas or terminology systems that have a bro... |
| [capable_of](capable_of.md) | holds between a physical entity and process or function, where the continuant... |
| [category](category.md) | Name of the high level ontology class in which this entity is categorized |
| [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | A statement qualifier representing a type of molecular control mechanism thro... |
| [caused_by](caused_by.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [causes](causes.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [chemically_similar_to](chemically_similar_to.md) | holds between one small molecule entity and another that it approximates for ... |
| [close_match](close_match.md) | a list of terms from different schemas or terminology systems that have a sem... |
| [coexists_with](coexists_with.md) | holds between two entities that are co-located in the same aggregate object, ... |
| [colocalizes_with](colocalizes_with.md) | holds between two entities that are observed to be located in the same place |
| [composed_primarily_of](composed_primarily_of.md) | x composed_primarily_of_y if:more than half of the mass of x is made from par... |
| [condition_associated_with_gene](condition_associated_with_gene.md) | holds between a gene and a disease or phenotypic feature that may be influenc... |
| [condition_exacerbated_by](condition_exacerbated_by.md) |  |
| [context_qualifier](context_qualifier.md) | Restricts the setting/context/location where the core concept (or qualified c... |
| [contributes_to](contributes_to.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [contribution_from](contribution_from.md) |  |
| [correlated_with](correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [decreases_sensitivity_to](decreases_sensitivity_to.md) | holds between two chemical entities or genes or gene products where the actio... |
| [derivative_qualifier](derivative_qualifier.md) | A qualifier that composes with a core subject/object  concept to describe som... |
| [derives_from](derives_from.md) | holds between two distinct material entities, the new entity and the old enti... |
| [derives_into](derives_into.md) | holds between two distinct material entities, the old entity and the new enti... |
| [description](description.md) | a human-readable description of an entity |
| [direction_qualifier](direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [disease_context_qualifier](disease_context_qualifier.md) | A context qualifier representing a disease or condition in which a relationsh... |
| [disrupts](disrupts.md) | describes a relationship where one entity degrades or interferes with the str... |
| [enabled_by](enabled_by.md) | holds between a process and a physical entity, where the physical entity exec... |
| [enables](enables.md) | holds between a physical entity and a process, where the physical entity exec... |
| [exact_match](exact_match.md) | holds between two entities that have strictly equivalent meanings, with a hig... |
| [expressed_in](expressed_in.md) | holds between a gene or gene product and an anatomical entity in which it is ... |
| [expresses](expresses.md) | holds between an anatomical entity and gene or gene product that is expressed... |
| [food_component_of](food_component_of.md) | holds between a one or more chemical entities present in food, irrespective o... |
| [form_or_variant_qualifier](form_or_variant_qualifier.md) | A qualifier that composes with a core subject/object concept to define a spec... |
| [frequency_qualifier](frequency_qualifier.md) | a qualifier used in a phenotypic association to state how frequent the phenot... |
| [gene_associated_with_condition](gene_associated_with_condition.md) | holds between a gene and a disease or phenotypic feature that the gene or its... |
| [gene_product_of](gene_product_of.md) | definition x has gene product of y if and only if y is a gene (SO:0000704) th... |
| [gene_fusion_with](gene_fusion_with.md) | holds between two independent genes that have fused through translocation, in... |
| [genetic_neighborhood_of](genetic_neighborhood_of.md) | holds between two genes located nearby one another on a chromosome |
| [genetically_associated_with](genetically_associated_with.md) | A statistical association, observed in genetic studies, between a genetic ent... |
| [genetically_interacts_with](genetically_interacts_with.md) | holds between two genes whose phenotypic effects are dependent on each other ... |
| [has_active_ingredient](has_active_ingredient.md) | holds between a drug and a molecular entity in which the latter is a part of ... |
| [has_biomarker](has_biomarker.md) | holds between a disease or phenotypic feature and a measurable chemical entit... |
| [has_excipient](has_excipient.md) | holds between a drug and a molecular entities in which the latter is a part o... |
| [has_food_component](has_food_component.md) | holds between food and one or more chemical entities composing it, irrespecti... |
| [has_gene_product](has_gene_product.md) | holds between a gene and a transcribed and/or translated product generated fr... |
| [has_input](has_input.md) | holds between a process and a continuant, where the continuant is an input in... |
| [has_member](has_member.md) | Defines a mereological relation between a collection and an item |
| [has_metabolite](has_metabolite.md) | holds between two molecular entities in which the second one is derived from ... |
| [has_mode_of_inheritance](has_mode_of_inheritance.md) | Relates a disease or phenotypic feature to its observed genetic segregation a... |
| [has_nutrient](has_nutrient.md) | one or more nutrients which are growth factors for a living organism |
| [has_output](has_output.md) | holds between a process and a continuant, where the continuant is an output o... |
| [has_part](has_part.md) | holds between wholes and their parts (material entities or processes) |
| [has_participant](has_participant.md) | holds between a process and a continuant, where the continuant is somehow inv... |
| [has_phenotype](has_phenotype.md) | holds between a biological entity and a phenotype, where a phenotype is const... |
| [has_plasma_membrane_part](has_plasma_membrane_part.md) | Holds between a cell c and a protein complex or protein p if and only if that... |
| [homologous_to](homologous_to.md) | holds between two biological entities that have common evolutionary origin |
| [id](id.md) | A unique identifier for an entity |
| [in_cell_population_with](in_cell_population_with.md) | holds between two genes or gene products that are expressed in the same cell ... |
| [in_clinical_trials_for](in_clinical_trials_for.md) | Holds between an intervention and a medical condition, and reports that a cli... |
| [in_complex_with](in_complex_with.md) | holds between two genes or gene products that are part of (or code for produc... |
| [in_pathway_with](in_pathway_with.md) | holds between two genes or gene products that are part of in the same biologi... |
| [in_preclinical_trials_for](in_preclinical_trials_for.md) | Holds between an  substance, procedure, or activity and a medical condition, ... |
| [in_taxon](in_taxon.md) | connects an entity to its taxonomic classification |
| [in_taxon_label](in_taxon_label.md) | The human readable scientific name for the taxon of the entity |
| [increases_sensitivity_to](increases_sensitivity_to.md) | holds between two chemical entities or genes or gene products where the actio... |
| [interacts_with](interacts_with.md) | holds between any two entities that directly or indirectly interact with each... |
| [iri](iri.md) | An IRI for an entity |
| [is_active_ingredient_of](is_active_ingredient_of.md) | holds between a molecular entity and a drug, in which the former is a part of... |
| [is_excipient_of](is_excipient_of.md) | holds between a molecular entity and a drug in which the former is a part of ... |
| [is_input_of](is_input_of.md) |  |
| [is_metabolite_of](is_metabolite_of.md) | holds between two molecular entities in which the first one is derived from t... |
| [is_output_of](is_output_of.md) |  |
| [located_in](located_in.md) | holds between a material entity and a material entity or site within which it... |
| [location_of](location_of.md) | holds between material entity or site and a material entity that is located w... |
| [manifestation_of](manifestation_of.md) | that part of a phenomenon which is directly observable or visibly expressed, ... |
| [member_of](member_of.md) | Defines a mereological relation between a item and a collection |
| [model_of](model_of.md) | holds between a thing and some other thing it approximates for purposes of sc... |
| [name](name.md) | A human-readable name for an attribute or entity |
| [narrow_match](narrow_match.md) | a list of terms from different schemas or terminology systems that have a nar... |
| [negatively_correlated_with](negatively_correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [nutrient_of](nutrient_of.md) | holds between a one or more chemical entities present in food, irrespective o... |
| [object_activity_qualifier](object_activity_qualifier.md) |  |
| [object_aspect_qualifier](object_aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [object_context_qualifier](object_context_qualifier.md) | A qualifier describing the context in which the object of an association hold... |
| [object_derivative_qualifier](object_derivative_qualifier.md) | A qualifier that composes with a core subject/object  concept to describe som... |
| [object_direction_qualifier](object_direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | A qualifier that composes with a core subject/object concept to define a spec... |
| [object_part_qualifier](object_part_qualifier.md) | defines a specific part/component of the core concept (used in cases there th... |
| [object_process_qualifier](object_process_qualifier.md) |  |
| [object_specialization_qualifier](object_specialization_qualifier.md) | A qualifier that composes with a core subject/object concept to define a more... |
| [occurs_in](occurs_in.md) | holds between a process and a material entity or site within which the proces... |
| [occurs_together_in_literature_with](occurs_together_in_literature_with.md) | holds between two entities where their co-occurrence is correlated by counts ... |
| [onset_qualifier](onset_qualifier.md) | a qualifier used in a phenotypic association to state when the phenotype appe... |
| [orthologous_to](orthologous_to.md) | a homology relationship between entities (typically genes) that diverged afte... |
| [overlaps](overlaps.md) | holds between entities that overlap in their extents (materials or processes) |
| [paralogous_to](paralogous_to.md) | a homology relationship that holds between entities (typically genes) that di... |
| [part_of](part_of.md) | holds between parts and wholes (material entities or processes) |
| [part_qualifier](part_qualifier.md) | defines a specific part/component of the core concept (used in cases there th... |
| [participates_in](participates_in.md) | holds between a continuant and a process, where the continuant is somehow inv... |
| [pharmacologically_interacts_with](pharmacologically_interacts_with.md) | holds between two pharmacologically active chemicals (typically drugs), where... |
| [physically_interacts_with](physically_interacts_with.md) | holds between two entities that make physical contact as part of some interac... |
| [positively_correlated_with](positively_correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [preceded_by](preceded_by.md) | holds between two processes, where the other is completed before the one begi... |
| [precedes](precedes.md) | holds between two processes, where one completes before the other begins |
| [predisposes_to_condition](predisposes_to_condition.md) | Holds between two entities where the presence or application of one increases... |
| [preventative_for_condition](preventative_for_condition.md) | Holds between a substance, procedure, or activity and a medical condition (di... |
| [process_qualifier](process_qualifier.md) | Restricts the biological process within which the core concept (or qualified ... |
| [produces](produces.md) | holds between a material entity and a product that is generated through the i... |
| [promotes_condition](promotes_condition.md) | Holds between a substance, procedure, or activity and a medical condition (di... |
| [qualifier](qualifier.md) | grouping slot for all qualifiers on an edge |
| [resource_id](resource_id.md) | The CURIE for an Information Resource that served as a source of knowledge ex... |
| [resource_role](resource_role.md) | The role played by the InformationResource in serving as a source for an Edge |
| [retrieval_source_ids](retrieval_source_ids.md) | A list of retrieval sources that served as a source of knowledge expressed in... |
| [same_as](same_as.md) | holds between two entities that are considered equivalent to each other |
| [semmed_agreement_count](semmed_agreement_count.md) | The number of times this concept has been asserted in the SemMedDB literature... |
| [sensitivity_affected_by](sensitivity_affected_by.md) |  |
| [sensitivity_decreased_by](sensitivity_decreased_by.md) |  |
| [sensitivity_increased_by](sensitivity_increased_by.md) |  |
| [severity_qualifier](severity_qualifier.md) | a qualifier used in a phenotypic association to state how severe the phenotyp... |
| [sex_qualifier](sex_qualifier.md) | a qualifier used in a phenotypic association to state whether the association... |
| [similar_to](similar_to.md) | holds between an entity and some other entity with similar features |
| [species_context_qualifier](species_context_qualifier.md) | A statement qualifier representing a taxonomic category of species in which a... |
| [stage_qualifier](stage_qualifier.md) | stage during which gene or protein expression of takes place |
| [statement_qualifier](statement_qualifier.md) | A property that qualifies the entirety of the statement made in an associatio... |
| [subclass_of](subclass_of.md) | holds between two classes where the domain class is a specialization of the r... |
| [subject_activity_qualifier](subject_activity_qualifier.md) |  |
| [subject_aspect_qualifier](subject_aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [subject_context_qualifier](subject_context_qualifier.md) | A qualifier describing the context in which the subject of an association hol... |
| [subject_derivative_qualifier](subject_derivative_qualifier.md) | A qualifier that composes with a core subject/object  concept to describe som... |
| [subject_direction_qualifier](subject_direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | A qualifier that composes with a core subject/object concept to define a spec... |
| [subject_part_qualifier](subject_part_qualifier.md) | defines a specific part/component of the core concept (used in cases there th... |
| [subject_process_qualifier](subject_process_qualifier.md) |  |
| [subject_specialization_qualifier](subject_specialization_qualifier.md) | A qualifier that composes with a core subject/object concept to define a more... |
| [superclass_of](superclass_of.md) | holds between two classes where the domain class is a super class of the rang... |
| [support_graphs](support_graphs.md) | A list of knowledge graphs that support the existence of this association |
| [synonym](synonym.md) | Alternate human-readable names for a thing |
| [taxon](taxon.md) | A property that indicates the taxonomic classification of an entity |
| [treated_by](treated_by.md) |  |
| [treats](treats.md) | Holds between an intervention (substance, procedure, or activity) and a medic... |
| [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md) | Holds between an substance, procedure, or activity and a medical condition (d... |
| [xenologous_to](xenologous_to.md) | a homology relationship characterized by an interspecies (horizontal) transfe... |
| [xref](xref.md) | A database cross reference or alternative identifier for a NamedThing or edge... |



## Enumerations in subset

| Enumeration | Description |
| --- | --- |
| [AgentTypeEnum](AgentTypeEnum.md) | An enumeration of agent types responsible for generating a statement of knowl... |
| [FDAIDAAdverseEventEnum](FDAIDAAdverseEventEnum.md) | please consult with the FDA guidelines as proposed in this document: https://... |
| [KnowledgeLevelEnum](KnowledgeLevelEnum.md) | An enumeration characterizing the type of knowledge expressed in a statement ... |
| [ResourceRoleEnum](ResourceRoleEnum.md) | The role played by the information reource in serving as a source for an edge... |


</div>