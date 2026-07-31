---
search:
  boost: 5.0
---

# Slot: associated_with 


_Expresses a relationship between two named things where the relationship is typically generated statistically (though not in all cases), and is weaker than its child, 'correlated with', but stronger than its parent, 'related to'. This relationship holds between two concepts represented by variables for which a statistical dependence is demonstrated.  E.g. the statement “Atrial Fibrillation (Afib) is associated with Myocardial Infraction (MI)” asserts that having Afib is not statistically independent from whether a patient will also have MI. Note that in Translator associations, the subject and object concepts may map exactly to the statistical variables, or represent related entities for which the variables serve as proxies in an Association (e.g. diseases, chemical entities or processes)._



<div data-search-exclude markdown="1">



URI: [namo:associated_with](https://w3id.org/monarch-initiative/namo/associated_with)
Alias: associated_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **associated_with**
            * [associated_with_likelihood_of](associated_with_likelihood_of.md)
            * [likelihood_associated_with](likelihood_associated_with.md)
            * [associated_with_response_to](associated_with_response_to.md)
            * [response_associated_with](response_associated_with.md)
            * [sensitivity_associated_with](sensitivity_associated_with.md)
            * [resistance_associated_with](resistance_associated_with.md)
            * [genetic_association](genetic_association.md)
            * [genetically_associated_with](genetically_associated_with.md)
            * [correlated_with](correlated_with.md)








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
| self | namo:associated_with |
| native | namo:associated_with |
| narrow | RO:0004029, SNOMEDCT:47429007 |




## LinkML Source

<details>
```yaml
name: associated with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Expresses a relationship between two named things where the relationship
  is typically generated statistically (though not in all cases), and is weaker than
  its child, 'correlated with', but stronger than its parent, 'related to'. This relationship
  holds between two concepts represented by variables for which a statistical dependence
  is demonstrated.  E.g. the statement “Atrial Fibrillation (Afib) is associated with
  Myocardial Infraction (MI)” asserts that having Afib is not statistically independent
  from whether a patient will also have MI. Note that in Translator associations,
  the subject and object concepts may map exactly to the statistical variables, or
  represent related entities for which the variables serve as proxies in an Association
  (e.g. diseases, chemical entities or processes).
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- RO:0004029
- SNOMEDCT:47429007
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: associated_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>