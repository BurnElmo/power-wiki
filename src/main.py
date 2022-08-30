import requests
from bs4 import BeautifulSoup

print("Keep in mind, the maximum header count, and the entire program might not be fully accurate since this is my first attempt at webscraping")

# Add input functionality with the amount of links or command line arguments
url = input("Enter a valid Wikipedia URl: ")
print(url)

count = 0
maxCount = int(input("Enter the maximum amount of parsed headers: "))

request_results = requests.get(url)

# Grab the main image and the first paragraph(s)

wiki_page = BeautifulSoup(request_results.text, "html.parser")

paragraphs = ""

# Title:
# wiki_page.find("h1", {"id": "firstHeading"}).getText()
# Paragraphs:
# for paragraph in wiki_page.select('p'):
#     print(paragraph.getText())

with open('pararaphs.txt', 'w') as f:
    f.write(wiki_page.find("h1", {"id": "firstHeading"}).getText() + "\n\n\n")

    for paragraph in wiki_page.select('p'):
        if count < maxCount:
            f.write(paragraph.getText())
            count += 1