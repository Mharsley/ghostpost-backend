from django.conf.urls import include, url
# from ghostpost.api.views import AuthorViewSet, PostViewSet
from ghostpost.api.views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()

# router.register(r'author', AuthorViewSet, basename='author')
router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^api/auth/", include('rest_framework.urls'))
]