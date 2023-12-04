from django.urls import path
from comentarios.views import (
    CommentsListView, CommentCreateView,
    CommentUpdateView, CommentDeleteView
)


urlpatterns = [
    path('list/', CommentsListView.as_view(), name='comment_list'),
    path('create/', CommentCreateView.as_view(), name='comment_create'),
    path('update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    #path('mimodelo/<int:pk>/', MiModeloDetailView.as_view(), name='mimodelo_detail'),
    #path('mimodelo/nuevo/', MiModeloCreateView.as_view(), name='mimodelo_create'),
]