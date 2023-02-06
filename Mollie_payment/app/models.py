from django.db import models

# Create your models here.
class Logs(models.Model):
    level=models.CharField(max_length=100)
    module=models.CharField(max_length=100)
    line=models.CharField(max_length=100)
    asctime=models.CharField(max_length=100)
    message=models.CharField(max_length=100)



    # id=models.CharField(max_length=100,blank=True,null=True)
    # product_id=models.CharField(max_length=100,blank=True,null=True)
    # product_title=models.CharField(max_length=100,blank=True,null=True)
    # variants_id=models.CharField(max_length=100,blank=True,null=True)
    # variants_title=models.CharField(max_length=100,blank=True,null=True)
    # created_at=models.DateTimeField(auto_now_add=True,blank=False,null=True)
    # updated_at=models.DateTimeField(auto_now_add=True,blank=False,null=True)
    # price=models.CharField(max_length=100,blank=True,null=True)
    # json_variant=models.TextField(max_length=100,blank=True,null=True)
