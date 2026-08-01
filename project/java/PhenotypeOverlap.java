package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Comparison of phenotypic manifestations between model and biological systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PhenotypeOverlap extends NamedThing {

  private Float phenotypeSimilarityScore;
  private List<PhenotypicFeature> sharedPhenotypes;
  private List<PhenotypicFeature> modelSpecificPhenotypes;
  private List<PhenotypicFeature> biologicalSpecificPhenotypes;
  private String phenotypeOntology;


}