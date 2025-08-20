package None;

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