from django.db import models

# Create your models here.
class productCategory(models.Model):
    categoryName=models.CharField(max_length=15,blank=False,unique=True)
    
    def __str__(self):
        return self.categoryName

class Product(models.Model):
    name=models.CharField(max_length=30,blank=False,unique=True)
    description=models.TextField(max_length=500,blank=True)
    categoryName=models.ForeignKey(productCategory, on_delete=models.DO_NOTHING)
    price=models.DecimalField(blank=False,max_digits=6,decimal_places=2)
    quantity=models.IntegerField(blank=False)