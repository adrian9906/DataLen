from matplotlib import pyplot as plt
from wordcloud import WordCloud
import wordcloud

from KeyWord.keyWordExtraction import keyWord_extraction

def WordCloud(text):
    stat,words=keyWord_extraction(text)
    print(words)
    wc = WordCloud(background_color="black",prefer_horizontal=1,contour_width=3, contour_color='steelblue', max_words=1000)

    wc.generate_from_frequencies(stat)

    # Muestra la nube de palabras
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()