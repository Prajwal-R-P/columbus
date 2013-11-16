from text import Word
import copy

class Similarity():
    def __init__(self):
        pass

    @staticmethod
    def words(word1,word2):
        word1 = Word(word1.lower())
        word2 = Word(word2.lower())
        result = 0

        for synset1 in word1.synsets:
            _max = 0
            for synset2 in word2.synsets:
                _max = max(synset1.wup_similarity(synset2),_max)
            result += _max

        if len(word1.synsets) > 0:
            result /= len(word1.synsets)

        result_old = result

        result = 0
        for synset1 in word2.synsets:
            _max = 0
            for synset2 in word1.synsets:
                _max = max(synset1.wup_similarity(synset2),_max)
            result += _max

        if len(word2.synsets) > 0:
            result /= len(word2.synsets)

        return max(result,result_old)

    @staticmethod
    def sentences(sentence1,sentence2):
        words1 = Similarity.get_tokens(sentence1)
        words2 = Similarity.get_tokens(sentence2)

        result = 0

        for word1 in words1:
            _max = 0
            for word2 in words2:
                _max = max(Similarity.words(word1,word2),_max)
            result += _max

        if len(words1) > 0:
            result /= len(words1)

        result_old = result

        result = 0
        for word2 in words2:
            _max = 0
            for word1 in words1:
                _max = max(Similarity.words(word1,word2),_max)
            result += _max

        if len(words2) > 0:
            result /= len(words2)

        return max(result,result_old)

    @staticmethod
    def get_tokens(string):
        #remove spaces in begining and ending places
        string=str(string).strip().replace("\n"," ")
        string=string.replace("@","%").replace("_","%").replace(" ","%")
        for char in range(ord('A'),ord('Z')+1):
            string=string.replace(chr(char),"%"+chr(char))
        for num in range(0,10):
            string=string.replace(str(num),"%"+str(num))
        tokens=string.split("%")

        # remove stop words
        for token in copy.deepcopy(tokens):
            if token in 'for a of the and to in'.split():
                tokens.remove(token)

        #merge CAPS
        caps=""
        delete_tokens=[]
        for i in range(0,len(tokens)):
            try:
                if not caps and len(tokens[i])==1 and tokens[i] in [ chr(x) for x in range(ord("A"),ord("Z")+1) ]:
                    caps=tokens[i]
                elif caps and tokens[i][0] in [ chr(x) for x in range(ord("A"),ord("Z")+1) ]:
                    delete_tokens.append(tokens[i-1])
                    tokens[i]=tokens[i-1]+tokens[i]
                else:
                    caps=""
            except:
                caps=""

        #now merge numbers
        num=None
        for i in range(0,len(tokens)):
            try:
                if not num and len(tokens[i])==1 and tokens[i] in [ str(x) for x in range(0,10) ]:
                    num=tokens[i]
                elif num and tokens[i][0] in [ str(x) for x in range(0,10) ]:
                    delete_tokens.append(tokens[i-1])
                    tokens[i]=tokens[i-1]+tokens[i]
                else:
                    num=None
            except:
                pass

        for delete in delete_tokens:
            if delete in tokens:
                tokens.remove(delete)

        return filter(None,list(set(tokens)))


#from gensim import corpora, models, similarities
#
#def compute(key):
#    #documents = ["Human machine interface for lab abc computer applications",
#    #             "A survey of user opinion of computer system response time", "The EPS user interface management system",
#    #             "System and human system engineering testing of EPS",
#    #             "Relation of user perceived response time to error measurement",
#    #             "The generation of random binary unordered trees", "The intersection graph of paths in trees",
#    #             "Graph minors IV Widths of trees and well quasi ordering", "Graph minors A survey"]
#    documents = ["read book", "book ticket"]
#
#    # remove common words and tokenize
#    stoplist = set('for a of the and to in'.split())
#    texts = [[word for word in document.lower().split() if word not in stoplist]
#             for document in documents]
#
#    print "a", texts
#
#    # remove words that appear only once
#    #all_tokens = sum(texts, [])
#    #tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
#    #texts = [[word for word in text if word not in tokens_once]
#    #         for text in texts]
#
#    dictionary = corpora.Dictionary(texts)
#    #dictionary.save('/tmp/deerwester.dict') # store the dictionary, for future reference
#
#    #new_doc = "Human computer interaction"
#    #new_vec = dictionary.doc2bow(new_doc.lower().split())
#
#    corpus = [dictionary.doc2bow(text) for text in texts]
#    #corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use
#
#    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2) # 2 dim lsi space
#
#    doc = "book flight"
#    vec_bow = dictionary.doc2bow(doc.lower().split())
#    vec_lsi = lsi[vec_bow]
#
#    index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
#    index.save('/tmp/deerwester.index')
#    index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')
#    sims = index[vec_lsi]
#    #sims = sorted(enumerate(sims), key=lambda item: -item[1]) # this will have the answer
#    print(sims)
#
#compute("Human computer interaction")