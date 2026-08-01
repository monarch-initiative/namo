package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A 3D cell culture system that self-organizes to recapitulate key structural and functional aspects of an organ or tissue
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Organoid extends ThreeDCellCulture {

  private GrossAnatomicalStructure organModeled;
  private String differentiationMethod;
  private String cultureSystem;


}