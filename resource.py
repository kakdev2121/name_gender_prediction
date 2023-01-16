# API creation
import numpy as np
import pandas as pd
import pickle
import os

# master dictionary for label encoding got from gender name dataframe
alpha_number = { ',': 0,'x': 1,'z': 2,'n': 3,'j': 4,'q': 5,'u': 6,'c': 7,'m': 8,'i': 9,'g': 10,'o': 11,'e': 12,'b': 13,'t': 14,'v': 15,'k': 16,'r': 17,'s': 18,'y': 19,'h': 20,'a': 21,'f': 22,
 'd': 23,
 'l': 24,
 'p': 25,
 'w': 26}

# max length is the maximum lenght of name in the corpus which is 15 in gender_name data base
maxlen = 15

def zero_padding(list1):
    for i in range(len(list1),maxlen):
        list1.append(0)
    return(list1)
    
def set_flag(i):
    tmp = np.zeros(len(alpha_number))
    tmp[i] = 1
    return(tmp)

def new_data_encode(name_encoded_vector):
    aa = []
    for i in name_encoded_vector:
        aa.append(set_flag(i))
    return(aa)

dirname = os.path.dirname(__file__)


def gender_prediction(name):
    try:
        chk_data = np.array(tuple(new_data_encode(zero_padding([alpha_number[i] for i in name.lower()]))))
        chk_data = chk_data.reshape(1,15,27)
        loaded_model = pickle.load(open("./gender_classification_lstm.h5", 'rb'))
        print("Model Loaded")
       # loaded_model = os.path.join(dirname, "gender_classification_lstm.sav",'rb')
        prediction = loaded_model.predict(chk_data)
#         print(prediction)
        if prediction[0][0] > prediction[0][1]:
            return("M")
        else:
            return("F")
    except Exception as e:
            print(f"check the data {e}")
    
    