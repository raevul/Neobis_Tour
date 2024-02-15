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
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField("Tour image", upload_to='Tour main image')
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'

    def __str__(self):
        return self.title


class TourImages(models.Model):
    images = models.ImageField("Other images", upload_to='Tour other images', null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour')

    class Meta:
        verbose_name = 'Tour image'
        verbose_name_plural = 'Tour images'

    def __str__(self):
        return self.tour.title
