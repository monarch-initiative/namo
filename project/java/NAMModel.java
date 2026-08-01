package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A New Approach Methodology (NAM) model, which is a type of model system that does not involve the use of animals.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class NAMModel extends ModelSystem {

  private String biologicalOrganizationLevel;
  private String spatialContext;
  private String complexityLevel;
  private List<Reference> references;


}