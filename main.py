from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schemas.user_input import UserInput
from model.predict import model, model_version, PredictInput
from schemas.predication_resp import OutputRes
#import ml model

app = FastAPI()

# Home Page route
@app.get('/')
def Home():
    return JSONResponse(status_code=200, content="Welcome to X Insurance")

# Health route
@app.get('/health')
def Health():
    return JSONResponse(status_code=200, content={
        "status": "ok",
        "model_version": model_version,
        "model": model is not None
    })

@app.post('/predict', response_model=OutputRes)
def predict_premium(data: UserInput):
    try:
        predication  = PredictInput(data)
        return JSONResponse(status_code=200, content=predication)
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))