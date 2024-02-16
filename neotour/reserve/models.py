# from django.db import models
#
# from tour.models import Tour
#
#
# class Reserve(models.Model):
#     phone = models.CharField(unique=True, max_length=9)
#     content = models.TextField(max_length=500)
#     tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reserve')
#
#     class Meta:
#         verbose_name = 'Reserve'
#         verbose_name_plural = 'Reserves'
#
#     def __str__(self):
#         return f"This reserve for {self.tour.title}"
