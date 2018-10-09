# content-based with memory    
    
First we do simple analysis for apts features. Then generate usefull new features, for instance, 'geo'->'nearby'(distance based), 'headline'->['semantics similarity'](https://github.com/nestseekers/recommender-system/blob/master/text_similarity.md). After that, [config.py](https://github.com/nestseekers/recommender-system/blob/master/pipenv/config.py) do "feature selection" and "feature importance"(weight). Another way is [features importance](https://github.com/nestseekers/recommender-system/tree/master/features_importance). In the end, merge all apt features and get final [apt rank](https://github.com/nestseekers/recommender-system/blob/master/pipenv/result/apt_rank.csv)
as csv.
* [apt features analysis](https://github.com/nestseekers/recommender-system/blob/master/apt_features_analysis.ipynb)
* [generate new features](https://github.com/nestseekers/recommender-system/blob/master/generate_features_similarity_matrix.md)                 
* [features importance](https://github.com/nestseekers/recommender-system/tree/master/features_importance)         
* [apt rank](https://github.com/nestseekers/recommender-system/blob/master/apt_rank.md)
* [pipenv](https://github.com/nestseekers/recommender-system/tree/master/pipenv)










