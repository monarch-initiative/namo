package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A generic grouping for any identifiable entity
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NamedThing  {

  private URI id;
  private String name;
  private String description;
  private String type;


}