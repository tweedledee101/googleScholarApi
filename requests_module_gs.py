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



#Getting Todays Date in the correct Format
today = datetime.date.today()
year = today.year
month = today.month
day = today.day

formatted_date = f'{month}/{day}/{year}'
print(f"This is todays date {formatted_date}")

r = requests.get('https://scholar.google.com')
print(r.status_code)

question = "Coffee and tea"
reformatted_question = question.replace(" ", "+")
print(reformatted_question)
params = {
     "engine": "google_scholar",
     "q": reformatted_question,
     "hl": "en"
    }

#new_request = requests.get(f"https://scholar.google.com/scholar?hl={params['hl']}&as_sdt=0%2C14&q={params['q']}")
#http = urllib3.PoolManager()
new_request = requests.get(f"https://scholar.google.com/scholar?hl={params['hl']}&q={params['q']}")
headers = new_request.headers
#print(headers)
#print(headers.keys())
print(headers["Content-Type"])
print(headers["Content-Encoding"])
encoding = new_request.encoding
print(encoding)
