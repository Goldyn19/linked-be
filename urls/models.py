from django.db import models
from members.models import User


class URL(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description



# Create your models here.
