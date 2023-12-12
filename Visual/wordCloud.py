from matplotlib import pyplot as plt
from wordcloud import WordCloud
import wordcloud

from DataLen.KeyWord.keyWordExtraction import keyWord_extraction





def WordCloud(text):
    stat,words=keyWord_extraction(text)
    print(words)
    wc = WordCloud(background_color="black",prefer_horizontal=1,contour_width=3, contour_color='steelblue', max_words=1000)

    wc.generate_from_frequencies(stat)

    # Muestra la nube de palabras
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    
text='''
    I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!

    My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much. ECASA is an Empresa Cubana de Aeropuertos y Servicios Aeronáuticos S.A.
    '''
wordcloud(text)