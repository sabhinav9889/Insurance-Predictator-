import pickle
from schemas.user_input import UserInput
import pandas as pd

with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

model_version = '1.0.0'

class_labels = model.classes_.tolist()

def PredictInput(data: UserInput):
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])
    predicted_class = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]
    confidence = max(probability)
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probability)))
    return {
        "predicted_category":  predicted_class,
        "confidence": round(confidence, 4),
        "class_probablities": class_probs
    }