from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index.html', index, name='index'),
    path('shop.html', shop, name='shop'),
    path('shop-detail.html',shopdetail,name='shop-detail'),
    path('cart.html',cart,name='cart'),
    path('chackout.html',chackout,name='chackout'),
    path('testimonial.html',testimonial,name='testimonial.html'),
    path("contact.html",contact,name='contact'),
    path("404.html",error,name='error'),
    path("login.html",login1,name='login'),
    path("registration.html",reg,name='reg'),
    path("logout",logoutpage,name='logout')
]
