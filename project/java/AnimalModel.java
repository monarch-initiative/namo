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
public class AnimalModel extends ModelSystem {

  private OrganismTaxon species;
  private OrganismTaxon strain;
  private LifeStage lifeStage;
  private QuantityValue ageValue;
  private EnvironmentalExposure environment;


}