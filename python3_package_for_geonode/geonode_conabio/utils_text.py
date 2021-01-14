import unicodedata

def normalize_name_classes(string):
    if string:
        return unicodedata.normalize('NFKD', string).encode('ASCII','ignore').decode('utf-8')