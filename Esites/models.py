from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    title  = models.CharField(default="1", max_length=100)
    amazon_price = models.DecimalField(default=299, max_digits=8, decimal_places=2)
    flipkart_price = models.DecimalField(default=499, max_digits=8, decimal_places=2)
    myntra_price = models.DecimalField(default=149, max_digits=8, decimal_places=2)
    amazon_link = models.CharField(default="https://www.amazon.in/", max_length=100)
    flipkart_link = models.CharField(default="https://www.flipkart.com/", max_length=100)
    myntra_link = models.CharField(default="https://www.flipkart.com/", max_length=100)
    description = models.TextField(default="All Product Are good")
    product_img = models.ImageField(upload_to = 'media', null=True, blank=True)
