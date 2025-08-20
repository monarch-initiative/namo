package None;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class ConcordanceResult  {

  private String phenotypeOverlap;
  private String molecularSimilarity;
  private String pathwayConcordance;
  private String cellTypeCoverage;
  private String functionalParity;
  private String reproducibility;

}