from .views import ItemList, ItemDetail
from django.urls import path

app_name = 'menu_api'

urlpatterns = [
    path('', ItemList.as_view(), name='listitem'),
    path('item/<str:pk>/', ItemDetail.as_view(), name='detailitem'),
]