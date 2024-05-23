from django.urls import path
from .views import AddToFavorite, FavoriteView, delete_favorite, add_shop_card, ShopCartView, ShopAddress, PaymentView,\
      delete_shop_card, delete_all_shop_card, add_whishlist

urlpatterns = [
    path('add_to_favorite/', AddToFavorite.as_view(), name="add_to_favorite"),
    path('favorite/', FavoriteView.as_view(), name="favorite"),
    path('delete_favorite/<uuid:uuid>/', delete_favorite, name='delete_favorite'),
    path('add_shop_card/<uuid:uuid>/', add_shop_card, name='add_shop_card'),
    path('add_whishlist/<uuid:uuid>/', add_whishlist, name='add_whishlist'),
    path('shop_cart/', ShopCartView.as_view(), name="shop_cart"),
    path('delete_shop/<uuid:uuid>/', delete_shop_card, name='delete_shop_card'),
    path('delete_all_shop_card/', delete_all_shop_card, name='delete_all_card'),
    path('shop_address/', ShopAddress.as_view(), name="shop_address"),
    path('payment/<uuid:uuid>/', PaymentView.as_view(), name='payment'),
    
]

