from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from tour.models import Tour


class Reserve(models.Model):
    phone = PhoneNumberField(region='KG', unique=True, max_length=13)
    content = models.TextField(max_length=500, null=True)
    number_people = models.PositiveSmallIntegerField("Number of people", default=1)
    reserved_date = models.DateTimeField(auto_now_add=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reserve')

    class Meta:
        verbose_name = 'Reserve'
        verbose_name_plural = 'Reserves'

    def __str__(self):
        return f"This reserve for {self.tour.title}"
