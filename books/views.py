from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})

# Read
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Update
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request,'update_book.html', {'form': form})

# Delete
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})




# Quering database from ORM
# Get all authors
# authors = Author.objects.all()
# Line no 18
# Get All Records	Model.objects.all()
# Get Single Record	Model.objects.get(id=1)
# Filter Records	Model.objects.filter(field=value)
# Exclude Records	Model.objects.exclude(field=value)
# Count Records	Model.objects.count()
# Aggregation	Model.objects.aggregate(Sum('field'))
# Ordering	Model.objects.order_by('field')
# Related Model Query	author.books.all()
# Update Record	book.save()
# Delete Record	book.delete()


