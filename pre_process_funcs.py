# Features #
# 1) word_punkt tokenizer #
# 2) porter stemmer #
# 3) Will calculate up to trigrams #

from nltk import ingrams
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
from nltk.stem.porter import PorterStemmer
from collections import defaultdict

def _remove_stopwords_lowercase(words):
    """
    Remove stopwords, convert all words to lowercase, exclude numbers
    """
    return [w.lower() for w in words if not w.lower()
        in stopwords.words('english') and w.isalpha()]


def _stemmer(words):
    """
    Uses nltk.porter.stemmer to stem all words.
    """
    st = PorterStemmer()
    return [st.stem(w) for w in words]


def make_ngram_dict(string, n_min=1, n_max=1):
    """
    Takes a string and turns into dictionary representation.
    Arguments:
    `string` - string to tokenize, etc.
    `n_min` - minimum size ngram
    `n_max - maximum size ngram
    """
    tokens = wordpunct_tokenize(string)
    lowercase = _remove_stopwords_lowercase(tokens)
    stemmed = _stemmer(lowercase)
    feature_dict = defaultdict(int)
    while (n_min <= n_max):
        for ngram in ingrams(stemmed, n_min):
            feature_dict[' '.join(ngram)] += 1
        n_min += 1
    return feature_dict


def gen_feature_dict(list_of_strings, n_min=1, n_max=1):
    """
    Takes a list of strings, pre-processes, creates feature
    dictionary able to pass to scikit learn's DictVectorizer
    """
    list_of_feature_dicts = []
    for counter, string in enumerate(list_of_strings):
        f_dict = make_ngram_dict(string, n_min, n_max)
        list_of_feature_dicts.append(f_dict)
    return list_of_feature_dicts
