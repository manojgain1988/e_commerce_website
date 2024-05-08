from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=20,blank=True)
    address=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=200,blank=True)
    country=models.CharField(max_length=200,blank=True)
    image=models.ImageField(blank=True, upload_to='user_img')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    
    def user_name(self):
        return self.user.first_name+' '+self.last_name+'['+self.user.username+']'

    def image_tag(self):
        return mark_safe('<img  src="{}" heights="30" width="30" />' .format(self.image.url))
    image_tag.short_description = 'Image'