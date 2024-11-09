from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=128, blank=True)

    def _str_(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'
