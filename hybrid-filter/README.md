# hybrid recommender system 
A hybrid recommender system is a combination of multiple types of machine learning algorithms, e.g. collaborative filtering combined with content- or context-aware filtering, or both of them, in order to create a more robust model[1].             

* cold problem      
Collaborative filtering, as an example, with its cold start problem. It can be combined with content-based filtering to minimize the cold start problem[2].             

* sparsity level         
A challenge for matrix- or tensor factorization-based recommender system is that the matrix or tensor to be factorized often is very sparse[2]. For instance, a user-item rating matrix would be 99.98 % empty, and a tensor with contextual information would be empty.         

* Hybrid   
For content-based filter and collaborative filtering have their weekness. Hence, we combine them. Firstly we use [content-based KNN](https://github.com/nestseekers/recommender-system/tree/master/content-based-wtih-model) find out top n (for intance 100) most similarty apts. Then use [collaborative filtering deep leaning](https://github.com/nestseekers/recommender-system/tree/master/collaborative-filter) to predict ranking if the item got rating with sparsity level not more than 98% 



[1] C. C. Aggarwal, Recommender Systems, 1st ed. Springer International Publishing, 2016.       

[2] [A hybrid recommender system for usage within e-commerce](http://publications.lib.chalmers.se/records/fulltext/249910/249910.pdf)       

[3] [data sparsity issues in the collaborative filtering framework](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.6112&rep=rep1&type=pdf)       

[4] [Hybrid Recommender Systems: Survey and Experiments](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.88.8200&rep=rep1&type=pdf)    









