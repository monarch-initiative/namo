package None;

import java.util.List;
import lombok.*;






/**
  A generic grouping for any identifiable entity
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NamedThing  {

  private String id;
  private String name;
  private String description;
  private String type;

}