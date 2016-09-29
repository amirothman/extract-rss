import feedparser
from readability.readability import Document
from bs4 import BeautifulSoup
import re
import requests
from dateutil.parser import parse
import json
from pathlib import Path
import socket
from extract_single_page import extract_single
import random

def extract_content(link):
    r  = requests.get(link)
    html = r.text
    readable = Document(html).summary()
    return BeautifulSoup(readable,"lxml").text

def test_rss_feeds(rss_feeds,accepted,rejected):

    for feed in rss_feeds:

        print(feed)
        try:
            parsed_feed = feedparser.parse(feed)

            links_dates = [ (el["link"],el["published"],el["title"]) for el in parsed_feed.entries]
            links_dates = [links_dates[0]]
            for link,date,title in links_dates:
                # print(link)
                date_parsed = parse(date)
                content = extract_content(link)
                article_dict = {"title":title,
                                "content":content,
                                "link":link,
                                "day":date_parsed.day,
                                "month":date_parsed.month,
                                "year":date_parsed.year,
                                }

                json_string = json.dumps(article_dict, sort_keys=True, indent=4)
                print(json_string)
                print(feed)

                with open(accepted,"a") as rejected_file:
                    rejected_file.write(feed)
                    rejected_file.write("\n")

        except IndexError:
            print("IndexError")
            with open(rejected,"a") as rejected_file:
                rejected_file.write(feed)
                rejected_file.write("\n")
        except KeyError:
            print("KeyError")
            with open(rejected,"a") as rejected_file:
                rejected_file.write(feed)
                rejected_file.write("\n")
        except ValueError:
            print("ValueError")
            with open(rejected,"a") as rejected_file:
                rejected_file.write(feed)
                rejected_file.write("\n")
        except socket.gaierror:
            print("socket.gaierror")
            with open(rejected,"a") as rejected_file:
                rejected_file.write(feed)
                rejected_file.write("\n")
        except requests.exceptions.ConnectionError:
            print("requests.exceptions.ConnectionError")
            with open(rejected,"a") as rejected_file:
                rejected_file.write(feed)
                rejected_file.write("\n")

filtered_rss = "filtered_2.txt"
filtered_rss_feeds = []
with open(filtered_rss,"r") as rss:
    for line in rss:
        filtered_rss_feeds.append(re.sub("\n","",line))

random.shuffle(filtered_rss_feeds)

test_rss_feeds(filtered_rss_feeds,"accepted_2.txt","rejected_2.txt")


p = Path("current_line_test")
i = 0
with open("rejected_2.txt","r") as rss_file:
    for line in rss_file:
        current_line = int(p.read_text())
        if i > current_line:
            print(line)
            rss = re.sub("\n","",line)
            rss_feeds = extract_single(rss)
            test_rss_feeds(rss_feeds,"accepted_2.txt","rejected_2.txt")
            print(i)
            p.write_text(str(i))
        i += 1
