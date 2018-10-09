# content-based recommender system with model   
Content-based recommenders are capable of recommending items not yet rated by any user to fix cold start problem[9]. 
K-nearest neighbor is a very simple machine learning algorithm, which finds the k most similar items to a particular instance based on a given distance metric like euclidean, jaccard similarity[10].   

### [data preprocessing](https://github.com/nestseekers/recommender-system/blob/master/content-based-wtih-model/data_preprocessing.ipynb)
1. convert string 't' and 'f' to binary number   
2. extract longitude and latitude from feature "geo"

### [KNN](https://github.com/nestseekers/recommender-system/blob/master/content-based-wtih-model/KNN.ipynb)    
#### prepare data
1. select apts features for search nearest neighbors       
2. set missing value as mean value[1]        
3. normalizing the features, gives every attribute the same influence in identifying neighbors when computing certain type of distances[2]. z-score normalization is selected[4].    
4. add weight for each feature    
#### knn model parameters           
use KNN model to find out k nearest apts.         
1.  Similarty Metrics     
cosine-based is used by item knn(because Pearson correlation coefficient is used to measure the extent to which two  variables linearly relate with each other, usually it is for similarity between two users)[3].      
2. Distance Metrics.     
For simplicity, Euclidean distance is selcted. Euclidean is a good distance measure to use if the input variables are similar in type (e.g. all measured widths and heights). Manhattan distance is a good measure to use if the input variables are not similar in type (such as age, height, etc…). For categorical attribute distances: we allow the use of two distances: Hamming distance and the Weighted Hamming distance. For binary attribute distances, Jaccard distance works[2].     

### [evalutation](https://github.com/nestseekers/recommender-system/blob/master/content-based-wtih-model/evaluation.ipynb)
RMSE with MRR weight is used to evaluate item-based ranking.    

* [Root Mean Squared Error (RMSE)](https://en.wikipedia.org/wiki/Root-mean-square_deviation)          
RMSE is perhaps the most popular metric used in evaluating accuracy of predicted recommender system[5][6].[Mean absolute error(MAE)](https://en.wikipedia.org/wiki/Mean_absolute_error) is another measure and easy to explain error. But in RMSE, large error will be panelized. So it is better[7].      

* [mean reciprocal rank(MRR)](https://en.wikipedia.org/wiki/Mean_reciprocal_rank)         
MRR only takes into account where the top n relevant result occurs[8]. For instance, the users probably only watch top 5-10 listing.    

### model analysis    
KNN   
* Advantages   
effective if the training data is large     

* Disadvantages:      
1. sensitive to noise(since it is based on the Euclidean distance), tend to overfitting.    
2. need to determine value of parameter k.   
3. distance based learning is not clear.  
4. computation cost is quite high, because need to compute distance of each query distance to all training sample. 

### reference   
[1] [Missing Value Treatment](http://r-statistics.co/Missing-Value-Treatment-With-R.html)      
[2] [The use of KNN for missing values](https://towardsdatascience.com/the-use-of-knn-for-missing-values-cf33d935c637)       
[3] [A Ranking based Recommender System for Cold Start & Data Sparsity Problem](https://zapdf.com/a-ranking-based-recommender-system-for-cold-start-amp-data-s.html)     
[4] [about feature scaling and normalization](https://sebastianraschka.com/Articles/2014_about_feature_scaling.html)     
[5] [Evaluating Recommendation Systems](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/EvaluationMetrics.TR_.pdf)        
[6] [KNN: K-Nearest Neighbors Essentials](http://www.sthda.com/english/articles/35-statistical-machine-learning-essentials/142-knn-k-nearest-neighbors-essentials/)   
[7] [MAE and RMSE — Which Metric is Better?](https://medium.com/human-in-a-machine-world/mae-and-rmse-which-metric-is-better-e60ac3bde13d)      
[8] [Evaluating Recommender Systems: Ensuring Replicability of Evaluation](https://pdfs.semanticscholar.org/presentation/d403/1e2ab5b109fbf69f7e42386534541dc3f2aa.pdf)     
[9] [Content-based Recommender Systems: State of
the Art and Trends](http://facweb.cs.depaul.edu/mobasher/classes/ect584/Papers/ContentBasedRS.pdf)      
[10][Recommending Animes Using Nearest Neighbors](https://medium.com/learning-machine-learning/recommending-animes-using-nearest-neighbors-61320a1a5934)







