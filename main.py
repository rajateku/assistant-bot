import sys

"""
Created on Mon Sep 29 17:11:00 2017

@author: Raja
"""

# things we need for NLP

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

# import our chat-bot intents file
import json
intents_file = "/home/Raja/Documents/Repositories/meeting_assistant_bot/intents.json"

with open(intents_file) as json_data:
    intents = json.load(json_data)

import sys

"""
Created on Mon Sep 29 17:11:00 2017

@author: Raja
"""

# things we need for NLP

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

# import our chat-bot intents file
import json
intents_file = "/home/Raja/Documents/Repositories/meeting_assistant_bot/intents.json"

with open(intents_file) as json_data:
    intents = json.load(json_data)

words = []
classes = []
documents = []
ignore_words = ['?']

# loop through each sentence in our intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# remove duplicates
classes = sorted(list(set(classes)))


# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)

# create train and test lists
train_x = list(training[:, 0])
train_y = list(training[:, 1])

# reset underlying graph data
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# # Start training (apply gradient descent algorithm)
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')

# save all of our data structures
import pickle

pickle.dump({'words': words, 'classes': classes, 'train_x': train_x, 'train_y': train_y}, open("training_data", "wb"))

# restore all of our data structures
import pickle

data = pickle.load(open("training_data", "rb"))
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']




# import our chat-bot intents file
import json

with open(intents_file) as json_data:
    intents = json.load(json_data)

import preprocessing

# load our saved model
model.load('./model.tflearn')



# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = preprocessing.standardize_sentence2(sentence)
    # bag of words
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return (np.array(bag))

ERROR_THRESHOLD = 0.25

def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list


def responsemessage(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # a random response from the intent
                    print i['tag']
                    resp = (random.choice(i['responses']))
                    final_reply = entities.frommain(i['tag'],sentence)
                    # print rep
                    return final_reply


            # results.pop(0)



def main():
    # text = "schedule a meeting in Australia with John and Andrew at 1:30" #sys.argv[1]
    # text = "Call Mom" #sys.argv[1]
    text = "Call Mom" #sys.argv[1]
    ser = responsemessage(text)
    probabilities = classify("Schedule a meeting with John")
    print ser, probabilities


if __name__ == '__main__':
    main()