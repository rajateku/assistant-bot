# Named entity recognition
import nltk

def frommain(tag , sentence):
    intent = tag
    print namedEntities(sentence)
    if intent == 'retrieve-email':
        email(sentence)
        return email(sentence)
    if intent == 'retrieve-document':
        return documents(sentence)
    if intent == 'make-call':
        return call(sentence)
    if intent == 'schedule-meeting':
        return meeting(sentence)
    if intent == 'add-action-item':
        return action(sentence)
    else:
        return intent
    # return intent




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


def email(sentence):
    # times = timeSlot(sentence)
    final_response = "fetching email"
    try:
        name = nameSlot(sentence)
        # print "calling " + name[0]
        if(len(name)>1):
            final_response = "fetching email " + name[1]
        else:
            final_response = "fetching email " + name[0]
    except Exception:
        pass
    return final_response


def documents(sentence):
    final_response = "fetching document"
    from_lookup = ["from"]
    from nltk import word_tokenize, sent_tokenize, pos_tag, ne_chunk_sents
    punctuations = ['.', ',', ':', "?", "!", "'", "\"", ";", "&", "a"]
    standardized_sentence = [token.lower() for token in word_tokenize(sentence) if token not in punctuations]
    from_position = []
    for i, token in enumerate(standardized_sentence):
        if token in from_lookup:
            from_position.append(i)
            # break

    document = standardized_sentence[from_position[0] - 1]
    document_location = standardized_sentence[from_position[0] + 1]
    final_response = final_response + " "+  document + " from " + document_location

    return final_response


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


