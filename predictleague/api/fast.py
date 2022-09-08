from datetime import datetime
from marshal import load
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pandas as pd


from tensorflow.keras.models import load_model
from predictleague.ml_logic.preprocessor import preprocess_input_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
@app.get("/predict")
def predict(match_outcomes):
    from tensorflow.keras.models import load_model
    from predictleague.ml_logic.preprocessor import preprocess_input_data

    match_outcomes = match_outcomes.split(",")
    match_outcomes = [int(x) for x in match_outcomes]
    X_pred = match_outcomes
    print(X_pred)

    model = load_model('my_model2.h5')
    X_processed = preprocess_input_data(X_pred)
    y_pred = model.predict(X_processed)

    higher_league = " "

    if y_pred > 0.5:
        higher_league = "**Yes, You have high chances**"
    else:
        higher_league = "**Sorry, You have to train a little more**"

    return (higher_league)


@app.get("/")
def root():
    return {
        'greeting': 'Hello hi'
        }
