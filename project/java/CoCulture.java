package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Co-culture systems combining multiple cell types to mimic  microenvironments and cell-cell interactions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CoCulture extends CellularSystem {

  private String cocultureConfiguration;
  private List<CellRatio> cellRatios;
  private List<String> interactionMechanisms;


}