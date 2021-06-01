from bs4 import BeautifulSoup
import requests as req
from time import gmtime, strftime
import time
import asyncio

def getNews(code,query):
    xml_doc = req.get(f"https://news.google.com/rss/search?hl=en-IN&gl=IN&q={query}&ceid=IN:en").text
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={code}&units=metric&appid=0a1540015ff9329ec87514758f7ebd78"
    response = req.get(url).json()
    try:
        weather = str(response["main"]["temp"])+"°C  ("+response["weather"][0]["description"]+")"
    except:
        weather = "PostalCode,CountryCode"

    headlines = []

    
    
    soup = BeautifulSoup(xml_doc,"lxml")

    currentTime = time.strftime("%a, %d %b %Y %I:%M:%S", time.gmtime()).split(" ")
    checkTime = (currentTime[1]) +" "+ currentTime[2]
    
    for title, Time in zip(soup.find_all("title"), soup.find_all("pubdate")):
        try:
            if checkTime in Time.text:
                headlines.append((title.text, Time.text))
        except :
            pass
    if len(headlines) == 0:
        nonews = "No news yet from "+ query
        headlines.append((nonews,currentTime))
    return (headlines, weather)

