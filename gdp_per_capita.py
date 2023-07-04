#!/usr/bin/env python
# coding: utf-8

# # gdp per capita in Canada 

# From 1970 to 2016, the examination of GDP per capita in Canada demonstrates patterns in economic growth and 
# living standards.During this time, Canada's GDP per capita increased generally, suggesting increased affluence.
# Fluctuations occurred as a result of a variety of variables, including economic cycles and policy changes. 
# This research sheds light on Canada's economic evolutionby emphasizing periods of prosperity and pinpointing probable
# implications on the country's level of life.

# In[2]:


import numpy as np
import random 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px


# In[14]:


gdp_per_capita_file = pd.read_csv('C://Users//mande//OneDrive//Desktop/canada_per_capita_income.csv')


# # list of years

# In[15]:


df= pd.DataFrame(gdp_per_capita_file)
df


# # Maximum gdp gdp capita

# In[25]:


per_capita_income_max = df['per capita income (US$)'].max()


# In[26]:


per_capita_income_max


# In[46]:


max_in_year= df[df['per capita income (US$)']==42676.46837]
max_in_year


# In 2013, Canada achieved a significant milestone with a peak per capita income of $42,676.47.
# 

# # minimum gdp captia

# In[28]:


per_capita_income_min = df['per capita income (US$)'].min()
per_capita_income_min


# In[34]:


min_in_year= df[df['per capita income (US$)']==3399.299037]
min_in_year


# lowest gdp per capita can be seen in 1970 that was (3399.299037)

# In[48]:


years= df['year']


# In[49]:


per_capita=df['per capita income (US$)']


# In[40]:


years = df['year']
per_capita = df['per capita income (US$)']
# Line graph
plt.figure(figsize=(10, 6))
plt.plot(years, per_capita, marker='o', linestyle='-', color='b')
plt.xlabel('Year')
plt.ylabel('Per Capita Income (US$)')
plt.title('Per Capita Income Over Time (Line Graph)')
plt.grid(True)
plt.show()

# Bar graph
plt.figure(figsize=(10, 6))
plt.bar(years, per_capita, color='b')
plt.xlabel('Year')
plt.ylabel('Per Capita Income (US$)')
plt.title('Per Capita Income Over Time (Bar Graph)')
plt.grid(True)
plt.show()


# The graph of GDP per capita in Canada shows a steady rise from 1970 to 2000, followed by a significant rise in the following years. However, there is a little reduction in the tendency following that. This points to a period of steady economic expansion and rising living standards until the early 2000s. The ensuing fall indicates that there might be obstacles or economic changes during that time period. Overall, the graph demonstrates Canada's GDP per capita's overall positive trend across the investigated period, with notable differences in the latter years warranting more examination.

# In[ ]:




