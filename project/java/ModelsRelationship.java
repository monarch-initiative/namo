package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

@Data
@EqualsAndHashCode(callSuper=false)
public class ModelsRelationship  {

  private BiologicalSystem biologicalSystemModeled;
  private Boolean isComputed;
  private ConcordanceResult concordance;
  private StructuredConcordanceResult structuredConcordance;


}