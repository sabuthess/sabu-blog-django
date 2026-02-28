from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-teal-400',
                'placeholder': 'Post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded h-32 focus:outline-none focus:ring-2 focus:ring-teal-400',
                'placeholder': 'Write your content here..!'
            }),
        }