import sys
import csv
import numpy as np
from sklearn.svm import LinearSVC


THERSHOULD = 0.2
VERSION = '04'

# ifile  = open('train.tsv', "r")
# read = csv.reader(ifile)
# posts = []
# documents = []
# labels = []
# for row in read :
#     posts.append(row)
#     labels.append(row[0])
#     documents.append(row[1])

# print(posts[0])
# print('documents[0]:',documents[0])
# print(documents[0])
# print(len(documents))


# read file
_file = open('train.tsv')
with open('train.tsv', 'r') as _file:
    train_raw_data = [line.split('\t') for line in _file.readlines()]

labels = []
documents = []
for post in train_raw_data:
    post[1] = post[1][:-1]
    labels.append(post[0])
    documents.append(post[1])
print('documents[0]:',documents[0])
documents.pop(0)
labels.pop(0)

labels = [int(label) for label in labels]

print(documents[0])
print(len(documents))
print('labels:',labels[0])
print('labels:',labels[1])
print('len labels:', len(labels))
# print('labels:',labels)


######## Feature Selection ##########

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1,2), min_df = 0, stop_words = 'english')
print('vectorizer.fit_transform(documents)...')
tfidf_matrix = vectorizer.fit_transform(documents)

######## Feature Selection ##########


import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# count_vectorizer = CountVectorizer()
# counts = count_vectorizer.fit_transform(documents)

from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()
# targets = data['class'].values
# classifier.fit(counts, labels)


from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('vectorizer',  CountVectorizer()),
    ('tfidf_transformer',  TfidfTransformer()),
    # ('classifier',  MultinomialNB() )
    ('classifier',  LinearSVC() )
    ])

pipeline.fit(documents, labels)



################ read clean test file ################
# ifile = open('test.tsv', "r")
# read = csv.reader(ifile)
# ground_truth_labels = []
# predict_data = []
# i = 1
# for row in read :
#     if i % 500 == 0:
#         print('|', end="")
#     if i % 1000 == 0:
#         print('')
#     i += 1
#     sys.stdout.flush()
#     ground_truth_labels.append(float(row[0]))
#     lst = row[1]
#     # lst = row[1].split(" ")
#     # lst = [float(a) for a in lst]
#     predict_data.append(lst)

# print('predict_data[0]:',predict_data[0])
# print(type(predict_data))




from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score

k_fold = KFold(n=len(documents), n_folds=6)
scores = []
confusion = numpy.array([[0, 0], [0, 0]])
i = 1
npdoc = np.array(documents)
nplabels = np.array(labels)
# npdoc.toarray()
for train_indices, test_indices in k_fold:
    # print('train_indices:',train_indices)
    # print('test_indices:',test_indices)
    # print(type(test_indices))
    print('.', end="")
    if i % 500 == 0:
        print('|', end="")
    if i % 1000 == 0:
        print('')
    sys.stdout.flush()

    i += 1

    train_text = npdoc[train_indices]
    train_y = nplabels[train_indices]
    print('.', end="")
    sys.stdout.flush()

    test_text = npdoc[test_indices]
    test_y = nplabels[test_indices]
    print('*', end="")
    sys.stdout.flush()

    pipeline.fit(train_text, train_y)
    print('.', end="")
    sys.stdout.flush()
    predictions = pipeline.predict(test_text)
    print(predictions)

    confusion += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions)
    scores.append(score)



print('Total emails classified:', len(documents))
print('Score:', sum(scores)/len(scores))
print('Confusion matrix:')
print(confusion)



# read file
_file = open('test.tsv')
with open('test.tsv', 'r') as _file:
    posts = [line.split('\t') for line in _file.readlines()]

predict_data = []
for post in posts:
    predict_data.append(post[1][:-1])

# predict_data.pop(0)
print('predict_data[0]:',predict_data[0])

predict_result = pipeline.predict(predict_data)
print(predict_result[0])

predict_data_lst = []
for i in range(len(predict_result)):

    data = {
        'Id': str(i),
        'Category': predict_result[i]
    }
    predict_data_lst.append(data)


################ write out file ################


print('write out header')
fieldnames = ['Id', 'Category']

with open('naive_bayes_' + str(VERSION) + '.csv', 'w') as csvfile:
    # just write headers now
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

print('write out file')
with open('naive_bayes_' + str(VERSION) + '.csv', 'a+') as csvfile:
    print('-', end="")
    sys.stdout.flush()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerows(predict_data_lst)
