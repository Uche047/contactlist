from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=25)
    address = models.TextField(max_length=80)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return f"{self.name}({self.relationship})"