package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Assessment of cell type representation and cellular diversity between systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CellTypeCoverage extends NamedThing {

  private Float coveragePercentage;
  private List<Cell> representedCellTypes;
  private List<Cell> missingCellTypes;
  private List<CellTypeProportion> cellTypeProportions;
  private String singleCellMethod;


}