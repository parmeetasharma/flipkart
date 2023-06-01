from django.db import models

# Create your models here.
class Customers(models.Model):
    
    first_name=models.CharField(max_length=12,null=True,blank=True)
    last_name=models.CharField(max_length=11,null=True,blank=True)
    mobile_no=models.IntegerField(null=True,blank=True)
    adress=models.TextField(max_length=12,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    city=models.CharField(max_length=14,null=True,blank=True)

    def __str__(self):
        return str(self.first_name)

class CustomerAddress(models.Model):
    Customer=models.ForeignKey(Customers,on_delete= models.CASCADE,null=True,related_name="customer_Adresses")
    street_name=models.CharField(max_length=15,null=True,blank=True)
    adress=models.CharField(max_length=13,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    city=models.CharField(max_length=14,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.street_name)

class CustomerAddhar(models.Model):
    Customer=models.OneToOneField(Customers,on_delete=models.CASCADE)
    street_name=models.CharField(max_length=15,null=True,blank=True)
    addharmobile_no=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.street_name)


