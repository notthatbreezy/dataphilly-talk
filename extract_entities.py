# Find Named Entities #

from nltk import batch_ne_chunk, pos_tag, word_tokenize, sent_tokenize, FreqDist
import os
def chunk_document(document):
    sentences = sent_tokenize(document)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]
    return batch_ne_chunk(tagged_sentences, binary=True)
 
def extract_entities(doc_tree):
    entities = []
    for sent_trees in doc_tree:
        for t in sent_trees:
            if hasattr(t, 'node') and t.node == 'NE':
                entities.append(t[0][0])
    return entities

def load_files(cat):
    path = './cleaned_html/'
    files = os.listdir(path)
    data = []
    for f in files:
        if f[0] != cat:
            continue
        data.append(open(path+f, 'r').read().decode('ascii', 'ignore'))
    return " ".join(data)

def entity_helper(catname, catnum):
    document = load_files(str(catnum))
    print "Extracting Chunks"
    chunks = chunk_document(document)
    print "Extracting Entities"
    entities = extract_entities(chunks)
    fdist = FreqDist(entities)
    print "5 most common entities ({0})".format(catname)
    for i in fdist.keys()[:10]:
        print i
    
if __name__ == '__main__':
    entity_helper('guantanomo', 0)
    entity_helper('Weiner', 8)
    entity_helper('Gun Control', 2)
    
    