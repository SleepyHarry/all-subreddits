import re
import requests

url = 'http://redditmetrics.com/history/'

class ConnectionError(Exception):
    pass

def get_dates():
    response = requests.get(url)

    if not response.ok:
        raise ConnectionError
    else:
        return set(re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", response.text))

def get_subs_from_text(text):
    return set(re.findall(r"/r/[a-z0-9-.]+", text, re.IGNORECASE))

def get_page_from_date(date):
    response = requests.get(url + date)
    
    if not response.ok:
        raise ConnectionError
    
    return response.text

def get_subs_from_date(date):
    return get_subs_from_page(get_page_from_date(date))
