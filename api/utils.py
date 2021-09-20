from django.db import transaction
from rest_framework.exceptions import APIException

from api.models import Inventory, Purchase


def buy(store_id: int, product_id: int, count: int) -> Purchase:
    with transaction.atomic():
        total_products = 0
        for inventory in Inventory.objects.filter(product_id=product_id):
            total_products += inventory.count

        purchased_products = 0
        for purchase in Purchase.objects.select_for_update().filter(product_id=product_id):
            purchased_products += purchase.count

    available_products = total_products - purchased_products
    if count > available_products:
        raise APIException('Out of stock')

    return Purchase.objects.create(
        store_id=store_id,
        product_id=product_id,
        count=count,
    )


def add(store_id: int, product_id: int, count: int) -> Inventory:
    return Inventory.objects.create(
        store_id=store_id,
        product_id=product_id,
        count=count,
    )
