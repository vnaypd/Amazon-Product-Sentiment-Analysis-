import argparse
import json
import io
import tensorflow as tf
from tensorflow import keras
from utils import process
from config import max_length, padd_type, trunc_type

model = keras.models.load_model('models/1stmodel.h5')



def load_tokenizer():
    with open('tokenizer.json') as f:
        data = json.load(f)
        tokenizer = keras.preprocessing.text.tokenizer_from_json(data)
    return tokenizer

def predict_review(review):
    #review = "this is the ok thing i\'ve ever bought"
    #review = input("please enter review for sentiment analysis:")
    
    tokenizer = load_tokenizer()
    
    processed_review = process(review)
    encoded_review = tokenizer.texts_to_sequences([processed_review])[0]
    encoded_review = keras.preprocessing.sequence.pad_sequences([encoded_review], maxlen=max_length, padding=padd_type, truncating=trunc_type)
    pred = model.predict(encoded_review)

    if pred[0][0] > 0.6:
        return('Review: "'+review+'" is Positive with '+str(pred[0][0]*100))
    else:
        return('Review: "'+review+'" is Negative with '+str(100-pred[0][0]*100))
    

#predict_review()
    
