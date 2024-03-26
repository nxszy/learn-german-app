from gettext import translation
from django.db import models

# Create your models here.
class ConjVerb(models.Model):
    
    translation = models.CharField(max_length=30)
    infinitive = models.CharField(max_length=30)
    sg_Ip_form = models.CharField(max_length=30)
    sg_IIp_form = models.CharField(max_length=30)
    sg_IIIp_form = models.CharField(max_length=30)
    pl_Ip_form = models.CharField(max_length=30)
    pl_IIp_form = models.CharField(max_length=30)
    pl_IIIp_form = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)

    class Meta:
        unique_together = (('translation', 'infinitive'),)
    
    def __str__(self):
        return "Conjugation verb: " + self.translation + ": " + self.infinitive
    
class PastForm(models.Model):

    translation = models.CharField(max_length=30)
    infinitive = models.CharField(max_length=30)
    prateritum = models.CharField(max_length=30)
    partizip2 = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)

    class Meta:
        unique_together = (('translation', 'infinitive'),)

    def __str__(self):
        return "Past form verb: " + self.translation + ": " + self.infinitive

class RectionVerb(models.Model):

    id = models.AutoField(primary_key=True)
    translation = models.CharField(max_length=30)
    infinitive = models.CharField(max_length=30)
    preposition = models.CharField(max_length=30)
    case = models.CharField(max_length=30)

    class Meta:
        unique_together = (('translation', 'infinitive'),)

    def __str__(self) -> str:
        return "Rection verb: " + self.translation + ": " + self.infinitive