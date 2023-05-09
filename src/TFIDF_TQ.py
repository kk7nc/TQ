import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class TFIDF_TQ:
    def __init__(self, max_nb_words=75000, ngram_range=(1, 2)):
        self.max_nb_words = max_nb_words
        self.ngram_range = ngram_range
        
    def train(self, X_train):
        # create instance of TfidfVectorizer with specified parameters
        vectorizer_x = TfidfVectorizer(max_features=self.max_nb_words, ngram_range=self.ngram_range)
        
        # fit the vectorizer on input data
        vectorizer_x.fit(X_train)
        
        # save the trained vectorizer to disk using pickle
        pickle.dump(vectorizer_x, open("tfidf_5features.pickle", "wb"))
        
        # transform the input data using the trained vectorizer and convert to numpy array
        X_train = vectorizer_x.transform(X_train).toarray()
        
        # print the number of features in the transformed data
        print("tf-idf with", str(np.array(X_train).shape[1]), "features")
        
        # return the transformed data
        return X_train
    
    def test(self, X_test):
        # load the pre-trained vectorizer from disk using pickle
        with open("tfidf_5features.pickle", 'rb') as file:
            vectorizer_x = pickle.load(file)
        
        # transform the input data using the pre-trained vectorizer and convert to numpy array
        X_test = vectorizer_x.transform(X_test).toarray()
        
        # return the transformed data
        return X_test
