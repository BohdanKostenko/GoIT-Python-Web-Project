from django.db import models, connections
from datetime import datetime


class Notes(models.Model):
    tag = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    note = models.TextField('note')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.note

    def get_absolute_url(self):
        return f'/noteapp.html/{self.id}'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name




# TAG_CHOICES = (
#         education
#     ('annotation','annotation'),
#     ('chronicle', 'chronicle'),
#     ('opened information','opened information'),
#     ('announcement','announcement'),
#     ('private note','private note'),
#     ('event note','event note'),
#     ('business note','business note'),
#     ('review','review'),
#     ('mini story','mini story'),
# )




