from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    template = 'fbv/fbv_list.html'
    book = Book.objects.all()
    context = {"book": book}
    return render(request, template, context)

def book_create(request):
    template = 'fbv/form.html'
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('fbv:index')
    context = {"form": form}
    return render(request, template, context)

def book_update(request, pk):
    template = 'fbv/form.html'
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('fbv:index')
    context = {"form": form}
    return render(request, template, context)

def book_delete(request, pk):
    template = 'fbv/delete.html'
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('fbv:index')
    context = {"book": book}
    return render(request, template, context)
