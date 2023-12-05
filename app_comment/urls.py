from django.urls import path
from .router import router
from app_comment.views import (
    CommentsListView, CommentCreateView,
    CommentUpdateView, CommentDeleteView
)


urlpatterns = [
    path('list/', CommentsListView.as_view(), name='comment_list'),
    path('create/', CommentCreateView.as_view(), name='comment_create'),
    path('update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]

urlpatterns += router.urls