from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("products/", mainapp.products, name="products"),
    path("contact/", mainapp.contact, name="contact"),
]
