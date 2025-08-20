package None;

import java.util.List;
import lombok.*;






/**
  A quality control measure and its associated value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class QualityControlMetric  {

  private String metricName;
  private Float metricValue;
  private Float threshold;
  private boolean passFailStatus;

}