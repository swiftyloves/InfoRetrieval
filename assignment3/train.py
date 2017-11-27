import csv
ifile  = open('traindata_clean.csv', "r")
read = csv.reader(ifile)
posts = []
for row in read :
    posts.append(row)




########  SVM ##########

# from sklearn import svm


########  export prediction ##########
# res = np.array([np.arange(len(predicted_final)), predicted_final])
# res = np.transpose(res)
# with open('prediction/pohechen_xg12.csv', 'w') as w:
#     w.write('Id,Category\n')
#     np.savetxt(w, res, fmt='%i',  delimiter=",")

