from symbol import term
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models.ldamodel import LdaModel
import spacy

from Topic_Extraction.Processing.pre_processing import preprocess_data


def ldaTopicExtraction(processData,nlp:spacy,wordList):

    id2word = corpora.Dictionary(processData)
    
    corpus = [id2word.doc2bow(text) for text in processData]

    num_topics = 10
    
    termsList = []
    
    lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=num_topics, random_state=42, passes=10, alpha="auto", per_word_topics=True)
    
    for i in range(num_topics):
        terms = lda_model.show_topic(i, topn=10)  
        termsList+=[term for term in terms]
    
    termsList = sorted(termsList,key=lambda x: x[1])
    
    termFinal=[]
    
    for word in wordList:
        wordSpacy=nlp(word)
        for terms in termsList:
            similar=nlp(terms[0])
            if wordSpacy.similarity(similar)>85:
               termFinal.append(terms[0])     
    #todo:ordenar esto por los score y obtner los similares
    return termFinal