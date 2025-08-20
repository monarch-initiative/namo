package None;

import java.util.List;
import lombok.*;






/**
  Dimensions of a microfluidic channel
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ChannelDimensions  {

  private String channelName;
  private Float width;
  private Float height;
  private Float length;

}