package None;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class AnimalModel extends ModelSystem {

  private Term species;
  private Term strain;
  private Term age;
  private Term environment;

}