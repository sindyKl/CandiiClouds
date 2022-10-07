from socket import fromshare
from django import forms 
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'photo']
        widgets = {
            "title": forms.TextInput(attrs={
#                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            "content": forms.Textarea(attrs={
#                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Введите текст',
            }),
            "photo": forms.FileInput(attrs={
#                'class': 'form-control',
                'accept': 'image/*',
                'placeholder': 'Выберите изображение',
            }),
        }