import TFIDF_TQ
tfidf = TFIDF_TQ()
X_train_tfidf = tfidf.train(X_train)
X_test_tfidf = tfidf.test(X_test)
