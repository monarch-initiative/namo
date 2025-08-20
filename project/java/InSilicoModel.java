package None;

import java.util.List;
import lombok.*;






/**
  Computational models that simulate biological processes without physical biological components.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class InSilicoModel extends NAMModel {

  private String computationalMethod;
  private String softwarePlatform;
  private List<String> validationDatasets;
  private String predictionScope;

}