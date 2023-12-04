from django import forms
from app_comment.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'username',
            'subjetc',
            'comment'
        ]
