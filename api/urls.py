from django.urls import path, include
from rest_framework import routers

from api.views import ProductViewSet, StoreViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stores', StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
