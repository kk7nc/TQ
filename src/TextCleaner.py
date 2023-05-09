import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from transliterate import translit

class TextCleaner:
    def __init__(self):
        self.rules = [
            {r'>\s+': u'>'},  # remove spaces after a tag opens or closes
            {r'\s+': u' '},  # replace consecutive spaces
            {r'\s*<br\s*/?>\s*': u'\n'},  # newline after a <br>
            {r'</(div)\s*>\s*': u'\n'},  # newline after </p> and </div> and <h1/>...
            {r'</(p|h\d)\s*>\s*': u'\n\n'},  # newline after </p> and </div> and <h1/>...
            {r'<head>.*<\s*(/head|body)[^>]*>': u''},  # remove <head> to </head>
            {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},  # show links instead of texts
            {r'[ \t]*<[^<]*?/?>': u''},  # remove remaining tags
            {r'^\s+': u''}  # remove spaces at the beginning
        ]

    def clean(self, text, deep_clean=False, stem=False, stop_words=True, translite_rate=False):
        for rule in self.rules:
            for (k, v) in rule.items():
                regex = re.compile(k)
                text = regex.sub(v, text)
            text = text.rstrip()
            text = text.strip()

        if deep_clean:
            text = text.replace(".", "")
            text = text.replace("[", " ")
            text = text.replace(",", " ")
            text = text.replace("]", " ")
            text = text.replace("(", " ")
            text = text.replace(")", " ")
            text = text.replace("\"", "")
            text = text.replace("-", " ")
            text = text.replace("=", " ")
            text = text.replace("?", " ")
            text = text.replace("!", " ")
            text = text.replace('+', ' ').replace('.', ' ').replace(',', ' ').replace(':', ' ')

            text = re.sub("(^|\W)\d+($|\W)", " ", text)
            if translite_rate:
                text = translit(text, 'ru', reversed=True)
            if stem:
                text = PorterStemmer().stem(text)
            else:
                text = WordNetLemmatizer().lemmatize(text)
            if stop_words:
                stop_words = set(stopwords.words('english'))
                word_tokens = word_tokenize(text)
                text = [w for w in word_tokens if not w in stop_words]
                text = ' '.join(str(e) for e in text)
        return text.lower()
