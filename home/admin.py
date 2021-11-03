from django.contrib import admin
from home.models import Product, ProductImage

admin.site.register((Product, ProductImage))
