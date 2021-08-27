from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import requests
import re
import os
import nltk


def BUILD_FREQBASED_INDEX(D):

#########opening, reading, and tokenizing 500 pages

    files=[]
    for filename in os.listdir(D):
        files.append(D+filename)

    n=0
    index={}
    index2={}
    token_list=[]
    uniquetokens=[]
    for d in files:
        n+=1
        
        with open(d,encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f, 'html.parser')
            text=soup.get_text()
            text=text.lower()
            text=re.sub("\[.*\]", " ", text)
            text=re.sub(r'[^\w\s]', " ", text)
            text=text.replace("\\", " ")
            tokens=nltk.word_tokenize(text)

            token_list.append(tokens)
        #print(tokens)

###############adding tokens and values to dictionary    
        for token in tokens:
            if token not in index:
                index[token]=[]
                index[token].append([n,0])
            prev_val=index[token][0][1]
            index[token][0][1]=prev_val+1
        

        for key in index:
            if key not in index2:
                index2[key]=[]
            index2[key].append([n, index[key]])
            

        index.clear()




#####################saving index to text file
            
    f=open('freq_index.txt', 'w', encoding = 'utf-8')
    for term in index2:
        f.write(term+' => ')
        for posting in index2[term]:
            fre=posting[1]
            f.write('(' +str(fre)+')'+', ')
        f.write('\n')
    f.close()

#################saves unique terms to text file from unique token list    
    length = len(index2.keys())
    fi=open('uniqueterms.txt', 'w', encoding = 'utf-8')
    fi.write("number of unique terms: " + str(length))
    f.write('\n')
    fi.write(str(index2.keys()))
    fi.close()

BUILD_FREQBASED_INDEX('C:/Users/Debbie Home Workstat/Desktop/500pg/')

