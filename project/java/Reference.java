package None;

import java.util.List;
import lombok.*;






/**
  A literature reference with identifier and title for citing published work.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Reference  {

  private String id;
  private String title;
  private List<String> authors;
  private String journal;
  private Integer year;
  private String url;

}