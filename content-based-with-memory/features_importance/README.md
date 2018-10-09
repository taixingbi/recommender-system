## features importance 
[source code](https://github.com/nestseekers/recommender-system/tree/master/features_importance)

In [config.py](https://github.com/nestseekers/recommender-system/blob/master/pipenv/config.py), what feature should be selected? how to rank these features as weight?   
Some users might care about 'price', others might care about 'location'. One way is we can set these parameters manually. Here another way is provided from "Traffic".  
#### traffic   
Traffic hides a lot of information. If some apts have high traffic, it means "pupular". Machine learning solution can figure out which feature cause high traffic. This is called "features importance". 
#### rondom forest
[random forest regression](https://en.wikipedia.org/wiki/Random_forest) can be used for feature selection and feature importance[[1]](https://blog.datadive.net/selecting-good-features-part-iii-random-forests/ ). The advantage of random forest could limit [overfitting](https://en.wikipedia.org/wiki/Overfitting). Also it can handle missing values(e.g. feature 'price','area'... contains so many missing values). It works well for big data sets(e.g. traffic data set)

More about it can be found in my previous task I did[[2]](https://github.com/taixingbi/email_signup_prediction/blob/master/feature%20selection%20and%20random%20forest.ipynb).


[1] https://blog.datadive.net/selecting-good-features-part-iii-random-forests/    
[2] https://github.com/taixingbi/email_signup_prediction/blob/master/feature%20selection%20and%20random%20forest.ipynb
