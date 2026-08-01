package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Statistical measures of significance for molecular comparisons.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StatisticalSignificance  {

  private Float pValue;
  private Float adjustedPValue;
  private Float confidenceIntervalLower;
  private Float confidenceIntervalUpper;
  private String statisticalTest;


}