import requests
from bs4 import BeautifulSoup
from csv import writer

#Request data from URL
r = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(r.text, "html.parser")
articles = soup.find_all("article")

#Share data to csv file
with open("blogz.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

#Pipe incoming html int BeautifulSoup
for article in articles:
    a_tag =  article.find("a")
    title =  a_tag.get_text()
    url   =  a_tag['href']
    date  =  article.find("time")["datetime"]

csv_writer.writerow([title, url, date])
  
