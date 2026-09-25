import requests
from bs4 import BeautifulSoup
import csv
url = input("Enter website URL: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find_all("h2")
with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(["Headline"])
    for headline in headlines:
        text = headline.get_text(strip=True)
        writer.writerow([text])
print("Headlines saved to headlines.csv")