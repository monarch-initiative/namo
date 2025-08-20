package None;

import java.util.List;
import lombok.*;






/**
  Quantitative comparison of cell type proportions between systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CellTypeProportion  {

  private Term cellType;
  private Float modelProportion;
  private Float biologicalProportion;
  private Float proportionRatio;

}