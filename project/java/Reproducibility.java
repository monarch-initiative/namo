package None;

import java.util.List;
import lombok.*;






/**
  Assessment of experimental reproducibility and consistency of the model system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Reproducibility extends NamedThing {

  private Float reproducibilityScore;
  private Float coefficientOfVariation;
  private Float batchToBatchVariation;
  private Float interLaboratoryConsistency;
  private Integer replicateCount;
  private List<QualityControlMetric> qualityControlMetrics;

}