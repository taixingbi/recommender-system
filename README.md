## Task:    
In [home page](https://www.nestseekers.com/sales/manhattan/). When the user click [one apt](https://www.nestseekers.com/924598/cielo-4-br-apartment-upper-east-side-manhattan-ny) and stay here for a while(set time threshold to make sure the user is really intested in this apt ), the user go back home page [home page](https://www.nestseekers.com/sales/manhattan/), where need reset listing show. The rank listing need to match the apt(features), which the user just clicked.  

## Background:
1. One of issues about "recommender system" before is we do apt recommended listings in [apt page](https://www.nestseekers.com/924598/cielo-4-br-apartment-upper-east-side-manhattan-ny), but the user contact the same agents in [apt page](https://www.nestseekers.com/924598/cielo-4-br-apartment-upper-east-side-manhattan-ny) when they go to recommended new apt page [for example](https://www.nestseekers.com/944185/the-crown-condominium-3-br-condo-harlem-manhattan-ny), where agent is different.
2. Improve recommender algorithm.

## algorithim    
* [content-based-with-memory](https://github.com/nestseekers/recommender-system/tree/master/content-based-with-memory) and [content-based-wtih-model](https://github.com/nestseekers/recommender-system/tree/master/content-based-wtih-model) are both content-based.           
  
* In [collaborative-filter](https://github.com/nestseekers/recommender-system/tree/master/collaborative-filter), [deep learning](https://github.com/nestseekers/recommender-system/tree/master/collaborative-filter/pipenv) is recommended.     

* Due to both algorithm above have their weekness, [hybrid-filter](https://github.com/nestseekers/recommender-system/tree/master/hybrid-filter), combine content-based and collaborative filtering is finally used. Firstly we use [content-based KNN](https://github.com/nestseekers/recommender-system/tree/master/content-based-wtih-model) find out top n (for intance 100) most similarty apts. Then use [collaborative filtering with deep leaning](https://github.com/nestseekers/recommender-system/tree/master/collaborative-filter) to predict ranking if the item got rating with sparsity level not more than 98% 


## WE DO NEED "RATING" window in our website.   











