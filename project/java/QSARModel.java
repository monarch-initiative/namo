package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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