#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from textblob import TextBlob
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
#%matplotlib inline
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd


# In[30]:



class Analysis:
    def __init__(self, term):
        self.term = term
        self.url =  'https://news.google.com/search?q={0}&source=lnms&tbm=news'.format(self.term)
        self.sentiment = 0
        self.subjectivity = 0 
        
        
    def run(self):
        webpage = requests.get(self.url)
        soup = BeautifulSoup(webpage.text , 'html.parser')
        #print(soup.text)
        extracted = soup.find_all('a' , class_ = "DY5T1d")
        for x,h in enumerate(extracted):
            
            print(x)
            print('gaaap')
            print(h.string)
           
            blob = TextBlob(h.string)
            self.sentiment+=blob.sentiment.polarity/len(extracted)
            #print(self.sentiment)
            self.subjectivity+=blob.sentiment.subjectivity/len(extracted)
           
            
            
        
        


# In[31]:


a = Analysis('Corona')
a.run()
print(a.sentiment , a.subjectivity)


# In[5]:


url2 = 'https://news.google.com/search?q=corona&source=lnms&tbm=news'


# In[19]:


#use this to save resuts as csv
x=1
sentiment_list = list()
subjectivity_list = list()
main_file = dict()
while x<30:
    webpage2 = requests.get(url2)
    soup2 = BeautifulSoup(webpage2.content , 'html.parser')
    cleaned = soup2.find_all( 'a' , class_ = "DY5T1d")
    sentiment = 0
    subjectivity = 0
    for s in cleaned:
        #print(s.string)
        blob = TextBlob(s.string)
        sentiment += blob.sentiment.polarity/len(cleaned)
        subjectivity +=blob.sentiment.subjectivity/len(cleaned)
        
    
        #print( sentiment , subjectivity)
    sentiment_list.append(sentiment)
    subjectivity_list.append(subjectivity)
    main_file = {'sentiment':sentiment_list , 'subjectivity': subjectivity_list }
    df = pd.DataFrame(main_file)
    df.to_csv('plot it')
    x+=1
    time.sleep(1)
print(main_file)


# In[32]:


df = pd.read_csv('plot it')


# In[34]:


x = df['sentiment']
y = df['subjectivity']
plt.plot(x , color ='red')
plt.plot(y,color='blue')
plt.show()


# In[ ]:




