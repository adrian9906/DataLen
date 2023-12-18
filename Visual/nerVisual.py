from spacy import displacy
from pathlib import Path

def visualnerFile(path,doc,style):
    
    svg = displacy.render(doc, style=style,page=True)
    
    output_path = Path(path)
    
    output_path.open("w", encoding="utf-8").write(svg)