package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Abstract parent for NAMO classes that stand in for a class in the Biolink Model.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class BiolinkEntity  {

  private URI id;
  private String name;
  private String description;


}