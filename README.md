#Financial sentences Sentiment Analyzer Python Web App

A web interface that performs sentiment analysis using machine learning

#### Basic Features
* Remove stop words 
* Pre-process text (remove punctuation, lower case)
* Lemmatization of words

#### Sentiment Analysis
* Show the sentiment of the finanancial statement


### Prerequisites

This app is built using **Python 3.9**

## Start Service
Now, to start the application, do the following:

    python app.py

Server will start and  you can connect by opening the web browser and connecting one of the URLs:

    http://127.0.0.1:5002/

### Batch Upload

TO succesfully upload a file, the file type must be CSV and also, the column containing the tweet for sentiment analysis must be named "text".
when the prediction is made, a report can be download with 0 = negative and 1 = positive sentiments

### Some Screenshots

<p align="center">
<img src="https://github.com/PrajaktaSelukar/Sentiment-Analysis-Web-App/blob/master/img/Flask-sample-1.png" alt="Drawing" style="width:40%;"/>
</p>

<p align="center">
<img src="https://github.com/PrajaktaSelukar/Sentiment-Analysis-Web-App/blob/master/img/Flask-sample-2.png" alt="Drawing" style="width:40%;"/>
</p>


## Use Heroku app

The app can be tested on heroku [sentiment-analyzer3.herokuapp.com/](https://sentiment-analyzer3.herokuapp.com/).

<p align="center">
<img src="https://github.com/PrajaktaSelukar/Sentiment-Analysis-Web-App/blob/master/img/Heroku-result.png" alt="Drawing" style="width:40%;"/>
</p>

