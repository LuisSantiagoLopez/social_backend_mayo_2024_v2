from django.db import models
from django.conf import settings 


class Antro(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="antro_images/antros")
    name = models.CharField(max_length=250)
    description = models.TextField()
    contact = models.CharField(max_length=250)
    approved = models.BooleanField(default=False)
    category = models.CharField(max_length=100)
    cost = models.CharField(max_length=3) # $ $$ or $$$

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="antro_images/menus")
    name = models.CharField(max_length=250)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    antro = models.ForeignKey(Antro, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    antro = models.ForeignKey(Antro, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment