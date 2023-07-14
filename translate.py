import sys

pronouns = {
    "I": "au",
    "Me": "ahau",
    "You": "koe",
    "You (1 incl)": "koe",
    "He": "ia",
    "She": "ia",
    "Him": "ia",
    "Her": "ia",
    "We (2 incl)": "t\u0101ua",
    "Us (2 incl)": "t\u0101ua",
    "We (2 excl)": "m\u0101ua",
    "Us (2 excl)": "m\u0101ua",
    "You (2 incl)": "kōrua",
    "They (2 excl)": "r\u0101ua",
    "Them (2 excl)": "r\u0101ua",
    "We (3 incl)": "t\u0101tou",
    "Us (3 incl)": "t\u0101tou",
    "We (3 excl)": "m\u0101tou",
    "Us (3 excl)": "m\u0101tou",
    "You (3 incl)": "koutou",
    "They (3 excl)": "r\u0101tou",
    "Them (3 excl)": "r\u0101tou"
}

verbs = {
    "go": "haere",
    "going": "haere",
    "gone": "haere",
    "went": "haere",
    "make": "hanga",
    "making": "hanga",
    "made": "hanga",
    "see": "kite",
    "seeing": "kite",
    "seen": "kite",     
    "saw": "kite",
    "want": "hiahia",
    "wanting": "hiahia",
    "wanted": "hiahia",
    "call": "karanga",
    "calling": "karanga",
    "called": "karanga",
    "ask": "p\u0101tai",
    "asking": "p\u0101tai",
    "asked": "p\u0101tai",
    "read": "p\u0101nui",
    "reading": "p\u0101nui",
    "learn": "ako",
    "learning": "ako",
    "learnt": "ako"
}

tenses = {
    "am": "Kei te",
    "were": "I",
    "was": "I",
    "are": "Kei te",
    "will": "Ka",
    "went": "I",
    "here": "Kei te",
    "go": "Kei te",
    "is": "Kei te",
    "has": "Kei te",
    "have": "Ka",
    "get": "Kei te",
    "made": "I",
    "called": "I",
    "call": "Kei te",
    "going": "Kei te",
    "see": "Kei te",
    "saw": "I",
    "want": "Ka",
    "asked": "I",
    "ask": "Kei te",
    "read": "I",
    "reading": "Kei te",
    "learnt": "I",
    "learned": "I",
    "wanted": "I"
}

def translate(sentance):

    words = sentance.split()

    pronoun = ""
    verb = ""
    tense = ""
    maori_sentence = ""
    number = 0
    if len(words) == 5:
        number = int(words[1].strip('()'))
        if number >= 4:
            words[1] = "(3"
        pronoun = words[0]+" "+words[1]+" "+words[2]
        verb = words[4]
        tense = words[3]
    if len(words) == 4:
        number = int(words[1].strip('()'))
        if number >= 3:
            words[1] = "(3"
        pronoun = words[0]+" "+words[1]+" "+words[2]
        verb = words[3]
        tense = words[3]
    if len(words) == 3:
        pronoun = words[0]
        verb = words[2]
        tense = words[1]
    if len(words) == 2:
        pronoun = words[0]
        verb = words[1]
        tense = words[1]

    maori_subject = tenses.get(tense, "INVALID")
    maori_verb = verbs.get(verb, "INVALID")
    maori_object = pronouns.get(pronoun, "INVALID")

    if maori_object == "INVALID" or maori_verb == "INVALID" or maori_subject == "INVALID":
        return "INVALID"
    else:
        maori_sentence = maori_subject+" "+maori_verb+" "+maori_object
    
    return maori_sentence
        

for line in sys.stdin:
    line.strip()
    maori_sentence = translate(line)
    print(maori_sentence)