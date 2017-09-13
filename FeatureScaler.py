from __future__ import division
import numpy as np

#test

def featureScaling(arr):
    
    if min(arr) == max(arr):
        arr_out = [0.5 for x in arr]
    else:
        arr_out = []
        for ii in arr:
            arr_out.append((ii-min(arr))/(max(arr)-min(arr)))

    return arr_out

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)

# sklearn implementation:


def ListToArray(input_data):
    return_arr = np.array(input_data).reshape([len(input_data),1])
    return return_arr

data = [115, 140, 175]
    
weights = ListToArray(data)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
rescaled_weights = scaler.fit_transform(weights)
print weights,'\n', rescaled_weights