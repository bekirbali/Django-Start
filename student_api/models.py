from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name