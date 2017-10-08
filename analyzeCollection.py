import nltk

# Clean stoplist
f_stoplist = open('assignment1/stoplist.txt','r')
stoplist = f_stoplist.readlines()


for i,w in enumerate(stoplist):
    stoplist[i] = w.replace("\r\n","")

f_stoplist.close()

# ====================================================
# Compute freq of stopwords
def computeStopwords(filename):

    f = open(filename,'r')
    line = f.readline().lower()

    stop_words = 0
    total_words = 0
    while(line):
        lines = line.split()
        for w in lines:
            total_words += 1
            if w in stoplist:
                stop_words += 1
        line = f.readline().lower()

    f.close()
    print (f.name, ": ", float(stop_words)/total_words)


computeStopwords('assignment1/ehr.txt')
computeStopwords('assignment1/medhelp.txt')

# ====================================================
# Frequency of capital letters

def capital_letters(filename):
    f = open(filename,'r')
    line = f.readline()
    capital_words = 0
    total_words = 0

    while(line):
        lines = line.split()
        for w in lines:
            total_words += 1
            if w[0].lower() != w[0]:
                capital_words += 1
        line = f.readline()

    f.close()
    print f.name, ": ", float(capital_words)/total_words

print('====== capital_letters ======')
capital_letters('assignment1/ehr.txt')
capital_letters('assignment1/medhelp.txt')


