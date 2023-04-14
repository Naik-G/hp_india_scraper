from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup
import requests
import lxml


driver = webdriver.Chrome()
driver.get('https://www.hp.com/in-en/shop/laptops-tablets.html')
list_of_link = []

amd_dict = {    'product_name':[],
                    'processor_model':[],
                    'processor_string':[],
                    'product_mrp':[],
                    'product_price':[],
                    'product_link':[],
                    'item_id':[],
                    'review':[],
                    'rating':[]     }


def main():
    # time.sleep(2)
    # try :
    #     driver.find_element(By.XPATH ,'//*[@id="onetrust-accept-btn-handler"]').click
    # except:
    #     print('no popup shown')

    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    # WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="category.product.list"]/div[4]/div[2]/ul/li[8]/a/div'))).click()
    # list_of_link.append(driver.current_url)
    # getlinks()
    page_source = driver.page_source
    # driver.close()
    proccesser(page_source)
    
# def getlinks():

#     for urls in range(1,8):
#         # driver.refresh()
#         # WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="category.product.list"]/div[4]/div[2]/ul/li[8]/a/div'))).click()
#         list_of_link.append(driver.current_url+"?p="+str(urls))
#         proccesser()

    

def proccesser(page_source):
    soup = BeautifulSoup(page_source, "lxml")

    product_name = soup.find_all("h2",class_="plp-h2-title stellar-title__small")
    processor_model = soup.find_all("li", class_="processorfamily")
    product_link = soup.find_all("a", class_="product-item-link")
    item_id = soup.find_all('div', class_='product-sku stellar-body__extra-small')
    mrp_div = soup.find_all('div', class_='suggest-retail-price simple')
    price_div = soup.find_all('span', class_='price-wrapper price-including-tax')
    
        
    for name, processors_name ,links, orignal_price, complete_price, id\
         in \
        zip(product_name, processor_model, product_link, mrp_div, price_div, item_id):
         
        if 'AMD' in processors_name.text:
            
            # ----------- Product name --------------
            amd_dict['product_name'].append(name.text.strip())
            
            # ----------- processor name --------------
            amd_dict['processor_string'].append(processors_name.text)

            # ----------- Processor model --------------
            amd_dict['processor_model'].append(processors_name.text.split('-')[1])

            # ----------- Product link --------------
            amd_dict['product_link'].append(links["href"])
            
            # ----------- Product id --------------
            amd_dict['item_id'].append(id.text)

            # ----------- MRP price --------------
            product_mrp = (orignal_price.find_all('span', class_='price'))
            amd_dict['product_mrp'].append([span_mrp.text.strip() for span_mrp in product_mrp][0])

            # ----------- but price --------------
            product_price = (complete_price.find_all('span', class_='price'))
            amd_dict['product_price'].append([price.text.strip() for price in product_price])
        
    else:
        print('complete')

    print(amd_dict['product_name'])
    print(amd_dict['processor_string'])
    print(amd_dict['processor_model'])
    print(amd_dict['product_link'])
    print(amd_dict['item_id'])
    print(amd_dict['product_mrp'])
    print(amd_dict['product_price'])
    


main()

