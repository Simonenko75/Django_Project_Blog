from .models import Post
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'text', 'published']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву поста'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть автора даного поста'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть короткий опис поста'
            }),
            'published': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть поточний рік публікації поста'
            })
        }
