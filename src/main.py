import requests
from bs4 import BeautifulSoup

url = input("Enter a valid Wikipedia URL: ")

count = 0
maxCont = int(input("Enter the maximum amount of paragraphs: "))

request_results = requests.get(url)

# Grab the main image and the first paragraph(s)

wiki_page = BeautifulSoup(request_results.text, "html.parser")

# Title:
# wiki_page.find("h1", {"id": "firstHeading"}).getText()
# Paragraphs:
# for paragraph in wiki_page.select('p'):
#     print(paragraph.getText())

with open('powerwiki.txt', 'w') as f:
    f.write(wiki_page.find("h1", {"id": "firstHeading"}).getText() + "\n\n\n")

    for paragraph in wiki_page.select('p'):
        if count < maxCont:
            f.write(paragraph.getText())
            count += 1