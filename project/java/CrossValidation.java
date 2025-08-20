package None;

import java.util.List;
import lombok.*;






/**
  Cross-validation strategy and results for ML models.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CrossValidation  {

  private String cvMethod;
  private Integer nFolds;
  private Float cvScore;
  private Float cvStd;

}