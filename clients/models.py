
from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    plan = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name