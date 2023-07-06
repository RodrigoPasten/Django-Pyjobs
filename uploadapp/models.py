from django.db import models


class Uploads(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.description
