from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize, WhitespaceTokenizer

s = "Hello SF Python. This is NLTK. Hello, Zachary. We missed you!"

#a = sent_tokenize(s)
#print a
#print word_tokenize(a)

#print [wordpunct_tokenize(t) for t in sent_tokenize(s)]

print list(WhitespaceTokenizer().span_tokenize(s))
