import nltk
def NormalizingTokenizer(doc):
    #Tokenize
    phrase = nltk.word_tokenize(doc)
    #Lemmatize
    phrase_lemma = []
    lemmatizer = nltk.stem.WordNetLemmatizer()
    for word in phrase:
        phrase_lemma.append(lemmatizer.lemmatize(word))
    #Handle negations
    phrase_iterator = iter(phrase_lemma)
    negation = False
    phrase_negated = []
    for word in phrase_iterator:
        phrase_negated.append(word)
        if word ==  'not':
            negation = True
            break 
    for word in phrase_iterator:
            phrase_negated.append('not_' + word) 
    return phrase_negated
