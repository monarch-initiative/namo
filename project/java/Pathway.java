package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A biological pathway with activity and enrichment information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Pathway extends NamedThing {

  private String pathwayDatabase;
  private String pathwayId;
  private Float activityScore;
  private Float enrichmentScore;


}