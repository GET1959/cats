from django.urls import path
from rest_framework.routers import SimpleRouter

from cats.apps import CatsConfig
from cats.views import CatViewSet

app_name = CatsConfig.name

router = SimpleRouter()
router.register("", CatViewSet)

urlpatterns = [
]
urlpatterns += router.urls
