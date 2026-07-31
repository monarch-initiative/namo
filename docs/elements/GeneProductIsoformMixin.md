---
search:
  boost: 10.0
---

# Class: GeneProductIsoformMixin 


_This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms._



<div data-search-exclude markdown="1">



URI: [namo:GeneProductIsoformMixin](https://w3id.org/monarch-initiative/namo/GeneProductIsoformMixin)





```mermaid
 classDiagram
    class GeneProductIsoformMixin
    click GeneProductIsoformMixin href "../GeneProductIsoformMixin/"
      GeneProductMixin <|-- GeneProductIsoformMixin
        click GeneProductMixin href "../GeneProductMixin/"
      

      GeneProductIsoformMixin <|-- NucleosomeModification
        click NucleosomeModification href "../NucleosomeModification/"
      GeneProductIsoformMixin <|-- ProteinIsoform
        click ProteinIsoform href "../ProteinIsoform/"
      GeneProductIsoformMixin <|-- PosttranslationalModification
        click PosttranslationalModification href "../PosttranslationalModification/"
      GeneProductIsoformMixin <|-- RNAProductIsoform
        click RNAProductIsoform href "../RNAProductIsoform/"
      

      GeneProductIsoformMixin : name
        
      GeneProductIsoformMixin : synonym
        
      GeneProductIsoformMixin : xref
        
      
```





## Inheritance
* [MacromolecularMachineMixin](MacromolecularMachineMixin.md)
    * [GeneOrGeneProduct](GeneOrGeneProduct.md)
        * [GeneProductMixin](GeneProductMixin.md)
            * **GeneProductIsoformMixin**


## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [synonym](synonym.md) | * <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing | [GeneProductMixin](GeneProductMixin.md) |
| [xref](xref.md) | * <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge... | [GeneProductMixin](GeneProductMixin.md) |
| [name](name.md) | 0..1 <br/> [SymbolType](SymbolType.md) | genes are typically designated by a short symbol and a full name | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [NucleosomeModification](NucleosomeModification.md) | A chemical modification of a histone protein within a nucleosome octomer or a... |
| [ProteinIsoform](ProteinIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |
| [PosttranslationalModification](PosttranslationalModification.md) | A chemical modification of a polypeptide or protein that occurs after transla... |
| [RNAProductIsoform](RNAProductIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |














## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:GeneProductIsoformMixin |
| native | namo:GeneProductIsoformMixin |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene product isoform mixin
description: This is an abstract class that can be mixed in with different kinds of
  gene products to indicate that the gene product is intended to represent a specific
  isoform rather than a canonical or reference or generic product. The designation
  of canonical or reference may be arbitrary, or it may represent the superclass of
  all isoforms.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: gene product mixin
mixin: true

```
</details>

### Induced

<details>
```yaml
name: gene product isoform mixin
description: This is an abstract class that can be mixed in with different kinds of
  gene products to indicate that the gene product is intended to represent a specific
  isoform rather than a canonical or reference or generic product. The designation
  of canonical or reference may be arbitrary, or it may represent the superclass of
  all isoforms.
from_schema: https://w3id.org/monarch-initiative/namo
is_a: gene product mixin
mixin: true
attributes:
  synonym:
    name: synonym
    description: Alternate human-readable names for a thing
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - alias
    narrow_mappings:
    - skos:altLabel
    - gff3:Alias
    - AGRKB:synonyms
    - gpi:DB_Object_Synonyms
    - HANCESTRO:0330
    - IAO:0000136
    - RXNORM:has_tradename
    rank: 1000
    is_a: node property
    domain: named thing
    owner: gene product isoform mixin
    domain_of:
    - named thing
    - gene product mixin
    range: label type
    multivalued: true
  xref:
    name: xref
    description: A database cross reference or alternative identifier for a NamedThing
      or edge between two NamedThings.  This property should point to a database record
      or webpage that supports the existence of the edge, or gives more detail about
      the edge. This property can be used on a node or edge to provide multiple URIs
      or CURIE cross references.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - dbxref
    - Dbxref
    - DbXref
    - record_url
    - source_record_urls
    narrow_mappings:
    - gff3:Dbxref
    - gpi:DB_Xrefs
    rank: 1000
    domain: named thing
    owner: gene product isoform mixin
    domain_of:
    - named thing
    - publication
    - retrieval source
    - gene
    - gene product mixin
    range: uriorcurie
    multivalued: true
  name:
    name: name
    description: genes are typically designated by a short symbol and a full name.
      We map the symbol to the default display name and use an additional slot for
      full name
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/monarch-initiative/namo
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    rank: 1000
    domain: entity
    slot_uri: rdfs:label
    owner: gene product isoform mixin
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: symbol type

```
</details></div>