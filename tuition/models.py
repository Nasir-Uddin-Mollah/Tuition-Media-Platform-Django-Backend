from django.db import models

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Tuition(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.class_name} - {self.subject}'
