#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd 


# In[4]:


def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'} 
    url = f'https://ae.indeed.com/jobs?q=data+analyst+&l=dubai&start={page}&pp=gQAPAAABgmL7RxEAAAAB4GR8vwAfAQEBBwEemO4yeiaPFDjt5WWUl6nNbtlDembDN04VGwAA&vjk=b3468a3c4a17ff54'
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'slider_item')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ = 'companyName').text.strip()
        summary = item.find('tr', class_ = 'underShelfFooter').text.strip().replace('\n', '')
        
        job = {
            'title': title,
            'company': company,
            'summary': summary
        }
        joblist.append(job)
    return
    
joblist = []

for i in range (0, 40, 10):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')


# In[ ]:




