from datetime import datetime
from django.utils.text import slugify
from django.db import models
import locale

# Establece la configuración regional
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')


class Skill(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, null=True)
    mail = models.EmailField(max_length=70)
    area = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Location(models.Model):
    ubication = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.ubication


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)
    # establecer la relación con otros modelos
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skill = models.ManyToManyField(Skill)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        return f' Cargo: {self.title} - Salario: $ {locale.format_string("%d", self.salary, grouping=True)}'
