package None;

import java.util.List;
import lombok.*;






/**
  Tissue-level microphysiological systems that model specific tissue functions and multi-cellular interactions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TissueOnChip extends MicrophysiologicalSystem {

  private Term tissueModeled;
  private String tissueArchitecture;
  private List<String> barrierFunctions;

}