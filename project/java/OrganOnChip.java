package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A model system that simulates the physiological functions of an organ using a microfluidic device. Examples: Airway-on-chip, ... Aligned with ISO 10991:2023 microfluidics terminology.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrganOnChip extends MicrophysiologicalSystem {

  private GrossAnatomicalStructure organModeled;
  private List<Cell> cellTypes;
  private String cellSource;


}