# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z1xUumdt6Rvsd6-N5epzHGU--WzoW7m8
"""

import nltk

"""NATURAL LANGUAGE PROCESSING (NLP)

Traditionally, feeding statistics and models have been the method of choice for interpreting phrases. Recent advances in this area include voice recognition software, human language translation, information retrieval and artificial intelligence. There is difficulty in developing human language translation software because language is constantly changing. Natural language processing is also being developed to create human readable text and to translate between one human language and another. The ultimate goal of NLP is to build software that will analyze, understand and generate human languages naturally, enabling communication with a computer as if it were a human.

NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.

The Natural Language Toolkit is an open source library for the Python programming language originally written by Steven Bird, Edward Loper and Ewan Klein for use in development and education.
It comes with a hands-on guide that introduces topics in computational linguistics as well as programming fundamentals for Python which makes it suitable for linguists who have no deep knowledge in programming, engineers and researchers that need to delve into computational linguistics, students and educators
"""

text= """Monte Carlo and Las Vegas are two Randomization algorithms developed in 90s , by some developers AND I AM ADDING THIS 
TEXT TO ONLY CHECK ABOUT THE FREQUENCY DISTRIBUTION BY REPEATING WORDS LIKE DISTRIBUTION AND MONTE CARLO"""

import regex
regex.split("[\s\.\,]",text)

nltk.download('punkt')
nltk.word_tokenize(text)



"""**One of the things we can do with NLTK is Stemming.**

**Stemming**: Stemming is the process of reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words known as a lemma. Stemming is important in natural language understanding (NLU) and obviously in natural language processing (NLP) as well.

We will discuss few types of stemming here:

1.   Porter Stemmer
2.   Snowball Stemmer
"""

from nltk.stem import PorterStemmer
stemmer= PorterStemmer()
plurals=['caresses','flies','dies','mules','denied','died','agreed','owned','humbled','sized','meeting','stating','seizing','itemization',
         'sensational','traditional','reference','colonizer','plotted']
for word in plurals:
  print(f"{word}>>>{stemmer.stem(word)}")

from nltk.stem.snowball import SnowballStemmer
SnowballStemmer.languages

sn_stemmer= SnowballStemmer("english")

sn_stemmer.stem("generously")

stemmer.stem("generously")

"""Lemmatization:
retrieving the source of the word
"""

from nltk.stem import WordNetLemmatizer
lemmatizer= WordNetLemmatizer()

import nltk
nltk.download('wordnet')

for word in plurals:
  print(f"{word}>>>{lemmatizer.lemmatize(word)}")

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)

from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)
#<FreqDist with 25 samples and 30 outcomes>
fdist.most_common(2)
[('is', 3), (',', 2)]
# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()

"""Stopwords

Stopwords considered as noise in the text. Text may contain stop words such as is, am, are, this, a, an, the, etc.

In NLTK for removing stopwords, you need to create a list of stopwords and filter out your list of tokens from these words.
"""

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)

"""POS Tagging

The primary target of Part-of-Speech(POS) tagging is to identify the grammatical group of a given word. Whether it is a NOUN, PRONOUN, ADJECTIVE, VERB, ADVERBS, etc. based on the context. POS Tagging looks for relationships within the sentence and assigns a corresponding tag to the word.
"""

sent = "Albert Einstein was born in Ulm, Germany in 1879."
tokens=nltk.word_tokenize(sent)
print(tokens)

import nltk
nltk.download('averaged_perceptron_tagger')

nltk.pos_tag(tokens)

