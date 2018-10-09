
# collaborative filter    

### I memory-based collaborative filtering
#### * user-item filtering         
A user-item filtering takes a particular user, find users that are similar to that user based on similarity of ratings, and recommend items that those similar users liked[1].

#### * item-item filtering      
In contrast, item-item filtering will take an item, find users who liked that item, and find other items that those users or similar users also liked. It takes items and outputs other items as recommendations[1][2].


##### * Selection of similarity metric
Here in this code, similarity metric chose Cosine for both item-based and user-based. Because we build collaborative filter from scratch. At very beginning, data is very sparse.     

More rule[3]:    
1. Use Pearson when your data is subject to user-bias/ different ratings scales of users.   
2. Use Cosine, if data is sparse (many ratings are undefined).     
3. Use Euclidean, if your data is not sparse and the magnitude of the attribute values is significant.    
4. Use adjusted cosine for Item-based approach to adjust for user-bias.  

#### * model pros and cons     
* PROS:
1. Easy to implement.     
2. Context independent.    
3. Compared to other techniques, such as content-based, it is much more accurate.       
 
* CONS:
1. Sparsity: The percentage of people who rate items is really low.       
2. Scalability: The more K neighbors we consider (under a certain threshold), the better my classification should be.  Nevertheless, the more users there are in the system, the greater the cost of finding the nearest K neighbors will be.
3. Cold-start: New users will have no to little information about them to be compared with other users.       
  New item: Just like the last point, new items will lack of ratings to create a solid ranking (More of this on ‘How to sort and rank items’)[4].    


### II model-based collaborative filtering
SVD is very classic model-based CF. It acheaves lower error than memory-based.   

### III Deep-Learning filtering     
Deep learning model is popular today. Because it performs much better than traditional methods. Neural model is from paper [5], was released in 2017. Framework is based Keras with Tensorflow as backend[6]

##### neural network model
Neural MF combines Multi-layer perceptron(MLP) and Generalized Matrix Factorisation(GMF). That is why accuracy is high.    
* User (u) and Item (i) are used to create embeddings (low-dimensional) for user and item.       
* GMF combines the two embeddings using the dot product. This is our regular matrix factorisation.      
* MLP can also create embeddings for user and items. However, instead of taking a dot product of these to obtain the rating, we can concatenate them to create a feature vector which can be passed on to the further layers[6].       
![alt text](https://nipunbatra.github.io/blog/2017/neumf.png)       

##### parametrs setting
* gradient decent:        
Gradient descent is one of the most popular algorithms to perform optimization and by far the most common way to optimize neural networks[7].    
In our code, adam is selected. Learing rate is 0.01. 
Adaptive Moment Estimation (Adam) computes adaptive learning rates for each parameter. In experiment of ResNet50 model, adam has higher accuracy[8] in fig, and here is related paper[9].              
![alt text](https://shaoanlu.files.wordpress.com/2017/05/trn_acc.png?w=788)  

* mini-batch  
Mini-batch gradient descent is a variation of the gradient descent algorithm that splits the training dataset into small batches that are used to calculate model error and update model coefficients[10].  


### IV evaluation 
from experiment:            
Item-based CF RMSE: 3.44         
User-based CF RMSE: 3.09     
User-based SVD CF MSE: 2.65       
Deep-Learning CF RMSE: 0.955          
So Deep-Learning is selected for CF model. Also prediction is so fast. 30 samples prediction only take 45 ms.        

### V dataset     
Here is [MovieLens](https://grouplens.org/datasets/movielens/100k/) in this code. Number of users is 943 and number of items is 1682. Data sparsity level is 93.7%. This is very popular public dataset, almost all collaborative filters algorithim use it as test.       

### VI more work     
we need rating window in our web, like zillow "favorite".     

### VII reference
[1] [Various Implementations of Collaborative Filtering](https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0)   
[2] [item-based collaborative filtering](http://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/itembased.html)  
[3] [Collaborative Filtering based Recommendation Systems exemplified](https://towardsdatascience.com/collaborative-filtering-based-recommendation-systems-exemplified-ecbffe1c20b1)        
[4] [Recommender Systems — User-Based and Item-Based Collaborative Filtering](https://medium.com/@cfpinela/recommender-systems-user-based-and-item-based-collaborative-filtering-5d5f375a127f)             
[5] [Neural Collaborative Filtering](https://www.comp.nus.edu.sg/~xiangnan/papers/ncf.pdf)           
[6] [neural networks for collaborative filtering](https://nipunbatra.github.io/blog/2017/neural-collaborative-filtering.html)     
[7] [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)           
[8] [SGD > Adam?? Which One Is The Best Optimizer: Dogs-VS-Cats Toy Experiment](https://shaoanlu.wordpress.com/2017/05/29/sgd-all-which-one-is-the-best-optimizer-dogs-vs-cats-toy-experiment/)       
[9] [The Marginal Value of Adaptive Gradient Methods
in Machine Learning](https://arxiv.org/pdf/1705.08292.pdf)         
[10] [Start Here Blog Topics Ebooks FAQ About Contact A Gentle Introduction to Mini-Batch Gradient Descent and How to Configure Batch Size](https://machinelearningmastery.com/gentle-introduction-mini-batch-gradient-descent-configure-batch-size/)
