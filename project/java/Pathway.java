package None;

import java.util.List;
import lombok.*;






/**
  A biological pathway with activity and enrichment information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Pathway extends NamedThing {

  private String pathwayDatabase;
  private String pathwayId;
  private Float activityScore;
  private Float enrichmentScore;

}