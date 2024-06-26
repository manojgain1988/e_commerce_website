from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.safestring import mark_safe
# Create your models here.

class ShopCart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity= models.IntegerField()
    

    def price(self):
        return self.product.new_price
 
  
    def amount(self):
        return self.quantity*self.product.new_price


    def __str__(self):
            return self.product.title
    


class ShopingCartForm(ModelForm):
     class Meta:
        model=ShopCart
        fields=['quantity']