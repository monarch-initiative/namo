package None;

import java.util.List;
import lombok.*;






/**
  Detailed assessment of molecular-level concordance between model and biological systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MolecularSimilarity extends NamedThing {

  private Float similarityScore;
  private Float correlationCoefficient;
  private List<Gene> differentiallyExpressedGenes;
  private List<Gene> conservedGenes;
  private String methodology;
  private String dataSource;
  private StatisticalSignificance statisticalSignificance;

}