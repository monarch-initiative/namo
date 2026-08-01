package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Machine Learning and AI-based models for prediction, mechanism inference, and hypothesis generation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MLModel extends InSilicoModel {

  private String mlAlgorithm;
  private List<String> featureTypes;
  private Integer trainingDataSize;
  private String modelInterpretability;
  private CrossValidation crossValidation;


}