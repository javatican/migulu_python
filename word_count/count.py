import numpy as np 
import matplotlib.pyplot as plt

dict_words={}
file=open("a_tale_of_two_cities.txt","r")
total_word_count=0
for i in file:
    # transform into upper case
    i2=i.upper()
    i3=[]
    # transform non-upper-letters to space characters
    for j in i2:
        if j>='A' and j<='Z' :
            i3.append(j)
        else:
            i3.append(" ")
    i4="".join(i3)
    # break up into words
    i5=i4.split()
    # update word count
    total_word_count+=len(i5)
    # loop through words in a line
    for k in i5:
        # get old count for each word. 
        # If the word does not exist, initialize with 0
        old_count = dict_words.get(k,0)
        # update word count and save in dict_words
        dict_words[k]=old_count+1

for key,value in dict_words.items():
    if key=='THE':
        print(key,value)
    if key=='A':
        print(key,value)
    if key=='AN':
        print(key,value)
    if key=='I':
        print(key,value)
    if key=='YOU':
        print(key,value)
    if key=='HE':
        print(key,value)
    if key=='SHE':
        print(key,value)
    if key=='IT':
        print(key,value)
    if key=='THEM':
        print(key,value)
    if key=='IF':
        print(key,value)
    if key=='WHEN':
        print(key,value)
    if key=='WHERE':
        print(key,value)
    if key=='WHAT':
        print(key,value)
    if key=='WHY':
        print(key,value)

    if key=='THRONE':
        print(key,value) 
    
    if key=='ROBBERIES':
        print(key,value) 
#print(total_word_count)
#plot histogram
#num_bins = 20

# fig, ax = plt.subplots()
# data = np.asarray(list(dict_words.values()))
# data = data[data<20]
# # the histogram of the data
# n, bins, patches = ax.hist(data, num_bins, normed=1)

# ax.set_xlabel('Words appear frequency')
# ax.set_ylabel('Probability density')
# ax.set_title(r'Histogram of Words')

# # Tweak spacing to prevent clipping of ylabel
# fig.tight_layout()
# plt.show()