from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import requests
import re
import os
import nltk


def BUILD_POSBASED_INDEX(D):

#########opening, reading, and tokenizing 500 pages

    files=[]
    for filename in os.listdir(D):
        files.append(D+filename)

    n=0
    index={} 
    for d in files:
        n+=1
        #print(d+str(n)+'\n')
        with open(d,encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f, 'html.parser')
            text=soup.get_text()
            text=text.lower()
            text=re.sub("\[.*\]", " ", text)
            text=re.sub(r'[^\w\s]', " ", text)
            text=text.replace("\\", " ")
            tokens=nltk.word_tokenize(text)
            #print(tokens)



            #inverted list storage temporary
        index2={}       #inverted list storage final


    ########adding tokens and values to dictionary
        p=0
        for token in tokens:
            if token not in index:
                index[token]=[]
                index[token].append([n, p])
            else:
                index[token].append([n, p])

            p+=1

        
                        
    ###########saving index to text file
    f=open('pos_index.txt', 'w', encoding = 'utf-8')
    for term in index:
        f.write(term+' => ')
        for posting in index[term]:
            doc_id=posting[0]
            fre=posting[1]
            #f.write('(' + doc_id+','+fre+')')
            f.write('['+str(doc_id)+', '+str(fre)+']')
        f.write('\n')
    f.close()


BUILD_POSBASED_INDEX('C:/Users/Debbie Home Workstat/Desktop/500pg/')
