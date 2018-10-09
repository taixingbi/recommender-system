import keras
import numpy as np
import pandas as pd
import datetime
import time

from keras.models import load_model

class PredictRating():
    def __init__(self, path_load_model):
        self.model = load_model(path_load_model)
    
    def predict(self, df_data):
        y_pred= self.model.predict( [df_data.user_id, df_data.item_id] )
        return y_pred

if __name__ == "__main__":     
    #random select 2 user-item data
    test= pd.read_csv('pipenv/data/test.csv')
    test1= test[:1]
    test30= test[:30]
    
    #load pretrained model
    path_load_model= 'pipenv/result/model.h5'
    model= PredictRating( path_load_model ) 
    #the first pass is always long because the backends are allocating the memory and stuff like that.
    pred_rating= model.predict(test1)

    #start predict
    print("\npredict 1 sample: ", test1)   
    start_time= datetime.datetime.now() 
    pred_rating= model.predict(test1)
    print("predict time: ", (datetime.datetime.now()-start_time), "h:m:s")        
    print( pred_rating )  
    
    print("\npredict 30 samples: ", test30.head())   
    start_time= datetime.datetime.now() 
    pred_rating= model.predict(test30)
    print("predict time: ", (datetime.datetime.now()-start_time), "h:m:s")        
    print( pred_rating )    