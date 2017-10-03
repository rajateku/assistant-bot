# Named entity recognition
import nltk

def frommain(tag , sentence):
    intent = tag
    print namedEntities(sentence)
    if intent == 'retrieve-email':
        email(sentence)
        # print "email"
        return email(sentence)
    if intent == 'retrieve-document':
        # print "document"
        return document(sentence)
    if intent == 'make-call':
        # print "call"
        return call(sentence)
    if intent == 'schedule-meeting':
        # print "meeting"
        return meeting(sentence)
    if intent == 'add-action-item':
        # print "action"
        return action(sentence)
    else:
        return intent
    # return intent

def email(sentence):
    names = nameSlot(sentence)
    times = timeSlot(sentence)
    return names , times

def document(sentence):
    nes = namedEntities(sentence)
    return  nes

def call(sentence):
    final_response = "calling"
    try:
        name = nameSlot(sentence)
        # print "calling " + name[0]
        final_response ="calling " + name[0] + " Contact-Person : " + name[0]
    except Exception:
        pass
    return final_response

def meeting(sentence):
    final_response = "meeting scheduled"
    try:
        names = nameSlot(sentence)
        places = locationSlot(sentence)
        time =  timeSlot(sentence)
        final_response = "Meeting Scheduled. Meeting Persons :"
        for name in names:
            final_response = final_response + name + " "
        try:
            final_response = final_response + "\nMeeting place : " + places[0]
        except Exception:
            pass
    except Exception:
        pass
    return  final_response

def action(sentence):
    nes = namedEntities(sentence)
    return  nes

def namedEntities(sentence):
    sent = nltk.tokenize.wordpunct_tokenize(sentence)
    pos_tag = nltk.pos_tag(sent)
    nes = nltk.ne_chunk(pos_tag)
    return nes

def locationSlot(sentence):
    sent = nltk.tokenize.wordpunct_tokenize(sentence)
    pos_tag = nltk.pos_tag(sent)
    nes = nltk.ne_chunk(pos_tag)
    places = []
    for ne in nes:
        if type(ne) is nltk.tree.Tree:
            if (ne.label() == 'GPE'):
                places.append(u' '.join([i[0] for i in ne.leaves()]))
    return places

def nameSlot(sentence):
    sent = nltk.tokenize.wordpunct_tokenize(sentence)
    pos_tag = nltk.pos_tag(sent)
    nes = nltk.ne_chunk(pos_tag)
    names = []
    for ne in nes:
        if type(ne) is nltk.tree.Tree:
            if (ne.label() == 'PERSON'):
                names.append(u' '.join([i[0] for i in ne.leaves()]))
    return names

def timeSlot(sentence):
    sent = nltk.tokenize.wordpunct_tokenize(sentence)
    pos_tag = nltk.pos_tag(sent)
    nes = nltk.ne_chunk(pos_tag)
    times = []
    for ne in nes:
        if type(ne) is nltk.tree.Tree:
            if (ne.label() == 'TIME'):
                times.append(u' '.join([i[0] for i in ne.leaves()]))
    return times

def organisatioSlot(sentence):
    sent = nltk.tokenize.wordpunct_tokenize(sentence)
    pos_tag = nltk.pos_tag(sent)
    nes = nltk.ne_chunk(pos_tag)
    orgs = []
    for ne in nes:
        if type(ne) is nltk.tree.Tree:
            if (ne.label() == 'ORGANIZATION'):
                orgs.append(u' '.join([i[0] for i in ne.leaves()]))
    return orgs
# locationSlot("he is in Aus")
# nameSlot("he is Raja Teku")
# namedEntities("he is in australia")

s = "June, 2008-06-29"
# print(nltk.ne_chunk("s", binary=True))