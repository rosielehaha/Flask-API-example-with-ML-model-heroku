# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:06:12 2022

@author: hong
"""

from keras.models import load_model
from numpy import loadtxt
import numpy as np
import pandas as pd
import time 



model=load_model('app/model/pump4_ANN_0606.h5')


def predict(input):
    pred=model.predict(input)[0]
    print("我自己的model預測結果是",pred)
    return 
