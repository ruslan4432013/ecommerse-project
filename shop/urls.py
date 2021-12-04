from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='products_by_category'),
    path('product/', views.product, name='product'),
    path('<slug:category_slug>/<slug:product_slug>', views.product, name='products_detail'),
]
