from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    CEO=models.CharField(max_length=100)
    est_year=models.IntegerField()
    origin=models.CharField()
    logo=models.ImageField(upload_to='logos',blank=True,null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail",kwargs={"pk":self.pk})


class Products(models.Model):
    product_name=models.CharField(max_length=100)
    color=models.CharField(max_length=10)
    price=models.FloatField()
    fuel_type=models.CharField(max_length=50)
    cc=models.IntegerField()
    miliege=models.IntegerField()
    company=models.ForeignKey(Company,related_name='companies',on_delete=models.CASCADE)
    prod_img=models.ImageField(upload_to='prodimg',blank=True,null=True)
    
    def __str__(self):
        return self.product_name
    

class InteriorImages(models.Model):
    inte_img=models.ImageField(upload_to='interiorimg/',blank=True,null=True)
    product=models.ForeignKey(Products,related_name="intproducts",on_delete=models.CASCADE)

class ExteriorImages(models.Model):
    exte_img=models.ImageField(upload_to='exteriorimg/',blank=True,null=True)
    product=models.ForeignKey(Products,related_name="extproducts",on_delete=models.CASCADE)