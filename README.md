# Scrape google

  python sedut_pakai_selenium.py

```
base_link = "https://www.google.de/#q={}+news{}"
  pages = ["","&start=10","&start=20"]
  wait = WebDriverWait(driver, 10)

  with open("news_links_2.txt","a") as newslinks_txt:
      for country in countries:
```

This script will collect google results.

# Get rss links

  python filter_news_links.py


```
with open("news_links_2.txt","r") as links:
    with open("filtered_2.txt","a") as filtered:
```

# Test rss

  python test_rss.py
