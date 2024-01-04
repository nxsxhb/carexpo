from django.db import models

# Create your models here.
class Car(models.Model):
    brand_name=models.CharField(max_length=250)
    model_name=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    year=models.IntegerField()
    image=models.ImageField(upload_to="Uploads")

    def __str__(self):
        return self.model_name