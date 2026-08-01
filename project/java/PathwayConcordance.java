package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Assessment of biological pathway conservation and activity between model and biological systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PathwayConcordance extends NamedThing {

  private Float pathwayOverlapScore;
  private List<Pathway> activePathways;
  private List<Pathway> divergentPathways;
  private String pathwayAnalysisMethod;
  private List<EnrichmentStatistics> enrichmentStatistics;


}