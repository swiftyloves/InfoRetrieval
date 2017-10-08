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
            # total_words += 1
            if w not in stoplist:
                total_words += 1
                if w[0].lower() != w[0]:
                    capital_words += 1
        line = f.readline()

    f.close()
    print f.name, ": ", float(capital_words)/total_words

print('====== capital_letters ======')
capital_letters('assignment1/ehr.txt')
capital_letters('assignment1/medhelp.txt')


# ====================================================
# avg_number_of_characters

def avg_number_of_characters(filename):
    f = open(filename,'r')
    line = f.readline()
    sum_characters = 0
    total_words = 0

    while(line):
        lines = line.split()
        for w in lines:
            # total_words += 1
            # sum_characters += len(w)
            if w not in stoplist:
                total_words += 1
                sum_characters += len(w)
        line = f.readline()

    f.close()
    print f.name, ": ", float(sum_characters)/total_words

print('====== avg_number_of_characters ======')
avg_number_of_characters('assignment1/ehr.txt')
avg_number_of_characters('assignment1/medhelp.txt')


# ====================================================
# Percentage of nouns, adjectives, verbs, adverbs, and pronouns

tags_collection = ['NN', 'JJ', 'VB', 'RB', 'PRP']
counts = [0, 0, 0, 0, 0]
# amount of nouns, adjectives, verbs, adverbs, and pronouns

def Percentage_of_5_tags(filename):
    f = open(filename,'r')
    line = f.readline()
    total_words = 0

    while(line):
        w_lst = nltk.word_tokenize(line)
        w_lst = nltk.pos_tag(w_lst)
        # total_words += len(w_lst)

        for w,tag in w_lst:
            if w not in stoplist:
                total_words += 1
                if tag in tags_collection:
                    counts[tags_collection.index(tag)] += 1

        line = f.readline()

    f.close()

    print f.name, ": ", map(lambda x: float(x)/total_words, counts)

print('====== Percentage_of_5_tags ======')
Percentage_of_5_tags('assignment1/ehr.txt')
Percentage_of_5_tags('assignment1/medhelp.txt')