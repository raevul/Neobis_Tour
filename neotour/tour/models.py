from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tour(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=1500, null=True)
    image = models.ImageField("Tour image", upload_to='Tour main image')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='tours')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'

    def __str__(self):
        return self.title


class TourImages(models.Model):
    images = models.ImageField("Other images", upload_to='Tour other images', null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Tour image'
        verbose_name_plural = 'Tour images'

    def __str__(self):
        return f'These images for {self.tour.title}'


class Review(models.Model):
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'These reviews for {self.tour.title}'
