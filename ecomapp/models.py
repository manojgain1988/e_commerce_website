from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


class Setting(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    fax = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    smptserver = models.CharField(max_length=200)
    smptemail = models.EmailField(max_length=50, blank=True, null=True)
    smptepassword = models.CharField(max_length=50, blank=True)
    smptport = models.CharField(max_length=200, blank=True)
    icon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    address = models.TextField()
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

  