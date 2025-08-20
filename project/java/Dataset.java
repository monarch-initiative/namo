package None;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class Dataset  {

  private List<ModelSystem> modelSystems;
  private List<Study> studies;

}