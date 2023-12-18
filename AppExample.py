

import pandas as pd
import spacy
from CRUD.Insert import Insert
from Dependecy_Parser.depParser import dependecy_parser
from NER_Extraction.ner_extraction import nerDetection
from KeyWord.keyWordExtraction import keyWord_extraction
from Topic_Extraction.extract_topics import topicExtractionBySimilarity
from Language_Detection.languageDetec import langDetect
from Visual.dependecyVisual import visualFile


if __name__=='__main__':
    text='''
    I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!

    My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much. ECASA is an Empresa Cubana de Aeropuertos y Servicios Aeronáuticos S.A. FMC is good
    '''
    
    lang=langDetect(text)
    if lang=='en':
        nlp = spacy.load("en_core_web_md")
    elif lang=='es':
        nlp = spacy.load("es_core_news_md")
    doc = nlp(text)
    data = {
        'text':text,
        'topics':topicExtractionBySimilarity(text,'acronimosCuba','Acronymos',['family','ECASA','FMC']),
        'keyWords':keyWord_extraction([text],lang),
        'ner':nerDetection(nlp,doc),
        }
    listText = dependecy_parser(doc)
    Insert("DataLen","documentInformation",data)
    
    visualFile('./examples/Dependecy.svg')
    
    