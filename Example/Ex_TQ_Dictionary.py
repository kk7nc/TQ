import TQ_Dictionary

dictionary = TQ_Dictionary('Dic.csv')
input_text = "AHF" # AHF is an abbreviation for "Acute Heart Failure," a medical condition characterized by the sudden onset or worsening of symptoms of heart failure.
translated_text = dictionary.translate(input_text)
print(translated_text)
