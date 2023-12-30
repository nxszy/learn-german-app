from django.db import models

# Create your models here.
class ConjVerb(models.Model):
    
    translation = models.CharField(max_length=30, primary_key=True)
    infinitive = models.CharField(max_length=30)
    sg_Ip_form = models.CharField(max_length=30)
    sg_IIp_form = models.CharField(max_length=30)
    sg_IIIp_form = models.CharField(max_length=30)
    pl_Ip_form = models.CharField(max_length=30)
    pl_IIp_form = models.CharField(max_length=30)
    pl_IIIp_form = models.CharField(max_length=30)
    
    def __str__(self):
        return self.translation