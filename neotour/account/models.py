from django.contrib.auth.models import User
from django.db import models

from reserve.models import Reserve


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    reserve = models.OneToOneField(Reserve, on_delete=models.CASCADE, related_name='reserve', null=True)

    def __str__(self):
        return self.user.username
