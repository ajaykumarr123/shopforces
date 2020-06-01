from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
#from orders.models import Order
from leave.models import leave_request
from PIL import Image

gender_choices =(
        ('M','M'),
        ('F','F'),
    )


class Employee(models.Model):
    name = models.CharField(max_length=80)
    phone = PhoneField(blank=True, help_text='Contact phone number') #update
    age = models.IntegerField()
    gender = models.CharField(max_length = 1,blank=True,choices = gender_choices)
    address = models.CharField(max_length=150,blank=True) #update
    city = models.CharField(max_length=50,blank=True)
    image = models.ImageField(default='def_M.jpg',blank=True, upload_to = 'profile_pics')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    leave_requests =models.ManyToManyField(leave_request,related_name="leave")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Customer(models.Model):
    name = models.CharField(max_length=80,default="Guest")
    age = models.IntegerField()
    city = models.CharField(max_length=50,blank=True)
    #customer_orders = models.ManyToManyField(Order,related_name="p1")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='def_M.jpg', upload_to = 'profile_pics')

    def __str__(self):
    	return self.user.username

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)




class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=1,default='A')

    def __str__(self):
        return self.user.username
