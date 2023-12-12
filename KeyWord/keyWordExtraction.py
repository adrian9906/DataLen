from pke import unsupervised

def pre_process(text):
    texto=" ".join([palabra for palabra in text.split('\w') if palabra != "\n"])
    return texto

def keyWord_extraction(documents,lang):
    wordsList=[]
    extractor=unsupervised.SingleRank()
    pos={'NOUN','PROPN','ADJ'}

    for document in documents:
        text=pre_process(document)
        extractor.load_document(input=text,language=lang,normalization=None)
        extractor.candidate_selection(pos=pos)
        extractor.candidate_weighting(window=2,pos=pos)
        words= extractor.get_n_best(n=15)
        wordsList+= words
    
    keyword=sorted(wordsList,key=lambda x: x[1], reverse=True)
    wordsFras=[x[0] for x in keyword]
    frequencies = {word: wordsFras.count(word) for word in set(wordsFras)}
                   
    return frequencies,keyword
    
