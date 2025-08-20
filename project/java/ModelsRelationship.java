package None;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class ModelsRelationship  {

  private BiologicalSystem biologicalSystemModeled;
  private boolean isComputed;
  private ConcordanceResult concordance;
  private StructuredConcordanceResult structuredConcordance;

}