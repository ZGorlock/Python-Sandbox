from nltk.chunk import ne_chunk
from nltk.help import upenn_tagset
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.tag import pos_tag

s = "And now for something completely different."

a = wordpunct_tokenize(s)
print a

b = pos_tag(a)
print b

c = ne_chunk(b)
print c
