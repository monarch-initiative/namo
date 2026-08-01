package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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