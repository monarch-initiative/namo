package None;

import java.util.List;
import lombok.*;






/**
  Comparison of phenotypic manifestations between model and biological systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PhenotypeOverlap extends NamedThing {

  private Float phenotypeSimilarityScore;
  private List<Term> sharedPhenotypes;
  private List<Term> modelSpecificPhenotypes;
  private List<Term> biologicalSpecificPhenotypes;
  private String phenotypeOntology;

}