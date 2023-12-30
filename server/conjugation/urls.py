from django.urls import path
from . import views

urlpatterns = [
    path('', views.conj_verbs, name='default_learning_set'),
    path('add', views.add_verb, name='add_verb')
]