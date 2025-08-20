package None;

import java.util.List;
import lombok.*;






/**
  A model system that simulates the physiological functions of an organ using a microfluidic device. Examples: Airway-on-chip, ...
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrganOnChip extends MicrophysiologicalSystem {

  private Term organModeled;
  private List<Term> cellTypes;
  private String cellSource;

}