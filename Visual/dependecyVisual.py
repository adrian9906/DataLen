from spacy import displacy
from pathlib import Path


'''
in style you can use the different styles to visualize 
(e.g. dep to visualize the dependey parser or ent to visualize the named entities)
''' 
def visualServer(doc,style):
    sentence_spans = list(doc.sents)
    
    displacy.serve(sentence_spans, style=style)
    
def visualFile(path,doc,style):
    sentence_spans = list(doc.sents)
    
    svg = displacy.render(sentence_spans, style=style)
    
    output_path = Path(path)
    
    output_path.open("w", encoding="utf-8").write(svg)