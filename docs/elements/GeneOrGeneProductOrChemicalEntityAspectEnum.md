---
search:
  boost: 2.0
---


# Enum: GeneOrGeneProductOrChemicalEntityAspectEnum 




_An enumeration used as a qualifier to indicate the specific aspect of a gene, gene product, or chemical entity that is affected or measured in an association. Values cover activity and abundance (expression, synthesis, degradation, stability, localization, transport), molecular interactions, and a wide range of molecular modifications such as phosphorylation, methylation, acetylation, ubiquitination, and other post-translational or chemical modifications._



<div data-search-exclude markdown="1">

URI: [namo:GeneOrGeneProductOrChemicalEntityAspectEnum](https://w3id.org/monarch-initiative/namo/GeneOrGeneProductOrChemicalEntityAspectEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| activity_or_abundance | None | Used in cases where the specificity of the relationship can not be determined... ||
| abundance | None |  | Is-A: NONE<br>|
| activity | None |  | Is-A: NONE<br>|
| expression | None |  | Is-A: NONE<br>|
| synthesis | None |  | Is-A: NONE<br>|
| degradation | None |  ||
| cleavage | None |  ||
| hydrolysis | None |  | Is-A: NONE<br>|
| metabolic_processing | None |  ||
| mutation_rate | None |  ||
| stability | None |  ||
| folding | None |  ||
| localization | None |  ||
| transport | None |  ||
| absorption | None |  ||
| aggregation | None |  ||
| interaction | None |  ||
| release | None |  ||
| isomerization | None |  ||
| secretion | None |  | Is-A: NONE<br>|
| uptake | None |  | Is-A: NONE<br>|
| splicing | None |  ||
| molecular_interaction | None |  ||
| guanyl_nucleotide_exchange | None |  | Is-A: NONE<br>|
| adenyl_nucleotide_exchange | None |  | Is-A: NONE<br>|
| molecular_modification | None |  ||
| acetylation | None |  | Is-A: NONE<br>|
| acylation | None |  | Is-A: NONE<br>|
| alkylation | None |  | Is-A: NONE<br>|
| amination | None |  | Is-A: NONE<br>|
| carbamoylation | None |  | Is-A: NONE<br>|
| ethylation | None |  | Is-A: NONE<br>|
| glutathionylation | None |  | Is-A: NONE<br>|
| glycation | None |  | Is-A: NONE<br>|
| glycosylation | None |  | Is-A: NONE<br>|
| glucuronidation | None |  | Is-A: NONE<br>|
| n_linked_glycosylation | None |  | Is-A: NONE<br>|
| o_linked_glycosylation | None |  | Is-A: NONE<br>|
| hydroxylation | None |  | Is-A: NONE<br>|
| lipidation | None |  | Is-A: NONE<br>|
| farnesylation | None |  | Is-A: NONE<br>|
| geranoylation | None |  | Is-A: NONE<br>|
| myristoylation | None |  | Is-A: NONE<br>|
| palmitoylation | None |  | Is-A: NONE<br>|
| prenylation | None |  | Is-A: NONE<br>|
| methylation | None |  | Is-A: NONE<br>|
| nitrosation | None |  | Is-A: NONE<br>|
| nucleotidylation | None |  | Is-A: NONE<br>|
| phosphorylation | None |  | Is-A: NONE<br>|
| ribosylation | None |  | Is-A: NONE<br>|
| ADP-ribosylation | None |  | Is-A: NONE<br>|
| sulfation | None |  | Is-A: NONE<br>|
| sumoylation | None |  | Is-A: NONE<br>|
| ubiquitination | None |  | Is-A: NONE<br>|
| oxidation | None |  | Is-A: NONE<br>|
| reduction | None |  | Is-A: NONE<br>|
| carboxylation | None |  | Is-A: NONE<br>|




## Slots

| Name | Description |
| ---  | --- |
| [aspect_qualifier](aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [subject_aspect_qualifier](subject_aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [object_aspect_qualifier](object_aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [object_aspect_qualifier](object_aspect_qualifier.md) |  |
| [object_aspect_qualifier](object_aspect_qualifier.md) | the aspect of the object gene or gene product that is being regulated, must b... |
| [subject_aspect_qualifier](subject_aspect_qualifier.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: GeneOrGeneProductOrChemicalEntityAspectEnum
description: An enumeration used as a qualifier to indicate the specific aspect of
  a gene, gene product, or chemical entity that is affected or measured in an association.
  Values cover activity and abundance (expression, synthesis, degradation, stability,
  localization, transport), molecular interactions, and a wide range of molecular
  modifications such as phosphorylation, methylation, acetylation, ubiquitination,
  and other post-translational or chemical modifications.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  activity_or_abundance:
    text: activity_or_abundance
    description: Used in cases where the specificity of the relationship can not be
      determined to be either activity or abundance.  In general, a more specific
      value from this enumeration should be used.
  abundance:
    text: abundance
    is_a: activity_or_abundance
  activity:
    text: activity
    is_a: activity_or_abundance
  expression:
    text: expression
    is_a: abundance
  synthesis:
    text: synthesis
    is_a: abundance
  degradation:
    text: degradation
  cleavage:
    text: cleavage
  hydrolysis:
    text: hydrolysis
    is_a: cleavage
  metabolic_processing:
    text: metabolic_processing
  mutation_rate:
    text: mutation_rate
  stability:
    text: stability
  folding:
    text: folding
  localization:
    text: localization
  transport:
    text: transport
  absorption:
    text: absorption
  aggregation:
    text: aggregation
  interaction:
    text: interaction
  release:
    text: release
  isomerization:
    text: isomerization
  secretion:
    text: secretion
    is_a: transport
  uptake:
    text: uptake
    is_a: transport
  splicing:
    text: splicing
  molecular_interaction:
    text: molecular_interaction
  guanyl_nucleotide_exchange:
    text: guanyl_nucleotide_exchange
    is_a: molecular_interaction
  adenyl_nucleotide_exchange:
    text: adenyl_nucleotide_exchange
    is_a: molecular_interaction
  molecular_modification:
    text: molecular_modification
  acetylation:
    text: acetylation
    is_a: molecular_modification
  acylation:
    text: acylation
    is_a: molecular_modification
  alkylation:
    text: alkylation
    is_a: molecular_modification
  amination:
    text: amination
    is_a: molecular_modification
  carbamoylation:
    text: carbamoylation
    is_a: molecular_modification
  ethylation:
    text: ethylation
    is_a: molecular_modification
  glutathionylation:
    text: glutathionylation
    is_a: molecular_modification
  glycation:
    text: glycation
    is_a: molecular_modification
  glycosylation:
    text: glycosylation
    is_a: molecular_modification
  glucuronidation:
    text: glucuronidation
    is_a: molecular_modification
  n_linked_glycosylation:
    text: n_linked_glycosylation
    is_a: molecular_modification
  o_linked_glycosylation:
    text: o_linked_glycosylation
    is_a: molecular_modification
  hydroxylation:
    text: hydroxylation
    is_a: molecular_modification
  lipidation:
    text: lipidation
    is_a: molecular_modification
  farnesylation:
    text: farnesylation
    is_a: molecular_modification
  geranoylation:
    text: geranoylation
    is_a: molecular_modification
  myristoylation:
    text: myristoylation
    is_a: molecular_modification
  palmitoylation:
    text: palmitoylation
    is_a: molecular_modification
  prenylation:
    text: prenylation
    is_a: molecular_modification
  methylation:
    text: methylation
    is_a: molecular_modification
  nitrosation:
    text: nitrosation
    is_a: molecular_modification
  nucleotidylation:
    text: nucleotidylation
    is_a: molecular_modification
  phosphorylation:
    text: phosphorylation
    is_a: molecular_modification
  ribosylation:
    text: ribosylation
    is_a: molecular_modification
  ADP-ribosylation:
    text: ADP-ribosylation
    is_a: molecular_modification
  sulfation:
    text: sulfation
    is_a: molecular_modification
  sumoylation:
    text: sumoylation
    is_a: molecular_modification
  ubiquitination:
    text: ubiquitination
    is_a: molecular_modification
  oxidation:
    text: oxidation
    is_a: molecular_modification
  reduction:
    text: reduction
    is_a: molecular_modification
  carboxylation:
    text: carboxylation
    is_a: molecular_modification

```
</details>

</div>