from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=256,blank=False,default="First Name")
    last_name=models.CharField(blank=True,max_length=256,default="Last Name")
    email=models.EmailField(blank=True,unique=True,null=True,max_length=256)
    #additional
    place=models.CharField(blank=False,max_length=256)
    #profile_pic=models.ImageField(upload_to='profile_pic',blank=True)
    def __str__(self):
        return self.user.username

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,default="")
    product_price=models.CharField(max_length=20,default="0")
    product_pic=models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    items_json=models.CharField(max_length=5000,default="")
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    zip_code=models.CharField(max_length=56,default="")
    phone=models.CharField(max_length=10,default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
        
"""
class Watch(models.Model):
    watch_id=models.AutoField
    watch_name=models.CharField(max_length=50,default="")
    watch_price=models.CharField(max_length=20,default="0")
    watch_pic=models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.watch_name

class Shirt(models.Model):
    shirt_id=models.AutoField
    shirt_name=models.CharField(max_length=50,default="")
    shirt=models.CharField(max_length=20,default="0")
    shirt_pic=models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.shirt_name
"""
