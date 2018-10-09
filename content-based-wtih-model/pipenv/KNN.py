import pandas as pd
import numpy as np

from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib

import config as cfg
import datetime

class Rank_apts():
    def __init__(self, path_read, path_write):
        self.path_read= path_read
        self.path_write= path_write
        self.features_selected= cfg.features
        
    def df_read(self, path_read):
        df= pd.read_csv(path_read, index_col = False)
        print(self.path_read)
        #print(df.columns)
        return df

    def df_write(self, df, path_write):
        df.to_csv(path_write, index=False)
        print(path_write)    
    
    def prepare_data(self, df):
        #reset index to make consequence 0,1,2,3,4
        df= df.reset_index()
        index2id= df['id']
        
        #get selected feature
        cols= [x[0] for x in self.features_selected]
        print(cols)
        df= df[cols]
        
        #set missing value as mean
        df= df.fillna(df.mean())       
        #df= df.dropna()
        
        #normalization 
        #col= cols[1:] #remove 'id'
        df = df/df.max().astype(np.float16)
        
        #add weight
        for col, w in self.features_selected:
            if col in cols:
                df[col]= df[col]*w
        #print(df.head())
        print(df.shape)
        return df.as_matrix(), index2id  #matrix, index map apt id #
    
    def KNN(self, X):
        nbrs = NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(X)
        start_time= datetime.datetime.now()
        distances, indices = nbrs.kneighbors(X)
        
        print("\nmodel training time taken: ", (datetime.datetime.now()-start_time), "h:m:s")
        print("this is off line training, not request\n")
        return distances, indices    
    
    def df_rank(self, indices, index2id):
        df_rank= pd.DataFrame(indices)
        df_rank= df_rank.applymap(lambda x: index2id[x])
        return df_rank    
    
    def analysis_distance(self, df_distances):
        df_distance_all_features_mean= df_distances.mean(axis=0)
        ax= df_distance_all_features_mean.plot(title="distance measure")
        ax.set_xlabel("rank")
        ax.set_ylabel("n dimentional distance")
        #return df_distance_all_features_mean 
    
    def nearest_neighbor_search(self, num_neighbors):
        df= self.df_read(self.path_read)
        X, index2id= self.prepare_data(df)
        distances, indices= self.KNN(X)
        df_rank= self.df_rank(indices, index2id) 
        df_distances= pd.DataFrame(distances)
        self.df_write(df, self.path_write)
        
        return df_rank, df_distances
if __name__ == "__main__": 
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('path_read', help='read data')
        parser.add_argument('path_write', help='write data')   
        parser.add_argument('num_nearest_neighbor', help='num_nearest_neighbor')
        args = parser.parse_args()
        path_read_features_matrix= args.path_read_features_matrix
        path_save_rank= args.path_save_rank 
        
    except:
        path_read= "pipenv/tmp/nsproperties_apt_exclusive_is_available_list_on_web_nyc_processed.csv"
        path_write= "pipenv/result/rank_nsproperties_apt_exclusive_is_available_list_on_web_nyc_processed.csv"
        num_nearest_neighbor= 100

    rnk= Rank_apts(path_read, path_write)
    df_rank, df_distances= rnk.nearest_neighbor_search(num_nearest_neighbor)
    distance_all_features_mean= rnk.analysis_distance(df_distances)