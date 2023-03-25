from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from string import punctuation
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download("wordnet")
nltk.download("omw-1.4")
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import pickle

nltk.download('stopwords')

set(stopwords.words('english'))

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    final =False
    #convert to lowercase
    text1 = request.form['text1'].lower()
    if text1!="" and text1!= None:
        final=True
    
    x=[text1]
    model_pickle = pickle.load(open('model.pkl','rb'))
    Tfidf_pickle = pickle.load(open('vectorizer.pkl','rb'))
    label_enc= pickle.load(open('label_enc.pkl','rb'))

    lemmatizer = WordNetLemmatizer()
    lemmatized_messages = []

    for message in x:
        lemmatized_message = " ".join([lemmatizer.lemmatize(word,pos="v") for word in message.split()])
        lemmatized_messages.append(lemmatized_message)


    X = Tfidf_pickle.transform(lemmatized_messages)

    y=model_pickle.predict(X)
    y=label_enc.inverse_transform(y)

    result=f'"{text1}" is {y[0]}'
   

    return render_template('form.html',final=final, result=result)
    #return render_template('form.html', final=compound, text1=text_final,text2=dd['pos'],text5=dd['neg'],text4=compound,text3=dd['neu'])

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
