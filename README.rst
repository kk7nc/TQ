|DOI| |arxiv| |GitHublicense| |twitter|

Objectives
----------

To compare the ability of a natural language processing (NLP) model to an existing human workflow in predictively identifying tertiary and quaternary (TQ) cases for transfer requests to an academic health center (AHC).

Materials and Methods
------------------------
Data on interhospital transfers were queried from the electronic health record (EHR) for the 6-month period from 7/1/2020 – 12/31/2020.
The NLP model was allowed to generate predictions on the same cases as the human predictive workflow during the study period.
These predictions were then retrospectively compared to the true TQ outcomes.


Results
------------

There were 1895 transfer cases labeled by both the human predictive workflow and the NLP model, all of which had retrospective confirmation of the true TQ label.
The NLP model Receiver Operating Characteristic (ROC) curve had an area under the curve (AUC) of 0.91.
Using a model probability threshold of >0.3 to be considered TQ positive, accuracy was 81.5% for the NLP model vs. 80.3% for the human predictions (p = 0.198) while sensitivity was 84% vs. 68% (p < .001).


Discussion
------------

The NLP model was as accurate as the human workflow but significantly more sensitive. This translated to 15.9% more TQ cases identified by the NLP model.
Conclusion

Integrating an NLP model into existing workflows as automated decision support could translate to more TQ cases identified at the onset of the transfer process.
In other words, the NLP model was able to identify TQ cases with greater sensitivity than the human workflow. This means that the NLP model was more likely to identify TQ cases that were missed by the human workflow. This could be a significant improvement in patient care, as it could lead to earlier identification and treatment of TQ cases.

Referenced paper : `Evaluating the Predictive Ability of NLP in Identifying Tertiary/Quaternary Cases in Prioritization Workflows for Interhospital Transfer <https://link.org/abs/>`__


Code Explanation
-----------------

.. code:: python

   import TextCleaner
   text = "This is a sample text! It contains punctuation, stop words, and HTML tags.</div>"
   cleaner = TextCleaner()
   cleaned_text = cleaner.clean(text, deep_clean=True, stem=True, stop_words=True, translite_rate=False)
   print(cleaned_text)


.. code:: python

   import TQ_Dictionary

   dictionary = TQ_Dictionary('Dic.csv')
   input_text = "AHF" # AHF is an abbreviation for "Acute Heart Failure," a medical condition characterized by the sudden onset or worsening of symptoms of heart failure.
   translated_text = dictionary.translate(input_text)
   print(translated_text)


.. code:: python

   import TFIDF_TQ
   tfidf = TFIDF_TQ()
   X_train_tfidf = tfidf.train(X_train)
   X_test_tfidf = tfidf.test(X_test)
   
.. code:: python

   nModel = 9
   X_train_tfidf = TFIDF_train(X_train)
   X_test_tfidf  = TFIDF_test(X_test)
   predicted = np.zeros((len(y_test),2)).astype(float)
   for i in range(0,nModel):
       model_DNN = Build_Model_DNN_Text(X_train_tfidf.shape[1], 2,i)

       model_DNN.fit(X_train_tfidf, y_train,
                                     validation_data=(X_test_tfidf, y_test),
                                     epochs=120,
                                     batch_size=64,
                                     verbose=2)

       predicted =  predicted +np.array(model_DNN.predict(X_test_tfidf)).astype(float)
     predicted = predicted/float(nModel)



.. |PowerPoint| image:: https://img.shields.io/badge/Presentation-download-red.svg?style=flat
   :target: https://github.com/kk7nc/TQ
.. |researchgate| image:: https://img.shields.io/badge/ResearchGate-RMDL-blue.svg?style=flat
   :target: https://www.researchgate.net/publicatio
.. |pdf| image:: https://img.shields.io/badge/pdf-download-red.svg?style=flat
   :target: https://github.com/kk7nc/RMDL/blob/master/docs/ACM-RMDL.pdf
.. |GitHublicense| image:: https://img.shields.io/badge/licence-MIT-blue.svg
   :target: ./LICENSE
.. |DOI| image:: https://img.shields.io/badge/DOI-10.1111/11111.111111-blue.svg?style=flat
   :target: https://doi.org/10.1145/
.. |arxiv| image:: https://img.shields.io/badge/arXiv-1805.01890-red.svg
    :target: https://arxiv.org/abs/xxxx.xxxx
.. |twitter| image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social
    :target: https://twitter.com/intent/tweet?text=Evaluating%20the%20Predictive%20Ability%20of%20NLP%20in%20Identifying%20Tertiary/Quaternary%20Cases%20in%20Prioritization%20Workflows%20for%20Interhospital%20Transfer%0aGitHub:&url=https://github.com/kk7nc/TQ&hashtags=TransferCenter,Hospital,TQ,DeepLearning,classification,MachineLearning,deep_neural_networks,EnsembleLearning
