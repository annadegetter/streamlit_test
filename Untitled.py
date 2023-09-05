#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st 
import pandas as pd
import numpy as np


# In[3]:


st.title("BPS Analysis Dashboard")


# In[4]:


uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


# In[7]:


if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file,sep=';')

    # Display the DataFrame
    st.write("Uploaded Data:", df)

    # Perform analysis (e.g., basic statistics)
    st.write("Basic Statistics:")
    st.write("Number of Rows:", df.shape[0])
    st.write("Number of Columns:", df.shape[1])
    st.write("Summary Statistics:", df.describe())


# In[8]:


#!jupyter nbconvert --to script Untitled.ipynb


# In[ ]:




