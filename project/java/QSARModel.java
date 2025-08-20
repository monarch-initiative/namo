package None;

import java.util.List;
import lombok.*;






/**
  Quantitative Structure-Activity Relationship models that predict  chemical/biological activity from molecular structure.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class QSARModel extends InSilicoModel {

  private List<String> molecularDescriptors;
  private String activityEndpoint;
  private Integer trainingDatasetSize;
  private ModelPerformance modelPerformance;

}