from django.shortcuts import render
from .utils import *
from bs4 import BeautifulSoup
import requests


# Create your views here.
def index(request):
    HEADERS = ({'User-Agent':
	            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US, en;q=0.5'})

	# The webpage URL
    A_URLs = [
    "https://www.amazon.in/Estele-Sublime-Devotion-Antique-Necklace/dp/B099ZJXH22/ref=sr_1_1_sspa?keywords=JEWELLERY&qid=1687957117&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
    ]

    F_URLs = [
    "https://www.flipkart.com/verent-brass-gold-plated-gold-jewellery-set/p/itme00bb77d42ed6?pid=JWSG9YRHATZVYHDS&lid=LSTJWSG9YRHATZVYHDSROJCVK&marketplace=FLIPKART&q=Estele+Necklace+Set+for+Women&store=mcr%2F96v%2Fyx2&srno=s_1_12&otracker=search&otracker1=search&fm=organic&iid=en_IDvQdE0tySnsa5MceFaPA1FYUOzHfVsLjxijEp2GLaH93H5eIgUEKD7j-1Qtl3SqV72vEksfv7Z4CKc1JY5pbw%3D%3D&ppt=hp&ppn=homepage&ssid=a9jh13255c0000001688025638284&qH=a1694a6c9bec04a5",
    ]
        
    M_URLs = [
    # "https://www.myntra.com/jewellery-set/estele/estele--gold-plated-jewellery-set/20271728/buy",
    ]
        

    A = []
    F = []
    M = []

    for URL in A_URLs:
        webpage = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "lxml")
        product_del = scrape_amazon_product(soup)
        A.append(product_del.keys)

    for URL in F_URLs:
        webpage = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "lxml")
        product_del = scrape_flipkart_product(soup)
        F.append(product_del.keys)
    
    for URL in M_URLs:
        webpage = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "lxml")
        product_del = scrape_myntra_product(soup)
        M.append(product_del.keys)

    product_data = {
        'Amazon' : A,
        'Flipkart' : F,
        'Myntra' : M,
    }
    # Pass the data to the template for rendering
    return render(request, 'index.html')

from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
