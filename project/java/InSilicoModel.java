package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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