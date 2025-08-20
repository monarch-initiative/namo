package None;

import java.util.List;
import lombok.*;






/**
  Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials,  and living cells to replicate tissue-level physiology and dynamics.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class MicrophysiologicalSystem extends NAMModel {

  private MicrofluidicDesign microfluidicDesign;
  private MechanicalStimulation mechanicalForces;
  private String perfusionSystem;
  private List<String> sensorIntegration;

}