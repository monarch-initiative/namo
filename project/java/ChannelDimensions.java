package None;

/* metamodel_version: 1.11.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Dimensions of a microfluidic channel according to ISO 10991:2023 definitions for microchannel geometry and dimensions
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ChannelDimensions  {

  private String channelName;
  private Float width;
  private Float height;
  private Float length;


}