package None;

import java.util.List;
import lombok.*;






/**
  Computational replicas of biological systems for real-time prediction and personalized modeling.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DigitalTwin extends InSilicoModel {

  private String twinScope;
  private List<String> realTimeDataSources;
  private List<String> personalizationParameters;
  private String updateFrequency;

}