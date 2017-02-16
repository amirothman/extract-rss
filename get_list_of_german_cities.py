from bs4 import BeautifulSoup
import requests

sites = ["Deutschland-Cities.html","Deutschland-BadenWurttemberg.html","Deutschland-Bayern.html","Deutschland-Berlin.html","Deutschland-Brandenburg.html","Deutschland-Bremen.html","Deutschland-Hamburg.html","Deutschland-Hessen.html","Deutschland-MecklenburgVorpommern.html","Deutschland-Niedersachsen.html","Deutschland-NordrheinWestfalen.html","Deutschland-RheinlandPfalz.html","Deutschland-Saarland.html","Deutschland-Sachsen.html","Deutschland-SachsenAnhalt.html","Deutschland-SchleswigHolstein.html","Deutschland-Thuringen.html"]


with open("cities.test.txt","ab") as f:

    for site in sites:

        link = "https://www.citypopulation.de/{}.html".format(site)
        print(link)
        html_doc = requests.get(link)

        soup = BeautifulSoup(html_doc.content,"html.parser")

        for a in soup.find_all("span",attrs={"itemprop":"name"}):
            f.write(a.get_text().encode("utf-8"))
            f.write("\n".encode("utf-8"))
