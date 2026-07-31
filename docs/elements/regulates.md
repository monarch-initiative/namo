---
search:
  boost: 5.0
---

# Slot: regulates 


_A more specific form of affects, that implies the effect results from a biologically evolved control mechanism. Gene-affects-gene relationships will (almost) always involve regulation.  Exogenous/environmental chemical-affects-gene relationships are not cases of regulation in this definition. Instead these would be captured using the 'affects' predicate, or possibly one of the 'interacts with' predicates depending on the nature of the interaction._



<div data-search-exclude markdown="1">



URI: [namo:regulates](https://w3id.org/monarch-initiative/namo/regulates)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **regulates** [ [interacts_with](interacts_with.md)]








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md) |
| Domain | [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |










## Notes

* The RO definition of 'directly regulates the activity of' is an exact_mapping here because it describes genetic regulation from the point of view of one genetic entity regulating another, as opposed to "RO:0002211" which describes process to process regulation.



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:regulates |
| native | namo:regulates |
| exact | RO:0002448 |
| broad | WIKIDATA_PROPERTY:P128, CHEMBL.MECHANISM:modulator, RO:0002295, RO:0002332, RO:0002448 |




## LinkML Source

<details>
```yaml
name: regulates
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A more specific form of affects, that implies the effect results from
  a biologically evolved control mechanism. Gene-affects-gene relationships will (almost)
  always involve regulation.  Exogenous/environmental chemical-affects-gene relationships
  are not cases of regulation in this definition. Instead these would be captured
  using the 'affects' predicate, or possibly one of the 'interacts with' predicates
  depending on the nature of the interaction.
notes:
- The RO definition of 'directly regulates the activity of' is an exact_mapping here
  because it describes genetic regulation from the point of view of one genetic entity
  regulating another, as opposed to "RO:0002211" which describes process to process
  regulation.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002448
broad_mappings:
- WIKIDATA_PROPERTY:P128
- CHEMBL.MECHANISM:modulator
- RO:0002295
- RO:0002332
- RO:0002448
rank: 1000
is_a: affects
mixins:
- interacts with
domain: physical essence or occurrent
inherited: true
range: physical essence or occurrent
multivalued: true

```
</details></div>