from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.db.models import Q

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
        if self.request.GET.get('query', None) is not None:
            context['query'] = self.request.GET.get('query')
        context['all_status'] = Book.STATUS
        context['status'] = self.request.GET.get('status', None)
        # context['ss'] = Book.objects.get(id=1).to_dict_json()
        return context

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        # status = self.request.GET.get('status', None)
        # print('status', status, type(status))
        if query is not None:
            return Book.objects.filter(name__icontains=query)
        else:
            # return Book.objects.filter(status=status)
            return Book.objects.all()


def test_json(request):
    books = Book.objects.all()
    data = [book.to_dict_json() for book in books]
    response = {'data': data}
    return JsonResponse(response, safe=False, content_type='application/json')


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


# --------------------------------------------------------------
# API
# --------------------------------------------------------------
@csrf_exempt
def get_all_book(request):
    try:
        b = Book.objects\
            .all()\
            .values()
    except Exception as e:
        raise ('[ERROR] get_all_book: ', e)
    return JsonResponse(list(b), safe=False)


@csrf_exempt
def search_book_by_get_method(request):
    """ through get method to get queryset by AJAX. """
    query = request.GET.get('query')
    try:
        b = Book.objects\
            .filter(name__icontains=query)\
            .values()
    except Exception as e:
        raise ('[ERROR] search_book_by_get_method: ', e)
    return JsonResponse(list(b), safe=False)


@csrf_exempt
def search_book_by_post_method(request):
    """ through post method to get queryset by AJAX. """
    res = []
    return JsonResponse(list(res), safe=False)
