from django.urls import path
from .views import HomePageView, DetailReviewView, CategoryProductsView, ContactView, BrandProductsView, DetailView, ShopAllView, ShopCategoryView, CategoryProductsView

urlpatterns =[
    path('', HomePageView.as_view(), name='home'),
    path('shop/', ShopAllView.as_view(), name='shop'),
    path('shop/<uuid:uuid>/', ShopCategoryView.as_view(), name="shop"),
    path('detail/<uuid:uuid>/', DetailView.as_view(), name='detail'),
    path('category_products/<uuid:uuid>/', CategoryProductsView.as_view(), name='category_products'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('brands/<uuid:uuid>/', BrandProductsView.as_view(), name="Shop_brand"),
    path('to_detail_review/<uuid:uuid>/', DetailReviewView.as_view(), name="review_page" )

]
