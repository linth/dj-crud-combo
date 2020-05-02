from django import forms
from markdownx.fields import MarkdownxFormField

from .models import Book


class BookForm(forms.ModelForm):
    description = MarkdownxFormField()

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['name', 'pages', 'status', 'current_price', 'description']
