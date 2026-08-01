package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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