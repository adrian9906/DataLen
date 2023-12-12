# DataLen

#####  This Python text analysis project uses several libraries and techniques to analyze and process Spanish and English texts.

* * *

### Features
1. SpaCy models for the analysis of texts in Spanish and English.
1. Topic extraction with the LDA algorithm and use of acronyms for a database in MongoDB.
1. Named entity extraction with spaCy.
1. Keyword extraction with PKE (Python Keyword Extraction).
1. Language detection with Apache Tika.

> [!NOTE]
> First of all you should download the corresponding spacy models, for example:
> `python -m spacy download es_core_news_sm`

* * *
## Workflow diagram
**The workflow diagram used to build the system is as follows:**
![FlujoDeTopicsCip2.drawio.png] (https://github.com/adrian9906/DataLen/blob/main/FlujoDeTopicsCip2.drawio.png?raw=true)
---
### Procesar los datos
##### **Antes de aplicar el análisis de textos, es necesario procesar los datos utilizando técnicas de procesamiento de lenguaje natural (NLP). Esto implica la eliminación de puntuación, palabras vacías, entre otros.**
- - -

### Modelado de tópicos con LDA
##### **El modelado de tópicos es una técnica de aprendizaje automático no supervisado para descubrir "tópicos" que ocurren en una colección de documentos. En este proyecto, se utiliza el algoritmo LDA para el modelado de tópicos.**

![FlujoDeTopicsCip2.drawio (1).png](https://github.com/adrian9906/DataLen/blob/main/FlujoDeTopicsCip2.png?raw=true)

---
###Extracción de entidades nombradas con spaCy
#####**La extracción de entidades nombradas es una tarea de NLP que consiste en identificar y clasificar entidades (como personas, lugares, organizaciones, etc.) en un texto. En este proyecto, se utiliza spaCy para la extracción de entidades nombradas.**
---
###Extracción de palabras clave con PKE
#####**La extracción de palabras clave es una tarea de NLP que consiste en identificar las palabras más importantes en un texto. En este proyecto, se utiliza PKE para la extracción de palabras clave 5.**

***
### Contribución
*Las contribuciones a este proyecto son bienvenidas. Si encuentras un error o tienes una sugerencia de mejora, por favor abre un issue o envía un pull request.*
