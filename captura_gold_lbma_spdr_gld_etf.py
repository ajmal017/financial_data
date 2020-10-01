#!/usr/bin/env python
# coding: utf-8

# In[84]:


#!pip install investpy yfinance
import investpy
from datetime import datetime
import yfinance as yf
import pandas as pd


# In[69]:


# Retrieve all the available stocks as a Python list
investpy.get_stocks(country='brazil')


# In[70]:


# Retrieve all the available etfs as a Python list
investpy.get_etfs(country='brazil')


# In[138]:


# Retrieve all the indexes
investpy.get_indices()

# get data using investing website
indice = 'LBMA Gold Fixing Price'
country = 'united kingdom'
from_date = '19/11/2004'
to_date = '25/09/2020'
#investpy.indices.get_index_historical_data(indice, country, from_date, to_date, order='ascending', interval='Daily')
for item in investpy.search.search_quotes('OZ1'):
    print(item)


# In[72]:


# get bonds
investpy.get_bonds(country='brazil')


# In[73]:


# get data using investing website
etf = 'SPDR Gold Shares'
country = 'united states'
from_date = '19/11/2004'
to_date = '25/09/2020'
investpy.etfs.get_etf_historical_data(etf, country, from_date, to_date, order='ascending', interval='Daily')


# In[74]:


# get data using yahoo finance
# get historical market data
hist = yf.Ticker("GLD").history(period="max")
hist


# In[75]:


# Retrieve all available funds information as a pandas.DataFrame
funds_df = investpy.get_funds(country='brazil')
funds_df


# In[76]:


# Retrieve a listing of all the available fund names
funds_list = investpy.get_funds_list(country='brazil')
funds_list

for fundo in funds_list:
    if 'caixa' in fundo.lower():
        print(fundo)


# In[77]:


# pega os dados recentes do fundo
nome_fundo = 'Fundo De Investimento Caixa Master Personalizado 50 Renda Fixa Longo Prazo'
investpy.get_fund_recent_data(fund=nome_fundo, country='brazil')


# In[78]:


# Retrieves historical data of 'Bankia Cauto Pp', which is a fund from 'Spain', on the specified date range as a pandas.DataFrame
investpy.get_fund_historical_data(fund=nome_fundo, country='brazil', from_date='01/01/2018', to_date='25/09/2020')


# In[91]:


# LBMA - Quandl
url = 'https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key=x1dVtsgtRJvLJ1tyNh8S'
df = pd.read_json(url)
df = pd.DataFrame(df['dataset']['data'], columns=df['dataset']['column_names'])
df


# In[ ]:




