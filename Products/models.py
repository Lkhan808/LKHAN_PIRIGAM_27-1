from django.db import models


# Create your models here.


class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self): return self.title


class Review(models.Model):
    text = models.TextField()
    rate = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self): return self.text
