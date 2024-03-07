from rest_framework.routers import DefaultRouter # ver os routers no django rest
from .viewset import ViaCepViewSet
from django.urls import include, path

router = DefaultRouter()

router.register("ViaCep" , viewset = ViaCepViewSet)

urlpatterns = [
    path("api/", include(router.urls))
]