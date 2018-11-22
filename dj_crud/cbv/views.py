from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book

# Create your views here.
class BookList(ListView):
    model = Book
    # template_name_suffix = '_list'

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    # template_name_suffix = '_form'
    success_url = reverse_lazy('cbv:index')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('cbv:index')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('cbv:index')

# def index(request):
#     template = 'cbv/cbv_list.html'
#     book = Book.objects.all()
#     context = {"book": book}
#     return render(request, template, context)
