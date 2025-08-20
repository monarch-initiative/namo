package None;

import java.util.List;
import lombok.*;






/**
  Statistical measures for pathway enrichment analysis.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EnrichmentStatistics  {

  private Float enrichmentScore;
  private Float pValue;
  private Float qValue;
  private Integer genesInPathway;
  private Integer genesInDataset;

}