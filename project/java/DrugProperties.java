package None;

import java.util.List;
import lombok.*;






/**
  Physicochemical and pharmacological properties of a drug in PBPK models.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DrugProperties  {

  private Float molecularWeight;
  private Float logp;
  private Float pka;
  private Float proteinBinding;
  private Float clearance;

}