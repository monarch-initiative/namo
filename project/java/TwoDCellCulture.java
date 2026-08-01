package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Conventional monolayer cell cultures grown on flat surfaces. Simple but limited in physiological relevance.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TwoDCellCulture extends CellularSystem {

  private String substrateType;
  private Float confluenceLevel;
  private String passageProtocol;


}