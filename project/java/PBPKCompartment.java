package None;

import java.util.List;
import lombok.*;






/**
  A physiological compartment in a PBPK model.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PBPKCompartment extends NamedThing {

  private String compartmentType;
  private Float volume;
  private Float bloodFlow;
  private Float partitionCoefficient;

}