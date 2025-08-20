package None;

import java.util.List;
import lombok.*;






/**
  Detailed structured assessment of concordance between model and biological systems with rich metadata, evidence, and quantitative measures.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StructuredConcordanceResult  {

  private MolecularSimilarity molecularSimilarity;
  private PathwayConcordance pathwayConcordance;
  private PhenotypeOverlap phenotypeOverlap;
  private CellTypeCoverage cellTypeCoverage;
  private FunctionalParity functionalParity;
  private Reproducibility reproducibility;

}