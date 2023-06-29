import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(soup):
    
    #price
    try:
        price = soup.find("span", attrs={'class': 'a-price-whole'}).string.strip()
        
    except AttributeError:
        price = "₹ 5000 "

    
    return {
        'price': price,
    }
    
       
def scrape_flipkart_product(soup):
    
       #price
    try:
        price = soup.find("div", attrs={'class': '_30jeq3 _16Jk6d'}).string.strip()
        
    except AttributeError:
        price = "₹ 5000 "

    
    return {
        'price': price,
    }

def scrape_myntra_product(soup):
    
        #price
    try:
        price = soup.find("span", attrs={'class': 'pdp-mrp-verbiage-amt'}).string.strip()
        
    except AttributeError:
        price = "₹ 5000 "

    
    return {
        'price': price,
    }