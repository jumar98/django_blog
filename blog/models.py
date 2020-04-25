from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(default="Anonimo", max_length=20)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField()

    def __str__(self):
        return self.title
