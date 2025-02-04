from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'published_date']
#         widgets = {
#             'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
#             'author': forms.TextInput(attrs={ 'placeholder': 'Enter author name'}),
#             'published_date': forms.DateInput(attrs={ 'type': 'date'}),


#         }
        
