from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134473ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134473", Testconnectors134473ViewSet, basename="testconnectors134473"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
