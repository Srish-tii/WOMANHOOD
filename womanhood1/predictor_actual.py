

# In[27]:


import pandas as pd
import numpy as np
import tensorflow as tf



# In[28]:

import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import SGD


# In[29]:


import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from sklearn.preprocessing import OneHotEncoder


# In[47]:


def load_dataset(filename):
    df = pd.read_csv(filename, encoding = "latin1", names = ["symptom", "disease"])
 
    disease = df["disease"]
    unique_disease = list(set(disease))
    symptom = list(df["symptom"])
    return (disease, unique_disease, symptom)


# In[50]:


disease, unique_disease, symptom = load_dataset("kaggle_dataset_final.csv")


# In[7]:


stemmer = LancasterStemmer()


# In[48]:


def cleaning(symptom):
    words = []
    for s in symptom:
        clean = re.sub(r'[^ a-z A-Z 0-9]', " ", s)
        w = word_tokenize(clean)
        #stemming
        words.append([i.lower() for i in w])
    
    return words  


# In[51]:


cleaned_words = cleaning(symptom)


# In[53]:


def create_tokenizer(words, filters = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'):
    token = Tokenizer(filters = filters)
    token.fit_on_texts(words)
    return token


# In[54]:


def max_length(words):
    return(len(max(words, key = len)))


# In[55]:


word_tokenizer = create_tokenizer(cleaned_words)
vocab_size = len(word_tokenizer.word_index) + 1
max_length = max_length(cleaned_words)


# In[56]:


def encoding_doc(token, words):
    return(token.texts_to_sequences(words))


# In[57]:


encoded_doc = encoding_doc(word_tokenizer, cleaned_words)


# In[58]:


def padding_doc(encoded_doc, max_length):
    return(pad_sequences(encoded_doc, maxlen = max_length, padding = "post"))


# In[62]:


output_tokenizer = create_tokenizer(unique_disease,filters = '!"#$%&()*+,-/:;<=>?@[\]^`{|}~')


# In[65]:


encoded_output = encoding_doc(output_tokenizer,disease)


# In[66]:


import numpy as np
encoded_output = np.array(encoded_output).reshape(len(encoded_output),1)



# In[67]:


def one_hot(encode):
    o = OneHotEncoder(sparse = False)
    return(o.fit_transform(encode))


# In[22]:


model = load_model("test5.h5")


# In[30]:


def predictions(text):
    clean = re.sub(r'[^ a-z A-Z 0-9]'," ", text)
    test_word = word_tokenize(clean)
    test_word = [w.lower() for w in test_word]
    test_ls = word_tokenizer.texts_to_sequences(test_word)
    #print(test_word)            ##
    #Check for unknown words
    if [] in test_ls:
        test_ls = list(filter(None, test_ls))
    
    test_ls = np.array(test_ls).reshape(1, len(test_ls))
 
    x = padding_doc(test_ls, max_length)
  
    pred = model.predict(x)
  
    return pred 


# In[31]:


def get_final_output(pred, classes):
    predictions = pred[0]
 
    classes = np.array(classes)
    ids = np.argsort(-predictions)
    classes = classes[ids]
    predictions = -np.sort(-predictions)
    pred_disease=classes[0]
    pred_disease1=classes[1]
    pred_disease2=classes[2]
 
    #for i in range(pred.shape[1]):
        #print("%s has confidence = %s" % (classes[i], (predictions[i])))
    
    print("You may have",pred_disease,"with confidence level: ",predictions[0]*100,"%")
    print("or You may have",pred_disease1,"with confidence level: ",predictions[1]*100,"%")
    print("or You you may have",pred_disease2,"with confidence level: ",predictions[2]*100,"%")
    return pred_disease,predictions[0]


# In[32]:


def user():
    text=sys.argv[1]
    pred = predictions(text)
    get_final_output(pred,unique_disease)


# In[68]:


user()


# In[ ]:




