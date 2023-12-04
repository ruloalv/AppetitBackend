from django import forms
from comentarios.models import Comentario

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'usuario',
            'asunto',
            'comentario'
        ]
