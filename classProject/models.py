from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=35, null=True, blank=True)
    number = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    joined_date = models.DateTimeField(auto_now_add=True) #kayıt yapıldığı an otomatik yaz
    updated_date = models.DateTimeField(auto_now=True) # kayıt güncellendiği an otomatik yaz
    email = models.EmailField()
    image = models.ImageField(upload_to='images/', default='', null=True, blank=True)

    def __str__(self):
       return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'The Students' #define title
        verbose_name_plural = 'The Students' #define title plural
        ordering = ["-first_name"]
   

class Lesson(models.Model):
    first_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.first_name