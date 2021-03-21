
# In[63]:

import sys,json
import pickle
loaded_model = pickle.load(open('PCOS_model.sav', 'rb'))


# In[64]:


import pandas as pd 
df=pd.read_csv('PCOS_final_cleaned_2.csv')
df.columns


# In[65]:


def make_input_usable(M):
    if M[0]== 'n':
        M[0]=0
    elif M[0]=='y':
        M[0]=1
    elif M[0]=='hb':
        M[0]=2
    elif M[0]=='im':
        M[0]=3
    elif M[0]=='ib':
        M[0]=4
    else :
        M[0]=0
        
    for i in range(1, 12):
        if M[i]=='y':
            M[i]=1
        elif M[i]=='hm':
            M[i]=1
        elif M[i]=='out':
            M[i]=0
        else:
            M[i]=0
            
    for i in range(12, 14):
        s1=M[i]
        s1=s1[0:2]
        s1=int(s1)
        M[i]=s1
        
    for i in range(14, 18):
        if M[i]=='y':
            M[i]=1
        else:
            M[i]=0
            
    if M[18]== 'ed':
        M[18]=1
    elif M[18]=='w':
        M[18]=2
    elif M[18]=='m':
        M[18]=3
    elif M[18]=='y':
        M[18]=4
    else :
        M[18]=1
        
    
    return M


# In[69]:


def user_input(): 
    # M=['y','y','y','y','y','y','y','y','y','y','y','y','3','5','y','y','y','y','e']
    M=json.loads(sys.argv[1])
    # regularity_periods=input("are your periods regular? Enter:\ny for Yes\nn for no\nim for Infrequent Menses\nib for Irregular Bleeding\nhb for Heavy Bleeding\n")
    # M.append(regularity_periods)
    # weight_gain=input("weight gain? ")
    # M.append(weight_gain)
    # excess_hair=input("excess hair? ")
    # M.append(excess_hair)
    # dark_patches=input('dark patches? ')
    # M.append(dark_patches)
    # pimples=input('pimples? ')
    # M.append(pimples)
    # depression_and_anxiety=input('depression and anxiety? ')
    # M.append(depression_and_anxiety)
    # family_diabetes  =input('family diabetes? ')
    # M.append(family_diabetes)
    # mantaining_weight=input('mantaining weight? ')
    # M.append(mantaining_weight)
    # oilyskin=input("oilyskin? ")
    # M.append(oilyskin)
    # hair_thinning=input('hair thinning? ')
    # M.append(hair_thinning)
    # freq_eat_places=input('freq eat places? hm for home, out for outside food ')
    # M.append(freq_eat_places)
    # regular_exercise=input("regular exercise? ")
    # M.append(regular_exercise)
    # sleep_time=input('what time do you usually sleep after? ')
    # M.append(sleep_time)
    # wake_time=input("what time do you usually wake up at? ")
    # M.append(wake_time)
    # hostel_stress=input("hostel stress? ")
    # M.append(hostel_stress)
    # personal_problems=input("personal problems? ")
    # M.append(personal_problems)
    # peer_pressure=input('peer pressure? ')
    # M.append(peer_pressure)
    # dietrty_habits=input("dietrty habits? ")
    # M.append(dietrty_habits)
    # fast_foods_freq=input("fast food? ed: everyday, w: weekly, m: monthly, y: yearly ")
    # M.append(fast_foods_freq)
    
    make_input_usable(M)
        
    return M


# In[70]:


#user_input()


# In[84]:


predict1=user_input()


# In[85]:


import numpy as np
predict1 = np.array(predict1).reshape(1, len(predict1))


# In[86]:


output=loaded_model.predict(predict1)


# In[87]:


if output[0]==False:
    print("You are not at risk of PCOS")
if output[0]==True:
    print("You maybe at risk of PCOS. Please Consult a doctor")


# In[ ]:





# In[ ]:




