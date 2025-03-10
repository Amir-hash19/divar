from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(null=True, blank=True)



class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    bio = models.TextField()
    national_id = models.PositiveIntegerField(unique=True)
    avatar = models.ImageField("avatars/")
    





    
