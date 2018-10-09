# pipenv

This is pip env.   
Need set up pipenv and run "pipenv shell" first.    
                     
* step1: do data preprocessing      

```
$ time python data_preprocessing.py path_read_apt_features path_write    
```

* step2: generate rank apts      

```
$ python KNN.py path_read path_write num_nearest_neighbor
```





