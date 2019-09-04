#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, SPEEDY!'


# In[2]:


#app.run()


# In[ ]:


'''

Application 運行（heroku版）

'''

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])


# In[ ]:




