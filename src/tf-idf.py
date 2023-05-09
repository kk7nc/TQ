import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# function to train TF-IDF vectorizer on input data
def TFIDF_train(X_train, MAX_NB_WORDS=75000):
    # create instance of TfidfVectorizer with specified parameters
    vectorizer_x = TfidfVectorizer(max_features=MAX_NB_WORDS, ngram_range=(1, 2))
    
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

# function to transform test data using a pre-trained vectorizer
def TFIDF_test(X_test):
    # load the pre-trained vectorizer from disk using pickle
    with open("tfidf_5features.pickle", 'rb') as file:
        vectorizer_x = pickle.load(file)
    
    # transform the input data using the pre-trained vectorizer and convert to numpy array
    X_test = vectorizer_x.transform(X_test).toarray()
    
    # return the transformed data
    return X_test
