from django import forms
from .models import Book # for cbv


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['name', 'pages', 'status', 'current_price']
