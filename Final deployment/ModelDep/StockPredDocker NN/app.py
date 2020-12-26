import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Model
from keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding, Bidirectional
from keras.optimizers import RMSprop
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence , text
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
import pickle
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
model._make_predict_function()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    input_final=pd.Series(int_features[0])
    
    max_words = 1000
    max_len = 150
    tokeval = Tokenizer(num_words=max_words)
    tokeval.fit_on_texts(input_final)
    sequenceseval = tokeval.texts_to_sequences(input_final)
    sequenceseval_matrix = sequence.pad_sequences(sequenceseval,maxlen=max_len)

#pickle.dump(Atnmodel2,open('BiDirRNNWithAttention.pkl','wb'))

    output=(model.predict(sequenceseval_matrix)[0])

    return render_template('index.html', input_text='Input News : {}'.format(int_features[0]),prediction_text='sentiment probabilty for news {}'.format(output))

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)


#if __name__ == "__main__":
#    app.run(debug=False)