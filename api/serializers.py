from rest_framework.fields import CharField, IntegerField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.validators import UniqueValidator

from api.models import Product, Store, Inventory, Purchase


class ProductSerializer(ModelSerializer):
    name = CharField(
        required=True,
        min_length=2,
        max_length=50,
        validators=[UniqueValidator(queryset=Product.objects.all())],
    )
    price = IntegerField(
        required=False,
        min_value=0,
        max_value=10000000,
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
        ]


class StoreSerializer(ModelSerializer):
    name = CharField(
        required=True,
        min_length=2,
        max_length=50,
        validators=[UniqueValidator(queryset=Store.objects.all())],
    )
    address = CharField(
        required=False,
        min_length=5,
        max_length=100,
    )
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = [
            'id',
            'name',
            'address',
            'products',
        ]


class InventorySerializer(ModelSerializer):
    store = StoreSerializer(required=True)
    product = ProductSerializer(required=True)
    count = IntegerField(required=False, min_value=1, max_value=10000000, default=1)

    class Meta:
        model = Inventory
        fields = [
            'id',
            'store',
            'product',
            'count',
        ]


class PurchaseSerializer(ModelSerializer):
    store = StoreSerializer(required=True)
    product = ProductSerializer(required=True)
    count = IntegerField(required=False, min_value=1, max_value=10000000, default=1)

    class Meta:
        model = Purchase
        fields = [
            'id',
            'store',
            'product',
            'count',
        ]


# noinspection PyAbstractClass
class BuySerializer(Serializer):
    product_id = PrimaryKeyRelatedField(
        source='product',
        queryset=Product.objects.all(),
        required=True,
    )
    count = IntegerField(required=False, min_value=1, max_value=10000000, default=1)


# noinspection PyAbstractClass
class AddSerializer(Serializer):
    product_id = PrimaryKeyRelatedField(
        source='product',
        queryset=Product.objects.all(),
        required=True,
    )
    count = IntegerField(required=False, min_value=1, max_value=10000000, default=1)
