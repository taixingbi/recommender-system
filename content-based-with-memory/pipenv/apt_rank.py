#python apt_rank.py 'tmp/' 'result/'
import pandas as pd
import numpy as np
from numpy import genfromtxt
import config as cfg
import argparse

class apt_similarity():
    def __init__(self, path_read_features_matrix, path_save_rank):
        self.path_read_features_matrix= path_read_features_matrix
        self.path_save_rank= path_save_rank
        self.features= cfg.features
        print("apt features weight:")
        for fea, weight in self.features:
            print(fea, weight)
            
    def pipeline(self):
        def read_apt_features(col):
            full_path_read_features_matrix= self.path_read_features_matrix + col + '.csv'
            return genfromtxt(full_path_read_features_matrix, delimiter=',')

        def read_apt_id():
            full_path_read_apt_id= self.path_read_features_matrix +'apt_id.csv'            
            return pd.read_csv(full_path_read_apt_id)
        
        def save_apt_sim(df_sim):
            full_path_save_rank= self.path_save_rank + 'apt_rank.csv'
            df_sim.to_csv(full_path_save_rank, index=False)
            print(full_path_save_rank)
        
        features= self.features
        fea_sum= read_apt_features(features[0][0]) * features[0][1] # similarity * weight
        for fea in features[1:]:
            fea_sum += read_apt_features(fea[0])*fea[1]

        mean= fea_sum/len(features)
        df_sim= pd.DataFrame(mean)

        #df_sim.head()
        df_index= read_apt_id()
        map_id= {i: id  for i, id in enumerate( df_index['id'].tolist() ) } 
        df_sim= df_sim.rename(index=map_id, columns= map_id)
        
        
        #csv for postgres
        def func(row):
            rank= row.sort_values(ascending=False)
            s= ",".join( str(x) for x in rank.index.values.tolist() if x!= row.name)
            return s
        df_sim['rank_id']= df_sim.apply(func)
        df_sim['apt_id'] = df_sim.index.astype('str')
        df_post= df_sim[['apt_id','rank_id']] 
        print( df_post[:5][:3] )
        
        save_apt_sim(df_post)
        
        return df_sim

class test_sim_apt():
    def __init__(self, df_sim, apt_id):
        self.df_sim= df_sim
        self.apt_id= apt_id

    def pipeline(self):
        id= self.apt_id
        df_rank= self.df_sim.sort_values(by=[id], ascending=False)[id]
        df_rank= df_rank.reset_index()
        def func(row):
            return  'https://www.nestseekers.com/' + str(row)

        df_rank['link']= df_rank['index'].apply(func)
        return df_rank
    
if __name__ == "__main__": 
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('path_read_features_matrix', help='path_read_features_matrix')
        parser.add_argument('path_save_rank', help='path_save_rank')          
        args = parser.parse_args()
        path_read_features_matrix= args.path_read_features_matrix
        path_save_rank= args.path_save_rank 
        
    except:
        path_read_features_matrix= 'pipenv/tmp/'
        path_save_rank= 'pipenv/result/'


    df_sim= apt_similarity(path_read_features_matrix, path_save_rank).pipeline()
    
    #id= 895091
    apt_id= 894458
    rank= test_sim_apt(df_sim, apt_id).pipeline()
    print(rank[:10])
    print("all done")