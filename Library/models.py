from django.db import models

# Create your models here.
class books(models.Model):
    book_name = models.CharField(max_length=20)
    author_name = models.CharField(max_length=20)
    edition = models.CharField(max_length=20)

