from django.shortcuts import get_object_or_404
from rest_framework import generics
from menu.models import Item
from .serializers import ItemSerializer
from rest_framework.views import APIView


#DisplayItems

class ItemList(generics.ListAPIView):

    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ItemSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Item, slug=item)



