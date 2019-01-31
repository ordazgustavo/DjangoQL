from django.db import models


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]


class HardCode(models.Model):
    language = models.TextField()
    sinner = models.TextField()
    test = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sinner

    def language_preview(self):
        return self.language
