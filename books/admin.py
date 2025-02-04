from django.contrib import admin
from .models import Book
# Register your models here.
admin.site.register(Book)




# Admin customization#####

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author')  # Display columns
#     list_filter = ('author',)  # Sidebar filter
#     search_fields = ('title', 'author__name')  # Search box
#     ordering = ('title',)  # Default ordering

# admin.site.register(Book, BookAdmin)