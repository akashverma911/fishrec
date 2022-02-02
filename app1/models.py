from django.db import models
from PIL import Image

# Create your models here.
class Fish(models.Model):
  name = models.CharField(max_length=300)
  specie = models.CharField(max_length=300)
  weight = models.IntegerField()
  length = models.IntegerField() 
  long = models.DecimalField(max_digits=8, decimal_places=3,blank=True)
  lat = models.DecimalField(max_digits=8, decimal_places=3,blank=True)
  date_created = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)
  image = models.ImageField(upload_to='media')
  # def save(self, *args, **kwargs):
  #     super().save(*args, **kwargs)  # saving image first

  #     img = Image.open(self.image.path)  # Open image using self

  #     if img.height > 140 or img.width > 140:
  #         new_img = (140, 140)
  #         img.thumbnail(new_img)
  #         img.save(self.image.path)
