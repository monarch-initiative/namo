---
search:
  boost: 5.0
---

# Slot: contributor 


_Links an information content entity (such as a dataset, publication, or software artefact) to an agent responsible for making contributions to it. Used as an abstract grouping predicate over more specific contribution roles (author, editor, publisher, provider). Corresponds to dct:contributor._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract slot and should not be populated directly


URI: [namo:contributor](https://w3id.org/monarch-initiative/namo/contributor)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **contributor**
            * [provider](provider.md)
            * [publisher](publisher.md)
            * [editor](editor.md)
            * [author](author.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InformationContentEntity](InformationContentEntity.md) |
| Domain | [Agent](Agent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |










## Comments

* This is a grouping for predicates relating entities to their associated contributors realizing them



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:contributor |
| native | namo:contributor |
| exact | dct:contributor |




## LinkML Source

<details>
```yaml
name: contributor
description: Links an information content entity (such as a dataset, publication,
  or software artefact) to an agent responsible for making contributions to it. Used
  as an abstract grouping predicate over more specific contribution roles (author,
  editor, publisher, provider). Corresponds to dct:contributor.
comments:
- This is a grouping for predicates relating entities to their associated contributors
  realizing them
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- dct:contributor
rank: 1000
is_a: related to at instance level
abstract: true
domain: agent
inherited: true
range: information content entity
multivalued: true

```
</details></div>