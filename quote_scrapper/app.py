import requests
from bs4 import BeautifulSoup as bs
import csv

response = requests.get('https://timesofindia.indiatimes.com/india/karnataka')

soup = bs(response.text,"html.parser")
fields = ["Image","Content"]
article_box = soup.find("div",{"id":"c_articlelist_stories_2"})
ul = article_box.find("ul")
articles = ul.find_all("li")
article_list = []
for (index,i) in enumerate(articles):
    a = i.find("a")
    response = requests.get("https://timesofindia.indiatimes.com"+a["href"])
    soup = bs(response.text,"html.parser")
    
    try:
        articleBox = soup.find("div",{"class":"heightCalc"})
        img = articleBox.find("section").find("img")
        article_content = articleBox.find("div",{"class":"clearfix"})
        image_link = img["src"]
        article_list.append([image_link,article_content.text])
    except:
        print("Error")



# write content to csv
print(article_list)
with open("./articles.csv","a") as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerow(fields)
    csvwriter.writerows(article_list)
    
    
   