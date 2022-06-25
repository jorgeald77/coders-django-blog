from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'foto', 'published_at')
        widgets = {
            'content': forms.Textarea(attrs={'required': True}),
            'foto': forms.FileInput(),
            'published_at': forms.DateInput(attrs={'type': 'date'}),
        }