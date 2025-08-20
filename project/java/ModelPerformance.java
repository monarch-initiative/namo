package None;

import java.util.List;
import lombok.*;






/**
  Statistical performance metrics for computational models.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ModelPerformance  {

  private Float accuracy;
  private Float sensitivity;
  private Float specificity;
  private Float rSquared;
  private Float rmse;
  private Float auc;

}