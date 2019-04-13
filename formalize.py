from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from random import randint
import nltk.data

stopWords = set(stopwords.words('english'))
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def formalize(text):
    global stopWords, tokenizer
    output = []

    tokenized = tokenizer.tokenize(text)
    words = word_tokenize(text)
    tagged = nltk.pos_tag(words)

    for i in range(0,len(words)):
        if tagged[i][1] == 'NNP' or tagged[i][1] == 'DT' or tagged[i][1] == 'PRP' or tagged[i][1] == 'PRP$' or tagged[i][1] == 'TO' or tagged[i][1] == 'IN' or tagged[i][1] == 'CD' or tagged[i][1] == 'MD' or words[i] in stopWords:
            output.append(words[i])
        else:
            syns = wordnet.synsets(words[i])
            word_type = tagged[i][1][0].lower()
            if len(syns) > 0 and syns[0].name().find("."+word_type+"."):
                definition = remove_prefix(remove_prefix(remove_prefix(syns[0].definition(), 'an '), 'any '), 'a ').replace('(plural)', '')
                output.append(definition)
            else:
                output.append(words[i])

    print(' '.join(output) + '\n')

while True:
    sentence = raw_input('>> ')
    formalize(sentence)
