from django.db import models
from django.conf import settings


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
