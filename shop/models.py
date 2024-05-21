from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=50)
    category = models.CharField(max_length=100,default="")
    subcategory = models.CharField(max_length=100,default="")
    price=models.FloatField(max_length=10,default=0.0)
    image=models.ImageField(upload_to="shop/images",default="")
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()

    def __str__(self):
        return self.product_name