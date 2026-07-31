---
search:
  boost: 5.0
---

# Slot: genetically_associated_with 


_A statistical association, observed in genetic studies, between a genetic entity such as a gene, locus, or variant and a phenotype, disease, or trait._



<div data-search-exclude markdown="1">



URI: [namo:genetically_associated_with](https://w3id.org/monarch-initiative/namo/genetically_associated_with)
Alias: genetically_associated_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * **genetically_associated_with**
                * [gene_associated_with_condition](gene_associated_with_condition.md)
                * [condition_associated_with_gene](condition_associated_with_gene.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [NamedThing](NamedThing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Symmetric | Yes |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| description | Co-occurrence of a certain allele of a genetic marker and the phenotype of interest in the same individuals at above-chance level |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:genetically_associated_with |
| native | namo:genetically_associated_with |
| exact | WIKIDATA_PROPERTY:P2293 |




## LinkML Source

<details>
```yaml
name: genetically associated with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  description:
    tag: description
    value: Co-occurrence of a certain allele of a genetic marker and the phenotype
      of interest in the same individuals at above-chance level
description: A statistical association, observed in genetic studies, between a genetic
  entity such as a gene, locus, or variant and a phenotype, disease, or trait.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- WIKIDATA_PROPERTY:P2293
rank: 1000
is_a: associated with
domain: named thing
inherited: true
alias: genetically_associated_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>