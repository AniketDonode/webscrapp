#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


# In[2]:


#pip install html5lib


# In[3]:


url="https://coronaclusters.in/maharashtra"


# In[4]:


r=requests.get(url)


# In[5]:


# r.text[1000:2000]


# In[6]:


soup=BeautifulSoup(r.text,'html.parser')


# In[7]:


result=soup.find('table')


# In[8]:


len(result)


# In[9]:


# result


# In[10]:


result_one=result.find_all('tr')


# In[11]:


# result_one


# In[12]:


table_data=result.find_all('tr')


# In[13]:


table_data=table_data[1:]


# In[14]:


# table_data


# In[15]:


len(table_data)


# In[16]:


table_data[1]


# In[17]:


xy=table_data[1].contents


# In[18]:


for item in xy:
    print(item.text)


# In[19]:


print(xy)


# In[20]:


data=[]
for result in table_data:
    text=result.find('th').text
    z=result.contents[1].text
    z2=result.contents[2].text
    z3=result.contents[3].text
    z4=result.contents[4].text
    z5=result.contents[5].text
    z6=result.contents[6].text
    
    data.append((text,z,z2,z3,z4,z5,z6))
    


# In[21]:


data


# In[22]:


df=pd.DataFrame(data,columns=['District','Total_cases','New Cases','Total Deaths','New Deaths','Total Recovered','Active Cases'])


# In[ ]:





# In[23]:


import matplotlib.pyplot as plt


# In[24]:


df.columns=df.columns.str.replace(" ","_")


# In[25]:


df


# In[26]:


df.to_csv('covid_maha.csv',index=False)


# In[27]:


df2=pd.read_csv('covid_maha.csv',index_col='District')


# In[31]:


df2.head()


# In[32]:


df2.index.name=None


# In[33]:


df2.head()


# In[36]:


df2[['Active_Cases']].sort_values('Active_Cases',ascending=False).head().plot(kind='bar',
                                                           color='red')
plt.style.use('ggplot')
plt.title("covid Report of Maharastra")
plt.xlabel("Districts")
plt.ylabel("Active Cases")

plt.show()


# In[ ]:




