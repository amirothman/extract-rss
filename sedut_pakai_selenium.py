from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from readability.readability import Document
import re

def return_links(html):
    soup = BeautifulSoup(html, 'html.parser')

    return[ l["href"] for l in soup.find_all("a", href=True)]

if __name__=="__main__":

    driver = webdriver.Chrome("./chromedriver")
    # links_cleared = []
    countries = []
    with open("countries","r") as country:
        for line in country:
            countries.append(re.sub(r"\n","",line).lower())
    base_link = "https://www.google.de/#q={}+news{}"
    pages = ["","&start=10","&start=20"]
    wait = WebDriverWait(driver, 10)

    with open("news_links_2.txt","a") as newslinks_txt:
        for country in countries:
            for p in pages:
                url = base_link.format(country,p)
                # print(link)

                driver.get(url)
                # wait.until(EC.text_to_be_present_in_element((By.ID,'resultStats'),"Sekunden"))
                time.sleep(4)

                links = return_links(driver.page_source)

                # links = [f.get_attribute("href") for f in driver.find_elements_by_tag_name("a")]
                for link in links:
                    if link and not re.search(r"google|youtube|javascript|blogger",str(link)):
                        print(link)
                        # links_cleared.append(link)
                        newslinks_txt.write(link)
                        newslinks_txt.write("\n")
    driver.quit()
