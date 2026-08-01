package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A physiological compartment in a PBPK model.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PBPKCompartment extends NamedThing {

  private String compartmentType;
  private Float volume;
  private Float bloodFlow;
  private Float partitionCoefficient;


}