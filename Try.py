#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date, datetime


# In[ ]:


from Article import NYTAPI


# In[ ]:


nyt = NYTAPI(
    key="Sa2OXGEz5mdVEbOgemrjxenQlGeOvElB", 
    parse_dates=True,
)


# In[ ]:


biden = nyt.article_search("biden")


# In[ ]:


biden_january = nyt.article_search(
    query="biden", dates={"begin": date(2021, 1, 1), "end": date(2021, 1, 31)}
)


# In[ ]:


biden = nyt.article_search(
    "biden",

