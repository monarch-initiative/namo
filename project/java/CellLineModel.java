package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A model system based on immortalized cell lines that can be maintained in culture indefinitely. Examples: HepG2, A549, Caco-2, etc.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CellLineModel extends TwoDCellCulture {

  private String passageRange;
  private String authenticationMethod;


}