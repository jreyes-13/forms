from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# JR: class name starts with uppercase and should be defined in singular
class Login(models.Model):
    # name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email