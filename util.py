import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,BHK,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = BHK
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)
def get_loccation_naam():
    return __locations

def load_saved_Artifacts():
    print("Load Saved Artifacts...& here we go")
    global  __data_columns
    global __locations

    with open("./Artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model

    with open("./Artifacts/day9_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Leh,ho gya kaam")


if __name__ == "__main__":
    load_saved_Artifacts()
    print(get_loccation_naam())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))