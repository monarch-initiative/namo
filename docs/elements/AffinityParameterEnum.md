---
search:
  boost: 2.0
---


# Enum: AffinityParameterEnum 




_The types of parameters that can be used to describe the affinity between two entities, characteristically chemicals and proteins. The values are generally stated as the negative base 10 logarithm of the raw measurements._



<div data-search-exclude markdown="1">

URI: [namo:AffinityParameterEnum](https://w3id.org/monarch-initiative/namo/AffinityParameterEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| pIC50 | None | Negative base 10 logarithm of the the inhibitory concentration 50% (IC50) mea... |
| pEC50 | None | Negative base 10 logarithm of the molar concentration of a chemical that prod... |
| pAC50 | None |  |
| pXC50 | None |  |
| pKi | None | Negative base 10 logarithm of the equilibrium binding affinity for a ligand t... |
| pKon | None | Negative base 10 logarithm of the association rate constant (Kon) describes t... |
| pKoff | None | Negative base 10 logarithm of the dissociation rate constant (koff) describes... |
| pKd | None | Negative base 10 logarithm of the equilibrium dissociation constant (KD) whic... |




## Slots

| Name | Description |
| ---  | --- |
| [affinity_parameter](affinity_parameter.md) | The type of parameter describing the strength of an affinity between two enti... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: AffinityParameterEnum
description: The types of parameters that can be used to describe the affinity between
  two entities, characteristically chemicals and proteins. The values are generally
  stated as the negative base 10 logarithm of the raw measurements.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  pIC50:
    text: pIC50
    description: Negative base 10 logarithm of the the inhibitory concentration 50%
      (IC50) measures the concentration needed to block or inhibit a biological response.
  pEC50:
    text: pEC50
    description: Negative base 10 logarithm of the molar concentration of a chemical
      that produces a 50% excitation of a function
  pAC50:
    text: pAC50
  pXC50:
    text: pXC50
  pKi:
    text: pKi
    description: Negative base 10 logarithm of the equilibrium binding affinity for
      a ligand that reduces the activity of its binding partner. Ki represents the
      concentration at which the inhibitor ligand occupies 50% of the receptor sites
      when no competing ligand is present
  pKon:
    text: pKon
    description: Negative base 10 logarithm of the association rate constant (Kon)
      describes the rate at which molecules bind to each other.
  pKoff:
    text: pKoff
    description: Negative base 10 logarithm of the dissociation rate constant (koff)
      describes the rate at which they dissociate.
  pKd:
    text: pKd
    description: Negative base 10 logarithm of the equilibrium dissociation constant
      (KD) which is a measure of the binding affinity and is defined as the ratio
      of koff to kon.

```
</details>

</div>