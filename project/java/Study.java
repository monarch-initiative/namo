package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A study is a structured investigation or analysis, often involving the collection and interpretation of data, to answer specific research questions or test hypotheses.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Study extends NamedThing {

  private String contextOfUse;
  private String biologicalContext;
  private String perturbations;
  private String endpoints;
  private String planComparators;


}