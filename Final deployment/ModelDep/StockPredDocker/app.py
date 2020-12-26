import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import nltk
nltk.download('wordnet')

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize_text(text):
    return [lemmatizer.lemmatize(w,'v') for w in w_tokenizer.tokenize(text)]

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
    #count_vectorizer = CountVectorizer(max_features=100, min_df=1, max_df=1,stop_words='english',tokenizer=lemmatize_text)
    count_vectorizer = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("vectorfeature.pkl", "rb")))

    countvn=count_vectorizer.transform(input_final.values)


    #final_features = [np.array(int_features)]
    #prediction = model.predict(countvn)

    if(model.predict(countvn)[0])==1:
        output='+ive'
    else:
        output='-ive'

    #output = round(prediction[0], 2)

    return render_template('index.html', input_text='Input News : {}'.format(int_features[0]),prediction_text='sentiment for news {}'.format(output))

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)


#if __name__ == "__main__":
#    app.run(debug=False)