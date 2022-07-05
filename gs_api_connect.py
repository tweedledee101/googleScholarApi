from datetime import date
import datetime
import requests
from  datetime import date
from pprint import pprint
import urllib3
import json
from serpapi import GoogleSearch

greeting = "Hello and welcome to Josh's Citing Program, lets get this thing started"
center = greeting.center(5)
print(center)

api_key = 'fc99a3d6577c4033faafffacf965daa087d6c2ab385d0f7eeded27fe276d2534'

r = requests.get("https://serpapi.com/account.json")
print(r.status_code)

#Getting Todays Date in the correct Format
today = datetime.date.today()
year = today.year
month = today.month
day = today.day

formatted_date = f'{month}/{day}/{year}'
print(f"This is todays date {formatted_date}")


question = "Coffee and tea"
reformatted_question = question.replace(" ", "+")
print(reformatted_question)
params = {
     "engine": "google_scholar",
     "q": question,
     "hl": "en",
     "api_key": api_key
    }

search = GoogleSearch(params)
results = search.get_dict()

pprint(results)
