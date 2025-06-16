import requests
import json

slug = "elon-musk-of-tweets-feb-28-mar-7"
api_url = f"https://gamma-api.polymarket.com/events?slug={slug}&active=true&closed=false"

r = requests.get(api_url)
response = r.json()

elon_events = {}
for event in response:
  if 'Elon' in event['title']:
    elon_events[event['id']] = event

elon_events['19918']['markets']

for market in elon_events['19918']['markets']:
  if 'outcomePrices' in market and 'clobTokenIds' in market:
    print(market['id'], market['question'], 'outcomePrices' in market and market['outcomePrices'])
    print('clobTokenIds' in market and market['clobTokenIds'])
    print('=====')

