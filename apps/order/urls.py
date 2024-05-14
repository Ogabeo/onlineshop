from django.urls import path
from .views import AddToFavorite, FavoriteView, delete_favorite, add_shop_card

urlpatterns = [
    path('add_to_favorite/', AddToFavorite.as_view(), name="add_to_favorite"),
    path('favorite/', FavoriteView.as_view(), name="favorite"),
    path('delete_favorite/<uuid:uuid>/', delete_favorite, name='delete_favorite'),
    path('add_shop_card/<uuid:uuid>/', add_shop_card, name='add_shop_card'),
]
