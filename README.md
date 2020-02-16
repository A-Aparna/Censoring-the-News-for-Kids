# NLP-Newsheadline-censoring
## Introduction
Parental Guide to censoring the news articles for kids: The aim of this project is to use Sentiment analysis on news articles. So this NLP model will decide whether a piece of news article should be allowed for kids to read on not. Based on the model outputs the news articled will be censored if found inappropriate. 
Demo can be seen [here](https://newsheadline-censoring.herokuapp.com/).<br>


![https://newsheadline-censoring.herokuapp.com/](https://github.com/A-Aparna/NLP-Newsheadline-censoring/blob/master/Images/AppDemo.jpg)
<br>
The input to the data can be given in 2 ways:
1)	Enter the URL to scrape: Enter the URL of the Newspaper website you want to censor. (Currently it’s been customized to work only for ‘inshorts’ news website. For other websites it can be customised.)
Input: “https://inshorts.com/en/read”
Output: List of the headlines from the ‘inshorts’ along with their URL’s displaying only the ones appropriate for kids to read.
2)	Enter the Headline: Enter one or more headlines in the text area. Each headline should be on a new line.
Input: eg: A man was murdered
	    A girl wins medal in chess championship 
Output: List of the headlines displaying only the ones appropriate for kids to read.

### List of files in the repository
*[app.py](https://github.com/A-Aparna/NLP-Newsheadline-censoring/blob/master/app.py) - The python code to run the model and deploy it on the webpage.
*Pickle files (headline_transform,censor_predict )
*[Templates](https://github.com/A-Aparna/NLP-Newsheadline-censoring/tree/master/templates) - Folder containing the html pages.
*Static - CSS styling
*Procfile, Requirements.txt -for deployement on Heroku

## About the Data

## Exploratory Data Analysis

## Modeling
1) Scraped various websites and collected news headlines on different days and archives to have a variety in the training dataset.
2) Manually labelled the dataset as to be censored (label=1) and not to be censored (label=0) for the training dataset of roughly 2000 headlines.
3) Trained the data on various models using NLTK library using various methods: TF-IDF, Skipgrams and used ML models: Tree classifier, Naïve Based and Logistic regression.
4) Used flask model to create ReST API’s and deploy the model locally.
5) Used Heroku cloud service to deploy the model as a web app.


## Summary
