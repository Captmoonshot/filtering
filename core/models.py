from django.db import models

from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Journal(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def get_my_categories(self):
        # list-display method for ManyToManyField
        return ", ".join([c.name for c in self.categories.all()])

    def __str__(self):
        return self.title


