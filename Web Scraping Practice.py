#!/usr/bin/env python
# coding: utf-8

# In[189]:


import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[192]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text,"html")


# In[233]:


table =soup.find_all("table")[1]


# In[234]:


print(table)


# In[241]:


world_table_titles = table.find_all("th")
print(world_table_titles)


# In[248]:


world_table_titles = table.find_all("th")
world_table_titles = [title.text.strip() for title in world_table_titles]
print(world_table_titles)
    


# In[249]:


df = pd.DataFrame(columns = world_table_titles )
df


# In[254]:


column_data = table.find_all("tr")
for row in column_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length]= individual_row_data


# In[255]:


df


# In[275]:


df.to_csv(r'C:\Users\sharang1.dutt\Desktop\List_of_the_largest_companies.xlsx', index = False)


# In[ ]:





# In[ ]:




