package None;

import java.util.List;
import lombok.*;






/**
  A functional assay used to assess biological capabilities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FunctionalAssay extends NamedThing {

  private String assayType;
  private Float assayResult;
  private Float referenceValue;
  private String units;
  private String methodology;

}