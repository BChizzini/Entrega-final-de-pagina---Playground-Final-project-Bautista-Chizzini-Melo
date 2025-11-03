from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('coleccionista', 'Coleccionista'),
        ('visitante', 'Visitante'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='visitante') 

    def __str__(self):
        return f"{self.user.username}'s profile ({self.get_user_type_display()})"