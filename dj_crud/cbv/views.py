from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse

from .models import Book
from .forms import BookForm


class BookList(ListView):
    model = Book
    paginate_by = 10
    context_object_name = "book" # Defailt: object_list.
    template_name = 'cbv/book_list.html' # Default: <app_label>/<model_name>_list.html

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['num_of_book_pages'] = Book.object.get_num_of_book_pages()['pages__sum']
        context['num_of_draft'] = Book.object.get_num_of_drafts()
        context['num_of_published'] = Book.object.get_num_of_published()
        return context

    def get_queryset(self):
        return Book.object.all()


class DraftsBookList(BookList):
    def get_queryset(self, **kwargs):
        return Book.object.get_drafts()


class BookCreate(CreateView):
    model = Book
    message = ("Your book has been created.")
    form_class = BookForm
    template_name = 'cbv/book_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse('cbv:list')


class BookUpdate(UpdateView):
    model = Book
    message = ('Your book has been updated.')
    form_class = BookForm
    template_name = 'cbv/book_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse('cbv:list')


class BookDelete(DeleteView):
    model = Book
    # TODO: need to check what's different between reverse and reverse_lazy.
    success_url = reverse_lazy('cbv:list')


class BookDetail(DetailView):
    model = Book