from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator


from .models import Book
from .forms import BookForm


class BookList(ListView):
    model = Book
    paginate_by = 10
    context_object_name = "book" # Defailt: object_list.
    template_name = 'cbv/book_list.html' # Default: <app_label>/<model_name>_list.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_of_book_pages'] = Book.objects.get_num_of_book_pages()['pages__sum']
        context['num_of_draft'] = Book.objects.get_num_of_drafts()
        context['num_of_published'] = Book.objects.get_num_of_published()
        return context

    def get_queryset(self):
        # TODO: change the queryset by different query conditions.
        query = self.request.GET.get('query')
        if query is not None:
            return Book.objects.filter(name__icontains=query)
        else:
            return Book.objects.all()


class DraftsBookList(BookList):
    def get_queryset(self, **kwargs):
        return Book.objects.get_drafts()


class SortedNameBookList(BookList):
    def get_queryset(self, **kwargs):
        return Book.objects.all().order_by('name')


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
        context['price'] = book_object.current_price
        context['created_at'] = book_object.created_at
        context['updated_at'] = book_object.updated_at
        return context


# API
@csrf_exempt
def get_all_book(request):
    b = Book.objects.all().values()
    return JsonResponse(list(b), safe=False)


@csrf_exempt
def search_book_by_get_method(request):
    query = request.GET.get('query')
    b = Book.objects.filter(name__icontains=query)
    return JsonResponse(list(b), safe=False)


@csrf_exempt
def search_book_by_post_method(request):
    pass
