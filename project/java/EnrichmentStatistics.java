package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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