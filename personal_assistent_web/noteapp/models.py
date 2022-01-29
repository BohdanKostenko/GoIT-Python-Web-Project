from django.db import models


class Notes(models.Model):
    tag = models.CharField('tag', max_length=30)
    note = models.TextField('note')

    def __str__(self):
        return self.note
