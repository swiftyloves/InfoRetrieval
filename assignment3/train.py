import sys

import csv
ifile  = open('traindata_clean_2.csv', "r")
read = csv.reader(ifile)
posts = []
documents = []
labels = []
for row in read :
    posts.append(row)
    labels.append(row[0])
    documents.append(row[1])

print(posts[0])
print('documents[0]:',documents[0])
print(documents[0])
print(len(documents))

######## Feature Selection ##########

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1,2), min_df = 0, stop_words = 'english')
print('vectorizer.fit_transform(documents)...')
tfidf_matrix = vectorizer.fit_transform(documents)
# tfidf_matrix:
# [[ 0.          0.          0.16903085  0.16903085  0.16903085  0.16903085
#    0.          0.          0.          0.          0.16903085  0.          0.
#    0.16903085  0.16903085  0.          0.          0.          0.          0.
#    0.          0.16903085  0.16903085  0.          0.          0.          0.
#    0.16903085  0.16903085  0.          0.          0.16903085  0.16903085
#    0.16903085  0.16903085  0.          0.          0.          0.
#    0.16903085  0.16903085  0.16903085  0.16903085  0.16903085  0.16903085
#    0.16903085  0.16903085  0.16903085  0.16903085  0.16903085  0.16903085
#    0.16903085  0.16903085  0.          0.          0.          0.          0.
#    0.          0.          0.          0.16903085  0.16903085  0.          0.
#    0.          0.          0.16903085  0.16903085  0.          0.          0.
#    0.          0.          0.          0.          0.          0.          0.
#    0.16903085  0.16903085  0.          0.          0.        ]
#  [ 0.14285714  0.14285714  0.          0.          0.          0.
#    0.14285714  0.14285714  0.14285714  0.14285714  0.          0.14285714
#    0.14285714  0.          0.          0.14285714  0.14285714  0.14285714
#    0.14285714  0.14285714  0.14285714  0.          0.          0.14285714
#    0.14285714  0.14285714  0.14285714  0.          0.          0.14285714
#    0.14285714  0.          0.          0.          0.          0.14285714
#    0.14285714  0.14285714  0.14285714  0.          0.          0.          0.
#    0.          0.          0.          0.          0.          0.          0.
#    0.          0.          0.          0.14285714  0.14285714  0.14285714
#    0.14285714  0.14285714  0.14285714  0.14285714  0.14285714  0.          0.
#    0.14285714  0.14285714  0.14285714  0.14285714  0.          0.
#    0.14285714  0.14285714  0.14285714  0.14285714  0.14285714  0.14285714
#    0.14285714  0.14285714  0.14285714  0.14285714  0.          0.
#    0.14285714  0.14285714  0.14285714]]
# (6111, 115433)    0.200381919894
# (#documetn, some term index) tf-idf score


######## Feature Selection ##########

from sklearn.feature_selection import chi2
print('chi2...')
# http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html
# chi2(X, y)
# X : {array-like, sparse matrix}, shape = (n_samples, n_features_in)
# y : array-like, shape = (n_samples,)
# Target vector (class labels).

tmp = chi2(tfidf_matrix, labels)
print('features_tfidf = tmp[1] < 0.05')
selected_features_mapping = tmp[1] < 0.07 # magic number
print('sum(selected_features_mapping)')
# the number of features is equal to the value sum(selected_features_mapping)
print(sum(selected_features_mapping))
# only left to the feature that matters
# tfidf_matrix = tfidf_matrix[:, selected_features_mapping]

feature_names_lst = vectorizer.get_feature_names()
selected_feature_names_lst = []
print('selected_features: ')
for i in range(len(feature_names_lst)):
    if selected_features_mapping[i] == True: #####
        print(i, ' ', feature_names_lst[i])
        selected_feature_names_lst.append(feature_names_lst[i])
print('len(selected_feature_names_lst)')
print(len(selected_feature_names_lst))

############# map selected feature to corresponded tfidf score
tfidf_dict_lst = []


for i in range(len(documents)):
    print('.', end="")
    if i % 500 == 0:
        print('|', end="")
    if i % 1000 == 0:
        print('')
    sys.stdout.flush()
    full_data_dict = dict(zip(vectorizer.get_feature_names(), tfidf_matrix[i].toarray()[0]))
    selected_data_dict = {}
    selected_data_lst = []

    for k in selected_feature_names_lst:
        value = full_data_dict[k] if k in full_data_dict else 0.0
        selected_data_dict[k] = value
        selected_data_lst.append(str(value))

    data = {
        'label': labels[i],
        'tfidf': " ".join(selected_data_lst)
    }
    tfidf_dict_lst.append(data)
print('len(tfidf_dict_lst):',len(tfidf_dict_lst))
print(tfidf_dict_lst[0])

############# CACHE ##################

print('write out header')
fieldnames = ['label', 'tfidf']

with open('tfidf_dict_lst.csv', 'w') as csvfile:
    # just write headers now
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

print('write out file')
with open('tfidf_dict_lst_007_3_string.csv', 'a+') as csvfile:
    print('-', end="")
    sys.stdout.flush()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerows(tfidf_dict_lst)
