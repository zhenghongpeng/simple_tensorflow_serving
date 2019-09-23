#!/usr/bin/env python

import requests
import time
import pandas as pd
import os
from sklearn.externals import joblib
import json
import numpy

def main():

    start=time.time()

    #### Model files path containing (ScalerX, Scalery, LSTM_model.h5 and LSTM_model.json)
    model_path='models/keras_well/'

    #### Loading Scaler files
    scalerX = joblib.load(model_path+'Scaler_X.sav')               
    scalery = joblib.load(model_path+'Scaler_y.sav')

    #### Input test files
    data_store = pd.HDFStore(model_path+'1524001569_Curve_4.h5')
    df = data_store['Features']
    data_store.close()

    #### Separting X and y values from the loaded dataframe
    test_data_y = df['Rate Of Penetration (ft_per_hr)'].copy()
    test_data_x = df.drop(columns=['Rate Of Penetration (ft_per_hr)'])
    test_depth = df['Hole Depth (feet)'].copy()

    #### transfer to json input
    cols_name = [''.join(col).replace(' ','_').replace('(','_').replace(')','_') for col in test_data_x.columns]
    test_data_x.columns = cols_name


    # values_test_y = test_data_y.values
    values_test_x = test_data_x.values

    # values_test_y = values_test_y.astype('float64')
    values_test_x = values_test_x.astype('float64')

    # values_test_y=values_test_y.reshape(-1, 1)


    #### Scaling the input data
    # test_y = scalery.transform(values_test_y)
    test_X = scalerX.transform(values_test_x)
    # test_y = values_test_y
    # test_X = values_test_x
    # print(test_X)

    test_X_LSTM = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))

    endpoint = "http://127.0.0.1:5000"
    json_data = {"model_name": "default", "data": {"input_file":test_X_LSTM.tolist() }}
    with open('input.json', 'w') as outfile:
        json.dump(json_data, outfile)
    result = requests.post(endpoint, json=json_data)
    print(result.json())




if __name__ == "__main__":
    main()
  


