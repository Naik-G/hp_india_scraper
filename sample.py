import requests
from bs4 import BeautifulSoup
import lxml

# Send a GET request to the URL
url = "https://www.hp.com/in-en/shop/laptops-tablets/hp-pavilion-laptop-14-ec1019au-6d9t7pa.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

list_of_review = []



dl = soup.find_all('dd')
for h4 in dl:
    # print(h4)
    proc = h4.find_all('h4' , class_='value')
    for item in proc:
        # print(item)
        if "AMD" in item.text:
            x = item.text.split(" ")[3]
            print(x)
            # amd_dict['processor_model'].append(item.text.split(" ")[3])


# reviews = soup.find("div",class_="iSvbrG").text
# print(reviews)
# for item in reviews:
#     name = item.text
#     list_of_review.append(name)

# print(list_of_review)