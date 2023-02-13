from django.urls import path, include
from rest_framework import routers

from api.views import PostModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'post', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
