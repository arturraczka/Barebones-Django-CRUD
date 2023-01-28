from django.db import models


class Note(models.Model):

    title = models.CharField(max_length = 40)
    body = models.TextField(max_length = 5000)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/{}'.format(self.pk)
