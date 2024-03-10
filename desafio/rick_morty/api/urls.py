from rest_framework.routers import DefaultRouter
from .viewset import RickMortyViewSet
from django.urls import include, path

router = DefaultRouter()

router.register("RickMorty", RickMortyViewSet)

urlpatterns = [
    path("api/", include(router.urls))
]