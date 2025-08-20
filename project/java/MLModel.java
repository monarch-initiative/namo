package None;

import java.util.List;
import lombok.*;






/**
  Machine Learning and AI-based models for prediction, mechanism inference, and hypothesis generation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MLModel extends InSilicoModel {

  private String mlAlgorithm;
  private List<String> featureTypes;
  private Integer trainingDataSize;
  private String modelInterpretability;
  private CrossValidation crossValidation;

}