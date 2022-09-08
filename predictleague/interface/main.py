import numpy as np
import pandas as pd

from ml_logic.preprocessor import preprocess_input_data

def pred(X_pred: list = None):
    """
    Make a prediction using the model
    """

    print("\n⭐️ use case: predict")

    from tensorflow.keras.models import load_model
    import numpy as np
    import pandas as pd
    from ml_logic.preprocessor import preprocess_input_data

    if X_pred is None:
        X_pred = [0,1,1,0,1,1,1,1,1,1,1,1,1]

    # Recreate the exact same model, including its weights and the optimizer
    model = load_model('my_model.h5')

    X_processed = preprocess_input_data(X_pred)

    y_pred = model.predict(X_processed)

    print("\n✅ prediction done: ", y_pred, y_pred.shape)

    return y_pred


