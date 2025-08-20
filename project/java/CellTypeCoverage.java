package None;

import java.util.List;
import lombok.*;






/**
  Assessment of cell type representation and cellular diversity between systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CellTypeCoverage extends NamedThing {

  private Float coveragePercentage;
  private List<Term> representedCellTypes;
  private List<Term> missingCellTypes;
  private List<CellTypeProportion> cellTypeProportions;
  private String singleCellMethod;

}