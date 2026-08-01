package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Physicochemical and pharmacological properties of a drug in PBPK models.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DrugProperties  {

  private Float molecularWeight;
  private Float logp;
  private Float pka;
  private Float proteinBinding;
  private Float clearance;


}