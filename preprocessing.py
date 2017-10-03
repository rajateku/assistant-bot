# This file is used for cleaning / pre-processing of the input documents

import nltk
import nltk
from nltk.stem.lancaster import LancasterStemmer
import urllib2
import json
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random
import entities

from nltk import word_tokenize, sent_tokenize, pos_tag, ne_chunk_sents


def standardize_sentence(sentence):
    punctuations = ['.', ',', ':', "?", "!", "'", "\"", ";", "&", "a"]
    standardized_sentence = [token.lower() for token in word_tokenize(sentence) if token not in punctuations]
    # sentence = sentence.lower()
    # tokenizer = RegexpTokenizer(r'\w+')
    # standardized_sentence = tokenizer.tokenize(sentence)

    # print(standardized_sentence)



    return standardized_sentence

def standardize_sentence2(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

