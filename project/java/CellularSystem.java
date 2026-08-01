package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Cell-based model systems that use living cells to model biological processes. Includes 2D cultures, 3D systems, and co-cultures. Conforms to MIACA (Minimal Information About a Cellular Assay) standards.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CellularSystem extends NAMModel {

  private List<Cell> cellTypes;
  private String cellSource;
  private String cultureConditions;


}