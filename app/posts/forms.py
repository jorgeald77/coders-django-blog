from django import forms
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'foto', 'published_at')
        widgets = {
            'content': forms.Textarea(attrs={'required': True}),
            'foto': forms.FileInput(),
            'published_at': forms.DateInput(attrs={'type': 'date'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('person_name', 'content')
