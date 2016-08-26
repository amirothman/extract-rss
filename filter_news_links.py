import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path

p = Path("current_line")

i = 0

with open("news_links.txt","r") as links:
    with open("filtered.txt","a") as filtered:
        for line in links:
            try:
                current_line = int(p.read_text())
                if i > current_line:

                    p.write_text(str(i))
                    if re.search(r"^http",line):
                        c = re.sub("\n","",line)
                        if not re.search(r"facebook|twitter|wikipedia|htm",c):
                            # print(c)

                            r = requests.get(c)
                            if re.search(r"rss",r.text):
                                soup = BeautifulSoup(r.text,"html.parser")
                                rss = soup.findAll('a',href=True)
                                # print(re.search(r"rss",r.text))
                                # print(c)
                                for s in rss:
                                    if re.search(r"rss",s["href"]):
                                        if re.search(r"^http",s["href"]):
                                            real_rss = s["href"]
                                            real_rss = re.sub("//","/",real_rss)
                                            real_rss = re.sub("http:/","http://",real_rss)
                                            real_rss = re.sub("https:/","https://",real_rss)
                                        else:
                                            if re.search(r"/$",c):
                                                real_rss = re.sub(" ","","".join([c,s["href"]]))
                                            else:
                                                real_rss = re.sub(" ","","/".join([c,s["href"]]))
                                            real_rss = re.sub("//","/",real_rss)
                                            real_rss = re.sub("http:/","http://",real_rss)
                                            real_rss = re.sub("https:/","https://",real_rss)

                                        print(real_rss)
                                        filtered.write(real_rss)
                                        filtered.write("\n")
            except requests.exceptions.ConnectionError:
                print("requests.exceptions.ConnectionError")
            except requests.exceptions.TooManyRedirects:
                print("requests.exceptions.TooManyRedirects")
            except requests.exceptions.ContentDecodingError:
                print("requests.exceptions.ContentDecodingError:")
            except requests.exceptions.ChunkedEncodingError:
                print("requests.exceptions.ChunkedEncodingError:")
            i += 1
