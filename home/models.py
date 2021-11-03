import admin as admin
from django.db import models
from django.contrib import admin


def new_product_image(instance, filename):
    return 'products/{0}/{1}'.format(instance.product_name, filename)


def product_images(instance, filename):
    return 'products/multiple/{0}'.format(filename)


class ProductImage(models.Model):
    image = models.ImageField(upload_to=product_images, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    product_name = models.CharField(max_length=400, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=new_product_image, null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.product_name
