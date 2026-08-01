package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Physiologically Based Pharmacokinetic models that simulate drug  absorption, distribution, metabolism, and excretion.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PBPKModel extends InSilicoModel {

  private List<PBPKCompartment> compartments;
  private OrganismTaxon speciesModeled;
  private DrugProperties drugProperties;
  private List<String> eliminationPathways;


}