
def dependecy_parser(doc):
    dependecy_parserList = []
    for token in doc:
        dic = {
            'token': token.text,
            'Dependecy': token.dep_,
            'Parent': token.head.text,
            'Parent_pos': token.head.pos_,
            'Childrens': [child for child in token.children]        
        }
        dependecy_parserList.append(dic)
    
    return dependecy_parserList