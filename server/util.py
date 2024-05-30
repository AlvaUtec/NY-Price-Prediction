import os
import json
import pickle
import numpy as np

_sublocalities = None
_data_columns = None
_model = None

def get_sublocalities():
    return _sublocalities

def get_estimated_price(sublocality, sqft, bath, beds):
    try:
        loc_index = _data_columns.index(sublocality)
    except:
        loc_index = -1

    x = np.zeros(len(_data_columns))
    x[0] = beds
    x[1] = bath
    x[2] = sqft

    if loc_index >= 0:
        x[loc_index] = 1

    return round(_model.predict([x])[0],2)

def load_saved_artifacts():
    print('Loading saved artifacts...')
    global _data_columns
    global _sublocalities

    # Determine the current file's directory
    current_dir = os.path.dirname(__file__)

    # Construct the path to columns.json
    columns_path = os.path.join(current_dir, '..', 'model', 'columns.json')
    columns_path = os.path.abspath(columns_path)

    # Construct the path to ny_house_price_model.pickle
    model_path = os.path.join(current_dir, '..', 'model', 'ny_house_price_model.pickle')
    model_path = os.path.abspath(model_path)

    # Load the columns.json file
    with open(columns_path, 'r') as f:
        _data_columns = json.load(f)['data_columns']
        _sublocalities = _data_columns[3:]

    # Load the model pickle file
    global _model
    with open(model_path, 'rb') as f:
        _model = pickle.load(f)

    print('Loading artifacts done...')

if __name__ == '__main__':
    load_saved_artifacts()
