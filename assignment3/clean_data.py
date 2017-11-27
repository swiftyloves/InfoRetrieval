


# read file
_file = open('train.tsv')
with open('train.tsv', 'r') as _file:
    posts = [line.split('\t') for line in _file.readlines()]

for post in posts:
    post[1] = post[1][:-1]

posts.pop(0)
print(posts[0])

# posts (list)  (label, sentences)

######################################## PREPOSSENG ########################################

#****  Removing stop words with NLTK  ****#
# http://www.geeksforgeeks.org/removing-stop-words-nltk-python/

#****  Removing punctuation with string.punctuation (in addition to ! and ?) ****#

#****  Change to lowercase  ****#
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import csv

stop_words = set(stopwords.words('english'))

fieldnames = ['label','text']
# then check we can write the output file
# we don't want to complete process and show error about not
# able to write outputs
with open('traindata_clean.csv', 'w') as csvfile:
    # just write headers now
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

punctuation = string.punctuation + "'`'"
stop_punctuation_remove = punctuation.replace('()','')
stop_punctuation_remove = stop_punctuation_remove.replace('?','')
stop_punctuation_remove = stop_punctuation_remove.replace('!','')
# for punc in punctuation:
#     if (punc != "!" or punc != "?"):
#         stop_words.add(punc)
stop_characters = stop_punctuation_remove + "1234567890"
stop_words.add('(i)')
stop_words.add('(ii)')
stop_words.add('(iii)')
stop_words.add('(iv)')
stop_words.add('(v)')
stop_words.add('(vi)')
stop_words.add('(vii)')
stop_words.add('(viii)')
stop_words.add('(viiii)')

result = []
for post in posts:
    new_str = ""
    sentence = post[1]

    for char in post[1]:
        if char not in stop_characters:
            new_str += char
        else:
            new_str += ' '
    word_tokens = word_tokenize(new_str)
    filtered_sentence = []
    for w in word_tokens:
        # print('v',end="")
        w = w.lower()
        if not w in stop_words:
            w = w.replace('(', '')
            w = w.replace(')', '')
            filtered_sentence.append(w)
    data = {
        'label': post[0],
        'text': filtered_sentence
    }
    result.append(data)


####### CACHE

with open('traindata_clean.csv', 'a+') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerows(result)
