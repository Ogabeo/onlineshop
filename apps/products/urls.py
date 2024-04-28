from django.urls import path
from .views import HomePageView, CategoryProductsView, ShopAllView, ShopCategoryView

urlpatterns =[
    path('', HomePageView.as_view(), name='home'),
    path('category_products/' , CategoryProductsView.as_view(), name="category"),
    path('shop/', ShopAllView.as_view(), name='shop'),
    path('shop/<uuid:uuid>/', ShopCategoryView.as_view(), name="shop"),
    
    
]
