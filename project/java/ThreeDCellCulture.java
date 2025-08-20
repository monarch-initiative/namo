package None;

import java.util.List;
import lombok.*;






/**
  Three-dimensional cell culture systems including spheroids and organoids. More physiologically relevant with 3D architecture.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ThreeDCellCulture extends CellularSystem {

  private String threeDArchitecture;
  private String matrixComposition;
  private String sizeRange;

}