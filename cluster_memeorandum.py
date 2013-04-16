from pre_process_funcs import gen_feature_dict, make_ngram_dict
import os
from collections import OrderedDict

from sklearn.cluster import KMeans
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# Load Files #
path = './cleaned_html/'
files = os.listdir(path)

cats = []
data = []
files.sort()
for f in files:
    cats.append(f.split('_')[0])
    data.append(open(path+f, 'r').read().decode('ascii', 'ignore'))

unigrams = gen_feature_dict(data)
bigrams = gen_feature_dict(data, n_max=2)
trigrams = gen_feature_dict(data, n_max=3)

################
## Clustering ##
################

vec = DictVectorizer()
transformer = TfidfTransformer()
uni_tfidf = transformer.fit_transform(vec.fit_transform(unigrams).toarray())
bi_tfidf = transformer.fit_transform(vec.fit_transform(bigrams).toarray())
tri_tfidf = transformer.fit_transform(vec.fit_transform(trigrams).toarray())

kmeans = KMeans(n_clusters = 12)
res_uni = kmeans.fit_predict(uni_tfidf)
res_bi = kmeans.fit_predict(bi_tfidf)
res_tri = kmeans.fit_predict(tri_tfidf)

#################################
## Check Performance:          ##
## Each chunk in the resulting ##
## List should have only 1     ##
## Category                    ##
#################################

clusters = [(0, 8), (9, 13), (14, 23), (24, 36), (37, 59), (60, 68),
            (69, 81), (81, 90), (91, 95), (96, 99), (100, 104),
            (105, 109)]

def num_cats_in_cluster(l, beg, end):
    return len(set(l[beg:end]))

def results(l, clusters):
    res_list = [num_cats_in_cluster(l, c[0], c[1]) for c in clusters]
    res_dict = {}
    for i in res_list:
        key = "{0}".format(i)
        if key in res_dict:
            res_dict[key] += 1
        else:
            res_dict[key] = 1
    return OrderedDict(sorted(res_dict.items(), key=lambda t: t[0]))

uni_metrics = results(res_uni, clusters)
bi_metrics = results(res_bi, clusters)
tri_metrics = results(res_tri, clusters)

print uni_metrics
print bi_metrics
print tri_metrics

