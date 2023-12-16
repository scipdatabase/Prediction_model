#!/usr/bin/env python
# coding: utf-8

# In[49]:


#import libraries
import pandas as pd
import numpy as np
from keras.models import model_from_json
from sklearn.preprocessing import LabelEncoder
import joblib  # To save and load LabelEncoder


# In[56]:


# load json and create model
json_file = open('model_elu.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_elu.h5")
print("Loaded model from disk")
le = joblib.load('label_encoder.pkl')


# In[57]:


def preprocess_categorical_features(data, le):
    # Assuming 'Parameter' is a categorical feature in your dataset
    data['Parameter'] = le.transform(data['Parameter'])
    return data


# In[58]:


#Load the data for making predictions with the model 
X_test1 = pd.read_csv('example.csv')


# In[59]:


X_test1.drop(X_test1.columns[[0]],axis=1, inplace=True)


# In[60]:


predictions = loaded_model.predict(X_test1)


# In[62]:


#save the output
pdf[['predicted_class', 'predicted_reg']].to_csv('prediction_output.csv', index=False)


# In[63]:


pdf


# In[ ]:




