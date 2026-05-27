from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.predicted_response import PredictedResponse
from model.predict import MODEL_VERSION, model, predict_output 




app = FastAPI()


        
@app.post("/predict", response_model=PredictedResponse)
def predict_premium(data : UserInput):
    
    input_user = {
        "bmi" : [data.bmi],
        "age_group" : [data.age_group],
        "lifestyle_risk" : [data.lifestyle_risk],
        "city_tier" : [data.city_tier],
        "income_lpa" : [data.income_lpa],
        "occupation" : [data.occupation]
    }

    try: 
        result = predict_output(input_user)

        return JSONResponse(status_code=200, content={"result": result})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

@app.get("/")
def home():
    return {"Insurance Category Predictor API"}

@app.get("/health")
def health_check():
    return {
        "status" : "OK",
        "API Running " : "Yes",
        "Version" : MODEL_VERSION,
        "model_loaded" : model is not None
    }