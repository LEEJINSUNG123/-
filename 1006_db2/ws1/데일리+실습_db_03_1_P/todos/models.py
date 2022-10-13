
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings

# 조건 2
class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)