from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from comentarios.models import Comentario
from comentarios.forms import CommentForm


class CommentsListView(ListView):
    template_name = "pages/comments/list.html"
    context_object_name = "comments"

    def get_queryset(self):
        queryset = Comentario.objects.all()
        return queryset


class CommentCreateView(CreateView):
    model = Comentario
    form_class = CommentForm
    template_name = 'pages/comments/create.html'
    success_url = reverse_lazy('comment_list')


class CommentUpdateView(UpdateView):
    model = Comentario
    form_class = CommentForm
    template_name = 'pages/comments/create.html'
    success_url = reverse_lazy('comment_list')


class CommentDeleteView(DeleteView):
    model = Comentario
    template_name = 'pages/comments/list.html'
    success_url = reverse_lazy('comment_list')
