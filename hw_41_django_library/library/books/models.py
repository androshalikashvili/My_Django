from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    authors = models.CharField(max_length=100, null=False)
    publication_date = models.CharField(max_length=15, null=False)
    isbn = models.CharField(max_length=11, null=False)

    def __str__(self):
        return self.title
    