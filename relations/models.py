from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    email = models.EmailField(blank=True, null= True)

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    about = models.TextField()
    picture = models.ImageField(upload_to='profile/', null=True, blank=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'