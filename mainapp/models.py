from django.db import models

# Create your models here.

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    Fullname=models.CharField(max_length=250)
    Email=models.EmailField(max_length=250)
    Phone=models.CharField(max_length=250)
    Password=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    industry=models.CharField(max_length=250)
    image=models.ImageField(upload_to='Images/user')
    state=models.CharField(max_length=250)
    status=models.CharField(default="pending",max_length=250)
    Date=models.DateTimeField(auto_now=True,null=True)