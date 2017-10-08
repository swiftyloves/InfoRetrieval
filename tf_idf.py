import nltk
import numpy as np
import collections
import math
# Clean stoplist
f_stoplist = open('assignment1/stoplist.txt','r')
stoplist = f_stoplist.readlines()


for i,w in enumerate(stoplist):
    stoplist[i] = w.replace("\r\n","")

f_stoplist.close()

# ===========
# TF(t,d) = log(c(t,d) + 1)
# IDF(t)  = 1 + log(N/K)


f = open('assignment1/ehr.txt','r')
lines = f.readlines()
N = len(lines)

term_set = []
all_words = []
for doc in lines:
    doc = doc.replace("\n","")
    term_lst = doc.split()
    term_lst_clean = []
    term_lst = list(set(term_lst))
    for w in term_lst:
        if w not in stoplist:
            term_lst_clean.append(w)
    term_set.append(term_lst_clean)
    all_words += term_lst_clean

all_words = list(set(all_words)) # clean duplicate words

term_freq = {} # how many docs contain a certain term, key: term; value: number of documents containing this term
for term in all_words:
    count = 0
    for term_lst in term_set: # Run through all docs and count how many docs containing this word
        if term in term_lst:
            count += 1

    term_freq[term] = float(count) # how many docs contain this term

first_10_docs = lines[0:10]

# TF = [{},{},{},{},{},{},{},{},{},{}]
i = 1
for doc in first_10_docs:
    print '==================='
    print 'doc',i

    # Run over each doc
    doc = doc.replace("\n","")

    freq_map = {} # c(t,d) for this doc, i.e., how many times a word shows in this doc

    # all posible terms in this doc
    term_lst = doc.split()
    term_lst = list(set(term_lst))
    term_lst_clean = []
    for w in term_lst:
        if w not in stoplist:
            term_lst_clean.append(w)

    term_lst_clean = list(set(term_lst_clean))
    for t in term_lst_clean:
        freq_map[t] = freq_map[t] + 1 if t in freq_map else 1
    # print "freq_map: ",freq_map
    print len(freq_map.keys())
    tf_idf = {}
    for t in term_lst_clean:
        tf = math.log( freq_map[t] + 1.0,2)
        idf = 1 + math.log( N / term_freq[t] )
        tf_idf[t] = tf*idf
        # print tf, idf, tf*idf
        # print term_freq[t]

    d = collections.Counter(tf_idf)
    num = 20

    if i == 3 or i == 4 or i == 6 or i == 8 or i == 9:
        num = 80
    print 'num:',num
    for k,v in d.most_common(num):
        print '%s: %f' % (k, v)
    i += 1




print lines[0]