#time python generate_features_similarity_matrix.py "data/nsproperties_apt_exclusive_is_available_list_on_web_nyc.csv" 'data/GoogleNews-vectors-negative300.bin.gz' 'tmp/'

import pandas as pd
import numpy as np
from numpy import genfromtxt
from shapely import wkb
import datetime
import argparse

import text_similarity as text_sim #check pair_doc_similarity.py

class apt_features_similarity():
    def __init__(self, path_nsproperties_apt, path_preTrained_wv_model, path_save_features_matrix):
        self.path_nsproperties_apt= path_nsproperties_apt
        self.path_preTrained_wv_model= path_preTrained_wv_model
        self.path_save_features_matrix= path_save_features_matrix
        
    def pipeline(self):
        df= self.read_nsproperties_apt()
        self.apt_features_sim(df)
    
    def read_nsproperties_apt(self):
        df= pd.read_csv(self.path_nsproperties_apt, index_col = False)
        #df= df[df['city_id']==1.0]# new york
        print(df.shape)
        #print all apt features
        print(df.columns)
        return df

    def apt_features_sim(self, df):
        def sim_text(class_text_sim, a, b):
            if a and b:
                try:
                    score= class_text_sim.doc_similarity(a, b)
                    return score
                except:
                    return np.nan
            else: return np.nan         
        
        def sim_binary(a, b):
            if a==np.nan or b==np.nan: return np.nan
            if a==b:  return 1
            if a!=b:  return 0 

        def sim_continues(a, b):
            # abs(a-b)/a: percent deviation
            if a and b:  return 1 - ( abs(a-b)/a )
            else: return np.nan
        
        def sim_location(a, b):
            if a and b:
                try:
                    p1, p2= wkb.loads(a, hex=True), wkb.loads(b, hex=True)
                    ##p1.distance(p2): 2D distance
                    nearby= 1-p1.distance(p2)
                    return nearby
                except: return np.nan
            else: return np.nan
        
        def get_sim_matrix(df, col, category, path_save):
            l= df[col].tolist()
            n= len(l)
            m = np.empty((n,n,))
            m[:] = np.nan
            
            if category=='text': 
                #loading word2vec pretained model for text similarity
                class_text_sim= text_sim.pairDoc(self.path_preTrained_wv_model)
                
            for i in range(n): #row
                for j in range(n): 
                    if category=='binary': m[i][j]= sim_binary(l[i], l[j])
                    if category=='continues': m[i][j]= sim_continues(l[i], l[j])
                    if category=='location': m[i][j]= sim_location(l[i], l[j])
                    if category=='text': m[i][j]= sim_text(class_text_sim, l[i], l[j])
                        
            m[np.isnan(m)]= -0.0001
            np.savetxt(path_save, m, delimiter=",")
            #genfromtxt(path_save, delimiter=',') # numpy read array
            return m

        def generate_apt_sim_matrix(cols, category):
            for col in cols:
                path_save= self.path_save_features_matrix + col + '.csv'
                get_sim_matrix(df, col, category, path_save) 
                print(path_save)
        
        def generate_apt_id(df):
            path_save_index= self.path_save_features_matrix + 'apt_id.csv'
            df.to_csv(path_save_index, index=False)
            print(path_save_index)        
        
        features_binary= ['is_rental', 'show_price', 'is_no_fee', 'is_furnished', 'is_commercial', 'listing_type', 'is_available','list_on_web',
         'is_approved', 'pets', 'is_new_development']
        features_continues= ['price', 'financing_allowed', 'rent','area','num_rooms', 'num_bedrooms', 
        'num_bathrooms', 'common_charges', 'lot_size']   
        features_loc= ['geo']
        features_text= ['headline']        
        
        start_time= datetime.datetime.now()
        generate_apt_sim_matrix(features_text, 'text')
        print("\ntext training time taken: ", (datetime.datetime.now()-start_time), "h:m:s \n")
        
        generate_apt_sim_matrix(features_continues, 'continues')
        generate_apt_sim_matrix(features_binary, 'binary')
        generate_apt_sim_matrix(features_loc, 'location')    
        generate_apt_id(df)
  
if __name__ == "__main__":       
    try:
        print("training start ...")
        parser = argparse.ArgumentParser()
        parser.add_argument('path_nsproperties_apt', help='input nsproperties_apt')
        parser.add_argument('path_preTrained_wv_model', help='input path_preTrained_wv_model')        
        parser.add_argument('path_save_features_matrix', help='output features matrix')    
        args = parser.parse_args()

        path_nsproperties_apt= args.path_nsproperties_apt
        path_preTrained_wv_model= args.path_preTrained_wv_model
        path_save_features_matrix= args.path_save_features_matrix 
        print(path_nsproperties_apt)
    except:
        path_nsproperties_apt= "pipenv/data/nsproperties_apt_exclusive_is_available_list_on_web_nyc.csv"
        path_preTrained_wv_model= 'pipenv/data/GoogleNews-vectors-negative300.bin.gz'
        path_save_features_matrix= 'pipenv/tmp/'    
    
    
    apt_features_similarity(path_nsproperties_apt, path_preTrained_wv_model, path_save_features_matrix).pipeline()
    print("done")

