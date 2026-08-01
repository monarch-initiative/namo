package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Ratio specification for different cell types in co-culture systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CellRatio  {

  private Cell cellType;
  private Float ratio;
  private String ratioType;


}