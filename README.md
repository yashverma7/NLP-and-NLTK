# natural-language-tool-kit-NLTK

# NATURAL LANGUAGE PROCESSING (NLP)
Traditionally, feeding statistics and models have been the method of choice for interpreting phrases. 
Recent advances in this area include voice recognition software, human language translation, information retrieval and artificial intelligence. 
There is difficulty in developing human language translation software because language is constantly changing. 
Natural language processing is also being developed to create human readable text and to translate between one human language and another. 
The ultimate goal of NLP is to build software that will analyze, understand and generate human languages naturally, enabling communication with a computer as if it were a human.

# NLTK 
is a leading platform for building Python programs to work with human language data.
It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet,
along with a suite of text processing libraries for classification, tokenization, stemming,
tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.
The Natural Language Toolkit is an open source library for the Python programming language originally written by 
Steven Bird, Edward Loper and Ewan Klein for use in development and education.
It comes with a hands-on guide that introduces topics in computational linguistics as well as programming fundamentals for Python
which makes it suitable for linguists who have no deep knowledge in programming, engineers and
researchers that need to delve into computational linguistics, students and educators.

These are the most prominent areas where we can use Text Analytics and NLP with the help of NLTK library:
1. Compare Text Analytics, NLP and Text Mining 
2. Text Analysis Operations using NLTK 
3. Tokenization 
4. Stopwords 
5. Lexicon Normalization such as Stemming and Lemmatization 
6. POS Tagging
7. Sentiment Analysis 
8. Text Classification 
9. Performing Sentiment Analysis using Text Classification

# Tokenization 
Tokenization is the first step in text analytics. 
The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. 
Token is a single entity that is building blocks for sentence or paragraph. 
1.Sentence Tokenization: breaks text paragraph into sentences.
2.Word Tokenization : Breaks sentence into words

# Stemming

Stemming is the process of reducing a word to its word stem that affixes to suffixes and
prefixes or to the roots of words known as a lemma. Stemming is important in natural language understanding (NLU) 
and obviously in natural language processing (NLP) as well.
It is a process of linguistic normalization, which reduces words to their word root word
or chops off the derivational affixes. For example, connection, connected, connecting word reduce to a common word "connect".
We will discuss few types of stemming here:
1. Porter Stemmer
2. Snowball Stemmer

# Lemmatization: 
retrieving the source of the word Lemmatization reduces words to their base word, which is linguistically correct lemmas. 
It transforms root word with the use of vocabulary and morphological analysis. 
Lemmatization is usually more sophisticated than stemming.
Stemmer works on an individual word without knowledge of the context.
For example, The word "better" has "good" as its lemma. 
This thing will miss by stemming because it requires a dictionary look-up.

# Stopwords
Stopwords considered as noise in the text. Text may contain stop words such as is, am, are, this, a, an, the, etc.
In NLTK for removing stopwords, you need to create a list of stopwords and filter out your list of tokens from these words.


# POS Tagging
The primary target of Part-of-Speech(POS) tagging is to identify the grammatical group of a given word. 
Whether it is a NOUN, PRONOUN, ADJECTIVE, VERB, ADVERBS, etc. based on the context. 
POS Tagging looks for relationships within the sentence and assigns a corresponding tag to the word.

# Lexicon Normalization 
Lexicon normalization considers another type of noise in the text. 
For example, connection, connected, connecting word reduce to a common word "connect".
It reduces derivationally related forms of a word to a common root word.

# Sentiment Analysis 
Nowadays companies want to understand, what went wrong with their latest products? What users and the general public think about the latest feature?
You can quantify such information with reasonable accuracy using sentiment analysis.
Quantifying users content, idea, belief, and opinion is known as sentiment analysis. 
User's online post, blogs, tweets, feedback of product helps business people to the target audience and innovate in products and services. 
Sentiment analysis helps in understanding people in a better and more accurate way. 
It is not only limited to marketing, but it can also be utilized in politics, research, and security. 
Human communication just not limited to words, it is more than words. 
Sentiments are combination words, tone, and writing style. As a data analyst,
It is more important to understand our sentiments, what it really means?

There are mainly two approaches for performing sentiment analysis. 
1.Lexicon-based: count number of positive and negative words in given text and the larger count will be the sentiment of text. 
2.Machine learning based approach: Develop a classification model, which is trained using the pre-labeled dataset of positive, negative, and neutral.


# Text Classification 
Text classification is one of the important tasks of text mining. 
It is a supervised approach. 
Identifying category or class of given text such as a blog, book, web page, news
articles and tweets. 
It has various applications in today's computer world such as spam detection, task categorization 
in CRM services, categorizing products on E-retailer websites, 
classifying the content of websites for a search engine, sentiments of customer feedback, etc.
