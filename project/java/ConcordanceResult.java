package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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