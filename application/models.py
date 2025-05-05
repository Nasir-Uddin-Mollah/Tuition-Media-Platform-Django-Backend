from django.db import models
from django.contrib.auth.models import User
from tuition.models import Tuition
# Create your models here.


CHOICES = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
]


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    tuition = models.ForeignKey(Tuition, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CHOICES, default='pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.status == 'accepted':
            self.tuition.is_available= False
            self.tuition.save()
            Application.objects.filter(tuition=self.tuition).exclude(id=self.id).update(status='rejected')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.tuition.class_name.name} - {self.tuition.subject}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    tuition = models.ForeignKey(Tuition, on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.CharField(max_length=5, choices=STAR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tuition.class_name.name}"
