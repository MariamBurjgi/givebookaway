from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference the User model

    def __str__(self):
        return self.title
