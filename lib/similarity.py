from gensim import corpora, models, similarities

def compute(key):
    #documents = ["Human machine interface for lab abc computer applications",
    #             "A survey of user opinion of computer system response time", "The EPS user interface management system",
    #             "System and human system engineering testing of EPS",
    #             "Relation of user perceived response time to error measurement",
    #             "The generation of random binary unordered trees", "The intersection graph of paths in trees",
    #             "Graph minors IV Widths of trees and well quasi ordering", "Graph minors A survey"]
    documents = ["read book", "book ticket"]

    # remove common words and tokenize
    stoplist = set('for a of the and to in'.split())
    texts = [[word for word in document.lower().split() if word not in stoplist]
             for document in documents]

    print "a", texts

    # remove words that appear only once
    #all_tokens = sum(texts, [])
    #tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    #texts = [[word for word in text if word not in tokens_once]
    #         for text in texts]

    dictionary = corpora.Dictionary(texts)
    #dictionary.save('/tmp/deerwester.dict') # store the dictionary, for future reference

    #new_doc = "Human computer interaction"
    #new_vec = dictionary.doc2bow(new_doc.lower().split())

    corpus = [dictionary.doc2bow(text) for text in texts]
    #corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use

    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2) # 2 dim lsi space

    doc = "book flight"
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow]

    index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
    index.save('/tmp/deerwester.index')
    index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')
    sims = index[vec_lsi]
    #sims = sorted(enumerate(sims), key=lambda item: -item[1]) # this will have the answer
    print(sims)

compute("Human computer interaction")