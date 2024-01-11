# this is 6th project from this link: https://medium.com/@luisprooc/30-data-engineering-project-ideas-9ecf0a70cbea
import requests
from csv import writer
import datetime
import time
import os

# define query parameters to get top articles from bbc news with my api key
# you can use this link to get your own api key : https://newsapi.org/
query_parameters = {"source": "bbc-news", "sort-by": "top", "apiKey": "55cb6679922540db94b8c4df97715841"}
url = " https://newsapi.org/v1/articles"

# request to fetch data from the url in json format
result = requests.get(url, query_parameters)
data = result.json()

# getting articles
articles = data["articles"]

# write the data into a csv file
with open("articles.csv", "a") as csv_file:
    writer = writer(csv_file)
    for ar in articles:
        # get date and time and remove microseconds
        current_time = datetime.datetime.now().replace(microsecond=0)
        # concat date and time to the article's title
        complete_data = str(current_time) + ' ' + str(ar["title"])
        time.sleep(2)
        writer.writerow([complete_data])

# remove redundant double quotes
with open("articles.csv") as file:
    for row in file:
        text = row
        text = ''.join([i for i in text]).replace('"', '')
        x = open("final_articles.csv", "a")
        x.writelines([text])

# remove redundant file
os.remove("articles.csv")
