# Insurance Predictator

A FastAPI service that predicts an insurance premium category from user details, using a pickled scikit-learn model.

## Endpoints
- `GET /` – welcome message
- `GET /health` – service status and model version
- `POST /predict` – returns the prediction for the submitted user data
- `GET /docs` – interactive Swagger UI

## Run with Docker
```bash
docker run -p 8000:8000 abhinav9889/insurance-predictor:1.0
```
Then open http://localhost:8000/docs

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Build the image yourself
```bash
docker build -t insurance-predictor .
docker run -p 8000:8000 insurance-predictor
```
