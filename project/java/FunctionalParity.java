package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Evaluation of functional capabilities and physiological responses between systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FunctionalParity extends NamedThing {

  private Float functionalSimilarityScore;
  private List<String> conservedFunctions;
  private List<String> impairedFunctions;
  private List<FunctionalAssay> functionalAssays;
  private DoseResponseSimilarity doseResponseSimilarity;


}