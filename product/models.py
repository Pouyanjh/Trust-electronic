from django.db import models


class Product(models.Model):
  title = models.CharField(max_length=100, unique=True, blank=True)
  id = models.AutoField(primary_key=True)
  image = models.URLField(max_length=500, blank=True)
  description = models.TextField(blank=True)
  price = models.IntegerField(blank=True)

  class Meta:
      verbose_name = 'product'
      verbose_name_plural = 'products'
      
  def __str__(self):
     return str(self.title)
  

class Topproduct(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=True)
    id = models.AutoField(primary_key=True)
    image = models.URLField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'topproduct'
        verbose_name_plural = 'topproducts'

    def __str__(self):
        return str(self.title)
    

class Popproduct(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=True)
    id = models.AutoField(primary_key=True)
    image = models.URLField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'popproduct'
        verbose_name_plural = 'popproducts'

    def __str__(self):
        return str(self.title)
     




     