from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Product, Store
from api.serializers import (
    ProductSerializer,
    StoreSerializer,
    BuySerializer,
    AddSerializer,
    PurchaseSerializer,
    InventorySerializer,
)
from api.utils import buy, add


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        serializer = BuySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        purchase = buy(
            store_id=pk,
            product_id=serializer.validated_data['product'].id,
            count=serializer.validated_data['count'],
        )

        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add(self, request, pk=None):
        serializer = AddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        inventory = add(
            store_id=pk,
            product_id=serializer.validated_data['product'].id,
            count=serializer.validated_data['count'],
        )

        serializer = InventorySerializer(inventory)
        return Response(serializer.data)
