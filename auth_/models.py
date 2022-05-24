from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ROLES =(
        (1, 'SuperAdmin'),
        (2, 'Guest')
    )
    role = models.IntegerField(choices=ROLES, default=2)

    def __str__(self):
        return f'{self.username} -{self.role}'
