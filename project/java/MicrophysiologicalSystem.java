package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials, and living cells to replicate tissue-level physiology and dynamics. Conforms to ISO 22916:2022 interoperability requirements for dimensions, connections, and device classification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class MicrophysiologicalSystem extends NAMModel {

  private MicrofluidicDesign microfluidicDesign;
  private MechanicalStimulation mechanicalForces;
  private String perfusionSystem;
  private List<String> sensorIntegration;


}