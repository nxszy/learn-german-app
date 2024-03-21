from rest_framework import serializers
from .models import *

class ConjSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConjVerb
        fields = ['translation', 'infinitive', 'sg_Ip_form', 'sg_IIp_form', 'sg_IIIp_form',
                  'pl_Ip_form', 'pl_IIp_form', 'pl_IIIp_form']
        
class PastFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = PastForm
        fields = ['translation', 'infinitive', 'prateritum', 'partizip2']