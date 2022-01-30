from django.db import models
from datetime import datetime
from django import forms

TAG_CHOICES = (
    ('annotation','annotation'),
    ('chronicle', 'chronicle'),
    ('opened information','opened information'),
    ('announcement','announcement'),
    ('private note','private note'),
    ('event note','event note'),
    ('business note','business note'),
    ('review','review'),
    ('mini story','mini story'),
)


class Notes(models.Model):
    # tag = models.CharField(max_length=30)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES, default='annotation')
    note = models.TextField('note')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.note, self.tag



