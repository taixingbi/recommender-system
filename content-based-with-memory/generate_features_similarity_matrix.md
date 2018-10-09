## generate new features:
[source code](https://github.com/nestseekers/recommender-system/blob/master/generate_features_similarity_matrix.ipynb)

Generate new features: compute every two apt similarity(match) score for each feature(e.g. 'headline'),     
There are 3 types of features: binary, continues, and special(e.g. 'geo'->'nearby'(distance based), 'headline'->['semantics similarity'](https://github.com/nestseekers/recommender-system/blob/master/text_similarity.md)) In practise, we need generate all possible useful features, even though in end some are not selected.   

#### *Binary: 
Regarding these features, only two apts have the same value, the score would be 1, otherwise 0.     
For instance: "pets" have "1: Pets Allowed 2: Pets Unknown 3: Pets No 4: Pets Case By Case".
If two apt only both is "1: Pets Allowed " , in this case, (1, 1) score is 1. otherwise (1,2),(1,3),(1,4) similarity is 0
(But actually (1,4) is more similar rather than (1,3), we could update it, if eventaully, we assume the 'pets' feature is very important)

binary feature includes: 'is_rental', 'show_price', 'is_no_fee', 'is_furnished', 'is_commercial', 'listing_type', 'is_available','list_on_web', 'is_approved', 'pets', 'is_new_development'

#### *Continues: 
For continues feature, absolute [percent deviation](http://science.halleyhosting.com/swrp/info/analysis/percentdev.htm)(abs(a-b)/a) is computed, then (1-percent deviation) as similar score.    
For example, apt A,B,C rent price is 1200, 1150, 1500, hence score(A,B)= 1- (abs(1200-1150)/1200)= .975; score(A,B)= 1- (abs(1200-1500)/1200)= .75. Hence, A is more similar to B than C in rent price feature. 

binary feature includes: 'price', 'financing_allowed', 'rent','area','num_rooms', 'num_bedrooms', 'num_bathrooms', 'common_charges', 'lot_size' 

#### *location:
This is "neaby" feature. Compare distance between every two apts.    
For instance, if the distance between apt A and apt B are 1 mile and the distance between A and C are 10 miles. Hence apt A is nearby to B rather than C. In code "p1.distance(p2)" is 2D distance between two apts. 
In apt features, even though there are other spatial features "distance, zipcode, neighborhood, region", they are related. "distance" features to measure distance have higher precision than "zipcode, neighborhood, region". Thats why other spatial features are not selected. But we could use them, becuase these features are still different. 

location feature includes: ['geo'].  

#### *text:
From [text similarity](https://github.com/nestseekers/recommender-system/blob/master/text_similarity.md), compute two document/sentense/text semantics similarity socre. The score is between (0, 1). '0'means zero semantics similarity, '1' means the same semantics similarity.    
For example     
"this apartment is great" vs "very nice apartment" score: 0.8760053    
"this apartment is great" vs "bad house" score: 0.5727214     
From above, "this apartment is great" is more similar to "very nice apartment" rather than "bad house"   

text feature includes: ['headline']. 






