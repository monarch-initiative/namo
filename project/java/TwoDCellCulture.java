package None;

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