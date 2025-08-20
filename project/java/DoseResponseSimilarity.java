package None;

import java.util.List;
import lombok.*;






/**
  Comparison of dose-response relationships between model and biological systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DoseResponseSimilarity  {

  private Float correlationCoefficient;
  private Float ec50Ratio;
  private Float maxResponseRatio;
  private String compoundTested;

}