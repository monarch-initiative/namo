package None;

import java.util.List;
import lombok.*;






/**
  A 3D cell culture system that self-organizes to recapitulate key structural and functional aspects of an organ or tissue
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Organoid extends ThreeDCellCulture {

  private Term organModeled;
  private String differentiationMethod;
  private String cultureSystem;

}