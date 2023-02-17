#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json

# Set the API endpoint and query parameters
url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
params = {'api-key': 'tmziMUTxoYVQz9hdTiegZJprdlshm3H0', 'q': 'covid-19', 'begin_date': '20210101', 'end_date': '20210201'}

# Make the API request
response = requests.get(url, params=params)

# Parse the JSON response to extract the article text data
if response.status_code == 200:
    data = json.loads(response.text)
    articles = data['response']['docs']
    for article in articles:
        # Extract the headline and lead paragraph text from each article
        headline = article['headline']['main']
        lead_paragraph = article['lead_paragraph']
        # Do further processing or store the text data as needed
else:
    print('Error: Unable to retrieve data from NY Times API.')


# In[ ]:




