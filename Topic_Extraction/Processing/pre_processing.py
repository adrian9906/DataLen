import string
from nltk.tokenize import word_tokenize


def preprocess_data(documents,stopwords):
    stopwords+=string.punctuation
 
        # Tokenize and remove stopwords
    tokens = word_tokenize(documents)
    tokenfonal=[[token] for token in tokens if token not in stopwords]
    
    return tokenfonal