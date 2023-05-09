import re
from pathlib import Path
import csv

class TQ_Dictionary:
    def __init__(self, dictionary_file='Dic.csv'):
        self.dictionary = self._load_dictionary(dictionary_file)
    
    def _load_dictionary(self, dictionary_file):
        script_location = Path(__file__).absolute().parent
        dictionary_file = script_location/dictionary_file
        dic = {}
        with open(str(dictionary_file), 'r') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            next(data, None)  # skip header
            for row in data:
                dic[row[3]] = row[1]
        return dic
    
    def translate(self, input_text):
        str_out = input_text.split(" ")
        j = 0
        for _str in str_out:
            _str = re.sub('[^a-zA-Z0-9-_+/.]', '', _str).lower()
            _str = _str.replace(",", " ")
            _str = _str.replace(".", " ")
            if _str in self.dictionary:
                str_out[j] = self.dictionary[_str]
            j = j + 1
        out = ' '.join(str_out)
        return out
