package None;

import java.util.List;
import lombok.*;






/**
  A gene entity with identifiers and expression information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Gene extends NamedThing {

  private String geneSymbol;
  private String ensemblId;
  private Integer entrezId;
  private Float foldChange;
  private Float pValue;
  private Float adjustedPValue;

}