from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    image = models.ImageField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def shorten_text(self):
        return ' '.join(self.text.split(' ')[0:100]) + '...'


class Comment(models.Model):
    text = models.TextField()
    time_create = models.DateTimeField(auto_now=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

