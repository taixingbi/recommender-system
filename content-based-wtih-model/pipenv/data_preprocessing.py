import pandas as pd
import numpy as np
from shapely import wkb

class data_prepocessing():
    def __init__(self, path_read, path_write):
        self.path_read= path_read
        self.path_write= path_write
        
    def str2number(self, df, col):
        df= df.applymap(lambda x: 1 if x == 't' else x)
        df= df.applymap(lambda x: 0 if x == 'f' else x)
        return df

    def geo2xy(self, df):
        def f_x(x):
            p= wkb.loads(x, hex=True)
            return p.x

        def f_y(x):
            p= wkb.loads(x, hex=True)
            return p.y

        df['x']= df['geo'].apply(f_x)
        df['y']= df['geo'].apply(f_y)
        df['xy']= df['x']*df['y']

        return df
    
    def df_read(self, path_read):
        df= pd.read_csv(path_read, index_col = False)
        print(path_read)
        return df
    
    def df_write(self, df, path_write):
        df.to_csv(path_write, index=False)
        print(path_write)
        
    def rent_or_sales(self, df):
        df_rent= df[ df['is_rental']==1 ]
        df_sale= df[ df['is_rental']==0 ]
        
        path_write_rent= "pipenv/data/nsproperties_apt_exclusive_is_available_list_on_web_nyc_rent.csv"
        path_write_sale= "pipenv/data/nsproperties_apt_exclusive_is_available_list_on_web_nyc_sale.csv"        
        self.df_write(df_rent, path_write_rent)
        self.df_write(df_sale, path_write_sale)
        return df_rent, df_sale
    
    def pipeline(self):
        df= self.df_read(self.path_read)
        
        # 't'->1 'f'->0
        features_bins= ['is_rental', 'is_no_fee', 'is_furnished', 'is_commercial', 'is_available', 
                        'is_approved', 'is_new_development']
        df= self.str2number(df, features_bins)  
        
        #generate x, y 
        df= self.geo2xy(df)

        self.df_write(df, self.path_write)
        #filter by 'is_rental'
        #df_rent, df_sale= self.rent_or_sales(df)
        #return df_rent, df_sale

if __name__ == "__main__": 
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('path_read_apt_features', help='read apts data')
        parser.add_argument('path_write', help='write data')          
        args = parser.parse_args()
        path_read_features_matrix= args.path_read_features_matrix
        path_save_rank= args.path_save_rank 
        
    except:
        path_read_apt_features= "pipenv/data/nsproperties_apt_exclusive_is_available_list_on_web_nyc.csv"
        path_write= "pipenv/tmp/nsproperties_apt_exclusive_is_available_list_on_web_nyc_processed.csv"        
        
    data_prepocessing(path_read_apt_features, path_write).pipeline()