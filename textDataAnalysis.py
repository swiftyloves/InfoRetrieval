import nltk
import numpy as np
import matplotlib.pyplot as plt
import math

# Clean stoplist
f_stoplist = open('assignment1/stoplist.txt','r')
stoplist = f_stoplist.readlines()


for i,w in enumerate(stoplist):
    stoplist[i] = w.replace("\r\n","")

operators = [".",",",":",";","\n","[","]","(",")","{","}","*","-"]
remove_list = stoplist + operators

f = open('assignment1/medhelp.txt','r')
# f = open('assignment1/ehr.txt','r')
line = f.readline().lower()

ehr_map = {}
while(line):
    lines = line.split()
    lines_clean = []
    for w in lines:
        if w not in remove_list:
            lines_clean.append(w)
            ehr_map[w] = ehr_map[w] + 1 if w in ehr_map else 1

    # print lines_clean
    line = f.readline()


# ehr_map = {w1: 3, w2: 2, w3: 3, w4: 4 ...}
f.close()


# plot x-axis: word frequency, proportion of words with the frequency
# cauculate freguency
sum = 0;
freq = []
frequency_map = {}
for w,i in ehr_map.items():
    cnt = ehr_map[w] # ch = 3 when w = w1 and so on
    sum = sum + cnt  
    freq.append(cnt)
    frequency_map[cnt] = frequency_map[cnt] + 1 if cnt in frequency_map else 1

# frequency_map = {3: 2, 2: 1, 4: 1}
print ('frequency_map:',frequency_map)
# freq = [3, 2, 3, 4]
print("sum: ",sum) # sum = 12
freq.sort()
print ('freq:',freq)
freq_set = list(set(freq)) 
# freq_set = [2, 3, 4]

freq_xaxis = map(lambda x: math.log(float(x)/sum, 2), freq_set)
print ('freq_xaxis:',freq_xaxis)
# freq_xaxis = [0.02, 0.03, 0.044]
## freq_xaxis.sort()

sum_word_amount = 0 # equals to all values of frequency_map
for cnt_k in frequency_map:
    sum_word_amount += frequency_map[cnt_k]

print ('sum_word_amount:',sum_word_amount)
proportion_word = []
proportion_word_raw = []
print ('freq_set:',freq_set)
for cnt in freq_set:
    proportion_word_raw.append( float(frequency_map[cnt])/sum_word_amount )
    proportion_word.append( math.log(float(frequency_map[cnt])/sum_word_amount,2))

# print len(proportion_word)
print ('proportion_word_raw:',proportion_word_raw)
print ('proportion_word:',proportion_word)
# print len(freq_xaxis)
# print freq_xaxis
plt.plot(np.array(freq_xaxis), np.array(proportion_word))
plt.xlabel('Word Frequency')
plt.ylabel('Proportion of Words')
plt.show()
# savefig("wf-pw.jpg", transparent=False)




#################### 




