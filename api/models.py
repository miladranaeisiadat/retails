from django.db.models import Model, TextField, IntegerField, ForeignKey, ManyToManyField, RESTRICT


class Product(Model):
    name = TextField(null=False, unique=True)
    price = IntegerField(null=True)


class Store(Model):
    name = TextField(null=False, unique=True)
    address = TextField(null=True)
    products = ManyToManyField(Product, through='Inventory')


class Inventory(Model):
    store = ForeignKey(Store, on_delete=RESTRICT)
    product = ForeignKey(Product, on_delete=RESTRICT)
    count = IntegerField(null=False)


class Purchase(Model):
    store = ForeignKey(Store, on_delete=RESTRICT)
    product = ForeignKey(Product, on_delete=RESTRICT)
    count = IntegerField(null=False)
