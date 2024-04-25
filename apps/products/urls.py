from django.urls import path
from .views import HomePageView, CategoryProductsView, ShopAllView

urlpatterns =[
    path('', HomePageView.as_view(), name='home'),
    path('category_products/' , CategoryProductsView.as_view(), name="category"),
    path('shop/', ShopAllView.as_view(), name='shop'),
    
]
