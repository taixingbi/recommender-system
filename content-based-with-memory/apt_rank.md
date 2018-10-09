# top rank:  
[source code](https://github.com/nestseekers/recommender-system/blob/master/apt_rank.ipynb)              
* Merge all [selected features](https://github.com/nestseekers/recommender-system/blob/master/pipenv/config.py) and generate apt rank ["apt_rank.csv"](https://github.com/nestseekers/recommender-system/blob/master/pipenv/result/apt_rank.csv).        
* In "apt_rank.csv", "apt_id" is the apt, which is assummed that the user is interested in, "rank_id" is apt ids, which is ranked already. Its type is "string", which can be easily to convert postgres table. The features and its weight can be reset to get good result. Another way to do it from traffic, please check [features improtance](https://github.com/nestseekers/recommender-system/tree/master/features_importance)        
* "ns_data_science.dump" is just demo, dumped from ["apt_rank.csv"](https://github.com/nestseekers/recommender-system/blob/master/pipenv/result/apt_rank.csv) to make sure web developer can request successfully.











