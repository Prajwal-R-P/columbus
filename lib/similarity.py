from text import Word
import copy
import sqlite3
from config import DB

class Similarity():
    def __init__(self):
        pass

    def words(self,word1,word2):
        word1=word1.lower()
        word2=word2.lower()
        if word1==word2:
            return 0
        #if already in database return
        similarity_pre_calculated=self.get_from_db(word1,word2)
        if similarity_pre_calculated in ["-2","-2.0",-2.0]:
            return 0
        elif similarity_pre_calculated:
            return similarity_pre_calculated

        string1=word1
        string2=word2
        word1 = Word(word1)
        word2 = Word(word2)
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

        result = max(result,result_old)
        if result == 0:
            self.new_db_entry(string1,string2,"-2")
        else:
            self.new_db_entry(string1,string2,result)

        return result

    def sentences(self,sentence1,sentence2):
        words1 = Similarity.get_tokens(sentence1)
        words2 = Similarity.get_tokens(sentence2)

        result = 0

        for word1 in words1:
            _max = 0
            for word2 in words2:
                _max = max(self.words(word1,word2),_max)
            result += _max

        if len(words1) > 0:
            result /= len(words1)

        result_old = result

        result = 0
        for word2 in words2:
            _max = 0
            for word1 in words1:
                _max = max(self.words(word1,word2),_max)
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
            if token in ['a','is','an','it','at','which','that','on','the','and',"soap","service","for","of","to","in","ing","exp","rec","non","dati","ment"]:
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

    def get_from_db(self,string1,string2):
        connect=sqlite3.connect(DB)
        cursor=connect.cursor()
        cursor.execute("select distance from ngd where (word1='"+string1+"' and word2='"+string2+"') or (word1='"+string2+"' and word2='"+string1+"')")
        data=cursor.fetchone()
        if data is None:
            return None
        else:
            return float(data[0])


    def new_db_entry(self,string1,string2,distance):
        connect=sqlite3.connect(DB)
        cursor=connect.cursor()
        cursor.execute("insert into ngd values('"+string1+"','"+string2+"',"+str(distance)+")")
        connect.commit()