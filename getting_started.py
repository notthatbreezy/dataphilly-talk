# First Download Corpora and Other Data #
import nltk
#nltk.download()

from nltk.corpus import brown

# Number of Categories #
print len(brown.categories()) #15

# Modal verbs are used differently #
# across some genres               #
modals = ['can', 'could', 'may', 'might', 'must', 'will']
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
cfd = nltk.ConditionalFreqDist(
      (genre, word)
      for genre in brown.categories()
      for word in brown.words(categories=genre))
cfd.tabulate(conditions=genres, samples=modals)

#                 can could  may might must will
#           news   93   86   66   38   50  389
#       religion   82   59   78   12   54   71
#        hobbies  268   58  131   22   83  264
#science_fiction   16   49    4   12    8   16
#        romance   74  193   11   51   45   43
#          humor   16   30    8    8    9   13

## Example Taken from Natural Language Processing with Python
## (Steve Bird, Ewan Klein, and Edward Loper 2009)
## Available at http://nltk.org/book/

from nltk import ngrams, wordpunct_tokenize
from ntlk.tag import pos_tag
from nltk.stem.porter import PorterStemmer
from nltk.chunk import ne_chunk

s = "The Democrat admitted he's eying the mayor's race in a lengthy New York Times Magazine article that detailed his life with wife Huma Abedin, a close aide to former Secretary of State Hillary Clinton, and their attempts to stay out of the limelight over the past two years-until now."

tokens = wordpunct_tokenize(s)
st = PorterStemmer()
stemmed = [st.stem(w) for w in tokens]
pos = pos_tag(tokens)
tree = ne_chunk(pos)
tree.draw()
