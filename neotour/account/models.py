from django.contrib.auth.models import User
from django.db import models

from reserve.models import Reserve


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    reserve = models.OneToOneField(Reserve, on_delete=models.CASCADE, related_name='reserve')

    def __str__(self):
        return self.user.username
