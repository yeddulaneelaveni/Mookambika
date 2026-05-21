from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    CATEGORY_CHOICES = (
        ('silk', 'Silk'),
        ('wedding', 'Wedding'),
        ('haldi', 'Haldi'),
        ('reception', 'Reception'),
    )

    name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    sub_category = models.CharField(max_length=100)

    price = models.IntegerField()

    old_price = models.IntegerField()

    description = models.TextField()

    image = models.ImageField(upload_to='products/')

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name