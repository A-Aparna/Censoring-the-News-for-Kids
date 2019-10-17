from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        headline = request.form['message']
        print(type(headline))
        data = [headline]
        data = [l.split(',') for l in ','.join(data).split('\r\n')]
        data=[y for x in data for y in x]
        df=model_predict(data,1)
    return render_template('censor.html',prediction = df)

@app.route('/scrape',methods=['POST'])
def scrape():
    if request.method == 'POST':
        url = request.form['message']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        #scraping headlines
        headlines = soup.find_all(attrs={"itemprop": "headline"})
        dataset=[]
        for headline in headlines:
            dataset.append(headline.text)
        #print(dataset)
        #scraping links
        links=[]
        link_headlines = soup.find_all("span")
        
        for link_headline in link_headlines:
            var=link_headline.get('itemid')
            
            if var==None:
                continue
            else:
                links.append(var)
        
        df=model_predict(dataset,0,links)
        #print(df)
        df_dict=dict(zip(df.headline, df.links))
        #print(df_dict)
        #pred = {dataset[i]: test_values[i] for i in range(len(test_keys))} 
    return render_template('scrape_censor.html',prediction = df_dict,link=links)

def model_predict(data,flag,links=None):
    tr=open('headline_transform.pkl','rb')
    tr=pickle.load(tr)
    t_model= open('censor_predict.pkl','rb')
    t_model=pickle.load(t_model)

    test=pd.Series(data)
    
    test=tr.transform(test)
    pred=t_model.predict(test)
    if flag==0:
        print("scrappping")
        df=pd.DataFrame({'headline':data,'prediction':pred,'links':links})
        df=df[['headline','links']].where(df['prediction']==0).dropna()
    if flag==1:
        print("only predict")
        df=pd.DataFrame({'headline':data,'prediction':pred})
        df=df['headline'].where(df['prediction']==0).dropna()
    return df
if __name__ == '__main__':
    app.run()