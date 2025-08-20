package None;

import java.util.List;
import lombok.*;






/**
  Detailed specification of a microfluidic device design including its architecture, materials, dimensions, and functional features.
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