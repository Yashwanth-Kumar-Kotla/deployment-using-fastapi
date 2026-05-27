from pydantic import BaseModel, Field
from typing import Dict

class PredictedResponse(BaseModel):

    predicted_output : str = Field(..., description="Output predicted by the model", examples=["High"])
    confidence : float = Field(..., description="Probability of predicting successfully by the model", examples=[0.84])
    class_probabilities : Dict[str, float] = Field(..., description="probabilities of each class", examples=[{"High" : 0.8, "Medium" : 0.17, "Low" : 0.03}])
