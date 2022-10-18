from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Familiar(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    age = models.IntegerField()
    birthday = models.DateField()
    
    def __str__(self):
        return f"{self.name} {self.last_name} | email: {self.email} | age: {self.age} | birthday: {self.birthday}"
    
    
    