from django.db import models
from users.models import CustomUser
# Create your models here.


class FinstaEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.TextField()
    caption = models.TextField()
    image = models.ImageField(null=True, upload_to='static')

    def __str__(self):
        return self.title
