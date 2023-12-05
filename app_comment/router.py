from rest_framework import routers
from .viewsets import CommentViewSet

router = routers.SimpleRouter()

router.register("api-comment", CommentViewSet)