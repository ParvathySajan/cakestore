from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=False,null=True,default=None)
    mobile_number=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['username']
    
    def __str__(self):
        return self.first_name

class Category(models.Model):
    slug=models.CharField(max_length=50,null=True,blank=False)
    category_name=models.CharField(max_length=100)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")

    def __str__(self):
        return self.category_name

class Cakes(models.Model):
    category_name=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    slug=models.CharField(max_length=50,null=True,blank=False)
    cakename=models.CharField(max_length=100)
    price=models.BigIntegerField()
    description=models.CharField(max_length=150)
    cakeimage=models.ImageField(upload_to="cakeimgs",null=True)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")

    def __str__(self):
        return self.cakename

class Feedbacks(models.Model):
    username=models.CharField(max_length=50)
    feedback=models.CharField(max_length=150)

    def __str__(self):
        return self.username

class Cart(models.Model):
    cakename=models.CharField(max_length=30)
    price=models.IntegerField()
    cakeimage=models.ImageField(upload_to='cakeimgs',null=True)

    def __str__(self):
        return self.cakename

class Orders(models.Model):
    customer=models.CharField(max_length=30)
    amount=models.BigIntegerField()
    address=models.CharField(max_length=200)
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.cakename
