package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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