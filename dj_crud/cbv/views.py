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
        context['num_of_book_pages'] = Book.objects.get_num_of_book_pages()['pages__sum']
        context['num_of_draft'] = Book.objects.get_num_of_drafts()
        context['num_of_published'] = Book.objects.get_num_of_published()

        query = self.request.GET.get('query')
        context['query'] = query
        return context

    def get_queryset(self):
        # TODO: change the queryset by different query conditions.
        return Book.objects.all()


class DraftsBookList(BookList):
    def get_queryset(self, **kwargs):
        return Book.objects.get_drafts()


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
    template_name = 'cbv/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_object = Book.objects.get(id=self.kwargs['pk'])
        context['name'] = book_object.name
        context['status'] = book_object.status
        context['pages'] = book_object.pages
        context['created_at'] = book_object.created_at
        context['updated_at'] = book_object.updated_at
        return context
