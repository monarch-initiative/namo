package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Detailed specification of a microfluidic device design including its architecture, materials, dimensions, and functional features. Terms aligned with ISO 10991:2023 Microfluidics Vocabulary standard.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MicrofluidicDesign extends NamedThing {

  private String architectureType;
  private Integer numberOfChannels;
  private List<String> channelConfiguration;
  private String membraneType;
  private Float membranePoreSize;
  private Float membraneThickness;
  private List<String> interfaceType;
  private List<ChannelDimensions> channelDimensions;
  private List<String> material;
  private List<String> surfaceTreatment;
  private List<String> flowControlMethod;
  private List<String> sensorsIntegrated;
  private List<String> specialFeatures;


}