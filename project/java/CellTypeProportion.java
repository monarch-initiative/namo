package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Quantitative comparison of cell type proportions between systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CellTypeProportion  {

  private Cell cellType;
  private Float modelProportion;
  private Float biologicalProportion;
  private Float proportionRatio;


}