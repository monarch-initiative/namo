package None;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public abstract class ModelSystem extends NamedThing {

  private List<ModelsRelationship> models;

}