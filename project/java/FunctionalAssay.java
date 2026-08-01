package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A functional assay used to assess biological capabilities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FunctionalAssay extends NamedThing {

  private String assayType;
  private Float assayResult;
  private Float referenceValue;
  private String units;
  private String methodology;


}