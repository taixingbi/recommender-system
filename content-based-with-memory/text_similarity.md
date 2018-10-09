## text similarty:    
[soure code](https://github.com/nestseekers/recommender-system/blob/master/text_similarity.ipynb)    
Compute two document/sentense/text semantics similarity socre. The score is between (0, 1). '0'means zero semantics similarity, '1' means the same semantics similarity. 
For example        
"this apartment is great"  vs  "very nice apartment"  score:  0.8760053 
"this apartment is great"  vs  "bad house"  score:  0.5727214
From above, "this apartment is great" is more similar to "very nice apartment" rather than "bad house"

* The algorithm is unsupervised machine learning, from "word2vec" to "doc2vec" [[1]](https://cs.stanford.edu/~quocle/paragraph_vector.pdf) [[2]](https://radimrehurek.com/gensim/models/word2vec.html), based on pre-trained model with "GoogleNews-vectors-negative300.bin.gz". This is not "word frequency" method like tf-idf[[3]](https://towardsdatascience.com/overview-of-text-similarity-metrics-3397c4601f50). Because "headline" is always short, "tf-idf" does not work well. For long sentense, like "Description", "tf-idf" could be as weight for each word above[[4]](http://nadbordrozd.github.io/blog/2016/05/20/text-classification-with-word2vec/).

* This algorithm is about [semantics similarity](https://en.wikipedia.org/wiki/Semantic_similarity), it can also avoid "word position change", and it peformances well for short text. Another benifit is the algorithm work for either sentense or multi-sentense. But if text is too long, it performs not well. LSI[[5]](http://mccormickml.com/2016/11/04/interpreting-lsi-document-similarity/) is suggested.      
"word position change" example:
"this apartment is great", "apartment" postion is 1
"very nice apartment", "apartment" postion is 2     


## reference           

[1] https://cs.stanford.edu/~quocle/paragraph_vector.pdf   
[2] https://radimrehurek.com/gensim/models/word2vec.html   
[3] https://towardsdatascience.com/overview-of-text-similarity-metrics-3397c4601f50   
[4] http://nadbordrozd.github.io/blog/2016/05/20/text-classification-with-word2vec/     
[5] http://mccormickml.com/2016/11/04/interpreting-lsi-document-similarity/






