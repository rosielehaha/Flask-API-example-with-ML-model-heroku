# -*- coding: UTF-8 -*-
import pickle
import gzip

from keras.models import load_model
from numpy import loadtxt
import numpy as np
import pandas as pd
import time 


# 載入Model
model=load_model('app/model/pump4_ANN_0606.h5')


def predict(input):
    pred=model.predict(input)[0]
    print(pred)
    return 
