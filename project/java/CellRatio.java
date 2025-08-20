package None;

import java.util.List;
import lombok.*;






/**
  Ratio specification for different cell types in co-culture systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CellRatio  {

  private Term cellType;
  private Float ratio;
  private String ratioType;

}