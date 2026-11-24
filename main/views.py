from django.shortcuts import render
from .serializers import ItemSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderView(APIView):
    def post(self, request):
        order = OrderSerializer(data=request.data)
        if order.is_valid():
            order.save()
            return Response({'result': 'Заказ успешно оформлен!'})

        return Response({'result': 'Ошибка при оформлении заказа!'})

class ItemEditView(APIView):
    def put(self, request, *args, **kwargs):
        item = Item.objects.get(slug=kwargs.get('slug'))
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'{item.title} успешно отредактирован!'})
        return Response({'result': f'При редактировании {item.title} произошла ошибка!'})