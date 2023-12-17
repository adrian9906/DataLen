

import json
import re
from CRUD.Find import findDoc
from Topic_Extraction.ldaExtraction import ldaTopicExtraction

from Topic_Extraction.Processing.pre_processing import preprocess_data


def topicExtraction(document,collection,database):
    with open('./resources/stop_words.json',mode='r') as file:
        wordsFile = json.loads(file)
        stopwords = wordsFile.split('\W')
    
    text = preprocess_data(document, stopwords)
    
    lda = ldaTopicExtraction(text)
    
    return lda
     
                
def topicExtractionBySimilarity(document,collection,database,wordList:list,spacy):
    topics = []
    
    topicFinalList = []
    
    
    with open('D:/apps/Proyectos Freelance/DataLen/Topic_Extraction/resources/stop_words.json',mode='r') as file:
        stopwords = json.load(file)
    
    text = preprocess_data(document, stopwords)
    
    lda = ldaTopicExtraction(text,spacy,wordList)
    
    for word in wordList:
        word=word.upper()
        doc=findDoc(database,collection,query=word)
        for docu in doc:
            if docu:
                topics.append(docu)
    
    for topic in topics:
        tmp = [x[0] for x in text if topic['acronym'] in x and x[0] not in lda]
        if tmp:
            topicFinalList+= tmp
        for word in topic['related_terms']:
            tmp2 = [x[0] for x in text if word in x and x[0] not in lda]
            if tmp2:
                topicFinalList+= tmp2
                    
    topicFinalList+=lda
    
    return topicFinalList
    