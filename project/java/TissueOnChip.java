package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Tissue-level microphysiological systems that model specific tissue functions and multi-cellular interactions. Aligned with ISO 10991:2023 microfluidics terminology.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TissueOnChip extends MicrophysiologicalSystem {

  private GrossAnatomicalStructure anatomicalStructureModeled;
  private String tissueArchitecture;
  private List<String> barrierFunctions;


}