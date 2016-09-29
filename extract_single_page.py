import requests
from bs4 import BeautifulSoup
from urllib import parse
import re

def extract_single(url):
    res = requests.get(url)
    parsed = parse.urlparse(url)
    p = parsed.netloc
    soup = BeautifulSoup(res.text,"html.parser")
    rss = soup.find_all('a',href=True)
    links = []
    for s in rss:
        if re.search(r"rss|blitz|xml|feed",s["href"]):
            if not re.search(r"facebook|linkedin|twitter|feedly|aol|netvibe|live|gator|msn|google|blogline|yahoo",s["href"]):
                if re.search(r"^/",s["href"]):
                    links.append("".join(["http://",p,s["href"]]))
                else:
                    links.append(s["href"])

    return set(links)
