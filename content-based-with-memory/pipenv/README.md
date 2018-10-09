# pipenv

This is pip env.   
Need set up pipenv and run "pipenv shell" first.    
Please check ["tmp/"](https://github.com/nestseekers/recommender-system/tree/master/pipenv/tmp), if there is csv files, it means features has been generated already. please skip step1 and step2. 

* step1: download pretrained model: "GoogleNews-vectors-negative300.bin.gz" from [here](https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download)
and put it under ["pipenv/data/"](https://github.com/taixingbi/recommender-system/tree/master/pipenv/data)     
load apt feature data and put ["/data"](https://github.com/nestseekers/recommender-system/tree/master/pipenv/data)
                     
* step2: generate apt features matrix, the generated matrix should be in ["tmp/"](https://github.com/nestseekers/recommender-system/tree/master/pipenv/tmp), do not need to run again.          
run:  $ python generate_features_similarity_matrix.py path_nsproperties_apt path_preTrained_wv_model path_save_features_matrix

```
$ time python generate_features_similarity_matrix.py data/nsproperties_apt_exclusive_is_available_list_on_web_nyc.csv" 'data/GoogleNews-vectors-negative300.bin.gz' 'tmp/'      
```

* step3: generate [apt rank](https://github.com/nestseekers/recommender-system/blob/master/pipenv/result/apt_rank.csv). features seletion and weight setting can be modified in [config.py](https://github.com/nestseekers/recommender-system/blob/master/pipenv/config.py).       
run : $ python apt_rank.py path_read_features_matrix path_save_rank     

```
$ python apt_rank.py 'tmp/' 'result/'
```





