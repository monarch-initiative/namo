package None;

import java.util.List;
import lombok.*;






/**
  Physiologically Based Pharmacokinetic models that simulate drug  absorption, distribution, metabolism, and excretion.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PBPKModel extends InSilicoModel {

  private List<PBPKCompartment> compartments;
  private Term speciesModeled;
  private DrugProperties drugProperties;
  private List<String> eliminationPathways;

}