from django.db import models

# Create your models here.
class Categorydb(models.Model):
    Category_name = models.CharField(max_length=100, null=True, blank=True)
    Category_description = models.CharField(max_length=200, null=True, blank=True)
    Category_image = models.ImageField(upload_to="Category image", null=True, blank=True)

class Productdb(models.Model):
    Category_name = models.CharField(max_length=100, null=True, blank=True)
    Product_name = models.CharField(max_length=100, null=True, blank=True)
    Product_description = models.CharField(max_length=200, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="Product", null=True, blank=True)

class contactdb(models.Model):
    c_name = models.CharField(max_length=100, null=True, blank=True)
    c_email = models.EmailField(max_length=100, null=True, blank=True)
    c_address = models.CharField(max_length=100, null=True, blank=True)
    c_city = models.CharField(max_length=100, null=True, blank=True)
    c_Country = models.CharField(max_length=100, null=True, blank=True)
    c_zipcode = models.IntegerField(null=True, blank=True)
    c_phone = models.IntegerField(null=True, blank=True)


class frndlogindb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    u_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)

class cartdb(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    productname = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    quentity = models.IntegerField(null=True, blank=True)
    totalprice = models.IntegerField(null=True, blank=True)


