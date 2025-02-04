from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title



# Author Model (Parent)
# class Author(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# Book Model (Child, linked to Author)
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

#     def __str__(self):
#         return self.title


# Author: Stores author names.
# Book: Each book belongs to one author using ForeignKey.