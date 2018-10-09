#https://nipunbatra.github.io/blog/2017/neural-collaborative-filtering.html
#https://www.comp.nus.edu.sg/~xiangnan/papers/ncf.pdf
import keras
class DeepLearning():
    def __init__(self, n_users, n_items):
        self.n_users= n_users
        self.n_items= n_items

    def cnn(self):
        n_users= self.n_users
        n_items= self.n_items

        n_latent_factors_user = 8
        n_latent_factors_movie = 10
        n_latent_factors_mf = 3

        movie_input = keras.layers.Input(shape=[1],name='Item')
        movie_embedding_mlp = keras.layers.Embedding(n_items + 1, n_latent_factors_movie, name='Item-Embedding-MLP')(movie_input)
        movie_vec_mlp = keras.layers.Flatten(name='FlattenItems-MLP')(movie_embedding_mlp)
        movie_vec_mlp = keras.layers.Dropout(0.2)(movie_vec_mlp)

        movie_embedding_mf = keras.layers.Embedding(n_items + 1, n_latent_factors_mf, name='Movie-Embedding-MF')(movie_input)
        movie_vec_mf = keras.layers.Flatten(name='FlattenItems-MF')(movie_embedding_mf)
        movie_vec_mf = keras.layers.Dropout(0.2)(movie_vec_mf)

        user_input = keras.layers.Input(shape=[1],name='User')
        user_vec_mlp = keras.layers.Flatten(name='FlattenUsers-MLP')(keras.layers.Embedding(n_users + 1, n_latent_factors_user,name='User-Embedding-MLP')(user_input))
        user_vec_mlp = keras.layers.Dropout(0.2)(user_vec_mlp)

        user_vec_mf = keras.layers.Flatten(name='FlattenUsers-MF')(keras.layers.Embedding(n_users + 1, n_latent_factors_mf,name='User-Embedding-MF')(user_input))
        user_vec_mf = keras.layers.Dropout(0.2)(user_vec_mf)

        concat = keras.layers.concatenate([movie_vec_mlp, user_vec_mlp], name='Concat')
        concat_dropout = keras.layers.Dropout(0.2)(concat)
        dense = keras.layers.Dense(200,name='FullyConnected')(concat_dropout)
        dense_batch = keras.layers.BatchNormalization(name='Batch')(dense)
        dropout_1 = keras.layers.Dropout(0.2,name='Dropout-1')(dense_batch)
        dense_2 = keras.layers.Dense(100,name='FullyConnected-1')(dropout_1)
        dense_batch_2 = keras.layers.BatchNormalization(name='Batch-2')(dense_2)

        dropout_2 = keras.layers.Dropout(0.2,name='Dropout-2')(dense_batch_2)
        dense_3 = keras.layers.Dense(50,name='FullyConnected-2')(dropout_2)
        dense_4 = keras.layers.Dense(20,name='FullyConnected-3', activation='relu')(dense_3)

        pred_mf = keras.layers.concatenate([movie_vec_mf, user_vec_mf])
        pred_mlp = keras.layers.Dense(1, activation='relu',name='Activation')(dense_4)

        combine_mlp_mf = keras.layers.concatenate([pred_mf, pred_mlp],name='Concat-MF-MLP')
        result_combine = keras.layers.Dense(100,name='Combine-MF-MLP')(combine_mlp_mf)
        deep_combine = keras.layers.Dense(100,name='FullyConnected-4')(result_combine)

        result = keras.layers.Dense(1,name='Prediction')(deep_combine)

        model = keras.Model([user_input, movie_input], result)
        opt = keras.optimizers.Adam(lr =0.01)
        model.compile(optimizer='adam',loss= 'mean_absolute_error')
        model.summary()
        
        return model