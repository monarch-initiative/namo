package None;

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