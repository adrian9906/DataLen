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
![FlujoDeTopicsCip2.drawio.png](https://github.com/adrian9906/DataLen/blob/main/TopicWorkFlow.png?raw=true)
---
### Data processing
##### **Before applying text analysis, it is necessary to process the data using natural language processing (NLP) techniques. This involves the elimination of punctuation, empty words, among others**
- - -

### Topical modeling with LDA
##### **Topic modeling is an unsupervised machine learning technique for discovering "topics" occurring in a collection of documents. In this project, the LDA algorithm is used for topic modeling.**

![FlujoDeTopicsCip2.drawio (1).png](https://github.com/adrian9906/DataLen/blob/main/NerWorkFlow?raw=true)

---
### Named entity extraction with spaCy
##### **Named entity extraction is an NLP task that consists of identifying and classifying entities (such as people, places, organizations, etc.) in a text. In this project, spaCy is used for named entity extraction.**
---
### Keyword extraction with PKE
##### **Keyword extraction is an NLP task that consists of identifying the most important words in a text. In this project, PKE is used for keyword extraction 5.**
---
### Dependecy Parser with spaCy
##### **The dependency parsing algorithm in Spacy is based on a transition approach, which jointly learns sentence segmentation and dependency parsing with tags. This dependency parsing can learn to merge tokens that had been over-segmented by the tokenizer.**

***
### Contribution
*Contributions to this project are welcome. If you find a bug or have a suggestion for improvement, please open an issue or send a pull request.*
