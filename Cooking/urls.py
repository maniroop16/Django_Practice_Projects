from rest_framework.routers import DefaultRouter
from Cooking.views import Addressview
from django.urls import include, path

router = DefaultRouter()
router.register("address", Addressview)

urlpatterns = [
    path("api/", include(router.urls))
]