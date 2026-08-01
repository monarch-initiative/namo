package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Specification of mechanical forces applied to the model system
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MechanicalStimulation extends NamedThing {

  private List<String> stimulationType;
  private Float cyclicStretchPercent;
  private Float frequencyHz;
  private Float shearStress;
  private Float pressurePascal;
  private Float durationMinutes;


}