# assistant-bot

Tools used: 
Python, tensorflow, tflearn


Tasks : 
Created a chatbot framework and build a conversational model for an hypothetical meeting assistant

Approach:
To classify a sentence and match with intent based on category and then extract entities out of it for subsequent action


Concept: 
Train all the sentences of each category based on their categories using tensorflow
Then classify the new sentence into one of the category based on the percentage match or probability 
One can check the probabilites using function  
example : classify("Schedule a meeting with John") 
Outcome format [(u'schedule-meeting', 0.87971735)]


Model: 
Used tensorflow which follows Deep neural network framework for text classification.
I used internet resources for the text classification model.

Each conversational intent contains:
a tag (a unique name)
patterns (sentence patterns for our neural network text classifier)

We create a list of documents (sentences), each sentence is a list of stemmed words and each document is associated with an intent (a class).


50 documents => 50 sentences
5 classes => 5 intents
 unique stemmed words => yet to figure out after adding more sentences



Categories (labels or tags or classes) :
retrieve-email
retrieve-document
make-call
schedule-meeting
add-action-item


Issues faced:
Tough to find a library which extracts time from sentence 





Running the code.
Files used :
1) main.py
2) preprocessing.py
3) entities.py
4) intents.json

run main.py file by changing the text inside main() function for appropriate bot response. 
In case of names start with capital letters eg : John


Conclusion : I have gone wwith tensorflow for Deep 
