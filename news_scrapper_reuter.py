#Packages
#--Web scraping packages
from bs4 import BeautifulSoup
import requests
#Pandas/numpy for data manipulation
import pandas as pd
import numpy as np
import sys

company_name= str(sys.argv[1])
print ('company_name :'+ company_name)
#load URLs we want to scrape into an array
BASE_URL = [
'https://www.reuters.com/news/archive/{}?view=page&page={}'
]


#loading empty array for board members
news_row = []
news_row_without = []
#Loop through our URLs we loaded above
for b in BASE_URL:
    for i in range(2,400,1):
        url=b.format(company_name,i)
        print(url)

        html = requests.get(url).text  
        soup = BeautifulSoup(html, "html.parser")
      
        news_table = soup.find('div', {"class" : "news-headline-list"})
     
        for news in news_table.find_all('div', {"class" : "story-content"}):
            title = news.find('h3', {'class': 'story-title'})
            description= news.find('p')
            date = news.find('span', {'class': 'timestamp'})
            if(company_name.lower() in title.text.strip().lower()):
                news_row.append((company_name,date.text.strip(),title.text.strip(),description.text.strip()))

            news_row_without.append((company_name,date.text.strip(),title.text.strip(),description.text.strip()))   

news_final_rows=np.asarray(news_row)
news_final_rows_without=np.asarray(news_row_without)

print(len(news_final_rows))
print(len(news_final_rows_without))

df=pd.DataFrame(news_final_rows)
df1=pd.DataFrame(news_final_rows_without)

df.columns=['Firm','Date','Headlines','Description']
df1.columns=['Firm','Date','Headlines','Description']


df['Date']=pd.to_datetime(df['Date'], format = "%b %d %Y").apply(lambda x: x.strftime('%m-%d-%Y'))
df1['Date']=pd.to_datetime(df1['Date'], format = "%b %d %Y").apply(lambda x: x.strftime('%m-%d-%Y'))

print(df.head(2))
print(df1.head(2))

df.to_csv("C:\\Dev\\mycode\\reuter_{}csv".format(company_name))
df1.to_csv("C:\\Dev\\mycode\\reute_without_{}.csv".format(company_name))




