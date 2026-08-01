package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A literature reference with identifier and title for citing published work.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Reference  {

  private URI id;
  private String title;
  private List<String> authors;
  private String journal;
  private Integer year;
  private URI url;


}