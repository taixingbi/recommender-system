import pandas as pd
import numpy as np

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

import keras
from pipenv.model import DeepLearning as Model

class Training():
    def __init__(self, 
                 path_read_data= 'pipenv/data/data.csv', 
                 path_read_train='pipenv/data/train.csv',
                 path_read_test= 'pipenv/data/test.csv',
                 path_save_model= 'pipenv/result/model.h5' ):
        
        self.path_read_data= path_read_data
        self.path_read_train= path_read_train
        self.path_read_test= path_read_test
        self.path_save_model= path_save_model

    def read_data(self, path_read):
        df= pd.read_csv(path_read)
        print( path_read )
        return df

    def pre_precossing(self):
        data= self.read_data( self.path_read_data )
        train= self.read_data( self.path_read_train )
        test= self.read_data( self.path_read_test )
        
        n_users = data.user_id.unique().shape[0]
        n_items = data.item_id.unique().shape[0]
        print ('Number of users = ' + str(n_users) + ' | Number of apts = ' + str(n_items) )

        return n_users, n_items, train, test
    
    def save_model(self, model, path_save):
        model.save(path_save)
        print(path_save)
    
    def measure(self, y_pred, test):
        #y_hat_2 = np.round(model.predict([test.user_id, test.item_id]),0)
        y_true = test.rating
        rmse= mean_squared_error(y_true, y_pred)**.5 
        print(' ')
        print ( 'Deep Learning CF RMSE: '   + str(rmse) )
        #print( mean_absolute_error(y_true, y_pred) )        
    
    def pipeline(self):
        n_users, n_items, train, test = self.pre_precossing()
        model= Model(n_users, n_items).cnn()
        model.fit([train.user_id, train.item_id], train.rating, epochs=2, verbose=1, validation_split=0.1)
        y_pred= model.predict([test.user_id, test.item_id])
        self.save_model(model, self.path_save_model)
        self.measure(y_pred, test)
        
if __name__ == "__main__": 
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('path_read_data', help='path_read_data')
        parser.add_argument('path_read_train', help='path_read_train') 
        parser.add_argument('path_read_test', help='path_read_test')
        parser.add_argument('path_save_model', help='path_save_model')        
        args = parser.parse_args()
        path_read_data= args.path_read_data
        path_read_train= args.path_read_train 
        path_read_test= args.path_read_test
        path_save_model= args.path_save_model 
        
    except:
        path_read_data= 'pipenv/data/data.csv' 
        path_read_train='pipenv/data/train.csv'
        path_read_test= 'pipenv/data/test.csv'
        path_save_model= 'pipenv/result/model.h5' 
    
        Training(path_read_data,
                 path_read_train,
                 path_read_test,
                 path_save_model).pipeline()