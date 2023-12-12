

def nerDetection(nlp,text):
    doc = nlp(text)
    entities=[]
    for ent in doc.ents:
        entitie={"ner":ent.text, 
                 "start":ent.start_char, 
                 "end":ent.end_char, 
                "tag":ent.label_}
        entities.append(entitie)
    
    return entities