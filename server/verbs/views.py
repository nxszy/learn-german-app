from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *
from .models import *

# Create your views here.
@api_view(['GET'])
def conj_verbs(request):
    conj_verbs = ConjVerb.objects.all()
    serializer = ConjSerializer(conj_verbs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def past_forms(request):
    past_forms = PastForm.objects.all()
    serializer = PastFormSerializer(past_forms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)