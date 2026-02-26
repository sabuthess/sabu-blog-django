from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields=['title', 'content']

    title = forms.CharField(max_length=255)
    content = forms.FileField(widget=forms.Textarea(attrs={
        "rows": 10,
        "cols": 80
    })) 