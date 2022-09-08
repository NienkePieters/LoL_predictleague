from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, StandardScaler
from sklearn.impute import SimpleImputer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.pipeline import make_pipeline
from tensorflow.keras.models import load_model

import numpy as np
import pandas as pd

def preprocess_input_data(X_input):
    '''The input should be a list of wins/losses, e.g. [0,1,1,0]'''
    X = pd.DataFrame(X_input)
    X.replace(0,-0.939943)
    X.replace(1,1.063894)

    #make tensor again
    X_tensor = []
    X_tensor.append(X.loc[:,0])

    # Padding data
    X_processed = pad_sequences(np.array(X_tensor, dtype=object), dtype='float32', padding = 'post', value=-1000, maxlen=150) # int32 by default

    print("\n✅ X_processed, with shape", X_processed.shape)

    return X_processed
