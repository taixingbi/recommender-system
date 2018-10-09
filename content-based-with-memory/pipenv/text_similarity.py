import pandas as pd
import numpy as np
import gensim
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

import datetime

import nltk
nltk.download('stopwords')

class pairDoc():
    def __init__(self, path_pretained_model= 'data/GoogleNews-vectors-negative300.bin.gz'):
        start_time= datetime.datetime.now()
        
        print("googlenews model start loading...")
        #load pretained google pretained model, this could take a few minutes
        self.model_wv = gensim.models.KeyedVectors.load_word2vec_format( path_pretained_model, binary=True )
        print("googlenews model load done")
        
        delta= datetime.datetime.now()-start_time
        print("\nloading model time taken: ", delta, "h:m:s \n")        
        
        #load stop words
        self.stop_words= stopwords.words('english')

    def doc_similarity(self, doc1, doc2):
        def doc_vector(doc):
            def tokenize_doc(doc):
                #tokenize document
                tokens= TweetTokenizer() .tokenize(doc)
                #token sentense, remove number, stop word and lower case 
                token= [ token.lower() for token in tokens if token.isalpha() and token not in self.stop_words ] 
                return token

            def wv2dv(words):#word vector to document vector
                #if word not in vocab of google pretained model, then ignore it
                words= [ word for word in words if word in self.model_wv.vocab ]
                #average all words with 300 dimentional features
                doc_vec = sum( self.model_wv[word] for word in words) / len(words)
                return doc_vec

            words= tokenize_doc(doc)
            return wv2dv(words)

        def cosine_sim(u, v):
            #cosine similarity  cos sim= u * v* cos(u^v) 
            return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

        return cosine_sim( doc_vector(doc1), doc_vector(doc2) )        

if __name__ == "__main__":   
    path_pretained_model= 'data/GoogleNews-vectors-negative300.bin.gz'
    p= pairDoc(path_pretained_model)

    def pair_doc_similarity_score(pair):
        print(pair[0], " vs ", pair[1])
        score= p.doc_similarity(pair[0], pair[1])
        print( "score: ", score, "\n")
    
    #---------------------------test cases---------------------------
    #test special char with number, stop word, and in vocab of google pretained model (for example, cooool)
    pair = ["This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--",  "This is really nice apt"]    
    pair_doc_similarity_score(pair)

    #test postive semantics, words' position changes 
    pair= ["this apartment is great", "very nice apartment"]
    pair_doc_similarity_score(pair)

    #test nagative semantics
    pair= ["this apartment is great", "bad house"]
    pair_doc_similarity_score(pair)



