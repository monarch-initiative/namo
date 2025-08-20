package None;

import java.util.List;
import lombok.*;






/**
  Cell-based model systems that use living cells to model biological processes. Includes 2D cultures, 3D systems, and co-cultures.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CellularSystem extends NAMModel {

  private List<Term> cellTypes;
  private String cellSource;
  private String cultureConditions;

}