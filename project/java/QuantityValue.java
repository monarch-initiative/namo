package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value. Biolink models this as an annotation rather than a named thing, so it has no identifier and is inlined by value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class QuantityValue  {

  private Double hasNumericValue;
  private URI hasUnit;


}