import TextCleaner
text = "This is a sample text! It contains punctuation, stop words, and HTML tags.</div>"
cleaner = TextCleaner()
cleaned_text = cleaner.clean(text, deep_clean=True, stem=True, stop_words=True, translite_rate=False)
print(cleaned_text)

