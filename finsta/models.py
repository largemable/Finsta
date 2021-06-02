from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FinstaEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    caption = models.TextField()
    image = models.ImageField(null=True, upload_to='static')

    def __str__(self):
        return self.title
