from nltk.chunk import ne_chunk
import nltk.data
from nltk.help import upenn_tagset
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.tag import pos_tag

def bag_of_words(words):
    return dict([(word, True) for word in words])

feats = bag_of_words(word_tokenize("great movie"))
#print feats

classifier = nltk.data.load('C:/nltk_data/tokenizers/punkt/english.pickle')
classifier.classify(feats)
